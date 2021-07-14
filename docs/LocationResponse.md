# LocationResponse

This type is used by the base response payload for the getInventoryLocations call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | The URI of the current page of results from the result set. | [optional] 
**limit** | **int** | The number of items returned on a single page from the result set. | [optional] 
**next** | **str** | The URI for the following page of results. This value is returned only if there is an additional page of results to display from the result set. Max length: 2048 | [optional] 
**offset** | **int** | The number of results skipped in the result set before listing the first returned result. This value is set in the request with the offset query parameter. Note: The items in a paginated result set use a zero-based list where the first item in the list has an offset of 0. | [optional] 
**prev** | **str** | The URI for the preceding page of results. This value is returned only if there is a previous page of results to display from the result set. Max length: 2048 | [optional] 
**total** | **int** | The total number of items retrieved in the result set. If no items are found, this field is returned with a value of 0. | [optional] 
**locations** | [**[InventoryLocationResponse]**](InventoryLocationResponse.md) | An array of one or more of the merchant&#39;s inventory locations. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


