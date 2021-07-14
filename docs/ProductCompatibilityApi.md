# openapi_client.ProductCompatibilityApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_replace_product_compatibility**](ProductCompatibilityApi.md#create_or_replace_product_compatibility) | **PUT** /inventory_item/{sku}/product_compatibility | 
[**delete_product_compatibility**](ProductCompatibilityApi.md#delete_product_compatibility) | **DELETE** /inventory_item/{sku}/product_compatibility | 
[**get_product_compatibility**](ProductCompatibilityApi.md#get_product_compatibility) | **GET** /inventory_item/{sku}/product_compatibility | 


# **create_or_replace_product_compatibility**
> BaseResponse create_or_replace_product_compatibility(content_language, sku, compatibility)



This call is used by the seller to create or replace a list of products that are compatible with the inventory item. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future. In addition to the authorization header, which is required for all eBay REST API calls, the createOrReplaceProductCompatibility call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import product_compatibility_api
from openapi_client.model.base_response import BaseResponse
from openapi_client.model.compatibility import Compatibility
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
    api_instance = product_compatibility_api.ProductCompatibilityApi(api_client)
    content_language = "Content-Language_example" # str | This request header sets the natural language that will be provided in the field values of the request payload.
    sku = "sku_example" # str | A SKU (stock keeping unit) is an unique identifier defined by a seller for a product
    compatibility = Compatibility(
        compatible_products=[
            CompatibleProduct(
                compatibility_properties=[
                    NameValueList(
                        name="name_example",
                        value="value_example",
                    ),
                ],
                notes="notes_example",
                product_family_properties=ProductFamilyProperties(
                    engine="engine_example",
                    make="make_example",
                    model="model_example",
                    trim="trim_example",
                    year="year_example",
                ),
                product_identifier=ProductIdentifier(
                    epid="epid_example",
                    gtin="gtin_example",
                    ktype="ktype_example",
                ),
            ),
        ],
        sku="sku_example",
    ) # Compatibility | Details of the compatibility

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_or_replace_product_compatibility(content_language, sku, compatibility)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductCompatibilityApi->create_or_replace_product_compatibility: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_language** | **str**| This request header sets the natural language that will be provided in the field values of the request payload. |
 **sku** | **str**| A SKU (stock keeping unit) is an unique identifier defined by a seller for a product |
 **compatibility** | [**Compatibility**](Compatibility.md)| Details of the compatibility |

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

# **delete_product_compatibility**
> delete_product_compatibility(sku)



This call is used by the seller to delete the list of products that are compatible with the inventory item that is associated with the compatible product list. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import product_compatibility_api
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
    api_instance = product_compatibility_api.ProductCompatibilityApi(api_client)
    sku = "sku_example" # str | A SKU (stock keeping unit) is an unique identifier defined by a seller for a product

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_product_compatibility(sku)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductCompatibilityApi->delete_product_compatibility: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| A SKU (stock keeping unit) is an unique identifier defined by a seller for a product |

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

# **get_product_compatibility**
> Compatibility get_product_compatibility(sku)



This call is used by the seller to retrieve the list of products that are compatible with the inventory item. The SKU value for the inventory item is passed into the call URI, and a successful call with return the compatible vehicle list associated with this inventory item. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import product_compatibility_api
from openapi_client.model.compatibility import Compatibility
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
    api_instance = product_compatibility_api.ProductCompatibilityApi(api_client)
    sku = "sku_example" # str | A SKU (stock keeping unit) is an unique identifier defined by a seller for a product

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_product_compatibility(sku)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProductCompatibilityApi->get_product_compatibility: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**| A SKU (stock keeping unit) is an unique identifier defined by a seller for a product |

### Return type

[**Compatibility**](Compatibility.md)

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

