# openapi_client.InventoryItemApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_create_or_replace_inventory_item**](InventoryItemApi.md#bulk_create_or_replace_inventory_item) | **POST** /bulk_create_or_replace_inventory_item | 
[**bulk_get_inventory_item**](InventoryItemApi.md#bulk_get_inventory_item) | **POST** /bulk_get_inventory_item | 
[**bulk_update_price_quantity**](InventoryItemApi.md#bulk_update_price_quantity) | **POST** /bulk_update_price_quantity | 
[**create_or_replace_inventory_item**](InventoryItemApi.md#create_or_replace_inventory_item) | **PUT** /inventory_item/{sku} | 
[**delete_inventory_item**](InventoryItemApi.md#delete_inventory_item) | **DELETE** /inventory_item/{sku} | 
[**get_inventory_item**](InventoryItemApi.md#get_inventory_item) | **GET** /inventory_item/{sku} | 
[**get_inventory_items**](InventoryItemApi.md#get_inventory_items) | **GET** /inventory_item | 


# **bulk_create_or_replace_inventory_item**
> BulkInventoryItemResponse bulk_create_or_replace_inventory_item(bulk_inventory_item)



Note: Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls. This call can be used to create and/or update up to 25 new inventory item records. It is up to sellers whether they want to create a complete inventory item records right from the start, or sellers can provide only some information with the initial bulkCreateOrReplaceInventoryItem call, and then make one or more additional bulkCreateOrReplaceInventoryItem calls to complete all required fields for the inventory item records and prepare for publishing. Upon first creating inventory item records, only the SKU values are required. In the case of updating existing inventory item records, the bulkCreateOrReplaceInventoryItem call will do a complete replacement of the existing inventory item records, so all fields that are currently defined for the inventory item record are required in that update action, regardless of whether their values changed. So, when replacing/updating an inventory item record, it is advised that the seller run a 'Get' call to retrieve the full details of the inventory item records and see all of its current values/settings before attempting to update the records. Any changes that are made to inventory item records that are part of one or more active eBay listings, a successful call will automatically update these active listings. The key information that is set with the bulkCreateOrReplaceInventoryItem call include: Seller-defined SKU value for the product. Each seller product, including products within an item inventory group, must have their own SKU value. Condition of the item Product details, including any product identifier(s), such as a UPC, ISBN, EAN, or Brand/Manufacturer Part Number pair, a product description, a product title, product/item aspects, and links to images. eBay will use any supplied eBay Product ID (ePID) or a GTIN (UPC, ISBN, or EAN) and attempt to match those identifiers to a product in the eBay Catalog, and if a product match is found, the product details for the inventory item will automatically be populated. Quantity of the inventory item that is available for purchase Package weight and dimensions, which is required if the seller will be offering calculated shipping options. The package weight will also be required if the seller will be providing flat-rate shipping services, but charging a weight surcharge. In addition to the authorization header, which is required for all eBay REST API calls, the bulkCreateOrReplaceInventoryItem call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document. For those who prefer to create or update a single inventory item record, the createOrReplaceInventoryItem method can be used.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_api
from openapi_client.model.bulk_inventory_item import BulkInventoryItem
from openapi_client.model.bulk_inventory_item_response import BulkInventoryItemResponse
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
    api_instance = inventory_item_api.InventoryItemApi(api_client)
    bulk_inventory_item = BulkInventoryItem(
        requests=[
            InventoryItemWithSkuLocale(
                availability=Availability(
                    pickup_at_location_availability=[
                        PickupAtLocationAvailability(
                            availability_type="availability_type_example",
                            fulfillment_time=TimeDuration(
                                unit="unit_example",
                                value=1,
                            ),
                            merchant_location_key="merchant_location_key_example",
                            quantity=1,
                        ),
                    ],
                    ship_to_location_availability=ShipToLocationAvailability(
                        availability_distributions=[
                            AvailabilityDistribution(
                                fulfillment_time=TimeDuration(
                                    unit="unit_example",
                                    value=1,
                                ),
                                merchant_location_key="merchant_location_key_example",
                                quantity=1,
                            ),
                        ],
                        quantity=1,
                    ),
                ),
                condition="condition_example",
                condition_description="condition_description_example",
                locale="locale_example",
                package_weight_and_size=PackageWeightAndSize(
                    dimensions=Dimension(
                        height=3.14,
                        length=3.14,
                        unit="unit_example",
                        width=3.14,
                    ),
                    package_type="package_type_example",
                    weight=Weight(
                        unit="unit_example",
                        value=3.14,
                    ),
                ),
                product=Product(
                    aspects=[
                        "aspects_example",
                    ],
                    brand="brand_example",
                    description="description_example",
                    ean=[
                        "ean_example",
                    ],
                    epid="epid_example",
                    image_urls=[
                        "image_urls_example",
                    ],
                    isbn=[
                        "isbn_example",
                    ],
                    mpn="mpn_example",
                    subtitle="subtitle_example",
                    title="title_example",
                    upc=[
                        "upc_example",
                    ],
                ),
                sku="sku_example",
            ),
        ],
    ) # BulkInventoryItem | Details of the inventories with sku and locale

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_create_or_replace_inventory_item(bulk_inventory_item)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemApi->bulk_create_or_replace_inventory_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_inventory_item** | [**BulkInventoryItem**](BulkInventoryItem.md)| Details of the inventories with sku and locale |

### Return type

[**BulkInventoryItemResponse**](BulkInventoryItemResponse.md)

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

# **bulk_get_inventory_item**
> BulkGetInventoryItemResponse bulk_get_inventory_item(bulk_get_inventory_item)



This call retrieves up to 25 inventory item records. The SKU value of each inventory item record to retrieve is specified in the request payload. The authorization header is the only required HTTP header for this call, and it is required for all Inventory API calls. See the HTTP request headers section for more information. For those who prefer to retrieve only one inventory item record by SKU value, , the getInventoryItem method can be used. To retrieve all inventory item records defined on the seller's account, the getInventoryItems method can be used (with pagination control if desired).

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_api
from openapi_client.model.bulk_get_inventory_item import BulkGetInventoryItem
from openapi_client.model.bulk_get_inventory_item_response import BulkGetInventoryItemResponse
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
    api_instance = inventory_item_api.InventoryItemApi(api_client)
    bulk_get_inventory_item = BulkGetInventoryItem(
        requests=[
            GetInventoryItem(
                sku="sku_example",
            ),
        ],
    ) # BulkGetInventoryItem | Details of the inventories with sku and locale

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_get_inventory_item(bulk_get_inventory_item)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemApi->bulk_get_inventory_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_get_inventory_item** | [**BulkGetInventoryItem**](BulkGetInventoryItem.md)| Details of the inventories with sku and locale |

### Return type

[**BulkGetInventoryItemResponse**](BulkGetInventoryItemResponse.md)

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

# **bulk_update_price_quantity**
> BulkPriceQuantityResponse bulk_update_price_quantity(bulk_price_quantity)



This call is used by the seller to update the total ship-to-home quantity of one inventory item, and/or to update the price and/or quantity of one or more offers associated with one inventory item. Up to 25 offers associated with an inventory item may be updated with one bulkUpdatePriceQuantity call. Only one SKU (one product) can be updated per call. The getOffers call can be used to retrieve all offers associated with a SKU. The seller will just pass in the correct SKU value through the sku query parameter. To update an offer, the offerId value is required, and this value is returned in the getOffers call response. It is also useful to know which offers are unpublished and which ones are published. To get this status, look for the status value in the getOffers call response. Offers in the published state are live eBay listings, and these listings will be revised with a successful bulkUpdatePriceQuantity call. An issue will occur if duplicate offerId values are passed through the same offers container, or if one or more of the specified offers are associated with different products/SKUs. Note: For multiple-variation listings, it is recommended that the bulkUpdatePriceQuantity call be used to update price and quantity information for each SKU within that multiple-variation listing instead of using createOrReplaceInventoryItem calls to update the price and quantity for each SKU. Just remember that only one SKU (one product variation) can be updated per call. The authorization header is the only required HTTP header for this call. See the HTTP request headers section for more information.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_api
from openapi_client.model.bulk_price_quantity import BulkPriceQuantity
from openapi_client.model.bulk_price_quantity_response import BulkPriceQuantityResponse
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
    api_instance = inventory_item_api.InventoryItemApi(api_client)
    bulk_price_quantity = BulkPriceQuantity(
        requests=[
            PriceQuantity(
                offers=[
                    OfferPriceQuantity(
                        available_quantity=1,
                        offer_id="offer_id_example",
                        price=Amount(
                            currency="currency_example",
                            value="value_example",
                        ),
                    ),
                ],
                ship_to_location_availability=ShipToLocationAvailability(
                    availability_distributions=[
                        AvailabilityDistribution(
                            fulfillment_time=TimeDuration(
                                unit="unit_example",
                                value=1,
                            ),
                            merchant_location_key="merchant_location_key_example",
                            quantity=1,
                        ),
                    ],
                    quantity=1,
                ),
                sku="sku_example",
            ),
        ],
    ) # BulkPriceQuantity | Price and allocation details for the given SKU and Marketplace

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_update_price_quantity(bulk_price_quantity)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemApi->bulk_update_price_quantity: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_price_quantity** | [**BulkPriceQuantity**](BulkPriceQuantity.md)| Price and allocation details for the given SKU and Marketplace |

### Return type

[**BulkPriceQuantityResponse**](BulkPriceQuantityResponse.md)

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

# **create_or_replace_inventory_item**
> BaseResponse create_or_replace_inventory_item(content_language, sku, inventory_item)



Note: Please note that any eBay listing created using the Inventory API cannot be revised or relisted using the Trading API calls. This call creates a new inventory item record or replaces an existing inventory item record. It is up to sellers whether they want to create a complete inventory item record right from the start, or sellers can provide only some information with the initial createOrReplaceInventoryItem call, and then make one or more additional createOrReplaceInventoryItem calls to complete all required fields for the inventory item record and prepare it for publishing. Upon first creating an inventory item record, only the SKU value in the call path is required. In the case of replacing an existing inventory item record, the createOrReplaceInventoryItem call will do a complete replacement of the existing inventory item record, so all fields that are currently defined for the inventory item record are required in that update action, regardless of whether their values changed. So, when replacing/updating an inventory item record, it is advised that the seller run a getInventoryItem call to retrieve the full inventory item record and see all of its current values/settings before attempting to update the record. And if changes are made to an inventory item that is part of one or more active eBay listings, a successful call will automatically update these eBay listings. The key information that is set with the createOrReplaceInventoryItem call include: Seller-defined SKU value for the product. Each seller product, including products within an item inventory group, must have their own SKU value. This SKU value is passed in at the end of the call URI Condition of the item Product details, including any product identifier(s), such as a UPC, ISBN, EAN, or Brand/Manufacturer Part Number pair, a product description, a product title, product/item aspects, and links to images. eBay will use any supplied eBay Product ID (ePID) or a GTIN (UPC, ISBN, or EAN) and attempt to match those identifiers to a product in the eBay Catalog, and if a product match is found, the product details for the inventory item will automatically be populated. Quantity of the inventory item that is available for purchase Package weight and dimensions, which is required if the seller will be offering calculated shipping options. The package weight will also be required if the seller will be providing flat-rate shipping services, but charging a weight surcharge. In addition to the authorization header, which is required for all eBay REST API calls, the createOrReplaceInventoryItem call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document. For those who prefer to create or update numerous inventory item records with one call (up to 25 at a time), the bulkCreateOrReplaceInventoryItem method can be used.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_api
from openapi_client.model.base_response import BaseResponse
from openapi_client.model.inventory_item import InventoryItem
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
    api_instance = inventory_item_api.InventoryItemApi(api_client)
    content_language = "Content-Language_example" # str | This request header sets the natural language that will be provided in the field values of the request payload.
    sku = "sku_example" # str | The seller-defined SKU value for the inventory item is required whether the seller is creating a new inventory item, or updating an existing inventory item. This SKU value is passed in at the end of the call URI. SKU values must be unique across the seller's inventory. Max length: 50.
    inventory_item = InventoryItem(
        availability=Availability(
            pickup_at_location_availability=[
                PickupAtLocationAvailability(
                    availability_type="availability_type_example",
                    fulfillment_time=TimeDuration(
                        unit="unit_example",
                        value=1,
                    ),
                    merchant_location_key="merchant_location_key_example",
                    quantity=1,
                ),
            ],
            ship_to_location_availability=ShipToLocationAvailability(
                availability_distributions=[
                    AvailabilityDistribution(
                        fulfillment_time=TimeDuration(
                            unit="unit_example",
                            value=1,
                        ),
                        merchant_location_key="merchant_location_key_example",
                        quantity=1,
                    ),
                ],
                quantity=1,
            ),
        ),
        condition="condition_example",
        condition_description="condition_description_example",
        package_weight_and_size=PackageWeightAndSize(
            dimensions=Dimension(
                height=3.14,
                length=3.14,
                unit="unit_example",
                width=3.14,
            ),
            package_type="package_type_example",
            weight=Weight(
                unit="unit_example",
                value=3.14,
            ),
        ),
        product=Product(
            aspects=[
                "aspects_example",
            ],
            brand="brand_example",
            description="description_example",
            ean=[
                "ean_example",
            ],
            epid="epid_example",
            image_urls=[
                "image_urls_example",
            ],
            isbn=[
                "isbn_example",
            ],
            mpn="mpn_example",
            subtitle="subtitle_example",
            title="title_example",
            upc=[
                "upc_example",
            ],
        ),
    ) # InventoryItem | Details of the inventory item record.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_replace_inventory_item(content_language, sku, inventory_item)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemApi->create_or_replace_inventory_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This request header sets the natural language that will be provided in the field values of the request payload. |
 **sku** | **str**| The seller-defined SKU value for the inventory item is required whether the seller is creating a new inventory item, or updating an existing inventory item. This SKU value is passed in at the end of the call URI. SKU values must be unique across the seller&#39;s inventory. Max length: 50. |
 **inventory_item** | [**InventoryItem**](InventoryItem.md)| Details of the inventory item record. |

### Return type

[**BaseResponse**](BaseResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Content-Language -  <br>  |
**201** | Created |  * Content-Language -  <br>  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_item**
> delete_inventory_item(sku)



This call is used to delete an inventory item record associated with a specified SKU. A successful call will not only delete that inventory item record, but will also have the following effects: Delete any and all unpublished offers associated with that SKU; Delete any and all single-variation eBay listings associated with that SKU; Automatically remove that SKU from a multiple-variation listing and remove that SKU from any and all inventory item groups in which that SKU was a member. The authorization header is the only required HTTP header for this call. See the HTTP request headers section for more information.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_api
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
    api_instance = inventory_item_api.InventoryItemApi(api_client)
    sku = "sku_example" # str | This is the seller-defined SKU value of the product whose inventory item record you wish to delete. Max length: 50.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_inventory_item(sku)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemApi->delete_inventory_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| This is the seller-defined SKU value of the product whose inventory item record you wish to delete. Max length: 50. |

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_item**
> InventoryItemWithSkuLocaleGroupid get_inventory_item(sku)



This call retrieves the inventory item record for a given SKU. The SKU value is passed in at the end of the call URI. There is no request payload for this call. The authorization header is the only required HTTP header for this call, and it is required for all Inventory API calls. See the HTTP request headers section for more information. For those who prefer to retrieve numerous inventory item records by SKU value with one call (up to 25 at a time), the bulkGetInventoryItem method can be used. To retrieve all inventory item records defined on the seller's account, the getInventoryItems method can be used (with pagination control if desired).

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_api
from openapi_client.model.inventory_item_with_sku_locale_groupid import InventoryItemWithSkuLocaleGroupid
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
    api_instance = inventory_item_api.InventoryItemApi(api_client)
    sku = "sku_example" # str | This is the seller-defined SKU value of the product whose inventory item record you wish to retrieve. Max length: 50.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_inventory_item(sku)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemApi->get_inventory_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| This is the seller-defined SKU value of the product whose inventory item record you wish to retrieve. Max length: 50. |

### Return type

[**InventoryItemWithSkuLocaleGroupid**](InventoryItemWithSkuLocaleGroupid.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_items**
> InventoryItems get_inventory_items()



This call retrieves all inventory item records defined for the seller's account. The limit query parameter allows the seller to control how many records are returned per page, and the offset query parameter is used to retrieve a specific page of records. The seller can make multiple calls to scan through multiple pages of records. There is no request payload for this call. The authorization header is the only required HTTP header for this call, and it is required for all Inventory API calls. See the HTTP request headers section for more information. For those who prefer to retrieve numerous inventory item records by SKU value with one call (up to 25 at a time), the bulkGetInventoryItem method can be used.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_api
from openapi_client.model.inventory_items import InventoryItems
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
    api_instance = inventory_item_api.InventoryItemApi(api_client)
    limit = "limit_example" # str | The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be an integer from 1 to 100. If this query parameter is not set, up to 100 records will be returned on each page of results. Min: 1, Max: 100 (optional)
    offset = "offset_example" # str | The value passed in this query parameter sets the page number to retrieve. The first page of records has a value of 0, the second page of records has a value of 1, and so on. If this query parameter is not set, its value defaults to 0, and the first page of records is returned. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_inventory_items(limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemApi->get_inventory_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be an integer from 1 to 100. If this query parameter is not set, up to 100 records will be returned on each page of results. Min: 1, Max: 100 | [optional]
 **offset** | **str**| The value passed in this query parameter sets the page number to retrieve. The first page of records has a value of 0, the second page of records has a value of 1, and so on. If this query parameter is not set, its value defaults to 0, and the first page of records is returned. | [optional]

### Return type

[**InventoryItems**](InventoryItems.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

