import json


class Visualizer:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.visuals = self._getVisuals(filepath)

    def _getVisuals(self, path: str):
        with open(path, encoding="utf-8") as f:
            return json.load(f)

    async def Visual(self, emotion: str):
        pass
