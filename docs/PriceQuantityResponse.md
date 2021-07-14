# PriceQuantityResponse

This type is used to display the result for each offer and/or inventory item that the seller attempted to update with a bulkUpdatePriceQuantity call. If any errors or warnings occur, the error/warning data is returned at the offer/inventory item level.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | This array will be returned if there were one or more errors associated with the update to the offer or inventory item record. | [optional] 
**offer_id** | **str** | The unique identifier of the offer that was updated. This field will not be returned in situations where the seller is only updating the total &#39;ship-to-home&#39; quantity of an inventory item record. | [optional] 
**sku** | **str** | This is the seller-defined SKU value of the product. This field is returned whether the seller attempted to update an offer with the SKU value or just attempted to update the total &#39;ship-to-home&#39; quantity of an inventory item record. Max Length: 50 | [optional] 
**status_code** | **int** | The value returned in this container will indicate the status of the attempt to update the price and/or quantity of the offer (specified in the corresponding offerId field) or the attempt to update the total &#39;ship-to-home&#39; quantity of an inventory item (specified in the corresponding sku field). For a completely successful update of an offer or inventory item record, a value of 200 will appear in this field. A user can view the HTTP status codes section for information on other status codes that may be returned with the bulkUpdatePriceQuantity method. | [optional] 
**warnings** | [**[Error]**](Error.md) | This array will be returned if there were one or more warnings associated with the update to the offer or inventory item record. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


