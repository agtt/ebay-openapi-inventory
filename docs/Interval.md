# Interval

This type is used by the intervals container to define the opening and closing times of a store's working day. Local time (in Military format) is used, with the following format: hh:mm:ss.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close** | **str** | The close value is actually the time that the store closes. Local time (in Military format) is used. So, if a store closed at 8 PM local time, the close time would look like the following: 20:00:00. This field is conditionally required if the intervals container is used to specify working hours or special hours for a store. This field is returned if set for the store location. | [optional] 
**open** | **str** | The open value is actually the time that the store opens. Local time (in Military format) is used. So, if a store opens at 9 AM local time, the close time would look like the following: 09:00:00. This field is conditionally required if the intervals container is used to specify working hours or special hours for a store. This field is returned if set for the store location. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


