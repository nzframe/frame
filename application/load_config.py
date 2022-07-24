import yaml


def load_config_from_yaml(file_path: str):
    with open(file_path, "r") as stream:
        rt = yaml.safe_load(stream)
    return rt
