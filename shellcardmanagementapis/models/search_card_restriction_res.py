# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.error_status import ErrorStatus
from shellcardmanagementapis.models.restriction import Restriction
from shellcardmanagementapis.models.restriction_card_list import RestrictionCardList


class SearchCardRestrictionRes(object):

    """Implementation of the 'SearchCardRestrictionRes' model.

    TODO: type model description here.

    Attributes:
        request_id (str): Request Id of the API call
        cards (List[RestrictionCardList]): TODO: type description here.
        restrictions (Restriction): TODO: type description here.
        error (ErrorStatus): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "cards": 'cards',
        "restrictions": 'Restrictions',
        "error": 'Error'
    }

    _optionals = [
        'request_id',
        'cards',
        'restrictions',
        'error',
    ]

    _nullables = [
        'request_id',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 cards=APIHelper.SKIP,
                 restrictions=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the SearchCardRestrictionRes class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if cards is not APIHelper.SKIP:
            self.cards = cards 
        if restrictions is not APIHelper.SKIP:
            self.restrictions = restrictions 
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
        cards = None
        if dictionary.get('cards') is not None:
            cards = [RestrictionCardList.from_dictionary(x) for x in dictionary.get('cards')]
        else:
            cards = APIHelper.SKIP
        restrictions = Restriction.from_dictionary(dictionary.get('Restrictions')) if 'Restrictions' in dictionary.keys() else APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   cards,
                   restrictions,
                   error)
