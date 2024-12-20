# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardMoveResponseSuccessfulRequestsItems(object):

    """Implementation of the 'CardMoveResponseSuccessfulRequestsItems' model.

    TODO: type model description here.

    Attributes:
        account_number (str): TODO: type description here.
        account_id (int): TODO: type description here.
        pan (str): TODO: type description here.
        card_id (int): TODO: type description here.
        move_card_reference (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_number": 'AccountNumber',
        "account_id": 'AccountId',
        "pan": 'PAN',
        "card_id": 'CardId',
        "move_card_reference": 'MoveCardReference'
    }

    _optionals = [
        'account_number',
        'account_id',
        'pan',
        'card_id',
        'move_card_reference',
    ]

    _nullables = [
        'account_number',
        'account_id',
        'pan',
        'card_id',
        'move_card_reference',
    ]

    def __init__(self,
                 account_number=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 move_card_reference=APIHelper.SKIP):
        """Constructor for the CardMoveResponseSuccessfulRequestsItems class"""

        # Initialize members of the class
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if move_card_reference is not APIHelper.SKIP:
            self.move_card_reference = move_card_reference 

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
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        move_card_reference = dictionary.get("MoveCardReference") if "MoveCardReference" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_number,
                   account_id,
                   pan,
                   card_id,
                   move_card_reference)
