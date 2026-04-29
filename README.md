# Telecom Churn Predictor

Predict customer churn with a production-ready Flask app, a scikit-learn model, and a live analytics dashboard backed by PostgreSQL.

## Highlights
- Real-time churn prediction from three business inputs
- Live charting of prediction history
- Render-ready deployment with automated model training during build

## Architecture
- Web: Flask
- Model: scikit-learn RandomForest
- Data: PostgreSQL
- UI: HTML, Bootstrap, Chart.js

## Local Quick Start

1. Clone the repository.
   ```bash
   git clone https://github.com/sumansingh20/ChurnPrediction.git
   cd ChurnPrediction
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model.
   ```bash
   python model/train_model.py
   ```

4. Start the app.
   ```bash
   python app.py
   ```

Open http://127.0.0.1:5000

## Remote Deployment (Render)

This repo includes a Render Blueprint in [render.yaml](render.yaml). It installs dependencies, trains the model during build, and starts the web service with Gunicorn.

1. Push the repository to GitHub.
2. In Render, create a new Blueprint and connect this repository.
3. Render builds the service and runs `python model/train_model.py` automatically.
4. Render injects `DATABASE_URL` and the app connects on startup.

## Environment Variables

- `DATABASE_URL`: PostgreSQL connection string used by Flask for prediction history.

## Project Structure

```
app.py
model/train_model.py
templates/index.html
render.yaml
requirements.txt
```
