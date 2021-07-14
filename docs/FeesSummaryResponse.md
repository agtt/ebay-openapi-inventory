# FeesSummaryResponse

This type is used by the base response payload for the getListingFees call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_summaries** | [**[FeeSummary]**](FeeSummary.md) | This container consists of an array of one or more listing fees that the seller can expect to pay for unpublished offers specified in the call request. Many fee types will get returned even when they are 0.0. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


