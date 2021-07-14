# BaseResponse

This is the base response of the createOrReplaceInventoryItem, createOrReplaceInventoryItemGroup, and createOrReplaceProductCompatibility calls. A response payload will only be returned for these three calls if one or more errors or warnings occur with the call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | [**[Error]**](Error.md) | This container will be returned in a call response payload if one or more warnings or errors are triggered when an Inventory API call is made. This container will contain detailed information about the error or warning. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


