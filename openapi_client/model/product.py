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



class Product(ModelNormal):
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
        return {
            'aspects': ([str],),  # noqa: E501
            'brand': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'ean': ([str],),  # noqa: E501
            'epid': (str,),  # noqa: E501
            'image_urls': ([str],),  # noqa: E501
            'isbn': ([str],),  # noqa: E501
            'mpn': (str,),  # noqa: E501
            'subtitle': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'upc': ([str],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'aspects': 'aspects',  # noqa: E501
        'brand': 'brand',  # noqa: E501
        'description': 'description',  # noqa: E501
        'ean': 'ean',  # noqa: E501
        'epid': 'epid',  # noqa: E501
        'image_urls': 'imageUrls',  # noqa: E501
        'isbn': 'isbn',  # noqa: E501
        'mpn': 'mpn',  # noqa: E501
        'subtitle': 'subtitle',  # noqa: E501
        'title': 'title',  # noqa: E501
        'upc': 'upc',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Product - a model defined in OpenAPI

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
            aspects ([str]): This is an array of item specific pairs that provide more information about the product and might make it easier for buyers to find. To view required/recommended product aspects/item specifics names (and corresponding values) for a specific eBay category, sellers can use the GetCategorySpecifics call of the Trading API. Alternatively, sellers can view similar items on eBay.com in the same category to get an idea of what other sellers are using for product aspects/item specifics. Sellers also have the option of specifying an eBay Product ID (ePID) or optionally, a Global Trade Item Number (GTIN) through the corresponding fields in the product container in an attempt to find a product match in the eBay Catalog. If a match is found based on the ePID or GTIN value, the product aspects that are defined for the eBay Catalog product will automatically get picked up by the newly created/updated inventory item. Below is an example of the proper JSON syntax to use when manually inputting item specifics: &quot;aspects&quot;: {  &quot;Brand&quot;: [&quot;GoPro&quot;],  &quot;Storage Type&quot;: [&quot;Removable&quot;]  } Note that inventory items that will become part of an inventory item group and multiple-variation listing should have the same attributes that are defined for the inventory item group. This container will be returned if one or more item specific pairs are defined for the inventory item. Max Length for Aspect Name: 40 Max Length for Aspect Value: 50. [optional]  # noqa: E501
            brand (str): The brand of the product. This field is often paired with the mpn field to identify a specific product by Manufacture Part Number. This field is conditionally required if the eBay category requires a Manufacturer Part Number (MPN) value. If eBay is able to find a product match in the eBay Catalog when an eBay Product ID (ePID) or GTIN value (UPC, ISBN, or EAN) is supplied, all product details of that eBay Catalog product is picked up by the inventory item record (including brand) if the createOrReplaceInventoryItem call is successful. This field is returned if defined for an inventory item. If a brand was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the brand field. Max Length: 65. [optional]  # noqa: E501
            description (str): The description of the product. The description of an existing inventory item can be added or modified with a createOrReplaceInventoryItem call. The description of an inventory item is automatically populated if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. Note that this field is optional but recommended. If a listingDescription field is omitted when creating and publishing a single-variation offer, the text in this field will be used instead. If neither the product.description field for the inventory item nor the listingDescription field for the offer exist, the publishOffer call will fail. If the inventory item will be part of an inventory item group/multiple-variation listing, this field should definitely be used to specify how the corresponding product variation is different (e.g. This is the green, extra-large version of the shirt). However, in the case of an inventory item group, the text in the description field of the inventory item group will become the listing description of the actual eBay listing instead of the text in this field. Basic HTML tags are supported, including the following tags: &lt;b&gt; &lt;strong&gt; &lt;br&gt; &lt;ol&gt; &lt;ul&gt; &lt;li&gt; Table tags including &lt;table&gt;, &lt;tr&gt;, &lt;td&gt;, &lt;th&gt;, &lt;thead&gt;, &lt;tfoot&gt;, &lt;tbody&gt;, &lt;caption&gt;, &lt;colgroup&gt;, and &lt;col&gt;A seller can not use any active content in their listing description. Active content includes animation or video via JavaScript, Flash, plug-ins, or form actions. This field is returned if defined for an inventory item. If one of the GTIN types (e.g. UPC) was passed in when the inventory item was created/modified and a product match was found in the eBay catalog, product description is one of the details that gets picked up from the catalog product. Max Length: 4000. [optional]  # noqa: E501
            ean ([str]): The European Article Number/International Article Number (EAN) for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified EAN value), and a link to any stock image that exists for the catalog product. This field is returned if defined for an inventory item. If an EAN was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the ean field.. [optional]  # noqa: E501
            epid (str): The eBay Product Identifier (ePID) for the product. This field can be used to directly identify an eBay Catalog product. Based on its specified ePID value, eBay will search for the product in the eBay Catalog, and if a match is found, the inventory item is automatically populated with available product details such as product title, product description, product aspects, and a link to any stock image that exists for the catalog product. In an attempt to find a eBay Catalog product match, an ePID value is always preferred over the other product identifiers, since it is possible that one GTIN value can be associated with multiple eBay Catalog products, and if multiple products are found, product details will not be picked up by the Inventory Item object. This field is returned if defined for an inventory item.. [optional]  # noqa: E501
            image_urls ([str]): An array of one or more links to images for the product. URLs must use the &quot;HTTPS&quot; protocol. Images can be self-hosted by the seller, or sellers can use the UploadSiteHostedPictures call of the Trading API to upload images to an eBay Picture Server. If successful, the response of the UploadSiteHostedPictures call will contain a full URL to the image on an eBay Picture Server. This is the URL that will be passed in through the imageUrls array. Before an offer can be published, at least one image must exist for the inventory item. Most eBay sites support up to 12 pictures free of charge, and eBay Motors listings can have up to 24 pictures. A link to a stock image for a product may automatically be populated for an inventory item if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. This container will always be returned for an inventory item that is part of a published offer since a published offer will always have at least one picture, but this container will only be returned if defined for inventory items that are not a part of a published offer.. [optional]  # noqa: E501
            isbn ([str]): The International Standard Book Number (ISBN) value for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified ISBN value), and a link to any stock image that exists for the catalog product. This field is returned if defined for an inventory item. If an ISBN was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the isbn field.. [optional]  # noqa: E501
            mpn (str): The Manufacturer Part Number (MPN) of a product. This field is paired with the brand field to identify a product. Some eBay categories require MPN values. The GetCategorySpecifics call of the Trading API can be used to see if a category requires an MPN. The MPN value for a product may automatically be populated for an inventory item if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. This field is returned if defined for an inventory item. If an MPN was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the mpn field. Max Length: 65. [optional]  # noqa: E501
            subtitle (str): A subtitle is an optional listing feature that allows the seller to provide more information about the product, possibly including keywords that may assist with search results. An additional listing fee will be charged to the seller if a subtitle is used. For more information on using listing subtitles on the US site, see the Adding a subtitle to your listings help page. The subtitle of an existing inventory item can added, modified, or removed with a createOrReplaceInventoryItem call. Note that the same subtitle text should be used for each inventory item that will be part of an inventory item group, and ultimately become one product variation within a multiple-variation listing. This field will only be returned if set for an inventory item. Max Length: 55. [optional]  # noqa: E501
            title (str): The title of an inventory item can be added or modified with a createOrReplaceInventoryItem call. Although not immediately required, a title will be needed before an offer with the inventory item is published. The title of an inventory item is automatically populated if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. If the inventory item will become part of a single-variation offer, and the listing is not a product-based listing, the text in this field will become the actual listing title for the published offer. However, if the inventory item will become part of a multiple-variation offer, the text in title field of the inventory item group entity will actually become the listing title for the published offer instead, although a title can still be provided for the inventory item, and it will actually become the title of the variation. This field will always be returned for an inventory item that is part of a published offer since a published offer will always have a listing title, but this field will only be returned if defined for inventory items that are not a part of a published offer. Max Length: 80. [optional]  # noqa: E501
            upc ([str]): The Universal Product Code (UPC) value for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified UPC value), and a link to any stock image that exists for the catalog product. This field is returned if defined for an inventory item. If a UPC was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the upc field.. [optional]  # noqa: E501
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
        """Product - a model defined in OpenAPI

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
            aspects ([str]): This is an array of item specific pairs that provide more information about the product and might make it easier for buyers to find. To view required/recommended product aspects/item specifics names (and corresponding values) for a specific eBay category, sellers can use the GetCategorySpecifics call of the Trading API. Alternatively, sellers can view similar items on eBay.com in the same category to get an idea of what other sellers are using for product aspects/item specifics. Sellers also have the option of specifying an eBay Product ID (ePID) or optionally, a Global Trade Item Number (GTIN) through the corresponding fields in the product container in an attempt to find a product match in the eBay Catalog. If a match is found based on the ePID or GTIN value, the product aspects that are defined for the eBay Catalog product will automatically get picked up by the newly created/updated inventory item. Below is an example of the proper JSON syntax to use when manually inputting item specifics: &quot;aspects&quot;: {  &quot;Brand&quot;: [&quot;GoPro&quot;],  &quot;Storage Type&quot;: [&quot;Removable&quot;]  } Note that inventory items that will become part of an inventory item group and multiple-variation listing should have the same attributes that are defined for the inventory item group. This container will be returned if one or more item specific pairs are defined for the inventory item. Max Length for Aspect Name: 40 Max Length for Aspect Value: 50. [optional]  # noqa: E501
            brand (str): The brand of the product. This field is often paired with the mpn field to identify a specific product by Manufacture Part Number. This field is conditionally required if the eBay category requires a Manufacturer Part Number (MPN) value. If eBay is able to find a product match in the eBay Catalog when an eBay Product ID (ePID) or GTIN value (UPC, ISBN, or EAN) is supplied, all product details of that eBay Catalog product is picked up by the inventory item record (including brand) if the createOrReplaceInventoryItem call is successful. This field is returned if defined for an inventory item. If a brand was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the brand field. Max Length: 65. [optional]  # noqa: E501
            description (str): The description of the product. The description of an existing inventory item can be added or modified with a createOrReplaceInventoryItem call. The description of an inventory item is automatically populated if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. Note that this field is optional but recommended. If a listingDescription field is omitted when creating and publishing a single-variation offer, the text in this field will be used instead. If neither the product.description field for the inventory item nor the listingDescription field for the offer exist, the publishOffer call will fail. If the inventory item will be part of an inventory item group/multiple-variation listing, this field should definitely be used to specify how the corresponding product variation is different (e.g. This is the green, extra-large version of the shirt). However, in the case of an inventory item group, the text in the description field of the inventory item group will become the listing description of the actual eBay listing instead of the text in this field. Basic HTML tags are supported, including the following tags: &lt;b&gt; &lt;strong&gt; &lt;br&gt; &lt;ol&gt; &lt;ul&gt; &lt;li&gt; Table tags including &lt;table&gt;, &lt;tr&gt;, &lt;td&gt;, &lt;th&gt;, &lt;thead&gt;, &lt;tfoot&gt;, &lt;tbody&gt;, &lt;caption&gt;, &lt;colgroup&gt;, and &lt;col&gt;A seller can not use any active content in their listing description. Active content includes animation or video via JavaScript, Flash, plug-ins, or form actions. This field is returned if defined for an inventory item. If one of the GTIN types (e.g. UPC) was passed in when the inventory item was created/modified and a product match was found in the eBay catalog, product description is one of the details that gets picked up from the catalog product. Max Length: 4000. [optional]  # noqa: E501
            ean ([str]): The European Article Number/International Article Number (EAN) for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified EAN value), and a link to any stock image that exists for the catalog product. This field is returned if defined for an inventory item. If an EAN was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the ean field.. [optional]  # noqa: E501
            epid (str): The eBay Product Identifier (ePID) for the product. This field can be used to directly identify an eBay Catalog product. Based on its specified ePID value, eBay will search for the product in the eBay Catalog, and if a match is found, the inventory item is automatically populated with available product details such as product title, product description, product aspects, and a link to any stock image that exists for the catalog product. In an attempt to find a eBay Catalog product match, an ePID value is always preferred over the other product identifiers, since it is possible that one GTIN value can be associated with multiple eBay Catalog products, and if multiple products are found, product details will not be picked up by the Inventory Item object. This field is returned if defined for an inventory item.. [optional]  # noqa: E501
            image_urls ([str]): An array of one or more links to images for the product. URLs must use the &quot;HTTPS&quot; protocol. Images can be self-hosted by the seller, or sellers can use the UploadSiteHostedPictures call of the Trading API to upload images to an eBay Picture Server. If successful, the response of the UploadSiteHostedPictures call will contain a full URL to the image on an eBay Picture Server. This is the URL that will be passed in through the imageUrls array. Before an offer can be published, at least one image must exist for the inventory item. Most eBay sites support up to 12 pictures free of charge, and eBay Motors listings can have up to 24 pictures. A link to a stock image for a product may automatically be populated for an inventory item if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. This container will always be returned for an inventory item that is part of a published offer since a published offer will always have at least one picture, but this container will only be returned if defined for inventory items that are not a part of a published offer.. [optional]  # noqa: E501
            isbn ([str]): The International Standard Book Number (ISBN) value for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified ISBN value), and a link to any stock image that exists for the catalog product. This field is returned if defined for an inventory item. If an ISBN was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the isbn field.. [optional]  # noqa: E501
            mpn (str): The Manufacturer Part Number (MPN) of a product. This field is paired with the brand field to identify a product. Some eBay categories require MPN values. The GetCategorySpecifics call of the Trading API can be used to see if a category requires an MPN. The MPN value for a product may automatically be populated for an inventory item if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. This field is returned if defined for an inventory item. If an MPN was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the mpn field. Max Length: 65. [optional]  # noqa: E501
            subtitle (str): A subtitle is an optional listing feature that allows the seller to provide more information about the product, possibly including keywords that may assist with search results. An additional listing fee will be charged to the seller if a subtitle is used. For more information on using listing subtitles on the US site, see the Adding a subtitle to your listings help page. The subtitle of an existing inventory item can added, modified, or removed with a createOrReplaceInventoryItem call. Note that the same subtitle text should be used for each inventory item that will be part of an inventory item group, and ultimately become one product variation within a multiple-variation listing. This field will only be returned if set for an inventory item. Max Length: 55. [optional]  # noqa: E501
            title (str): The title of an inventory item can be added or modified with a createOrReplaceInventoryItem call. Although not immediately required, a title will be needed before an offer with the inventory item is published. The title of an inventory item is automatically populated if the seller specifies an eBay Product ID (ePID) or a Global Trade Item Number (GTIN) and eBay is able to find a matching product in the eBay Catalog. If the inventory item will become part of a single-variation offer, and the listing is not a product-based listing, the text in this field will become the actual listing title for the published offer. However, if the inventory item will become part of a multiple-variation offer, the text in title field of the inventory item group entity will actually become the listing title for the published offer instead, although a title can still be provided for the inventory item, and it will actually become the title of the variation. This field will always be returned for an inventory item that is part of a published offer since a published offer will always have a listing title, but this field will only be returned if defined for inventory items that are not a part of a published offer. Max Length: 80. [optional]  # noqa: E501
            upc ([str]): The Universal Product Code (UPC) value for the product. Although an ePID value is preferred when trying to find a product match in the eBay Catalog, this field can also be used in an attempt to find a product match in the eBay Catalog. If a product match is found in the eBay Catalog, the inventory item is automatically populated with available product details such as a title, a product description, product aspects (including the specified UPC value), and a link to any stock image that exists for the catalog product. This field is returned if defined for an inventory item. If a UPC was passed in as an item specific name-value pair through the aspects array in a createOrReplaceInventoryItem call, this value is also picked up by the upc field.. [optional]  # noqa: E501
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
