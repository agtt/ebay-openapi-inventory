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
from openapi_client.model.base_response import BaseResponse
from openapi_client.model.compatibility import Compatibility


class ProductCompatibilityApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_or_replace_product_compatibility(
            self,
            content_language,
            sku,
            compatibility,
            **kwargs
        ):
            """create_or_replace_product_compatibility  # noqa: E501

            This call is used by the seller to create or replace a list of products that are compatible with the inventory item. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future. In addition to the authorization header, which is required for all eBay REST API calls, the createOrReplaceProductCompatibility call also requires the Content-Language header, that sets the natural language that will be used in the field values of the request payload. For US English, the code value passed in this header should be en-US. To view other supported Content-Language values, and to read more about all supported HTTP headers for eBay REST API calls, see the HTTP request headers topic in the Using eBay RESTful APIs document.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_or_replace_product_compatibility(content_language, sku, compatibility, async_req=True)
            >>> result = thread.get()

            Args:
                content_language (str): This request header sets the natural language that will be provided in the field values of the request payload.
                sku (str): A SKU (stock keeping unit) is an unique identifier defined by a seller for a product
                compatibility (Compatibility): Details of the compatibility

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
                BaseResponse
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
            kwargs['content_language'] = \
                content_language
            kwargs['sku'] = \
                sku
            kwargs['compatibility'] = \
                compatibility
            return self.call_with_http_info(**kwargs)

        self.create_or_replace_product_compatibility = _Endpoint(
            settings={
                'response_type': (BaseResponse,),
                'auth': [
                    'api_auth'
                ],
                'endpoint_path': '/inventory_item/{sku}/product_compatibility',
                'operation_id': 'create_or_replace_product_compatibility',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'content_language',
                    'sku',
                    'compatibility',
                ],
                'required': [
                    'content_language',
                    'sku',
                    'compatibility',
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
                    'content_language':
                        (str,),
                    'sku':
                        (str,),
                    'compatibility':
                        (Compatibility,),
                },
                'attribute_map': {
                    'content_language': 'Content-Language',
                    'sku': 'sku',
                },
                'location_map': {
                    'content_language': 'header',
                    'sku': 'path',
                    'compatibility': 'body',
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
            callable=__create_or_replace_product_compatibility
        )

        def __delete_product_compatibility(
            self,
            sku,
            **kwargs
        ):
            """delete_product_compatibility  # noqa: E501

            This call is used by the seller to delete the list of products that are compatible with the inventory item that is associated with the compatible product list. The inventory item is identified with a SKU value in the URI. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_product_compatibility(sku, async_req=True)
            >>> result = thread.get()

            Args:
                sku (str): A SKU (stock keeping unit) is an unique identifier defined by a seller for a product

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
                None
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
            kwargs['sku'] = \
                sku
            return self.call_with_http_info(**kwargs)

        self.delete_product_compatibility = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'api_auth'
                ],
                'endpoint_path': '/inventory_item/{sku}/product_compatibility',
                'operation_id': 'delete_product_compatibility',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'sku',
                ],
                'required': [
                    'sku',
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
                    'sku':
                        (str,),
                },
                'attribute_map': {
                    'sku': 'sku',
                },
                'location_map': {
                    'sku': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_product_compatibility
        )

        def __get_product_compatibility(
            self,
            sku,
            **kwargs
        ):
            """get_product_compatibility  # noqa: E501

            This call is used by the seller to retrieve the list of products that are compatible with the inventory item. The SKU value for the inventory item is passed into the call URI, and a successful call with return the compatible vehicle list associated with this inventory item. Product compatibility is currently only applicable to motor vehicle parts and accessory categories, but more categories may be supported in the future.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_product_compatibility(sku, async_req=True)
            >>> result = thread.get()

            Args:
                sku (str): A SKU (stock keeping unit) is an unique identifier defined by a seller for a product

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
                Compatibility
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
            kwargs['sku'] = \
                sku
            return self.call_with_http_info(**kwargs)

        self.get_product_compatibility = _Endpoint(
            settings={
                'response_type': (Compatibility,),
                'auth': [
                    'api_auth'
                ],
                'endpoint_path': '/inventory_item/{sku}/product_compatibility',
                'operation_id': 'get_product_compatibility',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sku',
                ],
                'required': [
                    'sku',
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
                    'sku':
                        (str,),
                },
                'attribute_map': {
                    'sku': 'sku',
                },
                'location_map': {
                    'sku': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_product_compatibility
        )
