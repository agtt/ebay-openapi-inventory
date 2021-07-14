"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.availability_with_all import AvailabilityWithAll
from openapi_client.model.package_weight_and_size import PackageWeightAndSize
from openapi_client.model.product import Product
globals()['AvailabilityWithAll'] = AvailabilityWithAll
globals()['PackageWeightAndSize'] = PackageWeightAndSize
globals()['Product'] = Product
from openapi_client.model.inventory_item_with_sku_locale_group_keys import InventoryItemWithSkuLocaleGroupKeys


class TestInventoryItemWithSkuLocaleGroupKeys(unittest.TestCase):
    """InventoryItemWithSkuLocaleGroupKeys unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInventoryItemWithSkuLocaleGroupKeys(self):
        """Test InventoryItemWithSkuLocaleGroupKeys"""
        # FIXME: construct object with mandatory attributes with example values
        # model = InventoryItemWithSkuLocaleGroupKeys()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
