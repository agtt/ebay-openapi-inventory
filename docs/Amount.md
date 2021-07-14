# Amount

This type is used to express a dollar value and the applicable currency.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | A three-digit string value respresenting the type of currency being used. Both the value and currency fields are required/always returned when expressing prices. See the CurrencyCodeEnum type for the full list of currencies and their corresponding three-digit string values. | [optional] 
**value** | **str** | A string representation of a dollar value expressed in the currency specified in the currency field. Both the value and currency fields are required/always returned when expressing prices. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


