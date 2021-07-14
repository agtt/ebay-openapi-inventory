# PickupAtLocationAvailability

This type is used to specify/indicate the quantity of the inventory item that is available for an In-Store Pickup order at the merchant's physical store (specified by the merchantLocationKey field).

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability_type** | **str** | The enumeration value in this field indicates the availability status of the inventory item at the merchant&#39;s physical store specified by the pickupAtLocationAvailability.merchantLocationKey field. This field is required if the pickupAtLocationAvailability container is used, and is always returned with the pickupAtLocationAvailability container. See AvailabilityTypeEnum for more information about how/when you use each enumeration value. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:AvailabilityTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**fulfillment_time** | [**TimeDuration**](TimeDuration.md) |  | [optional] 
**merchant_location_key** | **str** | The unique identifier of a merchant&#39;s store where the In-Store Pickup inventory item is currently located, or where inventory will be sent to. If the merchant&#39;s store is currently awaiting for inventory, the availabilityType value should be SHIP_TO_STORE. This field is required if the pickupAtLocationAvailability container is used, and is always returned with the pickupAtLocationAvailability container. Max length: 36 | [optional] 
**quantity** | **int** | This integer value indicates the quantity of the inventory item that is available for In-Store Pickup at the store identified by the merchantLocationKey value. The value of quantity should be an integer value greater than 0, unless the inventory item is out of stock. This field is required if the pickupAtLocationAvailability container is used, and is always returned with the pickupAtLocationAvailability container. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


