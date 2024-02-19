"""Synchronous Kramer API client"""
from typing import TypedDict

from homeassistant.components.media_player import MediaPlayerState

from kesslerav import get_media_switch, MediaSwitch

from .const import (
    DATA_INPUT_COUNT,
    DATA_SOURCE_LIST,
    DATA_SOURCE_SELECTED,
    DATA_STATE,
    LOGGER,
)

class KramerApiClientError(Exception):
    """Exception to indicate a general API error."""

class KramerApiClientCommunicationError(
    KramerApiClientError
):
    """Exception to indicate a communication error."""

class KramerApiState(TypedDict):
    """Serialized state of a media switch device."""
    DATA_INPUT_COUNT: int
    DATA_SOURCE_LIST: list[str]
    DATA_SOURCE_SELECTED: int
    DATA_STATE: MediaPlayerState

class KramerApiClient:
    """Wraps synchronous kessler-av client"""

    _DEFAULT_STATE: KramerApiState = {
        DATA_INPUT_COUNT: 0,
        DATA_SOURCE_LIST: [],
        DATA_SOURCE_SELECTED: '0',
        DATA_STATE: MediaPlayerState.OFF,
    }

    def __init__(
        self,
        name: str,
        ip_address: str,
        port: int | None = None,
    ) -> None:
        self._name = name
        self._ip_address = ip_address
        self._port = port

        self._device: MediaSwitch | None = None
        self._attr_device_url: str | None = None

        self._attr_input_count: int = 0
        self._attr_selected_source: str = '0'
        # Needs to be list[str] to avoid issues with HA frontend
        self._attr_source_list: list[str] = []

    def refresh_state(self) -> None:
        """Fetch and update device state"""
        try:
            if self._device is None:
                self._device = get_media_switch(self._device_url)
            else:
                self._device.update()
        except (TimeoutError, ConnectionRefusedError) as exception:
            self._device = None
            raise KramerApiClientCommunicationError(
                f"Failed connecting to device '{self._name}' at {self._device_url}:"
                f" {exception}"
            ) from exception
        except Exception as exception:
            self._device = None
            raise KramerApiClientError(
                f"Unknown error connecting to device '{self._name}' at {self._device_url}: "
                f" {exception}"
            ) from exception

        if self._attr_input_count != self._device.input_count:
            # Only recalculate source list when input count changes
            self._attr_input_count = self._device.input_count
            self._attr_source_list = list(
                map(str, range(self._device.input_count + 1))
            )
        self._attr_selected_source = str(self._device.selected_source)

    def select_source(self, source: int) -> None:
        """Select the specified input source."""
        try:
            source_number = int(source)
            self._device.select_source(source_number)
        except ValueError as exception:
            msg = f"Invalid source identifier '{source}'."
            LOGGER.warning(msg)
            raise KramerApiClientError(msg) from exception

    @property
    def state(self) -> KramerApiState:
        """Current device state serialized to a dictionary"""
        if not self.is_connected:
            return self._DEFAULT_STATE

        return {
            DATA_INPUT_COUNT: self.input_count,
            DATA_SOURCE_LIST: self.source_list,
            DATA_SOURCE_SELECTED: self.selected_source,
            DATA_STATE: MediaPlayerState.ON
        }

    @property
    def is_connected(self) -> bool:
        """Returns `true` if connection to device was successful; `false` otherwise."""
        return self._device is not None

    @property
    def name(self) -> str:
        """Returns the user-provided device name"""
        return self._name

    @property
    def input_count(self) -> int:
        """Returns the number of inputs the device supports."""
        return self._attr_input_count

    @property
    def selected_source(self) -> str:
        """Returns the currently selected source"""
        return self._attr_selected_source

    @property
    def source_list(self) -> list[int]:
        """Returns the list of selectable sources."""
        return self._attr_source_list

    @property
    def _device_url(self) -> str:
        # Builds device connection URL as required by `kessler-av`
        if self._attr_device_url is None:
            self._attr_device_url = f"tcp://{self._ip_address}"
            if self._port is not None:
                self._attr_device_url = f"{self._attr_device_url}:{self._port}"

        return self._attr_device_url
