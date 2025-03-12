# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .sitemap_crawler_settings_output import SitemapCrawlerSettingsOutput
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SourceSyncSitemapSettingsOutput(UncheckedBaseModel):
    source_archetype_id: typing.Literal["com.scoutos.sitemap"] = "com.scoutos.sitemap"
    sitemap_url: str = pydantic.Field()
    """
    The URL of the sitemap to be crawled.
    """

    crawler_settings: typing.Optional[SitemapCrawlerSettingsOutput] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
