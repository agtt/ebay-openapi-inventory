# AvailabilityWithAll

This type is used to specify the quantity of the inventory items that are available for purchase if the items will be shipped to the buyer, and the quantity of the inventory items that are available for In-Store Pickup at one or more of the merchant's physical stores. In-Store Pickup is only available to large merchants selling on the US, UK, Germany, and Australia sites.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_at_location_availability** | [**[PickupAtLocationAvailability]**](PickupAtLocationAvailability.md) | This container consists of an array of one or more of the merchant&#39;s physical stores where the inventory item is available for in-store pickup. The store ID, the quantity available, and the fulfillment time (how soon the item will be ready for pickup after the order occurs) are all returned in this container. | [optional] 
**ship_to_location_availability** | [**ShipToLocationAvailabilityWithAll**](ShipToLocationAvailabilityWithAll.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


