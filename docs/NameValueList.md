# NameValueList

This type is used by the compatibilityProperties container to identify a motor vehicle using name/value pairs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This string value identifies the motor vehicle aspect, such as &#39;make&#39;, &#39;model&#39;, &#39;year&#39;, &#39;trim&#39;, and &#39;engine&#39;. Typically, the make, model, and year of the motor vehicle are always required, with the trim and engine being necessary sometimes, but it will be dependent on the part or accessory, and on the vehicle class. | [optional] 
**value** | **str** | This string value identifies the motor vehicle aspect specified in the corresponding name field. For example, if the name field is &#39;make&#39;, this field may be &#39;Toyota&#39;, or if the name field is &#39;model&#39;, this field may be &#39;Camry&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


