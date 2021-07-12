import json
import os

CONFIG_PATH = os.path.join(os.getcwd(), "bin/config.json")


class LoaderConfig:
    def __init__(self):
        self.__json = {}
        config_path = os.path.join(os.getcwd(), "bin/config.json")
        with open(config_path) as config:
            self.__json = json.load(config)

    @property
    def load_colors(self):
        """
        Load the default colors
        :return: json config array with colors
        """
        return self.__json["colors"]

    @property
    def load_configurations(self):
        return self.__json["configurations"]
