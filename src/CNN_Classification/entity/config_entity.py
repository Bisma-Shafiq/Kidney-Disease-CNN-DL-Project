from dataclasses import dataclass
from pathlib import Path


#data ingestion config
@dataclass(frozen=True)
class DataIngestionConfig:
    """Data Ingestion Configuration"""
    root_dir: Path
    source_URl: str
    local_data_file: Path
    unzip_dir: Path
    
#base model config

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int