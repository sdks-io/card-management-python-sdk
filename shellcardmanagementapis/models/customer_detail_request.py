# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CustomerDetailRequest(object):

    """Implementation of the 'CustomerDetailRequest' model.

    Attributes:
        col_co_id (int): Collecting Company Id (in GFN) of the selected payer.
            Optional if ColCoCode is passed else Mandatory.  Example: 
            1-Philippines  5-UK
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86-Philippines  5-UK
        payer_id (int): Payer Id (i.e., Customer Id of the Payment Customer in
            H3 Cards Platform) of the selected payer. Optional if PayerNumber
            is passed else Mandatory Example: 123456
        payer_number (str): Payer Number of the selected payer. Optional if
            PayerId is passed else Mandatory Example: GB000000123
        account_id (int): Account ID of the customer. Optional if
            AccountNumber is passed else Mandatory.
        account_number (str): Account Number of the customer. Optional if
            AccountId is passed else Mandatory.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'account_id',
        'account_number',
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
                 account_number=APIHelper.SKIP):
        """Constructor for the CustomerDetailRequest class"""

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
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   account_id,
                   account_number)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s})')
