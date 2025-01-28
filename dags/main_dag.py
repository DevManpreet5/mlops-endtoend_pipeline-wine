from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_transform_pipeline import DataTransformPipeline
from src.pipeline.model_train_pipeline import trainingpiepline
from src.pipeline.model_test_pipeline import testingpipeline
from airflow import DAG
from airflow.decorators import task
from datetime import datetime


with DAG(
    dag_id="ml_pipeline_dag",
    description="DAG for ML Workflow wine",
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    @task
    def ingest_data():
        print("Started ingestion")
        pipeline1 = DataIngestionPipeline()
        pipeline1.run()
        print("End of ingestion")

    @task
    def transform_data():
        print("Started transformation")
        pipeline2 = DataTransformPipeline()
        pipeline2.run()
        print("End of transformation")

    @task
    def train_model():
        print("Started training")
        pipeline3 = trainingpiepline()
        pipeline3.run()
        print("End of training")

    @task
    def test_model():
        print("Started testing")
        pipeline4 = testingpipeline()
        pipeline4.run()
        print("End of testing")

    ingest_data() >> transform_data() >> train_model() >> test_model()