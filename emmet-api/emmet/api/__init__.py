"""
Core module exposes the document interfaces
These will be ingested via Drones, built by Builders, and served via the API
"""
from pkg_resources import DistributionNotFound, get_distribution

from emmet.core.settings import EmmetSettings
from _version import __version__

SETTINGS = EmmetSettings()

try:
    __version__ = get_distribution("emmet-api").version
except DistributionNotFound:  # pragma: no cover
    # package is not installed
    pass
