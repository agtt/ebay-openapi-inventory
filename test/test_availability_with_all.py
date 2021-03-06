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
from openapi_client.model.ship_to_location_availability_with_all import ShipToLocationAvailabilityWithAll
globals()['PickupAtLocationAvailability'] = PickupAtLocationAvailability
globals()['ShipToLocationAvailabilityWithAll'] = ShipToLocationAvailabilityWithAll
from openapi_client.model.availability_with_all import AvailabilityWithAll


class TestAvailabilityWithAll(unittest.TestCase):
    """AvailabilityWithAll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAvailabilityWithAll(self):
        """Test AvailabilityWithAll"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AvailabilityWithAll()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
