# This file was auto-generated by Fern from our API Definition.

import typing
from .block_config_item_boolean import BlockConfigItemBoolean
from .block_config_item_json import BlockConfigItemJson
from .block_config_item_number import BlockConfigItemNumber
from .block_config_item_llm import BlockConfigItemLlm
from .block_config_item_select import BlockConfigItemSelect
from .block_config_item_text_long import BlockConfigItemTextLong
from .block_config_item_text_short import BlockConfigItemTextShort

BlockInputBlockConfigItem = typing.Union[
    BlockConfigItemBoolean,
    BlockConfigItemJson,
    BlockConfigItemNumber,
    BlockConfigItemLlm,
    BlockConfigItemSelect,
    BlockConfigItemTextLong,
    BlockConfigItemTextShort,
]