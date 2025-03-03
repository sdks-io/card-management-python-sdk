# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.card_move_request_cards_items import CardMoveRequestCardsItems


class CardMoveRequest(object):

    """Implementation of the 'CardMoveRequest' model.

    Attributes:
        col_co_code (int): The model property of type int.
        col_co_id (int): The model property of type int.
        col_co_country_code (str): The model property of type str.
        payer_number (str): The model property of type str.
        payer_id (int): The model property of type int.
        cards (List[CardMoveRequestCardsItems]): The model property of type
            List[CardMoveRequestCardsItems].
        target_account_id (int): The model property of type int.
        target_account_number (str): The model property of type str.
        target_card_group_id (int): The model property of type int.
        target_new_card_group_name (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "col_co_country_code": 'ColCoCountryCode',
        "payer_number": 'PayerNumber',
        "payer_id": 'PayerId',
        "cards": 'Cards',
        "target_account_id": 'TargetAccountId',
        "target_account_number": 'TargetAccountNumber',
        "target_card_group_id": 'TargetCardGroupId',
        "target_new_card_group_name": 'TargetNewCardGroupName'
    }

    _optionals = [
        'col_co_code',
        'col_co_id',
        'col_co_country_code',
        'payer_number',
        'payer_id',
        'cards',
        'target_account_id',
        'target_account_number',
        'target_card_group_id',
        'target_new_card_group_name',
    ]

    _nullables = [
        'col_co_code',
        'col_co_id',
        'col_co_country_code',
        'payer_number',
        'payer_id',
    ]

    def __init__(self,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 cards=APIHelper.SKIP,
                 target_account_id=APIHelper.SKIP,
                 target_account_number=APIHelper.SKIP,
                 target_card_group_id=APIHelper.SKIP,
                 target_new_card_group_name=APIHelper.SKIP):
        """Constructor for the CardMoveRequest class"""

        # Initialize members of the class
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if cards is not APIHelper.SKIP:
            self.cards = cards 
        if target_account_id is not APIHelper.SKIP:
            self.target_account_id = target_account_id 
        if target_account_number is not APIHelper.SKIP:
            self.target_account_number = target_account_number 
        if target_card_group_id is not APIHelper.SKIP:
            self.target_card_group_id = target_card_group_id 
        if target_new_card_group_name is not APIHelper.SKIP:
            self.target_new_card_group_name = target_new_card_group_name 

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
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        cards = None
        if dictionary.get('Cards') is not None:
            cards = [CardMoveRequestCardsItems.from_dictionary(x) for x in dictionary.get('Cards')]
        else:
            cards = APIHelper.SKIP
        target_account_id = dictionary.get("TargetAccountId") if dictionary.get("TargetAccountId") else APIHelper.SKIP
        target_account_number = dictionary.get("TargetAccountNumber") if dictionary.get("TargetAccountNumber") else APIHelper.SKIP
        target_card_group_id = dictionary.get("TargetCardGroupId") if dictionary.get("TargetCardGroupId") else APIHelper.SKIP
        target_new_card_group_name = dictionary.get("TargetNewCardGroupName") if dictionary.get("TargetNewCardGroupName") else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_code,
                   col_co_id,
                   col_co_country_code,
                   payer_number,
                   payer_id,
                   cards,
                   target_account_id,
                   target_account_number,
                   target_card_group_id,
                   target_new_card_group_name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_country_code={(self.col_co_country_code if hasattr(self, "col_co_country_code") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'cards={(self.cards if hasattr(self, "cards") else None)!r}, '
                f'target_account_id={(self.target_account_id if hasattr(self, "target_account_id") else None)!r}, '
                f'target_account_number={(self.target_account_number if hasattr(self, "target_account_number") else None)!r}, '
                f'target_card_group_id={(self.target_card_group_id if hasattr(self, "target_card_group_id") else None)!r}, '
                f'target_new_card_group_name={(self.target_new_card_group_name if hasattr(self, "target_new_card_group_name") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_country_code={(self.col_co_country_code if hasattr(self, "col_co_country_code") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'cards={(self.cards if hasattr(self, "cards") else None)!s}, '
                f'target_account_id={(self.target_account_id if hasattr(self, "target_account_id") else None)!s}, '
                f'target_account_number={(self.target_account_number if hasattr(self, "target_account_number") else None)!s}, '
                f'target_card_group_id={(self.target_card_group_id if hasattr(self, "target_card_group_id") else None)!s}, '
                f'target_new_card_group_name={(self.target_new_card_group_name if hasattr(self, "target_new_card_group_name") else None)!s})')
