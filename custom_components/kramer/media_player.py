"""Media Player platform entity implementation"""
from homeassistant.components.media_player import (
    MediaPlayerDeviceClass,
    MediaPlayerEntityDescription,
    MediaPlayerEntityFeature,
    MediaPlayerEntity,
    MediaPlayerState,
)

from .const import (
    DATA_INPUT_COUNT,
    DATA_SOURCE_LIST,
    DATA_SOURCE_SELECTED,
    DATA_STATE,
    DOMAIN,
)
from .api import KramerApiClient
from .coordinator import KramerDataUpdateCoordinator
from .entity import KramerEntity

ENTITY_DESCRIPTIONS = (
    MediaPlayerEntityDescription(
        key=DOMAIN,
        device_class=MediaPlayerDeviceClass.RECEIVER
    ),
)

async def async_setup_entry(hass, entry, async_add_devices):
    """Setup the media_player platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        KramerMediaPlayer(
            coordinator=coordinator,
            entity_description=entity_description
        )
        for entity_description in ENTITY_DESCRIPTIONS
    )

class KramerMediaPlayer(KramerEntity, MediaPlayerEntity):
    """Representation of a Kramer media switch."""

    _attr_supported_features = (
        MediaPlayerEntityFeature.SELECT_SOURCE
    )

    def __init__(
        self,
        coordinator: KramerDataUpdateCoordinator,
        entity_description: MediaPlayerEntityDescription,
    ) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self.entity_description = entity_description
        self._attr_name = coordinator.client.name

    @property
    def input_count(self) -> int:
        """Number of inputs supported by the media player"""
        return self._prop(DATA_INPUT_COUNT)

    @property
    def source(self) -> str | None:
        """Name of the current input source."""
        return self._prop(DATA_SOURCE_SELECTED)

    @property
    def source_list(self) -> list[str] | None:
        """List of available input sources."""
        return self._prop(DATA_SOURCE_LIST)

    @property
    def state(self) -> MediaPlayerState | None:
        """State of the player."""
        return self._prop(DATA_STATE)

    def select_source(self, source: str) -> None:
        """Select input source."""
        self._client.select_source(source)

    async def async_select_source(self, source: str) -> None:
        """Select input source."""
        await self.hass.async_add_executor_job(self.select_source, source)
        await self.coordinator.async_request_refresh()

    @property
    def _client(self) -> KramerApiClient:
        return self.coordinator.client

    def _prop(self, key: str):
        return self.coordinator.data.get(key)
