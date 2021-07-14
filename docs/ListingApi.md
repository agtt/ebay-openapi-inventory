# openapi_client.ListingApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_migrate_listing**](ListingApi.md#bulk_migrate_listing) | **POST** /bulk_migrate_listing | 


# **bulk_migrate_listing**
> BulkMigrateListingResponse bulk_migrate_listing(bulk_migrate_listing)



This call is used to convert existing eBay Listings to the corresponding Inventory API objects. If an eBay listing is successfully migrated to the Inventory API model, new Inventory Location, Inventory Item, and Offer objects are created. For a multiple-variation listing that is successfully migrated, in addition to the three new Inventory API objects just mentioned, an Inventory Item Group object will also be created. If the eBay listing is a motor vehicle part or accessory listing with a compatible vehicle list (ItemCompatibilityList container in Trading API's Add/Revise/Relist/Verify calls), a Product Compatibility object will be created. Migration Requirements To be eligible for migration, the active eBay listings must meet the following requirements: Listing type is Fixed-Price Listing duration is 'GTC' (Good 'til Cancelled) The item(s) in the listings must have seller-defined SKU values associated with them, and in the case of a multiple-variation listing, each product variation must also have its own SKU value Business Polices (Payment, Return Policy, and Shipping) must be used on the listing, as legacy payment, return policy, and shipping fields will not be accepted. With the Payment Policy associated with a listing, the immediate payment requirement must be enabled, and the only accepted payment method should be PayPal The postal/zip code (PostalCode field in Trading's ItemType) or city (Location field in Trading's ItemType) must be set in the listing; the country is also needed, but this value is required in Trading API, so it will always be set for every listing Unsupported Listing Features The following features are not yet available to be set or modified through the Inventory API, but they will remain on the active eBay listing, even after a successful migration to the Inventory model. The downside to this is that the seller will be completely blocked (in APIs or My eBay) from revising these features/settings once the migration takes place: Any listing-level Buyer Requirements Charity donations from sale proceeds Listing Designer Template applied to the listing Listing enhancements like a bold listing title or Gallery Plus Making the Call In the request payload of the bulkMigrateListings call, the seller will pass in an array of one to five eBay listing IDs (aka Item IDs). To save time and hassle, that seller should do a pre-check on each listing to make sure those listings meet the requirements to be migrated to the new Inventory model. There are no path or query parameters for this call. Call Response If an eBay listing is migrated successfully to the new Inventory model, the following will occur: An Inventory Item object will be created for the item(s) in the listing, and this object will be accessible through the Inventory API An Offer object will be created for the listing, and this object will be accessible through the Inventory API An Inventory Location object will be created and associated with the Offer object, as an Inventory Location must be associated with a published OfferThe response payload of the Bulk Migrate Listings call will show the results of each listing migration. These results include an HTTP status code to indicate the success or failure of each listing migration, the SKU value associated with each item, and if the migration is successful, an Offer ID value. The SKU value will be used in the Inventory API to manage the Inventory Item object, and the Offer ID value will be used in the Inventory API to manage the Offer object. Errors and/or warnings containers will be returned for each listing where an error and/or warning occurred with the attempted migration. If a multiple-variation listing is successfully migrated, along with the Offer and Inventory Location objects, an Inventory Item object will be created for each product variation within the listing, and an Inventory Item Group object will also be created, grouping those variations together in the Inventory API platform. For a motor vehicle part or accessory listing that has a specified list of compatible vehicles, in addition to the Inventory Item, Inventory Location, and Offer objects that are created, a Product Compatibility object will also be created in the Inventory API platform.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import listing_api
from openapi_client.model.bulk_migrate_listing import BulkMigrateListing
from openapi_client.model.bulk_migrate_listing_response import BulkMigrateListingResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.ebay.com/sell/inventory/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: api_auth
configuration = openapi_client.Configuration(
    host = "https://api.ebay.com/sell/inventory/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = listing_api.ListingApi(api_client)
    bulk_migrate_listing = BulkMigrateListing(
        requests=[
            MigrateListing(
                listing_id="listing_id_example",
            ),
        ],
    ) # BulkMigrateListing | Details of the listings that needs to be migrated into Inventory

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_migrate_listing(bulk_migrate_listing)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ListingApi->bulk_migrate_listing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_migrate_listing** | [**BulkMigrateListing**](BulkMigrateListing.md)| Details of the listings that needs to be migrated into Inventory |

### Return type

[**BulkMigrateListingResponse**](BulkMigrateListingResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**207** | Multi-Status |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

