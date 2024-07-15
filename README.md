# tmo-monitor - reboot-only version

A lightweight, cross-platform Python 3 script that can reboot the T-Mobile Home Internet Nokia and Arcadyan 5G Gateways for 4G/5G bands, cellular site (tower), and internet connectivity and reboots as needed or on-demand.

It's based on [highvolt-dev/tmo-monitor](https://github.com/highvolt-dev/tmo-monitor): it's a stripped-down version of the code, with minimal dependencies.

## Usage

Simply run `tmo-reboot.py`.

All the configuration is done via environment variables:

- `TMHI_MODEL`: one of `NOK5G21` for the Nokia router or `ARCKVD21` for the
  Arcadyan router (required)
- `TMHI_USER`: name of the router's admin user; defaults to "admin"
- `TMHI_PASSWORD`: password for the router's admin user

## Motivation

The reason for stripping down to the minimum is for installing this software on
the least capable OpenWRT devices.
