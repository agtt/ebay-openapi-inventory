# Tax

This type is used to enable the use of a sales tax table, to pass in a tax exception category code, or to specify a VAT percentage.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_tax** | **bool** | This field will be included and set to true if the seller would like to reference their account-level Sales Tax Table to calculate sales tax for an order. A seller&#39;s Sales Tax Table can be created and managed manually in My eBay&#39;s Payment Preferences. This Sales Tax Table contains all tax jurisdictions for the seller&#39;s country (individual states and territories in US), and the seller can set the sales tax rate for these individual tax jurisdictions. The Trading API has a SetTaxTable call to add/modify sales tax rates for one or more tax jurisdictions, and a GetTaxTable call that will retrieve all tax jurisdictions and related data, such as the sales tax rate (if defined) and a boolean field to indicate if sales tax is applied to shipping and handling costs. The Account API has a getSalesTaxTable call to retrieve all tax jurisdictions that have a defined sales tax rate, a getSalesTaxTableEntry call to retrieve a sales tax rate for a specific tax jurisdiction, a createSalesTaxTableEntry call to set/modify a sales tax rate for a specific tax jurisdiction, and a deleteSalesTaxTableEntry call to remove a sales tax rate from a specific tax jurisdiction. Note that a seller can enable the use of a sales tax table, but if a sales tax rate is not specified for the buyer&#39;s state/tax jurisdiction, sales tax will not be applied to the order. If a thirdPartyTaxCategory value is used, the applyTax field must also be used and set to true This field will be returned if set for the offer. See the Using a tax table help page for more information on setting up and using a sales tax table. | [optional] 
**third_party_tax_category** | **str** | The tax exception category code. If this field is used, sales tax will also apply to a service/fee, and not just the item price. This is to be used only by sellers who have opted into sales tax being calculated by a sales tax calculation vendor. If you are interested in becoming a tax calculation vendor partner with eBay, contact developer-relations@ebay.com. One supported value for this field is WASTE_RECYCLING_FEE. If this field is used, the applyTax field must also be used and set to true This field will be returned if set for the offer. | [optional] 
**vat_percentage** | **float** | This value is the Value Add Tax (VAT) rate for the item, if any. When a VAT percentage is specified, the item&#39;s VAT information appears on the listing&#39;s View Item page. In addition, the seller can choose to print an invoice that includes the item&#39;s net price, VAT percent, VAT amount, and total price. Since VAT rates vary depending on the item and on the user&#39;s country of residence, a seller is responsible for entering the correct VAT rate; it is not calculated by eBay. To use VAT, a seller must be a business seller with a VAT-ID registered with eBay, and must be listing the item on a VAT-enabled site. Max applicable length is 6 characters, including the decimal (e.g., 12.345). The scale is 3 decimal places. (If you pass in 12.3456, eBay may round up the value to 12.346). This field will be returned if set for the offer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

