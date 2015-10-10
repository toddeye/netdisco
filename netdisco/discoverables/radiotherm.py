""" Discovers Radio Thermostat Wifi devices. """

from . import BaseDiscoverable
from radiotherm import discover

class Discoverable(BaseDiscoverable):
    """ Adds support for discovering Radio Thermostat Wifi platform. """
    def __init__(self, nd):
        pass

    def get_entries(self):
        """ Returns all Radio Thermostat wifi device/hosts. """
        return([discover.discover_address()])
