# InventoryItemListing

This type is used by the inventoryItems container that is returned in the response of the bulkMigrateListing call. Up to five sku/offerId pairs may be returned under the inventoryItems container, dependent on how many eBay listings the seller is attempting to migrate to the inventory model.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Upon a successful migration of a listing, eBay auto-generates this unique identifier, and this offer ID value will be used to retrieve and manage the newly-created offer object. This value will only be generated and returned if the eBay listing is migrated successfully. | [optional] 
**sku** | **str** | This is the seller-defined SKU value associated with the item(s) in a listing. This same SKU value will be used to retrieve and manage the newly-created inventory item object if the listing migration is successful. This SKU value will get returned even if the migration is not successful. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


