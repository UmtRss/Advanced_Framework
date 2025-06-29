import yaml
import os

def get_config():
    base_path = os.path.dirname(os.path.abspath(__file__))  # bu dosyanın yolu
    config_path = os.path.join(base_path, "..", "config", "config.yaml")
    config_path = os.path.abspath(config_path)

    with open(config_path, "r") as file:
        return yaml.safe_load(file)
