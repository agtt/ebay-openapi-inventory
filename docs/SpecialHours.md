# SpecialHours

This type is used to express the special operating hours of a store location on a specific date. A specialHours container is needed when the store's opening hours on a specific date are different than the normal operating hours on that particular day of the week.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **str** | A date value is required for each specific date that the store location has special operating hours. The timestamp is formatted as an ISO 8601 string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Format: [YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z Example: 2018-08-04T07:09:00.000Z This field is returned if set for the store location. | [optional] 
**intervals** | [**[Interval]**](Interval.md) | This container is used to define the opening and closing times of a store on a specific date (defined in the date field). An intervals container is needed for each specific date that the store has special operating hours. These special operating hours on the specific date override the normal operating hours for the specific day of the week. If a store location closes for lunch (or any other period during the day) and then reopens, multiple open and close pairs are needed. This container is returned if set for the store location. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


