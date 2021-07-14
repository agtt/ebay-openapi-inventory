# OfferResponse

This type is used by the response payload of the createOffer and updateOffer calls. The offerId field contains the unique identifier for the offer if the offer is successfully created by the createOffer call. The warnings field contains any errors and/or warnings that may have been triggered by the call. Note: The offerId value is only returned with a successful createOffer call. This field will not be returned in the updateOffer response.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | The unique identifier of the offer that was just created with a createOffer call. It is not returned if the createOffer call fails to create an offer. This identifier will be needed for many offer-related calls. Note: The offerId value is only returned with a successful createOffer call. This field will not be returned in the updateOffer response. | [optional] 
**warnings** | [**[Error]**](Error.md) | This container will contain an array of errors and/or warnings when a call is made, and errors and/or warnings occur. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


