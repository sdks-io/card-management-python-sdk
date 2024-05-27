# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardTypeResponseError(object):

    """Implementation of the 'CardTypeResponseError' model.

    TODO: type model description here.

    Attributes:
        code (str): TODO: type description here.
        description (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'Code',
        "description": 'Description'
    }

    _optionals = [
        'code',
        'description',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the CardTypeResponseError class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
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
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   description)
