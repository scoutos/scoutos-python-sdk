# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .copilot_config_mode import CopilotConfigMode
from .copilot_config_fab_value import CopilotConfigFabValue
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class CopilotConfig(UncheckedBaseModel):
    workflow_id: typing.Optional[str] = None
    img_url: typing.Optional[str] = None
    display_name: typing.Optional[str] = None
    mode: typing.Optional[CopilotConfigMode] = None
    colors: typing.Optional[typing.Dict[str, str]] = None
    fab: typing.Optional[typing.Dict[str, typing.Optional[CopilotConfigFabValue]]] = None
    message_placeholder: typing.Optional[str] = None
    initial_activity: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    allowed_origins: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow