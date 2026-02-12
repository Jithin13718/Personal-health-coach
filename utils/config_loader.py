import os
import json
from pathlib import Path

class ConfigLoader:
    def __init__(self, env: str = "development"):
        self.env = env
        self.base_path = Path("config")

    def load(self, filename: str) -> dict:
        """
        Loads config from:
        - environment variables (highest priority)
        - config/<env>/<filename>.json
        """

        config = {}

        file_path = self.base_path / self.env / filename

        if file_path.exists():
            with open(file_path, "r") as f:
                config = json.load(f)

        # Override with environment variables
        for key in config.keys():
            env_value = os.getenv(key.upper())
            if env_value is not None:
                config[key] = env_value

        return config
