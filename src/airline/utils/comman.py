import os
import sys

import numpy as np
import dill
import yaml
from pandas import DataFrame

from src.airline.exception import customException
from src.airline.logger import logging


def read_yaml_file(file_path: str) -> dict:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The configuration file '{file_path}' does not exist.")
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise customException(e, sys) from e



def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")
