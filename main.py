from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
if __name__ == "__main__":
    print('started')
    pipeline = DataIngestionPipeline()
    pipeline.run()
    print('end')