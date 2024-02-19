"""DataUpdateCoordinator for Kramer integration."""
from __future__ import annotations

from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from .api import (
    KramerApiState,
    KramerApiClient,
    KramerApiClientError,
)
from .const import DOMAIN, LOGGER


# https://developers.home-assistant.io/docs/integration_fetching_data#coordinated-single-api-poll-for-data-for-all-entities
class KramerDataUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching data from devices."""

    config_entry: ConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
        client: KramerApiClient,
    ) -> None:
        """Initialize."""
        self.client = client
        super().__init__(
            hass=hass,
            logger=LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=5),
        )

    async def _async_update_data(self) -> KramerApiState:
        """Update device state."""
        try:
            return await self.hass.async_add_executor_job(self._get_data)
        except KramerApiClientError as exception:
            raise UpdateFailed(exception) from exception

    # Synchronous; invoke via `hass.async_add_executor_job`
    def _get_data(self) -> KramerApiState:
        self.client.refresh_state()
        return self.client.state
