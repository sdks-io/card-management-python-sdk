# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.product_group import ProductGroup


class PurchaseCategory1AllOf0(object):

    """Implementation of the 'PurchaseCategory1AllOf0' model.

    Attributes:
        id (int): Purchase category ID
        code (str): Purchase category code
        name (str): Name of Purchase category .
        is_visible (bool): PurchaseCategory can be used while submitting new
            order cards requests if true else will not be used for ordering
            cards.
        product_groups (List[ProductGroup]): List of product sets
        title (str): Purchase category Title by given language code.  1.   
            Basic   2.    Essentials  3.    Extra   4.    Premium  5.    Basic
            and LNG  6.    Essentials and LNG  7.    Extra and LNG  8.   
            Premium and LNG  Note: Purchase Category name (GFN) is returned
            when Title does not exist for the given language Code and default
            language code (en-GB).
        description (str): Purchase category description by given language
            code.  Example:   0 - Diesel Products and TMF  1 - All Fuel
            Products and TMF  2 - All Fuels Products, Car related items and
            TMF  3 - No Restriction  0 - Diesel Products + LNG and TMF  1 -
            All Fuel Products + LNG and TMF  2 - All Fuels Products + LNG, Car
            related items and TMF  3 - No Restriction + LNG   Note: Purchase
            Category name (GFN) is returned when Title does not exist for the
            given language Code and default language code (en-GB).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'Id',
        "code": 'Code',
        "name": 'Name',
        "is_visible": 'IsVisible',
        "product_groups": 'ProductGroups',
        "title": 'Title',
        "description": 'Description'
    }

    _optionals = [
        'title',
        'description',
    ]

    _nullables = [
        'id',
        'code',
        'name',
    ]

    def __init__(self,
                 id=None,
                 code=None,
                 name=None,
                 is_visible=None,
                 product_groups=None,
                 title=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the PurchaseCategory1AllOf0 class"""

        # Initialize members of the class
        self.id = id 
        self.code = code 
        self.name = name 
        self.is_visible = is_visible 
        self.product_groups = product_groups 
        if title is not APIHelper.SKIP:
            self.title = title 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        id = dictionary.get("Id") if dictionary.get("Id") else None
        code = dictionary.get("Code") if dictionary.get("Code") else None
        name = dictionary.get("Name") if dictionary.get("Name") else None
        is_visible = dictionary.get("IsVisible") if "IsVisible" in dictionary.keys() else None
        product_groups = None
        if dictionary.get('ProductGroups') is not None:
            product_groups = [ProductGroup.from_dictionary(x) for x in dictionary.get('ProductGroups')]
        title = dictionary.get("Title") if dictionary.get("Title") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   code,
                   name,
                   is_visible,
                   product_groups,
                   title,
                   description)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'code={self.code!r}, '
                f'name={self.name!r}, '
                f'is_visible={self.is_visible!r}, '
                f'product_groups={self.product_groups!r}, '
                f'title={(self.title if hasattr(self, "title") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'code={self.code!s}, '
                f'name={self.name!s}, '
                f'is_visible={self.is_visible!s}, '
                f'product_groups={self.product_groups!s}, '
                f'title={(self.title if hasattr(self, "title") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s})')
