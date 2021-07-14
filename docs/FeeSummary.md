# FeeSummary

This type is used to display the expected listing fees for each unpublished offer specified in the request of the getListingFees call.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fees** | [**[Fee]**](Fee.md) | This container is an array of listing fees that can be expected to be applied to an offer on the specified eBay marketplace (marketplaceId value). Many fee types will get returned even when they are 0.0. See the Standard selling fees help page for more information on listing fees. | [optional] 
**marketplace_id** | **str** | This is the unique identifier of the eBay site for which listing fees for the offer are applicable. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum&#39;&gt;eBay API documentation&lt;/a&gt; | [optional] 
**warnings** | [**[Error]**](Error.md) | This container will contain an array of errors and/or warnings when a call is made, and errors and/or warnings occur. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


