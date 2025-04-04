# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CustomerContract(object):

    """Implementation of the 'CustomerContract' model.

    Attributes:
        partner_id (str): Partner Id in e-TM system
        partner_name (str): Partner Name in e-TM system

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "partner_id": 'PartnerId',
        "partner_name": 'PartnerName'
    }

    _optionals = [
        'partner_id',
        'partner_name',
    ]

    _nullables = [
        'partner_id',
        'partner_name',
    ]

    def __init__(self,
                 partner_id=APIHelper.SKIP,
                 partner_name=APIHelper.SKIP):
        """Constructor for the CustomerContract class"""

        # Initialize members of the class
        if partner_id is not APIHelper.SKIP:
            self.partner_id = partner_id 
        if partner_name is not APIHelper.SKIP:
            self.partner_name = partner_name 

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
        partner_id = dictionary.get("PartnerId") if "PartnerId" in dictionary.keys() else APIHelper.SKIP
        partner_name = dictionary.get("PartnerName") if "PartnerName" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(partner_id,
                   partner_name)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'partner_id={(self.partner_id if hasattr(self, "partner_id") else None)!r}, '
                f'partner_name={(self.partner_name if hasattr(self, "partner_name") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'partner_id={(self.partner_id if hasattr(self, "partner_id") else None)!s}, '
                f'partner_name={(self.partner_name if hasattr(self, "partner_name") else None)!s})')
