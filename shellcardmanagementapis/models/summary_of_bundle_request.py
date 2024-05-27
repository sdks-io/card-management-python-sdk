# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.summaryof_bundle import SummaryofBundle


class SummaryOfBundleRequest(object):

    """Implementation of the 'SummaryOfBundleRequest' model.

    TODO: type model description here.

    Attributes:
        filters (SummaryofBundle): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "filters": 'Filters'
    }

    _optionals = [
        'filters',
    ]

    def __init__(self,
                 filters=APIHelper.SKIP):
        """Constructor for the SummaryOfBundleRequest class"""

        # Initialize members of the class
        if filters is not APIHelper.SKIP:
            self.filters = filters 

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
        filters = SummaryofBundle.from_dictionary(dictionary.get('Filters')) if 'Filters' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(filters)
