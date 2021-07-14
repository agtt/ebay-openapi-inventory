"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.address import Address
from openapi_client.model.geo_coordinates import GeoCoordinates
globals()['Address'] = Address
globals()['GeoCoordinates'] = GeoCoordinates
from openapi_client.model.location import Location


class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLocation(self):
        """Test Location"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Location()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
