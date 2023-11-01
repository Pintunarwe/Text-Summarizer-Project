import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file

    Raises:
        ValueError: If the YAML file is empty or does not exist

    Returns:
        ConfigBox: The ConfigBox containing YAML file contents
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except FileNotFoundError:
        raise ValueError("YAML file not found or does not exist")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (list): List of paths for directories
        verbose (bool, optional): Enable/disable verbose output. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path of the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
