# OfferPriceQuantity

This type is used by the offers container in a Bulk Update Price and Quantity call to update the current price and/or quantity of one or more offers associated with a specific inventory item.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_quantity** | **int** | This field is used if the seller wants to modify the current quantity of the inventory item that will be available for purchase in the offer (identified by the corresponding offerId value). Either the availableQuantity field or the price container is required, but not necessarily both. | [optional] 
**offer_id** | **str** | This field is the unique identifier of the offer. If an offers container is used to update one or more offers associated to a specific inventory item, the offerId value is required in order to identify the offer to update with a modified price and/or quantity. The seller can run a getOffers call (passing in the correct SKU value as a query parameter) to retrieve offerId values for offers associated with the SKU. | [optional] 
**price** | [**Amount**](Amount.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


