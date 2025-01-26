from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_transform_pipeline import DataTransformPipeline
if __name__ == "__main__":
    print('started ingestion')
    pipeline1 = DataIngestionPipeline()
    pipeline1.run()
    print('end of ingestion')

    print('started transform')
    pipeline2 = DataTransformPipeline()
    pipeline2.run()
    print('end of transform')