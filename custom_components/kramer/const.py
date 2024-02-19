"""Constants for Kramer integration."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

NAME = "Kramer"
ENTITY_NAME = "Kramer Media Switch"
DOMAIN = "kramer"

DEFAULT_PORT = 5000

DATA_INPUT_COUNT = "input_count"
DATA_SOURCE_SELECTED = "source_selected"
DATA_SOURCE_LIST = "source_list"
DATA_STATE = "state"
