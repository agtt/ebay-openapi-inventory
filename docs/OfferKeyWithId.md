# OfferKeyWithId

This type is used by the getListingFees call to indicate the unpublished offer(s) for which expected listing fees will be retrieved. The user passes in one or more offerId values (a maximum of 250). See the Standard selling fees help page for more information on listing fees.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | The unique identifier of an unpublished offer for which expected listing fees will be retrieved. One to 250 offerId values can be passed in to the offers container for one getListingFees call. Errors will occur if offerId values representing published offers are passed in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


