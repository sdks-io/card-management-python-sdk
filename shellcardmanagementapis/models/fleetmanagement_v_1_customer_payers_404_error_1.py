# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.fault import Fault


class FleetmanagementV1CustomerPayers404Error1(object):

    """Implementation of the 'FleetmanagementV1CustomerPayers404Error1' model.

    Attributes:
        fault (Fault): The model property of type Fault.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "fault": 'fault'
    }

    _optionals = [
        'fault',
    ]

    def __init__(self,
                 fault=APIHelper.SKIP):
        """Constructor for the FleetmanagementV1CustomerPayers404Error1 class"""

        # Initialize members of the class
        if fault is not APIHelper.SKIP:
            self.fault = fault 

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
        fault = Fault.from_dictionary(dictionary.get('fault')) if 'fault' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(fault)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'fault={(self.fault if hasattr(self, "fault") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'fault={(self.fault if hasattr(self, "fault") else None)!s})')
