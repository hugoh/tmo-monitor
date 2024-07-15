from setuptools import setup

setup(
    name="tmo_reboot",
    version="0.1",
    description="A script to reboot the T-Mobile Home Internet 5G Gateways",
    long_description="A lightweight, cross-platform Python 3 script that can reboot the T-Mobile Home Internet Arcadyan and Nokia 5G Gateways.",
    url="https://github.com/hugoh/tmo-reboot",
    author="hugoh",
    license="MIT",
    packages=["tmo_monitor", "tmo_monitor.gateway"],
    entry_points={
        "console_scripts": ["tmo-reboot=tmo_reboot.command_line:main"],
    },
    install_requires=[
        "requests",
    ],
)
