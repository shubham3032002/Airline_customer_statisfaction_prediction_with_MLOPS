from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    host: str
    user: str
    password: str
    database: str
    table_name: str
    root: Path
    local_data_file: Path
