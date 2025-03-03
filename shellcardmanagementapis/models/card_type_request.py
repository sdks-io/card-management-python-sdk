# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardTypeRequest(object):

    """Implementation of the 'CardTypeRequest' model.

    Attributes:
        col_co_id (int): Collecting Company Id of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.
        payer_id (int): Payer Id of the selected payer.
        payer_number (str): Payer Number of the selected payer.
        account_id (int): Account Id of the customer. Optional if
            AccountNumber is passed else Mandatory.
        account_number (str): Account Number of the customer. Optional if
            AccountId is passed else Mandatory Example: GB000000124
        include_usage_restrictions (bool): Include usage restrictions in the
            response. Optional field– default value is False. Possible values:
            True/False
        include_purchase_categories (bool): Include purchase categories in the
            response. Optional field– default value is False. Possible values:
            True/False

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "include_usage_restrictions": 'IncludeUsageRestrictions',
        "include_purchase_categories": 'IncludePurchaseCategories'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'account_id',
        'account_number',
        'include_usage_restrictions',
        'include_purchase_categories',
    ]

    _nullables = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'account_id',
        'account_number',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 include_usage_restrictions=APIHelper.SKIP,
                 include_purchase_categories=APIHelper.SKIP):
        """Constructor for the CardTypeRequest class"""

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
        if include_usage_restrictions is not APIHelper.SKIP:
            self.include_usage_restrictions = include_usage_restrictions 
        if include_purchase_categories is not APIHelper.SKIP:
            self.include_purchase_categories = include_purchase_categories 

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
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        include_usage_restrictions = dictionary.get("IncludeUsageRestrictions") if "IncludeUsageRestrictions" in dictionary.keys() else APIHelper.SKIP
        include_purchase_categories = dictionary.get("IncludePurchaseCategories") if "IncludePurchaseCategories" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   account_id,
                   account_number,
                   include_usage_restrictions,
                   include_purchase_categories)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'include_usage_restrictions={(self.include_usage_restrictions if hasattr(self, "include_usage_restrictions") else None)!r}, '
                f'include_purchase_categories={(self.include_purchase_categories if hasattr(self, "include_purchase_categories") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'include_usage_restrictions={(self.include_usage_restrictions if hasattr(self, "include_usage_restrictions") else None)!s}, '
                f'include_purchase_categories={(self.include_purchase_categories if hasattr(self, "include_purchase_categories") else None)!s})')
