# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardDetailsRequest(object):

    """Implementation of the 'CardDetailsRequest' model.

    TODO: type model description here.

    Attributes:
        col_co_code (int): Collecting Company Id  of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example: 
            1-Philippines  5-UK
        col_co_id (int): Collecting Company Code (Shell Code) of the selected
            payer.   Mandatory for serviced OUs such as Romania, Latvia,
            Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86-Philippines  5-UK
        col_co_country_code (str): ISO Country code of collecting company
        client_reference_id (str): Customer reference number of the card.
            Optional
        payer_number (str): Payer Number of the selected payer.
        payer_id (int): Payer Id (i.e. Customer Id of the Payment of the
            selected payer.
        account_number (str): Account Number of the customer. Optional if
            AccountId is passed, else mandatory.
        account_id (int): Account ID of the customer. Optional if
            AccountNumber is passed, else mandatory.
        pan (str): PAN of the card. Optional if CardId is passed, else
            Mandatory.
        card_id (int): Card Id of the card. Optional if PAN is passed, else
            Mandatory.
        token_type_id (int): Token Type ID for the Card Optional
        token_type_name (str): Token Type name for the Card Optional
        creation_date (str): Card Creation Date time Optional Format: yyyyMMdd
        effective_date (str): Effective date for the Card Optional Format:
            yyyyMMdd
        include_bundle_details (bool): When the value is True, API will return
            bundle Id associated with card in the response, if available.
            Note: Use ‘Null’ or ‘False’ for optimum performance. A delay in
            response is expected when set to ‘True’.
        include_intermediate_status (bool): A flag which indicates if the
            response can contain intermediate statuses
        include_scheduled_card_blocks (bool): A flag which indicates if the
            response can contain scheduled card blocks details

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "col_co_country_code": 'ColCoCountryCode',
        "client_reference_id": 'ClientReferenceId',
        "payer_number": 'PayerNumber',
        "payer_id": 'PayerId',
        "account_number": 'AccountNumber',
        "account_id": 'AccountId',
        "pan": 'PAN',
        "card_id": 'CardId',
        "token_type_id": 'TokenTypeID',
        "token_type_name": 'TokenTypeName',
        "creation_date": 'CreationDate',
        "effective_date": 'EffectiveDate',
        "include_bundle_details": 'IncludeBundleDetails',
        "include_intermediate_status": 'IncludeIntermediateStatus',
        "include_scheduled_card_blocks": 'IncludeScheduledCardBlocks'
    }

    _optionals = [
        'col_co_code',
        'col_co_id',
        'col_co_country_code',
        'client_reference_id',
        'payer_number',
        'payer_id',
        'account_number',
        'account_id',
        'pan',
        'card_id',
        'token_type_id',
        'token_type_name',
        'creation_date',
        'effective_date',
        'include_bundle_details',
        'include_intermediate_status',
        'include_scheduled_card_blocks',
    ]

    _nullables = [
        'col_co_id',
        'col_co_country_code',
        'client_reference_id',
        'payer_number',
        'payer_id',
        'account_number',
        'account_id',
        'pan',
        'card_id',
        'token_type_id',
        'token_type_name',
        'creation_date',
        'effective_date',
    ]

    def __init__(self,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 client_reference_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 token_type_id=APIHelper.SKIP,
                 token_type_name=APIHelper.SKIP,
                 creation_date=APIHelper.SKIP,
                 effective_date=APIHelper.SKIP,
                 include_bundle_details=APIHelper.SKIP,
                 include_intermediate_status=APIHelper.SKIP,
                 include_scheduled_card_blocks=APIHelper.SKIP):
        """Constructor for the CardDetailsRequest class"""

        # Initialize members of the class
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if client_reference_id is not APIHelper.SKIP:
            self.client_reference_id = client_reference_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if token_type_id is not APIHelper.SKIP:
            self.token_type_id = token_type_id 
        if token_type_name is not APIHelper.SKIP:
            self.token_type_name = token_type_name 
        if creation_date is not APIHelper.SKIP:
            self.creation_date = creation_date 
        if effective_date is not APIHelper.SKIP:
            self.effective_date = effective_date 
        if include_bundle_details is not APIHelper.SKIP:
            self.include_bundle_details = include_bundle_details 
        if include_intermediate_status is not APIHelper.SKIP:
            self.include_intermediate_status = include_intermediate_status 
        if include_scheduled_card_blocks is not APIHelper.SKIP:
            self.include_scheduled_card_blocks = include_scheduled_card_blocks 

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
        col_co_code = dictionary.get("ColCoCode") if dictionary.get("ColCoCode") else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        client_reference_id = dictionary.get("ClientReferenceId") if "ClientReferenceId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        token_type_id = dictionary.get("TokenTypeID") if "TokenTypeID" in dictionary.keys() else APIHelper.SKIP
        token_type_name = dictionary.get("TokenTypeName") if "TokenTypeName" in dictionary.keys() else APIHelper.SKIP
        creation_date = dictionary.get("CreationDate") if "CreationDate" in dictionary.keys() else APIHelper.SKIP
        effective_date = dictionary.get("EffectiveDate") if "EffectiveDate" in dictionary.keys() else APIHelper.SKIP
        include_bundle_details = dictionary.get("IncludeBundleDetails") if "IncludeBundleDetails" in dictionary.keys() else APIHelper.SKIP
        include_intermediate_status = dictionary.get("IncludeIntermediateStatus") if "IncludeIntermediateStatus" in dictionary.keys() else APIHelper.SKIP
        include_scheduled_card_blocks = dictionary.get("IncludeScheduledCardBlocks") if "IncludeScheduledCardBlocks" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_code,
                   col_co_id,
                   col_co_country_code,
                   client_reference_id,
                   payer_number,
                   payer_id,
                   account_number,
                   account_id,
                   pan,
                   card_id,
                   token_type_id,
                   token_type_name,
                   creation_date,
                   effective_date,
                   include_bundle_details,
                   include_intermediate_status,
                   include_scheduled_card_blocks)
