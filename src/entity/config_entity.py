from dataclasses import dataclass
from typing import List

@dataclass
class Ingestionclassconfig:
    dataset_url: str
    raw_dataset_dir: str
    processed_dataset_dir: str
    dataset_name: str
    test_size: int
    random_state: int

@dataclass
class TransformationConfig:
    dataset_path: str
    output_dir: str
    file_name_train: str
    file_name_test: str
    features_to_scale: List[str]