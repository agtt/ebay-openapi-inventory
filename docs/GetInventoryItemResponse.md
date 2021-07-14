# GetInventoryItemResponse

This type is used by the response of the bulkGetInventoryItem method to give the status of each inventory item record that the user tried to retrieve.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | This container will be returned if there were one or more errors associated with retrieving the inventory item record. | [optional] 
**inventory_item** | [**InventoryItemWithSkuLocaleGroupKeys**](InventoryItemWithSkuLocaleGroupKeys.md) |  | [optional] 
**sku** | **str** | The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The seller should have a unique SKU value for every product that they sell. | [optional] 
**status_code** | **int** | The HTTP status code returned in this field indicates the success or failure of retrieving the inventory item record for the inventory item specified in the sku field. See the HTTP status codes table to see which each status code indicates. | [optional] 
**warnings** | [**[Error]**](Error.md) | This container will be returned if there were one or more warnings associated with retrieving the inventory item record. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


