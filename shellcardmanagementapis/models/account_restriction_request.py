# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.usage_restrictions import UsageRestrictions


class AccountRestrictionRequest(object):

    """Implementation of the 'AccountRestrictionRequest' model.

    TODO: type model description here.

    Attributes:
        col_co_id (int): Collecting Company Id of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86 for Philippines  5
            for UK
        payer_id (int): Payer Id of the selected payer.  Optional if
            PayerNumber is passed else Mandatory  Example: 123456
        payer_number (str): Payer Number of the selected payer.  Optional if
            PayerId is passed else Mandatory  Example: GB000000123
        account_number (str): Account Number of the customer on which the
            restrictions will be applied.  Optional if AccountId is passed,
            else Mandatory.
        reset_usage_restrictions (bool): If true, the usage restrictions
            applied on the account will be removed.  Optional  Default: False
        usage_restrictions (UsageRestrictions): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "account_number": 'AccountNumber',
        "reset_usage_restrictions": 'ResetUsageRestrictions',
        "usage_restrictions": 'UsageRestrictions'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'account_number',
        'reset_usage_restrictions',
        'usage_restrictions',
    ]

    _nullables = [
        'payer_id',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 reset_usage_restrictions=False,
                 usage_restrictions=APIHelper.SKIP):
        """Constructor for the AccountRestrictionRequest class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        self.reset_usage_restrictions = reset_usage_restrictions 
        if usage_restrictions is not APIHelper.SKIP:
            self.usage_restrictions = usage_restrictions 

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
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if dictionary.get("AccountNumber") else APIHelper.SKIP
        reset_usage_restrictions = dictionary.get("ResetUsageRestrictions") if dictionary.get("ResetUsageRestrictions") else False
        usage_restrictions = UsageRestrictions.from_dictionary(dictionary.get('UsageRestrictions')) if 'UsageRestrictions' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   account_number,
                   reset_usage_restrictions,
                   usage_restrictions)
