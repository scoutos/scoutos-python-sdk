# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .block_input import BlockInput
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class WorkflowConfigInput(UncheckedBaseModel):
    workflow_display_name: typing.Optional[str] = None
    workflow_schema_version: typing.Optional[str] = None
    workflow_img_url: typing.Optional[str] = None
    workflow_description: typing.Optional[str] = None
    blocks: typing.Optional[typing.List[BlockInput]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow