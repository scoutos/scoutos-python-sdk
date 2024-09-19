# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .event_version import EventVersion
from .block_run_completed_environment import BlockRunCompletedEnvironment
from .block_run_completed_data import BlockRunCompletedData
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BlockRunCompleted(UncheckedBaseModel):
    organization_id: str
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the event
    """

    correlation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the root cause of the event. If not set, it defaults to the event id.
    """

    version: typing.Optional[EventVersion] = None
    environment: BlockRunCompletedEnvironment
    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the event as UTC ISO 8601 string
    """

    data: BlockRunCompletedData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
