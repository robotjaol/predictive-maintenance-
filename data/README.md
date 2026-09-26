# Data

## Sample Data (used by default)

Notebook `01_generate_data.ipynb` creates `data/raw/sensor_data.csv` on
its own. No download needed to run this project.

## Real Dataset (optional upgrade)

**AI4I 2020 Predictive Maintenance Dataset**
- Source: UCI Machine Learning Repository
- Link: https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset
- Mirror on Kaggle: https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020
- 10,000 rows of sensor readings with a machine failure label and five
  more detailed failure type columns.

To use the real dataset, download it and rename its columns to match the
sample data:

| Real dataset column | Expected column name |
|---|---|
| Air temperature [K] | air_temperature_k |
| Process temperature [K] | process_temperature_k |
| Rotational speed [rpm] | rotational_speed_rpm |
| Torque [Nm] | torque_nm |
| Tool wear [min] | tool_wear_min |
| Machine failure | machine_failure |

Save the renamed file as `data/raw/sensor_data.csv`, replacing the
generated one, then run notebooks 02 and 03 as usual.

## Alternative Dataset (more advanced)

**NASA CMAPSS Turbofan Engine Degradation Simulation**
- Source: NASA Prognostics Center of Excellence Data Repository
- Link: https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
- Use this if extending the project to Remaining Useful Life regression
  instead of binary failure classification.
