# PackageWeightAndSize

This type is used to indicate the package type, weight, and dimensions of the shipping package. Package weight and dimensions are required when calculated shipping rates are used, and weight alone is required when flat-rate shipping is used, but with a weight surcharge. See the Calculated shipping help page for more information on calculated shipping.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensions** | [**Dimension**](Dimension.md) |  | [optional] 
**package_type** | **str** | This enumeration value indicates the type of shipping package used to ship the inventory item. The supported values for this field can be found in the PackageTypeEnum type. This field will be returned if the package type is set for the inventory item. Note: You can use the GeteBayDetails Trading API call to retrieve a list of supported package types for a specific marketplace. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:PackageTypeEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**weight** | [**Weight**](Weight.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


