"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.bulk_migrate_listing import BulkMigrateListing
from openapi_client.model.bulk_migrate_listing_response import BulkMigrateListingResponse


class ListingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __bulk_migrate_listing(
            self,
            bulk_migrate_listing,
            **kwargs
        ):
            """bulk_migrate_listing  # noqa: E501

            This call is used to convert existing eBay Listings to the corresponding Inventory API objects. If an eBay listing is successfully migrated to the Inventory API model, new Inventory Location, Inventory Item, and Offer objects are created. For a multiple-variation listing that is successfully migrated, in addition to the three new Inventory API objects just mentioned, an Inventory Item Group object will also be created. If the eBay listing is a motor vehicle part or accessory listing with a compatible vehicle list (ItemCompatibilityList container in Trading API's Add/Revise/Relist/Verify calls), a Product Compatibility object will be created. Migration Requirements To be eligible for migration, the active eBay listings must meet the following requirements: Listing type is Fixed-Price Listing duration is 'GTC' (Good 'til Cancelled) The item(s) in the listings must have seller-defined SKU values associated with them, and in the case of a multiple-variation listing, each product variation must also have its own SKU value Business Polices (Payment, Return Policy, and Shipping) must be used on the listing, as legacy payment, return policy, and shipping fields will not be accepted. With the Payment Policy associated with a listing, the immediate payment requirement must be enabled, and the only accepted payment method should be PayPal The postal/zip code (PostalCode field in Trading's ItemType) or city (Location field in Trading's ItemType) must be set in the listing; the country is also needed, but this value is required in Trading API, so it will always be set for every listing Unsupported Listing Features The following features are not yet available to be set or modified through the Inventory API, but they will remain on the active eBay listing, even after a successful migration to the Inventory model. The downside to this is that the seller will be completely blocked (in APIs or My eBay) from revising these features/settings once the migration takes place: Any listing-level Buyer Requirements Charity donations from sale proceeds Listing Designer Template applied to the listing Listing enhancements like a bold listing title or Gallery Plus Making the Call In the request payload of the bulkMigrateListings call, the seller will pass in an array of one to five eBay listing IDs (aka Item IDs). To save time and hassle, that seller should do a pre-check on each listing to make sure those listings meet the requirements to be migrated to the new Inventory model. There are no path or query parameters for this call. Call Response If an eBay listing is migrated successfully to the new Inventory model, the following will occur: An Inventory Item object will be created for the item(s) in the listing, and this object will be accessible through the Inventory API An Offer object will be created for the listing, and this object will be accessible through the Inventory API An Inventory Location object will be created and associated with the Offer object, as an Inventory Location must be associated with a published OfferThe response payload of the Bulk Migrate Listings call will show the results of each listing migration. These results include an HTTP status code to indicate the success or failure of each listing migration, the SKU value associated with each item, and if the migration is successful, an Offer ID value. The SKU value will be used in the Inventory API to manage the Inventory Item object, and the Offer ID value will be used in the Inventory API to manage the Offer object. Errors and/or warnings containers will be returned for each listing where an error and/or warning occurred with the attempted migration. If a multiple-variation listing is successfully migrated, along with the Offer and Inventory Location objects, an Inventory Item object will be created for each product variation within the listing, and an Inventory Item Group object will also be created, grouping those variations together in the Inventory API platform. For a motor vehicle part or accessory listing that has a specified list of compatible vehicles, in addition to the Inventory Item, Inventory Location, and Offer objects that are created, a Product Compatibility object will also be created in the Inventory API platform.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.bulk_migrate_listing(bulk_migrate_listing, async_req=True)
            >>> result = thread.get()

            Args:
                bulk_migrate_listing (BulkMigrateListing): Details of the listings that needs to be migrated into Inventory

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                BulkMigrateListingResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['bulk_migrate_listing'] = \
                bulk_migrate_listing
            return self.call_with_http_info(**kwargs)

        self.bulk_migrate_listing = _Endpoint(
            settings={
                'response_type': (BulkMigrateListingResponse,),
                'auth': [
                    'api_auth'
                ],
                'endpoint_path': '/bulk_migrate_listing',
                'operation_id': 'bulk_migrate_listing',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'bulk_migrate_listing',
                ],
                'required': [
                    'bulk_migrate_listing',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'bulk_migrate_listing':
                        (BulkMigrateListing,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'bulk_migrate_listing': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__bulk_migrate_listing
        )
