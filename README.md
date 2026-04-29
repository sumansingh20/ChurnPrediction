# churn-prediction-app

This is a machine learning app for predicting customer churn for telecom companies.

## Remote Deployment

The project is configured for Render Blueprint deployment through `render.yaml`.

1. Push the repository to GitHub.
2. In Render, create a new Blueprint and connect this repository.
3. Render will create the web service and PostgreSQL database automatically.
4. During the build, Render also runs `model/train_model.py` to generate `churn_model.pkl` and `columns.pkl`.
5. The app reads `DATABASE_URL` from Render, so no hardcoded database credentials are needed.

## Local Run

```bash
python app.py
```
