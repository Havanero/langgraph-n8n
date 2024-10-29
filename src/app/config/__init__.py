from typing import Literal

from typing_extensions import TypedDict


class GraphConfig(TypedDict):
    config_name: str
    model_name: Literal["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"]
