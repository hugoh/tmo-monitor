#!/usr/bin/env python3
import os
import sys
from tmo_monitor.gateway.model import GatewayModel
from tmo_monitor.gateway.arcadyan import CubeController
from tmo_monitor.gateway.nokia import TrashCanController
from tmo_monitor.status import ExitStatus

def main():
    user = os.getenv("TMHI_USER")
    if user is None or user == "":
        user = "admin"
    password = os.environ.get("TMHI_PASSWORD")
    
    model = os.getenv("TMHI_MODEL")

    if model == GatewayModel.NOKIA.value:
        gw_control = TrashCanController(user, password)
    elif model == GatewayModel.ARCADYAN.value:
        gw_control = CubeController(user, password)
    else:
        raise Exception("Unsupported Gateway Model: %s" % model)

    gw_control.reboot()

    sys.exit(ExitStatus.REBOOT_PERFORMED.value)
