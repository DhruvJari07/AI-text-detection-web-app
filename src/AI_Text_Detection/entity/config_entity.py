from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    raw_data_file: Path
    train_data_file: Path
    test_data_file: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    train_data_file: Path
    test_data_file: Path

@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    trained_model_path: Path