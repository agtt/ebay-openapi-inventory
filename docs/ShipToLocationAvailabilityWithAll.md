# ShipToLocationAvailabilityWithAll

This type is used to specify the total 'ship-to-home' quantity of the inventory items that will be available for purchase through one or more published offers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocation_by_format** | [**FormatAllocation**](FormatAllocation.md) |  | [optional] 
**availability_distributions** | [**[AvailabilityDistribution]**](AvailabilityDistribution.md) | This container is used to set the available quantity of the inventory item at one or more warehouse locations. This container will be returned if the available quantity is set for one or more inventory locations. | [optional] 
**quantity** | **int** | This container is used to set the total &#39;ship-to-home&#39; quantity of the inventory item that will be available for purchase through one or more published offers. This container is not immediately required, but &#39;ship-to-home&#39; quantity must be set before an offer of the inventory item can be published. If an existing inventory item is being updated, and the &#39;ship-to-home&#39; quantity already exists for the inventory item record, this container should be included again, even if the value is not changing, or the available quantity data will be lost. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


