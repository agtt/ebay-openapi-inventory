# Dimension

This type is used to specify the dimensions (and the unit used to measure those dimensions) of a shipping package. The dimensions container is conditionally required if the seller will be offering calculated shipping rates to determine shipping cost. See the Calculated shipping help page for more information on calculated shipping.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | The actual height (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &amp;quot;dimensions&amp;quot;: {  &amp;quot;length&amp;quot;: 21.5,  &amp;quot;width&amp;quot;: 15.0,  &amp;quot;height&amp;quot;: 12.0,  &amp;quot;unit&amp;quot;: &amp;quot;INCH&amp;quot;  } | [optional] 
**length** | **float** | The actual length (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &amp;quot;dimensions&amp;quot;: {  &amp;quot;length&amp;quot;: 21.5,  &amp;quot;width&amp;quot;: 15.0,  &amp;quot;height&amp;quot;: 12.0,  &amp;quot;unit&amp;quot;: &amp;quot;INCH&amp;quot;  } | [optional] 
**unit** | **str** | The unit of measurement used to specify the dimensions of a shipping package. All fields of the dimensions container are required if package dimensions are specified. If the English system of measurement is being used, the applicable values for dimension units are FEET and INCH. If the metric system of measurement is being used, the applicable values for weight units are METER and CENTIMETER. The metric system is used by most countries outside of the US. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:LengthUnitOfMeasureEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**width** | **float** | The actual width (in the measurement unit specified in the unit field) of the shipping package. All fields of the dimensions container are required if package dimensions are specified. If a shipping package measured 21.5 inches in length, 15.0 inches in width, and 12.0 inches in height, the dimensions container would look as follows: &amp;quot;dimensions&amp;quot;: {  &amp;quot;length&amp;quot;: 21.5,  &amp;quot;width&amp;quot;: 15.0,  &amp;quot;height&amp;quot;: 12.0,  &amp;quot;unit&amp;quot;: &amp;quot;INCH&amp;quot;  } | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


