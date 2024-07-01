# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class RestrictionProduct(object):

    """Implementation of the 'RestrictionProduct' model.

    TODO: type model description here.

    Attributes:
        global_product_code (str): The productCode returned by the Gateway
            API.  Example: 021
        description (str): The description returned by the Gateway API. 
            Example: High Performance Diesel

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "global_product_code": 'GlobalProductCode',
        "description": 'Description'
    }

    _optionals = [
        'global_product_code',
        'description',
    ]

    def __init__(self,
                 global_product_code=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the RestrictionProduct class"""

        # Initialize members of the class
        if global_product_code is not APIHelper.SKIP:
            self.global_product_code = global_product_code 
        if description is not APIHelper.SKIP:
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        global_product_code = dictionary.get("GlobalProductCode") if dictionary.get("GlobalProductCode") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        # Return an object of this model
        return cls(global_product_code,
                   description)