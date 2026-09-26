# Predictive Maintenance for Manufacturing Equipment

An end to end project that predicts machine failure from sensor readings.
Built as a portfolio project for an MT Manufacturing Technology application.

## Business Problem

Unexpected machine downtime causes lost production and expensive emergency
repairs. A predictive maintenance system lets the maintenance team step in
before a failure happens, based on patterns in sensor data like tool wear
and torque.

## How This Project Works

The notebooks run in order and do not require any external download:

1. `01_generate_data.ipynb` creates sample sensor readings, similar in
   structure to the AI4I 2020 Predictive Maintenance dataset.
2. `02_eda.ipynb` explores how each sensor reading relates to failure.
3. `03_train_model.ipynb` trains an XGBoost classifier and saves it.

To use a real dataset instead, download the AI4I 2020 dataset from UCI or
Kaggle and rename its columns to match what the notebooks expect (see
`data/README.md`).

## SMART Goals

| Criteria | Target |
|---|---|
| Specific | Classify machine failure risk from five sensor readings |
| Measurable | F1 score for the failure class as high as the data allows, API response under 200ms |
| Achievable | Notebooks run end to end on generated data, real dataset can be swapped in later |
| Relevant | Maps directly to downtime reduction and maintenance planning |
| Time-bound | 4 to 5 weeks part time |

## Project Structure

```
predictive-maintenance/
  data/            sample data and instructions for the real dataset
  notebooks/       the three notebooks listed above
  src/             the trained model and the API that serves it
  dashboard/       a Streamlit app that shows sensor summaries
  docs/            resource list and timeline
```

## How to Run

1. `pip install -r requirements.txt`
2. Run the notebooks in order, 01 through 03.
3. Start the API: `uvicorn src.api:app --reload`
4. Start the dashboard: `streamlit run dashboard/app.py`

## Notes for the Interview

Frame this project around downtime cost: how early warning on tool wear
and torque can let maintenance teams schedule a fix before a breakdown,
instead of reacting after the fact.
