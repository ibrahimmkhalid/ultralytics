# SFDT_Ibrahim 🚀 AGPL-3.0 License - https://sfdt_ibrahim.com/license

__version__ = "8.3.71"

import os

# Set ENV variables (place before imports)
if not os.environ.get("OMP_NUM_THREADS"):
    os.environ["OMP_NUM_THREADS"] = "1"  # default for reduced CPU utilization during training

from sfdt_ibrahim.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOWorld
from sfdt_ibrahim.utils import ASSETS, SETTINGS
from sfdt_ibrahim.utils.checks import check_yolo as checks
from sfdt_ibrahim.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
)
