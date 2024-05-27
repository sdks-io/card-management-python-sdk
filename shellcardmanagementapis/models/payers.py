# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class Payers(object):

    """Implementation of the 'Payers' model.

    TODO: type model description here.

    Attributes:
        col_co_id (int): Collecting Company Id of the payer
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.
        payer_id (int): Payer id of the customer.
        payer_number (str): Payer Number of the customer.
        payer_name (str): Payer Name of the customer.
        payer_group_id (int): Payer Group identifier of the customer

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "payer_name": 'PayerName',
        "payer_group_id": 'PayerGroupId'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'payer_name',
        'payer_group_id',
    ]

    _nullables = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'payer_name',
        'payer_group_id',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_name=APIHelper.SKIP,
                 payer_group_id=APIHelper.SKIP):
        """Constructor for the Payers class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_name is not APIHelper.SKIP:
            self.payer_name = payer_name 
        if payer_group_id is not APIHelper.SKIP:
            self.payer_group_id = payer_group_id 

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
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        payer_name = dictionary.get("PayerName") if "PayerName" in dictionary.keys() else APIHelper.SKIP
        payer_group_id = dictionary.get("PayerGroupId") if "PayerGroupId" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   payer_name,
                   payer_group_id)
