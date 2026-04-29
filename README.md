<br />
<div align="center">
  <h1 align="center">???? Telecom Churn Predictor</h1>
  <p align="center">
    <strong>Machine Learning application predicting customer retention.</strong>
    <br />
    <br />
    <a href="#remote-deployment">Deployment</a>
    ??
    <a href="#local-run">Quick Start</a>
  </p>
</div>

<hr />

## ???? About the Project

This is an end-to-end Machine Learning web application designed to predict the likelihood of a customer leaving their telecom provider (Churn). It's powered by **Scikit-Learn** for the ML model, **Flask** for the API, and stylized with a beautiful Glassmorphism UI dashboard.

### Features
* **Live AI Predictions:** Submit customer metrics (Tenure, Monthly Charges, Total Charges) to retrieve churn risks in real-time.
* **Analytics Dashboard:** Visualizes historical prediction distributions using `Chart.js` directly bound to a PostgreSQL backend.
* **Modern UI:** Features a fully responsive, dark-mode Glassmorphism interface.

## ???? Remote Deployment

The project is configured for **Render Blueprint** deployment, acting as its Infrastructure-as-Code foundation through `render.yaml`. 

1. Push your repository to GitHub.
2. In Render, create a new Blueprint and connect this repository.
3. Render will deploy the Python Web Service and provision the remote **PostgreSQL database**.
4. During the cloud build step, it runs the training script (`train_model.py`) to freshly generate `churn_model.pkl` and `columns.pkl`.
5. The `DATABASE_URL` is automatically ingested into the Flask app from Render.

## ???? Local Run

### Prerequisites
* Python 3.10+
* PostgreSQL (Optional, uses remote string as fallback)

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/sumansingh20/ChurnPrediction.git
   cd ChurnPrediction
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Train the local model** (Generates `churn_model.pkl`)
   ```sh
   python model/train_model.py
   ```

4. **Launch the application**
   ```sh
   python app.py
   ```
   > ???? Live at: **http://127.0.0.1:5000**
