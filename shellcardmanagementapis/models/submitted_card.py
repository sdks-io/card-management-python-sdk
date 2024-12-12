# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class SubmittedCard(object):

    """Implementation of the 'SubmittedCard' model.

    Response entity object for SubmittedCard list <br/>Note: This list will be
    empty for status 9006 and 9012 i.e., request for all the cards failed.

    Attributes:
        replacement_card_reference (int): Reference number for tracking of
            replacement card order request of the specific card,<br /> This is
            applicable for requests with target status as Block and
            OrderReplacement passed as True.
        update_card_reference (int): Reference number for tracking of update
            status request of the specific card,
        account_id (int): Account Id of the customer.<br /> Optional if
            AccountNumber is passed, else Mandatory.
        account_number (str): Account Number of the customer.<br /> Optional
            if AccountId is passed, else Mandatory.
        card_expiry_date (str): Expiry date of the card.<br /> Mandatory if
            PAN is passed, else optional.<br /> Format: yyyyMMdd
        card_id (int): Card Id of the card.<br /> Optional if PAN is passed,
            else Mandatory.
        col_co_code (int): Collecting company code of the customer. <br />
            Optional if ColCoId is passed, else Mandatory.<br />
        col_co_id (int): Collecting company id of the customer. <br />
            Optional if ColCoCode is passed, else Mandatory.<br />
        pan (str): PAN of the card.<br /> Optional if CardId is passed, else
            Mandatory.<br />
        panid (float): PANID of the card
        masked_pan (str): Card PAN
        payer_id (int): Payer id of the customer.<br /> Optional if
            PayerNumber is passed, else Mandatory.
        payer_number (str): PayerNumber of the customer.<br /> Optional if
            PayerId is passed, else Mandatory.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "replacement_card_reference": 'ReplacementCardReference',
        "update_card_reference": 'UpdateCardReference',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "card_expiry_date": 'CardExpiryDate',
        "card_id": 'CardId',
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "pan": 'PAN',
        "panid": 'PANID',
        "masked_pan": 'MaskedPAN',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber'
    }

    _optionals = [
        'replacement_card_reference',
        'update_card_reference',
        'account_id',
        'account_number',
        'card_expiry_date',
        'card_id',
        'col_co_code',
        'col_co_id',
        'pan',
        'panid',
        'masked_pan',
        'payer_id',
        'payer_number',
    ]

    _nullables = [
        'replacement_card_reference',
        'update_card_reference',
        'account_id',
        'account_number',
        'card_expiry_date',
        'card_id',
        'col_co_code',
        'col_co_id',
        'pan',
        'panid',
        'masked_pan',
        'payer_id',
        'payer_number',
    ]

    def __init__(self,
                 replacement_card_reference=APIHelper.SKIP,
                 update_card_reference=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 card_expiry_date=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 panid=APIHelper.SKIP,
                 masked_pan=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP):
        """Constructor for the SubmittedCard class"""

        # Initialize members of the class
        if replacement_card_reference is not APIHelper.SKIP:
            self.replacement_card_reference = replacement_card_reference 
        if update_card_reference is not APIHelper.SKIP:
            self.update_card_reference = update_card_reference 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if card_expiry_date is not APIHelper.SKIP:
            self.card_expiry_date = card_expiry_date 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if panid is not APIHelper.SKIP:
            self.panid = panid 
        if masked_pan is not APIHelper.SKIP:
            self.masked_pan = masked_pan 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 

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
        replacement_card_reference = dictionary.get("ReplacementCardReference") if "ReplacementCardReference" in dictionary.keys() else APIHelper.SKIP
        update_card_reference = dictionary.get("UpdateCardReference") if "UpdateCardReference" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        card_expiry_date = dictionary.get("CardExpiryDate") if "CardExpiryDate" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        panid = dictionary.get("PANID") if "PANID" in dictionary.keys() else APIHelper.SKIP
        masked_pan = dictionary.get("MaskedPAN") if "MaskedPAN" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(replacement_card_reference,
                   update_card_reference,
                   account_id,
                   account_number,
                   card_expiry_date,
                   card_id,
                   col_co_code,
                   col_co_id,
                   pan,
                   panid,
                   masked_pan,
                   payer_id,
                   payer_number)
