# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CardDetailsResponseFuelSetsItems(object):

    """Implementation of the 'CardDetailsResponseFuelSetsItems' model.

    Product restriction

    Attributes:
        product_restriction_id (int): product restriction identifier
        description (str): product set description.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_restriction_id": 'ProductRestrictionId',
        "description": 'Description'
    }

    def __init__(self,
                 product_restriction_id=None,
                 description=None):
        """Constructor for the CardDetailsResponseFuelSetsItems class"""

        # Initialize members of the class
        self.product_restriction_id = product_restriction_id 
        self.description = description 

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
        product_restriction_id = dictionary.get("ProductRestrictionId") if dictionary.get("ProductRestrictionId") else None
        description = dictionary.get("Description") if dictionary.get("Description") else None
        # Return an object of this model
        return cls(product_restriction_id,
                   description)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_restriction_id={self.product_restriction_id!r}, '
                f'description={self.description!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_restriction_id={self.product_restriction_id!s}, '
                f'description={self.description!s})')
