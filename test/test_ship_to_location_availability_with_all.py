"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.availability_distribution import AvailabilityDistribution
from openapi_client.model.format_allocation import FormatAllocation
globals()['AvailabilityDistribution'] = AvailabilityDistribution
globals()['FormatAllocation'] = FormatAllocation
from openapi_client.model.ship_to_location_availability_with_all import ShipToLocationAvailabilityWithAll


class TestShipToLocationAvailabilityWithAll(unittest.TestCase):
    """ShipToLocationAvailabilityWithAll unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testShipToLocationAvailabilityWithAll(self):
        """Test ShipToLocationAvailabilityWithAll"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ShipToLocationAvailabilityWithAll()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
