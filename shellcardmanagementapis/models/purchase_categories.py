# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class PurchaseCategories(object):

    """Implementation of the 'PurchaseCategories' model.

    TODO: type model description here.

    Attributes:
        id (int): Purchase category Id
        code (str): Purchase category code  Example: 0,1, 2 etc.  Full list
            below:  0 - All Fuels (without VP) and Lubricants  1 - Fuel Save
            only  2 - Fuel Save and Lubricants  3 - No Restrictions  4 - VP
            and Fuel Save  5 - Diesel ONLY  6 - Diesel and Lubricants  7 - VP
            and Lubricants  8 - VP and Fuel Save and Lubricants
        name (str): Purchase category name   Example: Fuel Save Only  Full
            list below:  0 - All Fuels (without VP) and Lubricants  1 - Fuel
            Save only  2 - Fuel Save and Lubricants  3 - No Restrictions  4 -
            VP and Fuel Save  5 - Diesel ONLY  6 - Diesel and Lubricants  7 -
            VP and Lubricants  8 - VP and Fuel Save and Lubricants
        is_visible (bool): If True then PurchaseCategory can be used while
            submitting new order cards requests.  If false this
            PurchaseCategory will not be used for Ordering Cards.
        product_groups (str): List of Default product groups

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'Id',
        "code": 'Code',
        "name": 'Name',
        "is_visible": 'IsVisible',
        "product_groups": 'ProductGroups'
    }

    _optionals = [
        'id',
        'code',
        'name',
        'is_visible',
        'product_groups',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 is_visible=APIHelper.SKIP,
                 product_groups=APIHelper.SKIP):
        """Constructor for the PurchaseCategories class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if code is not APIHelper.SKIP:
            self.code = code 
        if name is not APIHelper.SKIP:
            self.name = name 
        if is_visible is not APIHelper.SKIP:
            self.is_visible = is_visible 
        if product_groups is not APIHelper.SKIP:
            self.product_groups = product_groups 

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
        id = dictionary.get("Id") if dictionary.get("Id") else APIHelper.SKIP
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        is_visible = dictionary.get("IsVisible") if "IsVisible" in dictionary.keys() else APIHelper.SKIP
        product_groups = dictionary.get("ProductGroups") if dictionary.get("ProductGroups") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   code,
                   name,
                   is_visible,
                   product_groups)