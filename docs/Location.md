# Location

A complex type that is used to provide the physical address of a location, and it geo-coordinates.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**geo_coordinates** | [**GeoCoordinates**](GeoCoordinates.md) |  | [optional] 
**location_id** | **str** | A unique eBay-assigned ID for the location. Note: This field should not be confused with the seller-defined merchantLocationKey value. It is the merchantLocationKey value which is used to identify an inventory location when working with inventory location API calls. The locationId value is only used internally by eBay. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


