import configparser


def read_config(file_path, section):
    properties = {}
    config = configparser.ConfigParser()
    config.read(file_path)
    try:
        if section in config:
            properties.update(config.items(section))
        else:
            raise ValueError(f"Invalid or missing {section} section in the configuration file.")

    except configparser.Error as e:
        raise ValueError(f'Error reading configuration fileL {e}')

    return properties
