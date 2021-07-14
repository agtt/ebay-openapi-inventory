# OfferKeysWithId

This type is used by the base request payload of the getListingFees call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**[OfferKeyWithId]**](OfferKeyWithId.md) | This container is used to identify one or more (up to 250)unpublished offers for which expected listing fees will be retrieved. The user passes one or more offerId values (maximum of 250) in to this container to identify the unpublished offers in which to retrieve expected listing fees. This call is only applicable for offers in the unpublished state. The call response gives aggregate fee amounts per eBay marketplace, and does not give fee information at the individual offer level. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


