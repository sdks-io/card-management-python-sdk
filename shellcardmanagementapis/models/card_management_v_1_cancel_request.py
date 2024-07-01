# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.update_card import UpdateCard


class CardManagementV1CancelRequest(object):

    """Implementation of the 'Card Management V1 Cancel Request' model.

    TODO: type model description here.

    Attributes:
        cards (List[UpdateCard]): List of CancelCardRequest entity.   Each
            card in the list will be Cancelled.   The details of the entity
            are given below.
        reason_id (int): Reason id for cancelling the card.<br /> Optional if
            ReasonText is passed, else mandatory<br /> When passed, the reason
            Id will be validated with the allowed reason id’s configured for
            the card type of the card.<br /> If the reason Id is not allowed,
            then it will be included on the error cards response.   Possible
            values: 1 (Lost) 2 (Stolen) 3 (Card no longer required)
        reason_text (str): Reason text for cancelling the card.<br /> 
            Optional if ReasonId is passed, else mandatory<br />  When Reason
            Id is not known to the client, the reason text can be passed.<br
            />  When Reason Text is passed and the Target Status is either
            Block or Damaged, the text will be validated with the allowed list
            of values configured for the card type of the card.  If the text
            is not allowed, then it will be included on the error cards
            response.  However, if the Target status is Temporary block or
            Unblock then the text will be submitted     Possible Values:  1)
            Lost  2) Stolen  3) Card no longer required

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cards": 'Cards',
        "reason_id": 'ReasonId',
        "reason_text": 'ReasonText'
    }

    _optionals = [
        'reason_id',
        'reason_text',
    ]

    _nullables = [
        'reason_id',
        'reason_text',
    ]

    def __init__(self,
                 cards=None,
                 reason_id=APIHelper.SKIP,
                 reason_text=APIHelper.SKIP):
        """Constructor for the CardManagementV1CancelRequest class"""

        # Initialize members of the class
        self.cards = cards 
        if reason_id is not APIHelper.SKIP:
            self.reason_id = reason_id 
        if reason_text is not APIHelper.SKIP:
            self.reason_text = reason_text 

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
        cards = None
        if dictionary.get('Cards') is not None:
            cards = [UpdateCard.from_dictionary(x) for x in dictionary.get('Cards')]
        reason_id = dictionary.get("ReasonId") if "ReasonId" in dictionary.keys() else APIHelper.SKIP
        reason_text = dictionary.get("ReasonText") if "ReasonText" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(cards,
                   reason_id,
                   reason_text)