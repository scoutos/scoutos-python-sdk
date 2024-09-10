# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .event_name import EventName
from .event_version import EventVersion
from .app_run_completed_environment import AppRunCompletedEnvironment
from .app_run_completed_data import AppRunCompletedData
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class AppRunCompleted(UniversalBaseModel):
    organization_id: str
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the event
    """

    correlation_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the root cause of the event. If not set, it defaults to the event id.
    """

    name: typing.Optional[EventName] = None
    version: typing.Optional[EventVersion] = None
    environment: AppRunCompletedEnvironment
    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the event as UTC ISO 8601 string
    """

    data: AppRunCompletedData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
