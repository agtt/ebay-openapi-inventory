# Specification

This type is used to specify product aspects for which variations within an inventory item group vary, and the order in which they appear in the listing. For example, t-shirts in an inventory item group may be available in multiple sizes and colors.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | This is the name of product variation aspect. Typically, for clothing, typical aspect names are &amp;quot;Size&amp;quot; and &amp;quot;Color&amp;quot;. Product variation aspects are not required immediately upon creating an inventory item group, but these aspects will be required before a multiple-variation listing containing this inventory item group is published. For each product variation aspect that is specified through the specifications container, one name value is required and two or more variations of this aspect are required through the values array. Note: Each member of the inventory item group should have these same aspect names specified through the product.aspects container when the inventory item is created with the createOrReplaceInventoryItem or bulkCreateOrReplaceInventoryItem call. Max Length: 40 | [optional] 
**values** | **[str]** | This is an array of values pertaining to the corresponding product variation aspect (specified in the name field). Below is a sample of how these values will appear under a specifications container: &amp;quot;specifications&amp;quot;: [{  &amp;quot;name&amp;quot;: &amp;quot;Size&amp;quot;,  &amp;quot;values&amp;quot;: [&amp;quot;Small&amp;quot;,  &amp;quot;Medium&amp;quot;,  &amp;quot;Large&amp;quot;]  },  {  &amp;quot;name&amp;quot;: &amp;quot;Color&amp;quot;,  &amp;quot;values&amp;quot;: [&amp;quot;Blue&amp;quot;,  &amp;quot;White&amp;quot;,  &amp;quot;Red&amp;quot;]  }] Note: Each member of the inventory item group should have these same aspect names, and each individual inventory item should have each variation of the product aspect values specified through the product.aspects container when the inventory item is created with the createOrReplaceInventoryItem or bulkCreateOrReplaceInventoryItem call. Max Length: 50 | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


