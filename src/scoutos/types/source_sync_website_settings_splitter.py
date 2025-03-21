# This file was auto-generated by Fern from our API Definition.

import typing
from .markdown_splitter_config import MarkdownSplitterConfig
from .recursive_splitter_config import RecursiveSplitterConfig
from .sentence_splitter_config import SentenceSplitterConfig
from .paragraph_splitter_config import ParagraphSplitterConfig
from .mark_down_with_context import MarkDownWithContext

SourceSyncWebsiteSettingsSplitter = typing.Union[
    MarkdownSplitterConfig,
    RecursiveSplitterConfig,
    SentenceSplitterConfig,
    ParagraphSplitterConfig,
    MarkDownWithContext,
]
