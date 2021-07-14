# OfferSkuResponse

This type is used by the bulkCreateOffer response to show the status of each offer that the seller attempted to create with the bulkCreateOffer method. For each offer that is created successfully, the returned statusCode value should be 200, and a unique offerId should be created for each offer. If any issues occur with the creation of any offers, errors and/or warnings containers will be returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | This container will be returned at the offer level, and will contain one or more errors if any occurred with the attempted creation of the corresponding offer. | [optional] 
**format** | **str** | This enumeration value indicates the listing format of the offer. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:FormatTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**marketplace_id** | **str** | This enumeration value is the unique identifier of the eBay marketplace for which the offer will be made available. This enumeration value should be the same for all offers since the bulkCreateOffer method can only be used to create offers for one eBay marketplace at a time. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**offer_id** | **str** | The unique identifier of the newly-created offer. This identifier should be automatically created by eBay if the creation of the offer was successful. It is not returned if the creation of the offer was not successful. In which case, the user may want to scan the corresponding errors and/or warnings container to see what the issue may be. | [optional] 
**sku** | **str** | The seller-defined Stock-Keeping Unit (SKU) of the inventory item. The sku value is required for each product offer that the seller is trying to create, and it is always returned to identified the product that is associated with the offer. | [optional] 
**status_code** | **int** | The integer value returned in this field is the http status code. If an offer is created successfully, the value returned in this field should be 200. A user can view the HTTP status codes section for information on other status codes that may be returned with the bulkCreateOffer method. | [optional] 
**warnings** | [**[Error]**](Error.md) | This container will be returned at the offer level, and will contain one or more warnings if any occurred with the attempted creation of the corresponding offer. Note that it is possible that an offer can be created successfully even if one or more warnings are triggered. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


