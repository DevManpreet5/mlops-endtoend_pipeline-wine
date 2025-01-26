from dataclasses import dataclass

@dataclass
class Ingestionclassconfig:
    dataset_url: str
    raw_dataset_dir: str
    processed_dataset_dir: str
    dataset_name: str
    test_size: int
    random_state: int