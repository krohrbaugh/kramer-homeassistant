"""Base entity class"""
from __future__ import annotations

from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME
from .coordinator import KramerDataUpdateCoordinator


class KramerEntity(CoordinatorEntity):
    """Entity class."""

    def __init__(self, coordinator: KramerDataUpdateCoordinator) -> None:
        """Initialize."""
        super().__init__(coordinator)
        self._attr_unique_id = coordinator.config_entry.entry_id
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, self.unique_id)},
            manufacturer=NAME,
            name=coordinator.client.name,
        )
