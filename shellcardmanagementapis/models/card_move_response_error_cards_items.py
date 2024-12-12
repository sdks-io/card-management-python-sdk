# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardMoveResponseErrorCardsItems(object):

    """Implementation of the 'CardMoveResponseErrorCardsItems' model.

    TODO: type model description here.

    Attributes:
        account_number (str): TODO: type description here.
        account_id (int): TODO: type description here.
        pan (str): TODO: type description here.
        card_id (int): TODO: type description here.
        validation_error_code (str): TODO: type description here.
        validation_error_description (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_number": 'AccountNumber',
        "account_id": 'AccountId',
        "pan": 'PAN',
        "card_id": 'CardId',
        "validation_error_code": 'ValidationErrorCode',
        "validation_error_description": 'ValidationErrorDescription'
    }

    _optionals = [
        'account_number',
        'account_id',
        'pan',
        'card_id',
        'validation_error_code',
        'validation_error_description',
    ]

    _nullables = [
        'account_number',
        'account_id',
        'pan',
        'card_id',
        'validation_error_code',
        'validation_error_description',
    ]

    def __init__(self,
                 account_number=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 validation_error_code=APIHelper.SKIP,
                 validation_error_description=APIHelper.SKIP):
        """Constructor for the CardMoveResponseErrorCardsItems class"""

        # Initialize members of the class
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if validation_error_code is not APIHelper.SKIP:
            self.validation_error_code = validation_error_code 
        if validation_error_description is not APIHelper.SKIP:
            self.validation_error_description = validation_error_description 

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
        validation_error_code = dictionary.get("ValidationErrorCode") if "ValidationErrorCode" in dictionary.keys() else APIHelper.SKIP
        validation_error_description = dictionary.get("ValidationErrorDescription") if "ValidationErrorDescription" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_number,
                   account_id,
                   pan,
                   card_id,
                   validation_error_code,
                   validation_error_description)
