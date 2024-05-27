# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.product_all_of_0 import ProductAllOf0
from shellcardmanagementapis.models.product_group import ProductGroup


class SearchProductRestriction(object):

    """Implementation of the 'SearchProductRestriction' model.

    TODO: type model description here.

    Attributes:
        products (List[ProductAllOf0]): TODO: type description here.
        product_groups (List[ProductGroup]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "products": 'Products',
        "product_groups": 'ProductGroups'
    }

    _optionals = [
        'products',
        'product_groups',
    ]

    def __init__(self,
                 products=APIHelper.SKIP,
                 product_groups=APIHelper.SKIP):
        """Constructor for the SearchProductRestriction class"""

        # Initialize members of the class
        if products is not APIHelper.SKIP:
            self.products = products 
        if product_groups is not APIHelper.SKIP:
            self.product_groups = product_groups 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        products = None
        if dictionary.get('Products') is not None:
            products = [ProductAllOf0.from_dictionary(x) for x in dictionary.get('Products')]
        else:
            products = APIHelper.SKIP
        product_groups = None
        if dictionary.get('ProductGroups') is not None:
            product_groups = [ProductGroup.from_dictionary(x) for x in dictionary.get('ProductGroups')]
        else:
            product_groups = APIHelper.SKIP
        # Return an object of this model
        return cls(products,
                   product_groups)