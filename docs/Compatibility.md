# Compatibility

This type is used by the createOrReplaceProductCompatibility call to associate compatible vehicles to an inventory item. This type is also the base response of the getProductCompatibility call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compatible_products** | [**[CompatibleProduct]**](CompatibleProduct.md) | This container consists of an array of motor vehicles (make, model, year, trim, engine) that are compatible with the motor vehicle part or accessory specified by the sku value. | [optional] 
**sku** | **str** | This is the seller-defined SKU value of the inventory item that will be associated with the compatible vehicles. This field is not applicable to the createOrReplaceProductCompatibility call, but it is always returned with the getProductCompatibility call. For the createOrReplaceProductCompatibility call, the SKU value for the inventory item is actually passed in as part of the call URI, and not in the request payload. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


