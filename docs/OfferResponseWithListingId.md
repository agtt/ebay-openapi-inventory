# OfferResponseWithListingId

This type is used to indicate the status of each offer that the user attempted to publish. If an offer is successfully published, an eBay listing ID (also known as an Item ID) is returned. If there is an issue publishing the offer and creating the new eBay listing, the information about why the listing failed should be returned in the errors and/or warnings containers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | This container will be returned if there were one or more errors associated with publishing the offer. | [optional] 
**listing_id** | **str** | The unique identifier of the newly-created eBay listing. This field is only returned if the seller successfully published the offer and created the new eBay listing. | [optional] 
**offer_id** | **str** | The unique identifier of the offer that the seller published (or attempted to publish). | [optional] 
**status_code** | **int** | The HTTP status code returned in this field indicates the success or failure of publishing the offer specified in the offerId field. See the HTTP status codes table to see which each status code indicates. | [optional] 
**warnings** | [**[Error]**](Error.md) | This container will be returned if there were one or more warnings associated with publishing the offer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


