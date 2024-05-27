# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.search_request import SearchRequest


class SearchCardRequest(object):

    """Implementation of the 'SearchCardRequest' model.

    TODO: type model description here.

    Attributes:
        filters (SearchRequest): Encapsulate the Search details request.
        page_size (str): Page Size – Number of records to show on a page 
            Optional  Default value 50
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        filters = SearchRequest.from_dictionary(dictionary.get('Filters')) if 'Filters' in dictionary.keys() else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else APIHelper.SKIP
        page = dictionary.get("Page") if dictionary.get("Page") else APIHelper.SKIP
        # Return an object of this model
        return cls(filters,
                   page_size,
                   page)