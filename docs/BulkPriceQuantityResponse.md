# BulkPriceQuantityResponse

This type is use by the base response payload of the bulkUpdatePriceQuantity call. The bulkUpdatePriceQuantity call response will return an HTTP status code, offer ID, and SKU value for each offer/inventory item being updated, as well as an errors and/or warnings container if any errors or warnings are triggered while trying to update those offers/inventory items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**[PriceQuantityResponse]**](PriceQuantityResponse.md) | This container will return an HTTP status code, offer ID, and SKU value for each offer/inventory item being updated, as well as an errors and/or warnings container if any errors or warnings are triggered while trying to update those offers/inventory items. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


