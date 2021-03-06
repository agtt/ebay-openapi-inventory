"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.amount import Amount
globals()['Amount'] = Amount
from openapi_client.model.shipping_cost_override import ShippingCostOverride


class TestShippingCostOverride(unittest.TestCase):
    """ShippingCostOverride unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testShippingCostOverride(self):
        """Test ShippingCostOverride"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ShippingCostOverride()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
