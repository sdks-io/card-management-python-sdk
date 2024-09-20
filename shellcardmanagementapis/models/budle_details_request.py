# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class BudleDetailsRequest(object):

    """Implementation of the 'BudleDetailsRequest' model.

    TODO: type model description here.

    Attributes:
        col_co_id (int): Collecting Company Id  of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86 for Philippines  5
            for UK
        payer_id (str): Payer Id of the selected payer. Optional if
            PayerNumber is passed else Mandatory Example: 123456
        payer_number (str): Payer Number of the selected payer. Optional if
            PayerId is passed else Mandatory Example: GB000000123
        account_id (int): Account Id of the customer. Optional if Account
            Number is passed else Mandatory Example: 123456
        account_number (str): Account Number of the customer. Optional if
            Account Id is passed else Mandatory Example: GB000000123
        bundle_id (str): Bundle Id associated with account Mandatory. Example:
            835662721

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "bundle_id": 'BundleId'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'account_id',
        'account_number',
        'bundle_id',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 bundle_id=APIHelper.SKIP):
        """Constructor for the BudleDetailsRequest class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if bundle_id is not APIHelper.SKIP:
            self.bundle_id = bundle_id 

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
        col_co_id = dictionary.get("ColCoId") if dictionary.get("ColCoId") else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if dictionary.get("ColCoCode") else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if dictionary.get("PayerId") else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if dictionary.get("AccountId") else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if dictionary.get("AccountNumber") else APIHelper.SKIP
        bundle_id = dictionary.get("BundleId") if dictionary.get("BundleId") else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   account_id,
                   account_number,
                   bundle_id)
