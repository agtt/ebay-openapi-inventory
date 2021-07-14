# ListingDetails

This type is used by the listing container in the getOffer and getOffers calls to provide the eBay listing ID, the listing status, and quantity sold for the offer. The listing container is only returned for published offers, and is not returned for unpublished offers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | The unique identifier of the eBay listing that is associated with the published offer. | [optional] 
**listing_status** | **str** | The enumeration value returned in this field indicates the status of the listing that is associated with the published offer. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingStatusEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**sold_quantity** | **int** | This integer value indicates the quantity of the product that has been sold for the published offer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


