"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    The version of the OpenAPI document: 1.13.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.charity import Charity
    from openapi_client.model.listing_details import ListingDetails
    from openapi_client.model.listing_policies import ListingPolicies
    from openapi_client.model.pricing_summary import PricingSummary
    from openapi_client.model.tax import Tax
    globals()['Charity'] = Charity
    globals()['ListingDetails'] = ListingDetails
    globals()['ListingPolicies'] = ListingPolicies
    globals()['PricingSummary'] = PricingSummary
    globals()['Tax'] = Tax


class EbayOfferDetailsWithAll(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'available_quantity': (int,),  # noqa: E501
            'category_id': (str,),  # noqa: E501
            'charity': (Charity,),  # noqa: E501
            'format': (str,),  # noqa: E501
            'hide_buyer_details': (bool,),  # noqa: E501
            'include_catalog_product_details': (bool,),  # noqa: E501
            'listing': (ListingDetails,),  # noqa: E501
            'listing_description': (str,),  # noqa: E501
            'listing_duration': (str,),  # noqa: E501
            'listing_policies': (ListingPolicies,),  # noqa: E501
            'listing_start_date': (str,),  # noqa: E501
            'lot_size': (int,),  # noqa: E501
            'marketplace_id': (str,),  # noqa: E501
            'merchant_location_key': (str,),  # noqa: E501
            'offer_id': (str,),  # noqa: E501
            'pricing_summary': (PricingSummary,),  # noqa: E501
            'quantity_limit_per_buyer': (int,),  # noqa: E501
            'secondary_category_id': (str,),  # noqa: E501
            'sku': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'store_category_names': ([str],),  # noqa: E501
            'tax': (Tax,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'available_quantity': 'availableQuantity',  # noqa: E501
        'category_id': 'categoryId',  # noqa: E501
        'charity': 'charity',  # noqa: E501
        'format': 'format',  # noqa: E501
        'hide_buyer_details': 'hideBuyerDetails',  # noqa: E501
        'include_catalog_product_details': 'includeCatalogProductDetails',  # noqa: E501
        'listing': 'listing',  # noqa: E501
        'listing_description': 'listingDescription',  # noqa: E501
        'listing_duration': 'listingDuration',  # noqa: E501
        'listing_policies': 'listingPolicies',  # noqa: E501
        'listing_start_date': 'listingStartDate',  # noqa: E501
        'lot_size': 'lotSize',  # noqa: E501
        'marketplace_id': 'marketplaceId',  # noqa: E501
        'merchant_location_key': 'merchantLocationKey',  # noqa: E501
        'offer_id': 'offerId',  # noqa: E501
        'pricing_summary': 'pricingSummary',  # noqa: E501
        'quantity_limit_per_buyer': 'quantityLimitPerBuyer',  # noqa: E501
        'secondary_category_id': 'secondaryCategoryId',  # noqa: E501
        'sku': 'sku',  # noqa: E501
        'status': 'status',  # noqa: E501
        'store_category_names': 'storeCategoryNames',  # noqa: E501
        'tax': 'tax',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """EbayOfferDetailsWithAll - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            available_quantity (int): This integer value indicates the quantity of the inventory item (specified by the sku value) that will be available for purchase by buyers shopping on the eBay site specified in the marketplaceId field. For unpublished offers where the available quantity has yet to be set, the availableQuantity value is set to 0.. [optional]  # noqa: E501
            category_id (str): The unique identifier of the primary eBay category that the inventory item is listed under. This field is always returned for published offers, but is only returned if set for unpublished offers.. [optional]  # noqa: E501
            charity (Charity): [optional]  # noqa: E501
            format (str): This enumerated value indicates the listing format of the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:FormatTypeEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            hide_buyer_details (bool): This field is returned as true if the private listing feature has been enabled for the offer. Sellers may want to use this feature when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users. This field is always returned even if not explicitly set in the offer. It defaults to false, so will get returned as false if seller does not set this feature with a 'Create' or 'Update' offer method.. [optional]  # noqa: E501
            include_catalog_product_details (bool): This field indicates whether or not eBay product catalog details are applied to a listing. A value of true indicates the listing corresponds to the eBay product associated with the provided product identifier. The product identifier is provided in createOrReplaceInventoryItem. Note: Though the includeCatalogProductDetails parameter is not required to be submitted in the request, the parameter defaults to 'true' if omitted.. [optional]  # noqa: E501
            listing (ListingDetails): [optional]  # noqa: E501
            listing_description (str): The description of the eBay listing that is part of the unpublished or published offer. This field is always returned for published offers, but is only returned if set for unpublished offers. Max Length: 500000 (which includes HTML markup/tags). [optional]  # noqa: E501
            listing_duration (str): This field indicates the number of days that the listing will be active. This field is returned for both auction and fixed-price listings; however, the value returned for fixed-price listings will always be GTC. The GTC (Good 'Til Cancelled) listings are automatically renewed each calendar month until the seller decides to end the listing. Note: If the listing duration expires for an auction offer, the listing then becomes available as a fixed-price offer and will be GTC. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingDurationEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            listing_policies (ListingPolicies): [optional]  # noqa: E501
            listing_start_date (str): This timestamp is the date/time that the seller set for the scheduled listing. With the scheduled listing feature, the seller can set a time in the future that the listing will become active, instead of the listing becoming active immediately after a publishOffer call. Scheduled listings do not always start at the exact date/time specified by the seller, but the date/time of the timestamp returned in getOffer/getOffers will be the same as the timestamp passed into a 'Create' or 'Update' offer call. This field is returned if set for an offer.. [optional]  # noqa: E501
            lot_size (int): This field is only applicable and returned if the listing is a lot listing. A lot listing is a listing that has multiple quantity of the same product. An example would be a set of four identical car tires. The integer value in this field is the number of identical items being sold through the lot listing.. [optional]  # noqa: E501
            marketplace_id (str): This enumeration value is the unique identifier of the eBay site on which the offer is available, or will be made available. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            merchant_location_key (str): The unique identifier of the inventory location. This identifier is set up by the merchant when the inventory location is first created with the createInventoryLocation call. Once this value is set for an inventory location, it can not be modified. To get more information about this inventory location, the getInventoryLocation call can be used, passing in this value at the end of the call URI. This field is always returned for published offers, but is only returned if set for unpublished offers. Max length: 36. [optional]  # noqa: E501
            offer_id (str): The unique identifier of the offer. This identifier is used in many offer-related calls, and it is also used in the bulkUpdatePriceQuantity call.. [optional]  # noqa: E501
            pricing_summary (PricingSummary): [optional]  # noqa: E501
            quantity_limit_per_buyer (int): This field is only applicable and set if the seller wishes to set a restriction on the purchase quantity of an inventory item per seller. If this field is set by the seller for the offer, then each distinct buyer may purchase up to, but not exceed the quantity in this field. So, if this field's value is 5, each buyer may purchase a quantity of the inventory item between one and five, and the purchases can occur in one multiple-quantity purchase, or over multiple transactions. If a buyer attempts to purchase one or more of these products, and the cumulative quantity will take the buyer beyond the quantity limit, that buyer will be blocked from that purchase.. [optional]  # noqa: E501
            secondary_category_id (str): The unique identifier for a secondary category. This field is applicable if the seller decides to list the item under two categories. Sellers can use the getCategorySuggestions method of the Taxonomy API to retrieve suggested category ID values. A fee may be charged when adding a secondary category to a listing. Note: You cannot list US eBay Motors vehicles in two categories. However, you can list Parts &amp; Accessories in two categories.. [optional]  # noqa: E501
            sku (str): This is the seller-defined SKU value of the product in the offer. Max Length: 50. [optional]  # noqa: E501
            status (str): The enumeration value in this field specifies the status of the offer - either PUBLISHED or UNPUBLISHED. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:OfferStatusEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            store_category_names ([str]): This container is returned if the seller chose to place the inventory item into one or two eBay store categories that the seller has set up for their eBay store. The string value(s) in this container will be the full path(s) to the eBay store categories, as shown below: &quot;storeCategoryNames&quot;: [  &quot;/Fashion/Men/Shirts&quot;,  &quot;/Fashion/Men/Accessories&quot; ],. [optional]  # noqa: E501
            tax (Tax): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """EbayOfferDetailsWithAll - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            available_quantity (int): This integer value indicates the quantity of the inventory item (specified by the sku value) that will be available for purchase by buyers shopping on the eBay site specified in the marketplaceId field. For unpublished offers where the available quantity has yet to be set, the availableQuantity value is set to 0.. [optional]  # noqa: E501
            category_id (str): The unique identifier of the primary eBay category that the inventory item is listed under. This field is always returned for published offers, but is only returned if set for unpublished offers.. [optional]  # noqa: E501
            charity (Charity): [optional]  # noqa: E501
            format (str): This enumerated value indicates the listing format of the offer. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:FormatTypeEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            hide_buyer_details (bool): This field is returned as true if the private listing feature has been enabled for the offer. Sellers may want to use this feature when they believe that a listing's potential bidders/buyers would not want their obfuscated user IDs (and feedback scores) exposed to other users. This field is always returned even if not explicitly set in the offer. It defaults to false, so will get returned as false if seller does not set this feature with a 'Create' or 'Update' offer method.. [optional]  # noqa: E501
            include_catalog_product_details (bool): This field indicates whether or not eBay product catalog details are applied to a listing. A value of true indicates the listing corresponds to the eBay product associated with the provided product identifier. The product identifier is provided in createOrReplaceInventoryItem. Note: Though the includeCatalogProductDetails parameter is not required to be submitted in the request, the parameter defaults to 'true' if omitted.. [optional]  # noqa: E501
            listing (ListingDetails): [optional]  # noqa: E501
            listing_description (str): The description of the eBay listing that is part of the unpublished or published offer. This field is always returned for published offers, but is only returned if set for unpublished offers. Max Length: 500000 (which includes HTML markup/tags). [optional]  # noqa: E501
            listing_duration (str): This field indicates the number of days that the listing will be active. This field is returned for both auction and fixed-price listings; however, the value returned for fixed-price listings will always be GTC. The GTC (Good 'Til Cancelled) listings are automatically renewed each calendar month until the seller decides to end the listing. Note: If the listing duration expires for an auction offer, the listing then becomes available as a fixed-price offer and will be GTC. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:ListingDurationEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            listing_policies (ListingPolicies): [optional]  # noqa: E501
            listing_start_date (str): This timestamp is the date/time that the seller set for the scheduled listing. With the scheduled listing feature, the seller can set a time in the future that the listing will become active, instead of the listing becoming active immediately after a publishOffer call. Scheduled listings do not always start at the exact date/time specified by the seller, but the date/time of the timestamp returned in getOffer/getOffers will be the same as the timestamp passed into a 'Create' or 'Update' offer call. This field is returned if set for an offer.. [optional]  # noqa: E501
            lot_size (int): This field is only applicable and returned if the listing is a lot listing. A lot listing is a listing that has multiple quantity of the same product. An example would be a set of four identical car tires. The integer value in this field is the number of identical items being sold through the lot listing.. [optional]  # noqa: E501
            marketplace_id (str): This enumeration value is the unique identifier of the eBay site on which the offer is available, or will be made available. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:MarketplaceEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            merchant_location_key (str): The unique identifier of the inventory location. This identifier is set up by the merchant when the inventory location is first created with the createInventoryLocation call. Once this value is set for an inventory location, it can not be modified. To get more information about this inventory location, the getInventoryLocation call can be used, passing in this value at the end of the call URI. This field is always returned for published offers, but is only returned if set for unpublished offers. Max length: 36. [optional]  # noqa: E501
            offer_id (str): The unique identifier of the offer. This identifier is used in many offer-related calls, and it is also used in the bulkUpdatePriceQuantity call.. [optional]  # noqa: E501
            pricing_summary (PricingSummary): [optional]  # noqa: E501
            quantity_limit_per_buyer (int): This field is only applicable and set if the seller wishes to set a restriction on the purchase quantity of an inventory item per seller. If this field is set by the seller for the offer, then each distinct buyer may purchase up to, but not exceed the quantity in this field. So, if this field's value is 5, each buyer may purchase a quantity of the inventory item between one and five, and the purchases can occur in one multiple-quantity purchase, or over multiple transactions. If a buyer attempts to purchase one or more of these products, and the cumulative quantity will take the buyer beyond the quantity limit, that buyer will be blocked from that purchase.. [optional]  # noqa: E501
            secondary_category_id (str): The unique identifier for a secondary category. This field is applicable if the seller decides to list the item under two categories. Sellers can use the getCategorySuggestions method of the Taxonomy API to retrieve suggested category ID values. A fee may be charged when adding a secondary category to a listing. Note: You cannot list US eBay Motors vehicles in two categories. However, you can list Parts &amp; Accessories in two categories.. [optional]  # noqa: E501
            sku (str): This is the seller-defined SKU value of the product in the offer. Max Length: 50. [optional]  # noqa: E501
            status (str): The enumeration value in this field specifies the status of the offer - either PUBLISHED or UNPUBLISHED. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:OfferStatusEnum'>eBay API documentation</a>. [optional]  # noqa: E501
            store_category_names ([str]): This container is returned if the seller chose to place the inventory item into one or two eBay store categories that the seller has set up for their eBay store. The string value(s) in this container will be the full path(s) to the eBay store categories, as shown below: &quot;storeCategoryNames&quot;: [  &quot;/Fashion/Men/Shirts&quot;,  &quot;/Fashion/Men/Accessories&quot; ],. [optional]  # noqa: E501
            tax (Tax): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
