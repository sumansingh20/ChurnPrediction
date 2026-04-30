from flask import Flask, render_template, request
import joblib
import pandas as pd
import os
from pathlib import Path
from sqlalchemy import create_engine

app = Flask(__name__)

# =========================
# LOAD MODEL + COLUMNS
# =========================
BASE_DIR = Path(__file__).resolve().parent

try:
    model = joblib.load(BASE_DIR / 'churn_model.pkl')
    columns = joblib.load(BASE_DIR / 'columns.pkl')
except FileNotFoundError:
    model = None
    columns = None
    print("WARNING: Model files not found. Run model/train_model.py first.")

# =========================
# DATABASE CONNECTION (RENDER)
# =========================
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgre:WyW4B4CseTdMfRTPkTV6roah03tzIn4J@dpg-d7np5giqqhas738271e0-a.ohio-postgres.render.com/churn_db_np39"

try:
    engine = create_engine(DATABASE_URL)
except Exception as e:
    engine = None
    print(f"WARNING: Could not create database engine: {e}")


# =========================
# CREATE TABLE IF NOT EXISTS
# =========================
def create_table():
    if engine is None:
        return
    try:
        df = pd.DataFrame(columns=["tenure", "monthly", "total", "result"])
        df.to_sql("predictions", engine, if_exists="append", index=False)
    except Exception as e:
        print(f"WARNING: Could not create predictions table: {e}")

create_table()


# =========================
# HOME
# =========================
@app.route('/')
def home():
    return render_template('index.html')


# =========================
# PREDICT
# =========================
@app.route('/predict', methods=['POST'])
def predict():
    if model is None or columns is None:
        return "Error: model not trained yet. Run model/train_model.py first.", 503
    try:
        tenure = float(request.form['tenure'])
        monthly = float(request.form['MonthlyCharges'])
        total = float(request.form['TotalCharges'])

        # Build full input for model
        input_dict = {col: 0 for col in columns}
        input_dict['tenure'] = tenure
        input_dict['MonthlyCharges'] = monthly
        input_dict['TotalCharges'] = total

        input_df = pd.DataFrame([input_dict])

        prediction = model.predict(input_df)[0]
        result = "Churn" if prediction == 1 else "Stay"

        print("Prediction:", result)

        # Save to DB
        if engine is not None:
            df = pd.DataFrame([{
                "tenure": tenure,
                "monthly": monthly,
                "total": total,
                "result": result
            }])
            try:
                df.to_sql("predictions", engine, if_exists="append", index=False)
                print("Saved to DB")
            except Exception as db_err:
                print(f"WARNING: Could not save to DB: {db_err}")

        return result

    except Exception as e:
        print("ERROR:", e)
        return "Error"


# =========================
# STATS (FOR CHART)
# =========================
@app.route('/stats')
def stats():
    if engine is None:
        return {"error": "Database unavailable"}, 503
    try:
        df = pd.read_sql("SELECT * FROM predictions", engine)

        churn = len(df[df['result'] == 'Churn'])
        stay = len(df[df['result'] == 'Stay'])

        print("Stats:", churn, stay)

        return {"churn": churn, "stay": stay}

    except Exception as e:
        print("ERROR:", e)
        return {"error": "Could not fetch stats"}, 503


# =========================
# RUN
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug, host="0.0.0.0", port=port)