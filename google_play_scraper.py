"""
Local shim for `google_play_scraper` to satisfy editor/linters when
the real package isn't installed. This returns an empty result and
emits a warning at runtime. Install the real package for full
functionality:

    pip install -r requirements.txt

"""
import warnings
from typing import List, Tuple, Any


def reviews(app_id: str, lang: str = "en", country: str = "us", count: int = 200) -> Tuple[List[Any], None]:
    warnings.warn(
        "Local shim: 'google_play_scraper' not installed. Install the real package with 'pip install -r requirements.txt' to fetch real reviews.",
        UserWarning,
    )
    return [], None
