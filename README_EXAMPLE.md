# Kramer Integration

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

![Project Maintenance][maintenance-shield]

[![Community Forum][forum-shield]][forum]

_Integration to integrate with [Kramer media switches][kramer-integration]._

**This integration will set up the following platforms.**

Platform | Description
-- | --
`binary_sensor` | Show something `True` or `False`.
`sensor` | Show info from blueprint API.
`switch` | Switch something `True` or `False`.

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
1. If you do not have a `custom_components` directory (folder) there, you need to create it.
1. In the `custom_components` directory (folder) create a new folder called `integration_blueprint`.
1. Download _all_ the files from the `custom_components/integration_blueprint/` directory (folder) in this repository.
1. Place the files you downloaded in the new directory (folder) you created.
1. Restart Home Assistant
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Integration blueprint"

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[kramer-integration]: https://github.com/krohrbaugh/kramer-homeassistant
[commits-shield]: https://img.shields.io/github/commit-activity/y/krohrbaugh/kramer-homeassistant.svg?style=for-the-badge
[commits]: https://github.com/krohrbaugh/kramer-homeassistant/commits/main
[exampleimg]: example.png
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/krohrbaugh/kramer-homeassistant.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-Kevin%20Rohrbaugh%20%40krohrbaugh-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/krohrbaugh/kramer-homeassistant.svg?style=for-the-badge
[releases]: https://github.com/krohrbaugh/kramer-homeassistant/releases
