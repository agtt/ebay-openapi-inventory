# Offers

This type is used by the base response of the getOffers call, and it is an array of one or more of the seller's offers, along with pagination data.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | This is the URL to the current page of offers. | [optional] 
**limit** | **int** | This integer value is the number of offers that will be displayed on each results page. | [optional] 
**next** | **str** | This is the URL to the next page of offers. This field will only be returned if there are additional offers to view. | [optional] 
**offers** | [**[EbayOfferDetailsWithAll]**](EbayOfferDetailsWithAll.md) | This container is an array of one or more of the seller&#39;s offers for the SKU value that is passed in through the required sku query parameter. Note: Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the getOffers call will only return one offer. Max Occurs: 25 | [optional] 
**prev** | **str** | This is the URL to the previous page of offers. This field will only be returned if there are previous offers to view. | [optional] 
**size** | **int** | This integer value indicates the number of offers being displayed on the current page of results. This number will generally be the same as the limit value if there are additional pages of results to view. Note: Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the Get Offers call will only return one offer, so this value should always be 1. | [optional] 
**total** | **int** | This integer value is the total number of offers that exist for the specified SKU value. Based on this number and on the limit value, the seller may have to toggle through multiple pages to view all offers. Note: Currently, the Inventory API does not support the same SKU across multiple eBay marketplaces, so the Get Offers call will only return one offer, so this value should always be 1. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


