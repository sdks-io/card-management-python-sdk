# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class DeliveryAddressUpdateReferences(object):

    """Implementation of the 'DeliveryAddressUpdateReferences' model.

    List of Delivery address update entity. The fields of this entity are
    described below.

    Attributes:
        card_id (int): CardId
        card_pan (str): PAN of the card.
        account_id (int): AccountId
        account_number (str): Account number
        reference_id (int): Individual delivery address update reference
            number for the delivery address update request.
        error_info (str): Individual error information for the delivery
            address update request.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_id": 'CardId',
        "card_pan": 'CardPAN',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "reference_id": 'ReferenceId',
        "error_info": 'ErrorInfo'
    }

    _optionals = [
        'card_id',
        'card_pan',
        'account_id',
        'account_number',
        'reference_id',
        'error_info',
    ]

    def __init__(self,
                 card_id=APIHelper.SKIP,
                 card_pan=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 reference_id=APIHelper.SKIP,
                 error_info=APIHelper.SKIP):
        """Constructor for the DeliveryAddressUpdateReferences class"""

        # Initialize members of the class
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if card_pan is not APIHelper.SKIP:
            self.card_pan = card_pan 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if reference_id is not APIHelper.SKIP:
            self.reference_id = reference_id 
        if error_info is not APIHelper.SKIP:
            self.error_info = error_info 

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
        card_id = dictionary.get("CardId") if dictionary.get("CardId") else APIHelper.SKIP
        card_pan = dictionary.get("CardPAN") if dictionary.get("CardPAN") else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if dictionary.get("AccountId") else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if dictionary.get("AccountNumber") else APIHelper.SKIP
        reference_id = dictionary.get("ReferenceId") if dictionary.get("ReferenceId") else APIHelper.SKIP
        error_info = dictionary.get("ErrorInfo") if dictionary.get("ErrorInfo") else APIHelper.SKIP
        # Return an object of this model
        return cls(card_id,
                   card_pan,
                   account_id,
                   account_number,
                   reference_id,
                   error_info)
