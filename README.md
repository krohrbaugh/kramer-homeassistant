# Kramer Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]

[![Community Forum][forum-shield]][forum]

_Home Assistant integration for [Kramer media switches][kramer-integration] via
TCP._

**This integration will set up the following platforms.**

Platform | Description
-- | --
`media_player` | Select media source.

## Installation

### Prerequisites

Before installing the integration in Home Assistant (HA), you'll need to:

1. Confirm that your Kramer switch uses [Protocol 2000][p2000] for its control
protocol.  This should be outlined in your device's manual.
1. Ensure that your Kramer switch is assigned a static IP by your router.
1. Ensure that your Kramer switch is configured to use that static IP. Most
switches are _not_ configured to use [DHCP][dhcp] by default, and require
configuring via software (e.g., [KLAN Configurator][klan]). This should also be
outlined in your device's manual.
1. Ensure that your Kramer switch is reachable via the IP that you have
configured for it.

```sh
ping $IP_OF_SWITCH

# Success :)
# PING $IP_OF_SWITCH ($IP_OF_SWITCH): 56 data bytes
# 64 bytes from $IP_OF_SWITCH: icmp_seq=0 ttl=100 time=1.139 ms
# 64 bytes from $IP_OF_SWITCH: icmp_seq=1 ttl=100 time=1.121 ms

# Failure :(
# PING $IP_OF_SWITCH ($IP_OF_SWITCH): 56 data bytes
# Request timeout for icmp_seq 0
# Request timeout for icmp_seq 0
```

### Install the integration in Home Assistant

#### Manual install

1. Using your tool of choice, open the directory (folder) for your HA
configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need
to create it.
1. In the `custom_components` directory (folder) create a new folder called
`kramer`.
1. Download _all_ the files from the `custom_components/kramer/` directory
(folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant

### Configuration of a device is done in the UI

1. In the HA UI go to "Settings" -> "Devices & Services", then click "+ Add
Integration" and search for "Kramer"
1. Click on _Kramer_, and the device configuration form appears.
1. Fill out the form, providing a name for the Kramer switch, and the IP address
you configured for it.
    <img src="/assets/images/configure.png" width="250">
    **Figure 1** New device configuration form.
1. Click "Submit" to create the device. If successful, HA will ask what Area to assign the
device to.

## Device operation

1. Click on the _Kramer_ integration to view configured devices.
1. Click the device link under the name of the Kramer switch to view the device
information page.
    <img src="/assets/images/device_info.png" width="450">
    **Figure 2** Configured device information page.
1. Click on the device name under the "Controls" section to show the source
selection dialog. Select an input from the list and confirm that your switch
changed inputs.
    <img src="/assets/images/source_select.png" width="300">
    **Figure 3** Device source selection interface.

Once you've confirmed that your switch is working correctly, consider adding
source selection to some of your automations, such as part of a universal remote
control activity.

## Contributions welcome

If you want to contribute to this please read the
[Contribution guidelines](CONTRIBUTING.md).

***

[dhcp]: https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol
[kramer-integration]: https://github.com/krohrbaugh/kramer-homeassistant
[klan]: https://k.kramerav.com/support/download.asp?f=55565
[p2000]: https://cdn.kramerav.com/web/downloads/tech-papers/protocol_2000_rev0_51.pdf
[commits-shield]: https://img.shields.io/github/commit-activity/y/krohrbaugh/kramer-homeassistant.svg?style=for-the-badge
[commits]: https://github.com/krohrbaugh/kramer-homeassistant/commits/main
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/krohrbaugh/kramer-homeassistant.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Kevin%20Rohrbaugh%20%40krohrbaugh-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/krohrbaugh/kramer-homeassistant.svg?style=for-the-badge
[releases]: https://github.com/krohrbaugh/kramer-homeassistant/releases
