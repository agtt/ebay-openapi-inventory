# Fee

This type is used to express expected listing fees that the seller may incur for one or more unpublished offers, as well as any eBay-related promotional discounts being applied toward a specific fee. These fees are the expected cumulative fees per eBay marketplace (which is indicated in the marketplaceId field).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) |  | [optional] 
**fee_type** | **str** | The value returned in this field indicates the type of listing fee that the seller may incur if one or more unpublished offers (offers are specified in the call request) are published on the marketplace specified in the marketplaceId field. Applicable listing fees will often include things such as InsertionFee or SubtitleFee, but many fee types will get returned even when they are 0.0. See the Standard selling fees help page for more information on listing fees. | [optional] 
**promotional_discount** | [**Amount**](Amount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


