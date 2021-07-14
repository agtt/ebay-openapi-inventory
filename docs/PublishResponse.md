# PublishResponse

This type is used by the base response payload of the publishOffer and publishOfferByInventoryItemGroup calls.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | The unique identifier of the newly created eBay listing. This field is returned if the single offer (if publishOffer call was used) or group of offers in an inventory item group (if publishOfferByInventoryItemGroup call was used) was successfully converted into an eBay listing. | [optional] 
**warnings** | [**[Error]**](Error.md) | This container will contain an array of errors and/or warnings if any occur when a publishOffer or publishOfferByInventoryItemGroup call is made. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


