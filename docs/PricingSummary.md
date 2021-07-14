# PricingSummary

This type is used to specify the listing price for the product and settings for the Minimum Advertised Price and Strikethrough Pricing features. The price field must be supplied before an offer is published, but a seller may create an offer without supplying a price initially. The Minimum Advertised Price feature is only available on the US site. Strikethrough Pricing is available on the US, eBay Motors, UK, Germany, Canada (English and French), France, Italy, and Spain sites.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auction_reserve_price** | [**Amount**](Amount.md) |  | [optional] 
**auction_start_price** | [**Amount**](Amount.md) |  | [optional] 
**minimum_advertised_price** | [**Amount**](Amount.md) |  | [optional] 
**originally_sold_for_retail_price_on** | **str** | This field is needed if the Strikethrough Pricing (STP) feature will be used in the offer. This field indicates that the product was sold for the price in the originalRetailPrice field on an eBay site, or sold for that price by a third-party retailer. When using the createOffer or updateOffer calls, the seller will pass in a value of ON_EBAY to indicate that the product was sold for the originalRetailPrice on an eBay site, or the seller will pass in a value of OFF_EBAY to indicate that the product was sold for the originalRetailPrice through a third-party retailer. This field and the originalRetailPrice field are only applicable if the seller and listing are eligible to use the Strikethrough Pricing feature, a feature which is limited to the US (core site and Motors), UK, Germany, Canada (English and French versions), France, Italy, and Spain sites. This field will be returned if set for the offer. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:SoldOnEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**original_retail_price** | [**Amount**](Amount.md) |  | [optional] 
**price** | [**Amount**](Amount.md) |  | [optional] 
**pricing_visibility** | **str** | This field is needed if the Minimum Advertised Price (MAP) feature will be used in the offer. This field is only applicable if an eligible US seller is using the Minimum Advertised Price (MAP) feature and a minimumAdvertisedPrice has been specified. The value set in this field will determine whether the MAP price is shown to a prospective buyer prior to checkout through a pop-up window accessed from the View Item page, or if the MAP price is not shown until the checkout flow after the buyer has already committed to buying the item. To show the MAP price prior to checkout, the seller will set this value to PRE_CHECKOUT. To show the MAP price after the buyer already commits to buy the item, the seller will set this value to DURING_CHECKOUT. This field will be ignored if the seller and/or the listing is not eligible for the MAP feature. This field will be returned if set for the offer. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:MinimumAdvertisedPriceHandlingEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


