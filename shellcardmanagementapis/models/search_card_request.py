# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.filters import Filters


class SearchCardRequest(object):

    """Implementation of the 'SearchCardRequest' model.

    Attributes:
        filters (Filters): The model property of type Filters.
        page_size (str): Page Size – Number of records to show on a page
            Optional Default value 50
        page (str): Page Number

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filters": 'Filters',
        "page_size": 'PageSize',
        "page": 'Page'
    }

    _optionals = [
        'filters',
        'page_size',
        'page',
    ]

    def __init__(self,
                 filters=APIHelper.SKIP,
                 page_size=APIHelper.SKIP,
                 page=APIHelper.SKIP):
        """Constructor for the SearchCardRequest class"""

        # Initialize members of the class
        if filters is not APIHelper.SKIP:
            self.filters = filters 
        if page_size is not APIHelper.SKIP:
            self.page_size = page_size 
        if page is not APIHelper.SKIP:
            self.page = page 

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
        filters = Filters.from_dictionary(dictionary.get('Filters')) if 'Filters' in dictionary.keys() else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else APIHelper.SKIP
        page = dictionary.get("Page") if dictionary.get("Page") else APIHelper.SKIP
        # Return an object of this model
        return cls(filters,
                   page_size,
                   page)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'filters={(self.filters if hasattr(self, "filters") else None)!r}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!r}, '
                f'page={(self.page if hasattr(self, "page") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'filters={(self.filters if hasattr(self, "filters") else None)!s}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!s}, '
                f'page={(self.page if hasattr(self, "page") else None)!s})')
