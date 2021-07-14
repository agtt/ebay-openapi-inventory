# Weight

This type is used to specify the weight (and the unit used to measure that weight) of a shipping package. The weight container is conditionally required if the seller will be offering calculated shipping rates to determine shipping cost, or is using flat-rate costs, but charging a weight surcharge. See the Calculated shipping help page for more information on calculated shipping.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str** | The unit of measurement used to specify the weight of a shipping package. Both the unit and value fields are required if the weight container is used. If the English system of measurement is being used, the applicable values for weight units are POUND and OUNCE. If the metric system of measurement is being used, the applicable values for weight units are KILOGRAM and GRAM. The metric system is used by most countries outside of the US. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:WeightUnitOfMeasureEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**value** | **float** | The actual weight (in the measurement unit specified in the unit field) of the shipping package. Both the unit and value fields are required if the weight container is used. If a shipping package weighed 20.5 ounces, the container would look as follows: &amp;quot;weight&amp;quot;: {  &amp;quot;value&amp;quot;: 20.5,  &amp;quot;unit&amp;quot;: &amp;quot;OUNCE&amp;quot;  } | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


