# openapi_client.LocationApi

All URIs are relative to *https://api.ebay.com/sell/inventory/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_inventory_location**](LocationApi.md#create_inventory_location) | **POST** /location/{merchantLocationKey} | 
[**delete_inventory_location**](LocationApi.md#delete_inventory_location) | **DELETE** /location/{merchantLocationKey} | 
[**disable_inventory_location**](LocationApi.md#disable_inventory_location) | **POST** /location/{merchantLocationKey}/disable | 
[**enable_inventory_location**](LocationApi.md#enable_inventory_location) | **POST** /location/{merchantLocationKey}/enable | 
[**get_inventory_location**](LocationApi.md#get_inventory_location) | **GET** /location/{merchantLocationKey} | 
[**get_inventory_locations**](LocationApi.md#get_inventory_locations) | **GET** /location | 
[**update_inventory_location**](LocationApi.md#update_inventory_location) | **POST** /location/{merchantLocationKey}/update_location_details | 


# **create_inventory_location**
> create_inventory_location(merchant_location_key, inventory_location_full)



Use this call to create a new inventory location. In order to create and publish an offer (and create an eBay listing), a seller must have at least one inventory location, as every offer must be associated with a location. Upon first creating an inventory location, only a seller-defined location identifier and a physical location is required, and once set, these values can not be changed. The unique identifier value (merchantLocationKey) is passed in at the end of the call URI. This merchantLocationKey value will be used in other Inventory Location calls to identify the inventory location to perform an action against. At this time, location types are either warehouse or store. Warehouse locations are used for traditional shipping, and store locations are generally used by US merchants selling products through the In-Store Pickup program, or used by UK, Australian, and German merchants selling products through the Click and Collect program. A full address is required for store inventory locations. However, for warehouse inventory locations, a full street address is not needed, but the city, state/province, and country of the location must be provided. Note that all inventory locations are &quot;enabled&quot; by default when they are created, and you must specifically disable them (by passing in a value of DISABLED in the merchantLocationStatus field) if you want them to be set to the disabled state. The seller's inventory cannot be loaded to inventory locations in the disabled state. In addition to the authorization header, which is required for all eBay REST API calls, the following table includes another request header that is mandatory for the createInventoryLocation call, and two other request headers that are optional: Header Description Required? Applicable Values Accept Describes the response encoding, as required by the caller. Currently, the interfaces require payloads formatted in JSON, and JSON is the default. No application/json Content-Language Use this header to control the language that is used for any returned errors or warnings in the call response. No en-US Content-Type The MIME type of the body of the request. Must be JSON. Yes application/json Unless one or more errors and/or warnings occur with the call, there is no response payload for this call. A successful call will return an HTTP status value of 204 No Content.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import location_api
from openapi_client.model.inventory_location_full import InventoryLocationFull
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
    api_instance = location_api.LocationApi(api_client)
    merchant_location_key = "merchantLocationKey_example" # str | A unique, merchant-defined key (ID) for an inventory location. This unique identifier, or key, is used in other Inventory API calls to identify an inventory location. Max length: 36
    inventory_location_full = InventoryLocationFull(
        location=LocationDetails(
            address=Address(
                address_line1="address_line1_example",
                address_line2="address_line2_example",
                city="city_example",
                country="country_example",
                county="county_example",
                postal_code="postal_code_example",
                state_or_province="state_or_province_example",
            ),
            geo_coordinates=GeoCoordinates(
                latitude=3.14,
                longitude=3.14,
            ),
        ),
        location_additional_information="location_additional_information_example",
        location_instructions="location_instructions_example",
        location_types=[
            "location_types_example",
        ],
        location_web_url="location_web_url_example",
        merchant_location_status="merchant_location_status_example",
        name="name_example",
        operating_hours=[
            OperatingHours(
                day_of_week_enum="day_of_week_enum_example",
                intervals=[
                    Interval(
                        close="close_example",
                        open="open_example",
                    ),
                ],
            ),
        ],
        phone="phone_example",
        special_hours=[
            SpecialHours(
                date="date_example",
                intervals=[
                    Interval(
                        close="close_example",
                        open="open_example",
                    ),
                ],
            ),
        ],
    ) # InventoryLocationFull | Inventory Location details

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_inventory_location(merchant_location_key, inventory_location_full)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationApi->create_inventory_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_location_key** | **str**| A unique, merchant-defined key (ID) for an inventory location. This unique identifier, or key, is used in other Inventory API calls to identify an inventory location. Max length: 36 |
 **inventory_location_full** | [**InventoryLocationFull**](InventoryLocationFull.md)| Inventory Location details |

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**409** | Location Already Exists |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inventory_location**
> delete_inventory_location(merchant_location_key)



This call deletes the inventory location that is specified in the merchantLocationKey path parameter. Note that deleting a location will not affect any active eBay listings associated with the deleted location, but the seller will not be able modify the offers associated with the inventory location once it is deleted. The authorization HTTP header is the only required request header for this call. Unless one or more errors and/or warnings occur with the call, there is no response payload for this call. A successful call will return an HTTP status value of 200 OK.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import location_api
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
    api_instance = location_api.LocationApi(api_client)
    merchant_location_key = "merchantLocationKey_example" # str | A unique merchant-defined key (ID) for an inventory location. This value is passed in at the end of the call URI to indicate the inventory location to be deleted. Max length: 36

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_inventory_location(merchant_location_key)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationApi->delete_inventory_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_location_key** | **str**| A unique merchant-defined key (ID) for an inventory location. This value is passed in at the end of the call URI to indicate the inventory location to be deleted. Max length: 36 |

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
**204** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_inventory_location**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} disable_inventory_location(merchant_location_key)



This call disables the inventory location that is specified in the merchantLocationKey path parameter. Sellers can not load/modify inventory to disabled inventory locations. Note that disabling an inventory location will not affect any active eBay listings associated with the disabled location, but the seller will not be able modify the offers associated with a disabled inventory location. The authorization HTTP header is the only required request header for this call. A successful call will return an HTTP status value of 200 OK.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import location_api
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
    api_instance = location_api.LocationApi(api_client)
    merchant_location_key = "merchantLocationKey_example" # str | A unique merchant-defined key (ID) for an inventory location. This value is passed in through the call URI to disable the specified inventory location. Max length: 36

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.disable_inventory_location(merchant_location_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationApi->disable_inventory_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_location_key** | **str**| A unique merchant-defined key (ID) for an inventory location. This value is passed in through the call URI to disable the specified inventory location. Max length: 36 |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **enable_inventory_location**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} enable_inventory_location(merchant_location_key)



This call enables a disabled inventory location that is specified in the merchantLocationKey path parameter. Once a disabled inventory location is enabled, sellers can start loading/modifying inventory to that inventory location. The authorization HTTP header is the only required request header for this call. A successful call will return an HTTP status value of 200 OK.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import location_api
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
    api_instance = location_api.LocationApi(api_client)
    merchant_location_key = "merchantLocationKey_example" # str | A unique merchant-defined key (ID) for an inventory location. This value is passed in through the call URI to specify the disabled inventory location to enable. Max length: 36

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.enable_inventory_location(merchant_location_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationApi->enable_inventory_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_location_key** | **str**| A unique merchant-defined key (ID) for an inventory location. This value is passed in through the call URI to specify the disabled inventory location to enable. Max length: 36 |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **get_inventory_location**
> InventoryLocationResponse get_inventory_location(merchant_location_key)



This call retrieves all defined details of the inventory location that is specified by the merchantLocationKey path parameter. The authorization HTTP header is the only required request header for this call. A successful call will return an HTTP status value of 200 OK.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import location_api
from openapi_client.model.inventory_location_response import InventoryLocationResponse
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
    api_instance = location_api.LocationApi(api_client)
    merchant_location_key = "merchantLocationKey_example" # str | A unique merchant-defined key (ID) for an inventory location. This value is passed in at the end of the call URI to specify the inventory location to retrieve. Max length: 36

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_inventory_location(merchant_location_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationApi->get_inventory_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_location_key** | **str**| A unique merchant-defined key (ID) for an inventory location. This value is passed in at the end of the call URI to specify the inventory location to retrieve. Max length: 36 |

### Return type

[**InventoryLocationResponse**](InventoryLocationResponse.md)

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

# **get_inventory_locations**
> LocationResponse get_inventory_locations()



This call retrieves all defined details for every inventory location associated with the seller's account. There are no required parameters for this call and no request payload. However, there are two optional query parameters, limit and offset. The limit query parameter sets the maximum number of inventory locations returned on one page of data, and the offset query parameter specifies the page of data to return. These query parameters are discussed more in the URI parameters table below. The authorization HTTP header is the only required request header for this call. A successful call will return an HTTP status value of 200 OK.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import location_api
from openapi_client.model.location_response import LocationResponse
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
    api_instance = location_api.LocationApi(api_client)
    limit = "limit_example" # str | The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results. Min: 1 (optional)
    offset = "offset_example" # str | Specifies the number of locations to skip in the result set before returning the first location in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0 (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_inventory_locations(limit=limit, offset=offset)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationApi->get_inventory_locations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| The value passed in this query parameter sets the maximum number of records to return per page of data. Although this field is a string, the value passed in this field should be a positive integer value. If this query parameter is not set, up to 100 records will be returned on each page of results. Min: 1 | [optional]
 **offset** | **str**| Specifies the number of locations to skip in the result set before returning the first location in the paginated response. Combine offset with the limit query parameter to control the items returned in the response. For example, if you supply an offset of 0 and a limit of 10, the first page of the response contains the first 10 items from the complete list of items retrieved by the call. If offset is 10 and limit is 20, the first page of the response contains items 11-30 from the complete result set. Default: 0 | [optional]

### Return type

[**LocationResponse**](LocationResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inventory_location**
> update_inventory_location(merchant_location_key, inventory_location)



Use this call to update non-physical location details for an existing inventory location. Specify the inventory location you want to update using the merchantLocationKey path parameter. You can update the following text-based fields: name, phone, locationWebUrl, locationInstructions and locationAdditionalInformation. Whatever text is passed in for these fields in an updateInventoryLocation call will replace the current text strings defined for these fields. For store inventory locations, the operating hours and/or the special hours can also be updated. The merchant location key, the physical location of the store, and its geo-location coordinates can not be updated with an updateInventoryLocation call In addition to the authorization header, which is required for all eBay REST API calls, the following table includes another request header that is mandatory for the updateInventoryLocation call, and two other request headers that are optional: Header Description Required? Applicable Values Accept Describes the response encoding, as required by the caller. Currently, the interfaces require payloads formatted in JSON, and JSON is the default. No application/json Content-Language Use this header to control the language that is used for any returned errors or warnings in the call response. No en-US Content-Type The MIME type of the body of the request. Must be JSON. Yes application/json Unless one or more errors and/or warnings occurs with the call, there is no response payload for this call. A successful call will return an HTTP status value of 204 No Content.

### Example

* OAuth Authentication (api_auth):
```python
import time
import openapi_client
from openapi_client.api import location_api
from openapi_client.model.inventory_location import InventoryLocation
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
    api_instance = location_api.LocationApi(api_client)
    merchant_location_key = "merchantLocationKey_example" # str | A unique merchant-defined key (ID) for an inventory location. This value is passed in the call URI to indicate the inventory location to be updated. Max length: 36
    inventory_location = InventoryLocation(
        location_additional_information="location_additional_information_example",
        location_instructions="location_instructions_example",
        location_web_url="location_web_url_example",
        name="name_example",
        operating_hours=[
            OperatingHours(
                day_of_week_enum="day_of_week_enum_example",
                intervals=[
                    Interval(
                        close="close_example",
                        open="open_example",
                    ),
                ],
            ),
        ],
        phone="phone_example",
        special_hours=[
            SpecialHours(
                date="date_example",
                intervals=[
                    Interval(
                        close="close_example",
                        open="open_example",
                    ),
                ],
            ),
        ],
    ) # InventoryLocation | The inventory location details to be updated (other than the address and geo co-ordinates).

    # example passing only required values which don't have defaults set
    try:
        api_instance.update_inventory_location(merchant_location_key, inventory_location)
    except openapi_client.ApiException as e:
        print("Exception when calling LocationApi->update_inventory_location: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_location_key** | **str**| A unique merchant-defined key (ID) for an inventory location. This value is passed in the call URI to indicate the inventory location to be updated. Max length: 36 |
 **inventory_location** | [**InventoryLocation**](InventoryLocation.md)| The inventory location details to be updated (other than the address and geo co-ordinates). |

### Return type

void (empty response body)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

