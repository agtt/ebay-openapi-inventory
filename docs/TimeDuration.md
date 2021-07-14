# TimeDuration

This type is used to indicate the fulfillment time for an In-Store Pickup order, or for an order than will be shipped to the buyer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | This enumeration value indicates the time unit used to specify the fulfillment time, such as HOUR or BUSINESS_DAY. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:TimeDurationUnitEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**value** | **int** | The integer value in this field, along with the time unit in the unit field, will indicate the fulfillment time. For In-Store Pickup orders, this value will indicate how soon after an In-Store Pickup purchase can the buyer pick up the item at the designated store location. If the value of this field is 4, and the value of the unit field is HOUR, then the fulfillment time for the In-Store Pickup order is four hours, which means that the buyer will be able to pick up the item at the store four hours after the transaction took place. For standard orders that will be shipped, this value will indicate the expected fulfillment time if the inventory item is shipped from the inventory location. If the value of this field is 4, and the value of the unit field is BUSINESS_DAY, then the estimated delivery date after purchase is 4 business days. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


