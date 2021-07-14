"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.charity import Charity
from openapi_client.model.listing_policies import ListingPolicies
from openapi_client.model.pricing_summary import PricingSummary
from openapi_client.model.tax import Tax
globals()['Charity'] = Charity
globals()['ListingPolicies'] = ListingPolicies
globals()['PricingSummary'] = PricingSummary
globals()['Tax'] = Tax
from openapi_client.model.ebay_offer_details_with_keys import EbayOfferDetailsWithKeys


class TestEbayOfferDetailsWithKeys(unittest.TestCase):
    """EbayOfferDetailsWithKeys unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEbayOfferDetailsWithKeys(self):
        """Test EbayOfferDetailsWithKeys"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EbayOfferDetailsWithKeys()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()