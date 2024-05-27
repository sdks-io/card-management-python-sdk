# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class SearchCard(object):

    """Implementation of the 'SearchCard' model.

    SearchCard

    Attributes:
        card_id (int): Unique Card Id  Optional if PAN is given, else
            mandatory.
        pan (str): Card PAN.  Optional if CardId is given, else mandatory. 
            Note: PAN is ignored if CardId is given.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_id": 'CardId',
        "pan": 'PAN'
    }

    _optionals = [
        'card_id',
        'pan',
    ]

    _nullables = [
        'card_id',
        'pan',
    ]

    def __init__(self,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP):
        """Constructor for the SearchCard class"""

        # Initialize members of the class
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 

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
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(card_id,
                   pan)