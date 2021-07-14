# MigrateListing

This type is used to specify one to five eBay listings that will be migrated to the new Inventory model.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**listing_id** | **str** | The unique identifier of the eBay listing to migrate to the new Inventory model. In the Trading API, this field is known as the ItemID. Up to five unique eBay listings may be specified here in separate listingId fields. The seller should make sure that each of these listings meet the requirements that are stated at the top of this Call Reference page. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


