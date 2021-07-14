# openapi_client.InventoryItemGroupApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_replace_inventory_item_group**](InventoryItemGroupApi.md#create_or_replace_inventory_item_group) | **PUT** /inventory_item_group/{inventoryItemGroupKey} | 
[**delete_inventory_item_group**](InventoryItemGroupApi.md#delete_inventory_item_group) | **DELETE** /inventory_item_group/{inventoryItemGroupKey} | 
[**get_inventory_item_group**](InventoryItemGroupApi.md#get_inventory_item_group) | **GET** /inventory_item_group/{inventoryItemGroupKey} | 


# **create_or_replace_inventory_item_group**
> BaseResponse create_or_replace_inventory_item_group(content_language, inventory_item_group_key, inventory_item_group)



This call creates a new inventory item group or updates an existing inventory item group. It is up to sellers whether they want to create a complete inventory item group record right from the start, or sellers can provide only some information with the initial createOrReplaceInventoryItemGroup call, and then make one or more additional createOrReplaceInventoryItemGroup calls to complete the inventory item group record. Upon first creating an inventory item group record, the only required elements are the inventoryItemGroupKey identifier in the call URI, and the members of the inventory item group specified through the variantSKUs array in the request payload. In the case of updating/replacing an existing inventory item group, this call does a complete replacement of the existing inventory item group record, so all fields (including the member SKUs) that make up the inventory item group are required, regardless of whether their values changed. So, when replacing/updating an inventory item group record, it is advised that the seller run a getInventoryItemGroup call for that inventory item group to see all of its current values/settings/members before attempting to update the record. And if changes are made to an inventory item group that is part of a live, multiple-variation eBay listing, these changes automatically update the eBay listing. For example, if a SKU value is removed from the inventory item group, the corresponding product variation will be removed from the eBay listing as well. In addition to the required inventory item group identifier and member SKUs, other key information that is set with this call include: Title and description of the inventory item group. The string values provided in these fields will actually become the listing title and listing description of the listing once the first SKU of the inventory item group is published successfully Common aspects that inventory items in the qroup share Product aspects that vary within each product variation Links to images demonstrating the variations of the product, and these images should correspond to the product aspect that is set with the variesBy.aspectsImageVariesBy field In addition to the authorization header, which is required for all eBay REST API calls, the createOrReplaceInventoryItemGroup call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_group_api
from openapi_client.model.base_response import BaseResponse
from openapi_client.model.inventory_item_group import InventoryItemGroup
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
    api_instance = inventory_item_group_api.InventoryItemGroupApi(api_client)
    content_language = "Content-Language_example" # str | This request header sets the natural language that will be provided in the field values of the request payload.
    inventory_item_group_key = "inventoryItemGroupKey_example" # str | Unique identifier of the inventory item group. This identifier is supplied by the seller. The inventoryItemGroupKey value for the inventory item group to create/update is passed in at the end of the call URI. This value cannot be changed once it is set.
    inventory_item_group = InventoryItemGroup(
        aspects=[
            "aspects_example",
        ],
        description="description_example",
        image_urls=[
            "image_urls_example",
        ],
        inventory_item_group_key="inventory_item_group_key_example",
        subtitle="subtitle_example",
        title="title_example",
        variant_skus=[
            "variant_skus_example",
        ],
        varies_by=VariesBy(
            aspects_image_varies_by=[
                "aspects_image_varies_by_example",
            ],
            specifications=[
                Specification(
                    name="name_example",
                    values=[
                        "values_example",
                    ],
                ),
            ],
        ),
    ) # InventoryItemGroup | Details of the inventory Item Group

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_replace_inventory_item_group(content_language, inventory_item_group_key, inventory_item_group)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemGroupApi->create_or_replace_inventory_item_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This request header sets the natural language that will be provided in the field values of the request payload. |
 **inventory_item_group_key** | **str**| Unique identifier of the inventory item group. This identifier is supplied by the seller. The inventoryItemGroupKey value for the inventory item group to create/update is passed in at the end of the call URI. This value cannot be changed once it is set. |
 **inventory_item_group** | [**InventoryItemGroup**](InventoryItemGroup.md)| Details of the inventory Item Group |

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

# **delete_inventory_item_group**
> delete_inventory_item_group(inventory_item_group_key)



This call deletes the inventory item group for a given inventoryItemGroupKey value.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_group_api
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
    api_instance = inventory_item_group_api.InventoryItemGroupApi(api_client)
    inventory_item_group_key = "inventoryItemGroupKey_example" # str | The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to delete is passed in at the end of the call URI.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_inventory_item_group(inventory_item_group_key)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemGroupApi->delete_inventory_item_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_group_key** | **str**| The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to delete is passed in at the end of the call URI. |

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

# **get_inventory_item_group**
> InventoryItemGroup get_inventory_item_group(inventory_item_group_key)



This call retrieves the inventory item group for a given inventoryItemGroupKey value. The inventoryItemGroupKey value is passed in at the end of the call URI.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import inventory_item_group_api
from openapi_client.model.inventory_item_group import InventoryItemGroup
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
    api_instance = inventory_item_group_api.InventoryItemGroupApi(api_client)
    inventory_item_group_key = "inventoryItemGroupKey_example" # str | The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to retrieve is passed in at the end of the call URI.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_inventory_item_group(inventory_item_group_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling InventoryItemGroupApi->get_inventory_item_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inventory_item_group_key** | **str**| The unique identifier of an inventory item group. This value is assigned by the seller when an inventory item group is created. The inventoryItemGroupKey value for the inventory item group to retrieve is passed in at the end of the call URI. |

### Return type

[**InventoryItemGroup**](InventoryItemGroup.md)

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

