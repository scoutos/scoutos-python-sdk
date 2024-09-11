# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .select_option_item import SelectOptionItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class BlockConfigItemSelect(UniversalBaseModel):
    id: str
    display_name: str
    options: typing.List[SelectOptionItem]
    selected_option: typing.Optional[int] = None
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
