# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.error_status import ErrorStatus
from shellcardmanagementapis.models.restrictioncards_res import RestrictioncardsRes


class CardRestrictionResponse(object):

    """Implementation of the 'CardRestrictionResponse' model.

    Attributes:
        request_id (str): Request Id of the API call
        restriction_request_reference (float): Reference number for tracking
            the execution of the card restriction requests.
        cards (List[RestrictioncardsRes]): The model property of type
            List[RestrictioncardsRes].
        error (ErrorStatus): The model property of type ErrorStatus.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "restriction_request_reference": 'RestrictionRequestReference',
        "cards": 'Cards',
        "error": 'Error'
    }

    _optionals = [
        'request_id',
        'restriction_request_reference',
        'cards',
        'error',
    ]

    _nullables = [
        'request_id',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 restriction_request_reference=APIHelper.SKIP,
                 cards=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the CardRestrictionResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if restriction_request_reference is not APIHelper.SKIP:
            self.restriction_request_reference = restriction_request_reference 
        if cards is not APIHelper.SKIP:
            self.cards = cards 
        if error is not APIHelper.SKIP:
            self.error = error 

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
        request_id = dictionary.get("RequestId") if "RequestId" in dictionary.keys() else APIHelper.SKIP
        restriction_request_reference = dictionary.get("RestrictionRequestReference") if dictionary.get("RestrictionRequestReference") else APIHelper.SKIP
        cards = None
        if dictionary.get('Cards') is not None:
            cards = [RestrictioncardsRes.from_dictionary(x) for x in dictionary.get('Cards')]
        else:
            cards = APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   restriction_request_reference,
                   cards,
                   error)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!r}, '
                f'restriction_request_reference={(self.restriction_request_reference if hasattr(self, "restriction_request_reference") else None)!r}, '
                f'cards={(self.cards if hasattr(self, "cards") else None)!r}, '
                f'error={(self.error if hasattr(self, "error") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s}, '
                f'restriction_request_reference={(self.restriction_request_reference if hasattr(self, "restriction_request_reference") else None)!s}, '
                f'cards={(self.cards if hasattr(self, "cards") else None)!s}, '
                f'error={(self.error if hasattr(self, "error") else None)!s})')
