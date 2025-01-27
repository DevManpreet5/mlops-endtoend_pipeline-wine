# End to End Data Science Project
## Important Links

- **[MLflow Tracking](https://dagshub.com/DevManpreet5/mlops-endtoend_pipeline-wine.mlflow/)**: Model tracking and evaluation tool.
- **[Dagshub Repository](https://dagshub.com/DevManpreet5/mlops-endtoend_pipeline-wine)**: Main project repository for collaboration and code.

---
### Workflows--ML Pipeline

1. Data Ingestion
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py

## if face import module error

1. Verify PYTHONPATH
   Ensure that the root of your project (where src exists) is in the Python path. To check, run:

   python3 -c "import sys; print(sys.path)"

2. If the root directory (.../mlops_wine_end2end_pipeline) is not listed, explicitly set it:

   export PYTHONPATH=$(pwd)

3. python3 src/config/configuration.py


# Environment Setup

Before running the project, ensure you have the following environment variables set in your `.env` file:

```plaintext
MLFLOW_TRACKING_USERNAME="DevManpreet5"
MLFLOW_TRACKING_PASSWORD=""

