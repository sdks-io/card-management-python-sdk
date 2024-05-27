# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class UpdateCardGroupResponseMoveCardReferencesItems(object):

    """Implementation of the 'UpdateCardGroupResponseMoveCardReferencesItems' model.

    TODO: type model description here.

    Attributes:
        card_id (int): Card Id of the card.  Example: 123
        pan (str): PAN of the card.  Example: 7002051123456789145
        reference (int): Reference number for tracking of update status
            request of the specific card.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_id": 'CardId',
        "pan": 'PAN',
        "reference": 'Reference'
    }

    _optionals = [
        'card_id',
        'pan',
        'reference',
    ]

    _nullables = [
        'card_id',
        'pan',
        'reference',
    ]

    def __init__(self,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 reference=APIHelper.SKIP):
        """Constructor for the UpdateCardGroupResponseMoveCardReferencesItems class"""

        # Initialize members of the class
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if reference is not APIHelper.SKIP:
            self.reference = reference 

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
        reference = dictionary.get("Reference") if "Reference" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(card_id,
                   pan,
                   reference)
