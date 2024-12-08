import os
import yaml


def load_config():
    """
    Load default config and optionally override it with a custom config specified via an environment variable.
    :return: A dictionary containing specific config values.
    """
    # Get the file path from the environment variable
    config_file_path = os.getenv('CONFIG_FILE_PATH', 'config.yaml')

    if not config_file_path:
        raise ValueError("CONFIG_FILE_PATH environment variable is not set (and no default option)")

    # Load the YAML configuration file
    try:
        with open(config_file_path, 'r') as config_file:
            config_data = yaml.safe_load(config_file)

        return config_data
    except FileNotFoundError:
        raise FileNotFoundError(f"The configuration file at {config_file_path} was not found.")
    except yaml.YAMLError as e:
        raise ValueError(f"Error while parsing YAML file: {e}")
