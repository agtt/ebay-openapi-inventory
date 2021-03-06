"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.pickup_at_location_availability import PickupAtLocationAvailability
from openapi_client.model.ship_to_location_availability import ShipToLocationAvailability
globals()['PickupAtLocationAvailability'] = PickupAtLocationAvailability
globals()['ShipToLocationAvailability'] = ShipToLocationAvailability
from openapi_client.model.availability import Availability


class TestAvailability(unittest.TestCase):
    """Availability unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAvailability(self):
        """Test Availability"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Availability()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
