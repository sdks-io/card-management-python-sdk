# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.card_move_response_error_cards_items import CardMoveResponseErrorCardsItems
from shellcardmanagementapis.models.card_move_response_successful_requests_items import CardMoveResponseSuccessfulRequestsItems
from shellcardmanagementapis.models.error_status import ErrorStatus


class CardMoveResponse(object):

    """Implementation of the 'CardMoveResponse' model.

    TODO: type model description here.

    Attributes:
        move_card_request_reference (int): TODO: type description here.
        successful_requests (List[CardMoveResponseSuccessfulRequestsItems]):
            TODO: type description here.
        error_cards (List[CardMoveResponseErrorCardsItems]): TODO: type
            description here.
        request_id (str): TODO: type description here.
        error (ErrorStatus): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "move_card_request_reference": 'MoveCardRequestReference',
        "successful_requests": 'SuccessfulRequests',
        "error_cards": 'ErrorCards',
        "request_id": 'RequestId',
        "error": 'Error'
    }

    _optionals = [
        'move_card_request_reference',
        'successful_requests',
        'error_cards',
        'request_id',
        'error',
    ]

    def __init__(self,
                 move_card_request_reference=APIHelper.SKIP,
                 successful_requests=APIHelper.SKIP,
                 error_cards=APIHelper.SKIP,
                 request_id=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the CardMoveResponse class"""

        # Initialize members of the class
        if move_card_request_reference is not APIHelper.SKIP:
            self.move_card_request_reference = move_card_request_reference 
        if successful_requests is not APIHelper.SKIP:
            self.successful_requests = successful_requests 
        if error_cards is not APIHelper.SKIP:
            self.error_cards = error_cards 
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
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
        move_card_request_reference = dictionary.get("MoveCardRequestReference") if dictionary.get("MoveCardRequestReference") else APIHelper.SKIP
        successful_requests = None
        if dictionary.get('SuccessfulRequests') is not None:
            successful_requests = [CardMoveResponseSuccessfulRequestsItems.from_dictionary(x) for x in dictionary.get('SuccessfulRequests')]
        else:
            successful_requests = APIHelper.SKIP
        error_cards = None
        if dictionary.get('ErrorCards') is not None:
            error_cards = [CardMoveResponseErrorCardsItems.from_dictionary(x) for x in dictionary.get('ErrorCards')]
        else:
            error_cards = APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(move_card_request_reference,
                   successful_requests,
                   error_cards,
                   request_id,
                   error)
