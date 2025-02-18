# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from pathlib import Path

from ultralytics.engine.model import Model
from ultralytics.models import sfdt
from ultralytics.nn.tasks import (
    DetectionModel,
)
from ultralytics.utils import ROOT, yaml_load


class SFDT(Model):
    """SFDT (You Only Look Once) object detection model."""

    def __init__(self, model="sfdt11n.pt", task=None, verbose=False):
        """Initialize SFDT model."""
        path = Path(model)
        # Continue with default SFDT initialization
        super().__init__(model=model, task=task, verbose=verbose)

    @property
    def task_map(self):
        """Map head to model, trainer, validator, and predictor classes."""
        return {
            "detect": {
                "model": DetectionModel,
                "trainer": sfdt.detect.DetectionTrainer,
                "validator": sfdt.detect.DetectionValidator,
                "predictor": sfdt.detect.DetectionPredictor,
            },
        }
