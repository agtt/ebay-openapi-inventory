"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.offer_response_with_listing_id import OfferResponseWithListingId
globals()['OfferResponseWithListingId'] = OfferResponseWithListingId
from openapi_client.model.bulk_publish_response import BulkPublishResponse


class TestBulkPublishResponse(unittest.TestCase):
    """BulkPublishResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBulkPublishResponse(self):
        """Test BulkPublishResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BulkPublishResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
