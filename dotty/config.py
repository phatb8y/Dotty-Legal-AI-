from pathlib import Path
import yaml

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent.parent / "configs" / "dotty_persona.yaml"

class DottyConfig:
    def __init__(self, path: Path | None = None):
        self.path = Path(path) if path else DEFAULT_CONFIG_PATH
        self.raw = self._load_yaml(self.path)
        self.persona = self.raw.get("Dotty_Persona", {})
        self.logic = self.raw.get("Response_Logic", {})
        self.output_style = self.raw.get("Output_Style", [])

    @staticmethod
    def _load_yaml(path: Path) -> dict:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
