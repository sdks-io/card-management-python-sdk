# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardMoveResponseSuccessfulRequestsItems(object):

    """Implementation of the 'CardMoveResponseSuccessfulRequestsItems' model.

    Attributes:
        account_number (str): The model property of type str.
        account_id (int): The model property of type int.
        pan (str): The model property of type str.
        card_id (int): The model property of type int.
        move_card_reference (int): The model property of type int.

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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!r}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'move_card_reference={(self.move_card_reference if hasattr(self, "move_card_reference") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!s}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'move_card_reference={(self.move_card_reference if hasattr(self, "move_card_reference") else None)!s})')
