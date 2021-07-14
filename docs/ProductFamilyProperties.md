# ProductFamilyProperties

This type is used to specify the details of a motor vehicle that is compatible with the inventory item specified through the SKU value in the call URI.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | **str** | This field indicates the specifications of the engine, including its size, block type, and fuel type. An example is 2.7L V6 gas DOHC naturally aspirated. This field is conditionally required, but should be supplied if known/applicable. | [optional] 
**make** | **str** | This field indicates the make of the vehicle (e.g. Toyota). This field is always required to identify a motor vehicle. | [optional] 
**model** | **str** | This field indicates the model of the vehicle (e.g. Camry). This field is always required to identify a motor vehicle. | [optional] 
**trim** | **str** | This field indicates the trim of the vehicle (e.g. 2-door Coupe). This field is conditionally required, but should be supplied if known/applicable. | [optional] 
**year** | **str** | This field indicates the year of the vehicle (e.g. 2016). This field is always required to identify a motor vehicle. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


