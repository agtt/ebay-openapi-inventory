# AvailabilityDistribution

This type is used to set the available quantity of the inventory item at one or more warehouse locations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fulfillment_time** | [**TimeDuration**](TimeDuration.md) |  | [optional] 
**merchant_location_key** | **str** | The unique identifier of an inventory location where quantity is available for the inventory item. This field is conditionally required to identify the inventory location that has quantity of the inventory item. | [optional] 
**quantity** | **int** | The integer value passed into this field indicates the quantity of the inventory item that is available at this inventory location. This field is conditionally required. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


