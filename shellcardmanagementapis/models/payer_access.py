# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class PayerAccess(object):

    """Implementation of the 'PayerAccess' model.

    Attributes:
        is_default (bool): Whether this payer is the default payer of the user.
        colco_id (int): Collecting company id.
        colco_code (int): Collecting company code. Example: 86-Philippines 5-UK
        col_co_country_code (str): The 2-character ISO Code for the customer
            and card owning country
        payer_group_id (int): Payer Group Id of the payer.
        payer_group (str): Payer group of the payer.   The value of this
            parameter will always be null when the input parameter
            “IncludePayerGroup” is false.
        payer_id (int): Payer Id to which the user has access Example: 123456
        payer_number (str): Payer Number to which the user has access Example:
            GB000000123
        payer_name (str): Name of the Payer to which the user has access

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "is_default": 'IsDefault',
        "colco_id": 'ColcoId',
        "colco_code": 'ColcoCode',
        "col_co_country_code": 'ColCoCountryCode',
        "payer_group_id": 'PayerGroupId',
        "payer_group": 'PayerGroup',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "payer_name": 'PayerName'
    }

    _optionals = [
        'is_default',
        'colco_id',
        'colco_code',
        'col_co_country_code',
        'payer_group_id',
        'payer_group',
        'payer_id',
        'payer_number',
        'payer_name',
    ]

    _nullables = [
        'colco_id',
        'colco_code',
        'col_co_country_code',
        'payer_group_id',
        'payer_group',
        'payer_id',
        'payer_number',
        'payer_name',
    ]

    def __init__(self,
                 is_default=False,
                 colco_id=APIHelper.SKIP,
                 colco_code=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 payer_group_id=APIHelper.SKIP,
                 payer_group=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_name=APIHelper.SKIP):
        """Constructor for the PayerAccess class"""

        # Initialize members of the class
        self.is_default = is_default 
        if colco_id is not APIHelper.SKIP:
            self.colco_id = colco_id 
        if colco_code is not APIHelper.SKIP:
            self.colco_code = colco_code 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if payer_group_id is not APIHelper.SKIP:
            self.payer_group_id = payer_group_id 
        if payer_group is not APIHelper.SKIP:
            self.payer_group = payer_group 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_name is not APIHelper.SKIP:
            self.payer_name = payer_name 

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
        is_default = dictionary.get("IsDefault") if dictionary.get("IsDefault") else False
        colco_id = dictionary.get("ColcoId") if "ColcoId" in dictionary.keys() else APIHelper.SKIP
        colco_code = dictionary.get("ColcoCode") if "ColcoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        payer_group_id = dictionary.get("PayerGroupId") if "PayerGroupId" in dictionary.keys() else APIHelper.SKIP
        payer_group = dictionary.get("PayerGroup") if "PayerGroup" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_name = dictionary.get("PayerName") if "PayerName" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(is_default,
                   colco_id,
                   colco_code,
                   col_co_country_code,
                   payer_group_id,
                   payer_group,
                   payer_id,
                   payer_number,
                   payer_name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'is_default={(self.is_default if hasattr(self, "is_default") else None)!r}, '
                f'colco_id={(self.colco_id if hasattr(self, "colco_id") else None)!r}, '
                f'colco_code={(self.colco_code if hasattr(self, "colco_code") else None)!r}, '
                f'col_co_country_code={(self.col_co_country_code if hasattr(self, "col_co_country_code") else None)!r}, '
                f'payer_group_id={(self.payer_group_id if hasattr(self, "payer_group_id") else None)!r}, '
                f'payer_group={(self.payer_group if hasattr(self, "payer_group") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'payer_name={(self.payer_name if hasattr(self, "payer_name") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'is_default={(self.is_default if hasattr(self, "is_default") else None)!s}, '
                f'colco_id={(self.colco_id if hasattr(self, "colco_id") else None)!s}, '
                f'colco_code={(self.colco_code if hasattr(self, "colco_code") else None)!s}, '
                f'col_co_country_code={(self.col_co_country_code if hasattr(self, "col_co_country_code") else None)!s}, '
                f'payer_group_id={(self.payer_group_id if hasattr(self, "payer_group_id") else None)!s}, '
                f'payer_group={(self.payer_group if hasattr(self, "payer_group") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'payer_name={(self.payer_name if hasattr(self, "payer_name") else None)!s})')
