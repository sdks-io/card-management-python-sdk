# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class ProductRestrictionCard(object):

    """Implementation of the 'ProductRestrictionCard' model.

    Attributes:
        products (List[str]): An array of 3-digit global product codes.
            Optional. Example: [ "033", "021", "023”]
        product_groups (List[str]): An array of product group IDs. Optional.
            Example: [ "670246404", "40557126" ]

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
        """Constructor for the ProductRestrictionCard class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        products = dictionary.get("Products") if dictionary.get("Products") else APIHelper.SKIP
        product_groups = dictionary.get("ProductGroups") if dictionary.get("ProductGroups") else APIHelper.SKIP
        # Return an object of this model
        return cls(products,
                   product_groups)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'products={(self.products if hasattr(self, "products") else None)!r}, '
                f'product_groups={(self.product_groups if hasattr(self, "product_groups") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'products={(self.products if hasattr(self, "products") else None)!s}, '
                f'product_groups={(self.product_groups if hasattr(self, "product_groups") else None)!s})')
