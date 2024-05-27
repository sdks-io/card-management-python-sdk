# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.card_detail import CardDetail


class OrderCardRequest(object):

    """Implementation of the 'OrderCardRequest' model.

    This entity models the data that is sent in the http request body for this
    operation.

    Attributes:
        card_details (List[CardDetail]): List of CardOrder entity. The fields
            in this entity are described below.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_details": 'CardDetails'
    }

    _optionals = [
        'card_details',
    ]

    def __init__(self,
                 card_details=APIHelper.SKIP):
        """Constructor for the OrderCardRequest class"""

        # Initialize members of the class
        if card_details is not APIHelper.SKIP:
            self.card_details = card_details 

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
        card_details = None
        if dictionary.get('CardDetails') is not None:
            card_details = [CardDetail.from_dictionary(x) for x in dictionary.get('CardDetails')]
        else:
            card_details = APIHelper.SKIP
        # Return an object of this model
        return cls(card_details)
