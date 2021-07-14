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
    from openapi_client.model.best_offer import BestOffer
    from openapi_client.model.shipping_cost_override import ShippingCostOverride
    globals()['BestOffer'] = BestOffer
    globals()['ShippingCostOverride'] = ShippingCostOverride


class ListingPolicies(ModelNormal):
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
            'best_offer_terms': (BestOffer,),  # noqa: E501
            'e_bay_plus_if_eligible': (bool,),  # noqa: E501
            'fulfillment_policy_id': (str,),  # noqa: E501
            'payment_policy_id': (str,),  # noqa: E501
            'return_policy_id': (str,),  # noqa: E501
            'shipping_cost_overrides': ([ShippingCostOverride],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'best_offer_terms': 'bestOfferTerms',  # noqa: E501
        'e_bay_plus_if_eligible': 'eBayPlusIfEligible',  # noqa: E501
        'fulfillment_policy_id': 'fulfillmentPolicyId',  # noqa: E501
        'payment_policy_id': 'paymentPolicyId',  # noqa: E501
        'return_policy_id': 'returnPolicyId',  # noqa: E501
        'shipping_cost_overrides': 'shippingCostOverrides',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ListingPolicies - a model defined in OpenAPI

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
            best_offer_terms (BestOffer): [optional]  # noqa: E501
            e_bay_plus_if_eligible (bool): This field is included in an offer and set to true if a Top-Rated seller is opted in to the eBay Plus program. With the eBay Plus program, qualified sellers must commit to next-day delivery of the item, and the buyers must have an eBay Plus subscription to be eligible to receive the benefits of this program, which are free, next-day delivery, as well as free returns. Currently, this program is only available on the Germany and Australian sites. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            fulfillment_policy_id (str): This unique identifier indicates the fulfillment listing policy that will be used once an offer is published and converted to an eBay listing. This fulfillment listing policy will set all fulfillment-related settings for the eBay listing. Listing policies are not immediately required for offers, but are required before an offer can be published. The seller should review the fulfillment listing policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings. The seller may also want to review the shipping service costs in the fulfillment policy, and that seller might decide to override the shipping costs for one or more shipping service options by using the shippingCostOverrides container. Listing policies can be created and managed in My eBay or with the Account API. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's getFulfillmentPolicies call. There are also calls in the Account API to retrieve a fulfillment policy by policy ID or policy name. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            payment_policy_id (str): This unique identifier indicates the payment listing policy that will be used once an offer is published and converted to an eBay listing. This payment listing policy will set all payment-related settings for the eBay listing. Listing policies are not immediately required for offers, but are required before an offer can be published. The seller should review the payment listing policy before assigning it to the offer, as the following must be true for the payment listing policy to be compatible with the offer: The marketplaceId value should reflect where the offer is being published The immediatePay field value must be set to true since Inventory API offers only support immediate payment The only specified payment method should be 'PayPal', since immediate payment requires 'PayPal'Listing policies can be created and managed in My eBay or with the Account API. To get a list of all payment policies associated with a seller's account on a specific eBay Marketplace, use the Account API's getPaymentPolicies call. There are also calls in the Account API to retrieve a payment policy by policy ID or policy name. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            return_policy_id (str): This unique identifier indicates the return listing policy that will be used once an offer is published and converted to an eBay listing. This return listing policy will set all return policy settings for the eBay listing. Listing policies are not immediately required for offers, but are required before an offer can be published. The seller should review the return listing policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings. Listing policies can be created and managed in My eBay or with the Account API. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's getReturnPolicies call. There are also calls in the Account API to retrieve a return policy by policy ID or policy name. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            shipping_cost_overrides ([ShippingCostOverride]): This container is used if the seller wishes to override the shipping costs or surcharge for one or more domestic or international shipping service options defined in the fulfillment listing policy. To override the costs of a specific domestic or international shipping service option, the seller must know the priority/order of that shipping service in the fulfillment listing policy. The name of a shipping service option can be found in the shippingOptions.shippingServices.shippingServiceCode field of the fulfillment policy, and the priority/order of that shipping service option is found in the shippingOptions.shippingServices.sortOrderId field. Both of these values can be retrieved by searching for that fulfillment policy with the getFulfillmentPolicies or getFulfillmentPolicyByName calls of the Account API. The shippingCostOverrides.priority value should match the shippingOptions.shippingServices.sortOrderId in order to override the shipping costs for that shipping service option. The seller must also ensure that the shippingServiceType value is set to DOMESTIC to override a domestic shipping service option, or to INTERNATIONAL to override an international shipping service option. A separate ShippingCostOverrides node is needed for each shipping service option whose costs are being overridden. All defined fields of the shippingCostOverrides container should be included, even if the shipping costs and surcharge values are not changing. The shippingCostOverrides container is returned in the getOffer and getOffers calls if one or more shipping cost overrides are being applied to the fulfillment policy.. [optional]  # noqa: E501
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
        """ListingPolicies - a model defined in OpenAPI

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
            best_offer_terms (BestOffer): [optional]  # noqa: E501
            e_bay_plus_if_eligible (bool): This field is included in an offer and set to true if a Top-Rated seller is opted in to the eBay Plus program. With the eBay Plus program, qualified sellers must commit to next-day delivery of the item, and the buyers must have an eBay Plus subscription to be eligible to receive the benefits of this program, which are free, next-day delivery, as well as free returns. Currently, this program is only available on the Germany and Australian sites. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            fulfillment_policy_id (str): This unique identifier indicates the fulfillment listing policy that will be used once an offer is published and converted to an eBay listing. This fulfillment listing policy will set all fulfillment-related settings for the eBay listing. Listing policies are not immediately required for offers, but are required before an offer can be published. The seller should review the fulfillment listing policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings. The seller may also want to review the shipping service costs in the fulfillment policy, and that seller might decide to override the shipping costs for one or more shipping service options by using the shippingCostOverrides container. Listing policies can be created and managed in My eBay or with the Account API. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's getFulfillmentPolicies call. There are also calls in the Account API to retrieve a fulfillment policy by policy ID or policy name. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            payment_policy_id (str): This unique identifier indicates the payment listing policy that will be used once an offer is published and converted to an eBay listing. This payment listing policy will set all payment-related settings for the eBay listing. Listing policies are not immediately required for offers, but are required before an offer can be published. The seller should review the payment listing policy before assigning it to the offer, as the following must be true for the payment listing policy to be compatible with the offer: The marketplaceId value should reflect where the offer is being published The immediatePay field value must be set to true since Inventory API offers only support immediate payment The only specified payment method should be 'PayPal', since immediate payment requires 'PayPal'Listing policies can be created and managed in My eBay or with the Account API. To get a list of all payment policies associated with a seller's account on a specific eBay Marketplace, use the Account API's getPaymentPolicies call. There are also calls in the Account API to retrieve a payment policy by policy ID or policy name. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            return_policy_id (str): This unique identifier indicates the return listing policy that will be used once an offer is published and converted to an eBay listing. This return listing policy will set all return policy settings for the eBay listing. Listing policies are not immediately required for offers, but are required before an offer can be published. The seller should review the return listing policy before assigning it to the offer to make sure it is compatible with the inventory item and the offer settings. Listing policies can be created and managed in My eBay or with the Account API. To get a list of all return policies associated with a seller's account on a specific eBay Marketplace, use the Account API's getReturnPolicies call. There are also calls in the Account API to retrieve a return policy by policy ID or policy name. This field will be returned in the getOffer and getOffers calls if set for the offer.. [optional]  # noqa: E501
            shipping_cost_overrides ([ShippingCostOverride]): This container is used if the seller wishes to override the shipping costs or surcharge for one or more domestic or international shipping service options defined in the fulfillment listing policy. To override the costs of a specific domestic or international shipping service option, the seller must know the priority/order of that shipping service in the fulfillment listing policy. The name of a shipping service option can be found in the shippingOptions.shippingServices.shippingServiceCode field of the fulfillment policy, and the priority/order of that shipping service option is found in the shippingOptions.shippingServices.sortOrderId field. Both of these values can be retrieved by searching for that fulfillment policy with the getFulfillmentPolicies or getFulfillmentPolicyByName calls of the Account API. The shippingCostOverrides.priority value should match the shippingOptions.shippingServices.sortOrderId in order to override the shipping costs for that shipping service option. The seller must also ensure that the shippingServiceType value is set to DOMESTIC to override a domestic shipping service option, or to INTERNATIONAL to override an international shipping service option. A separate ShippingCostOverrides node is needed for each shipping service option whose costs are being overridden. All defined fields of the shippingCostOverrides container should be included, even if the shipping costs and surcharge values are not changing. The shippingCostOverrides container is returned in the getOffer and getOffers calls if one or more shipping cost overrides are being applied to the fulfillment policy.. [optional]  # noqa: E501
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
