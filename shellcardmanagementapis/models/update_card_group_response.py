# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.error_status import ErrorStatus
from shellcardmanagementapis.models.update_card_group_response_move_card_references_items import UpdateCardGroupResponseMoveCardReferencesItems


class UpdateCardGroupResponse(object):

    """Implementation of the 'UpdateCardGroupResponse' model.

    TODO: type model description here.

    Attributes:
        main_reference (int): Reference number for tracking the overall
            request.  The value will be null when the validation fails.
        update_card_group_reference (int): Reference number for tracking the
            execution of terminate card-group request.  Reference number will
            be null when the validations fail or TerminateCardGroup in the
            request object is false.
        new_card_group_reference (int): Reference number for tracking the
            execution of new card group creation in the case when the cards in
            the terminating card-group have to be moved to a new card-group.  
            Reference number will be null when the validations fail or new
            card-group creation is not requested.
        move_card_references
            (List[UpdateCardGroupResponseMoveCardReferencesItems]): List of
            cards submitted successfully for processing the move to the target
            card-group or to change card-group to null.  This list will be
            empty when the validations fail or there are no cards in the
            card-group that is getting terminated or MoveCards in the request
            object is false
        error (ErrorStatus): TODO: type description here.
        request_id (str): API Request ID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "main_reference": 'MainReference',
        "update_card_group_reference": 'UpdateCardGroupReference',
        "new_card_group_reference": 'NewCardGroupReference',
        "move_card_references": 'MoveCardReferences',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'main_reference',
        'update_card_group_reference',
        'new_card_group_reference',
        'move_card_references',
        'error',
        'request_id',
    ]

    def __init__(self,
                 main_reference=APIHelper.SKIP,
                 update_card_group_reference=APIHelper.SKIP,
                 new_card_group_reference=APIHelper.SKIP,
                 move_card_references=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the UpdateCardGroupResponse class"""

        # Initialize members of the class
        if main_reference is not APIHelper.SKIP:
            self.main_reference = main_reference 
        if update_card_group_reference is not APIHelper.SKIP:
            self.update_card_group_reference = update_card_group_reference 
        if new_card_group_reference is not APIHelper.SKIP:
            self.new_card_group_reference = new_card_group_reference 
        if move_card_references is not APIHelper.SKIP:
            self.move_card_references = move_card_references 
        if error is not APIHelper.SKIP:
            self.error = error 
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 

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
        main_reference = dictionary.get("MainReference") if dictionary.get("MainReference") else APIHelper.SKIP
        update_card_group_reference = dictionary.get("UpdateCardGroupReference") if dictionary.get("UpdateCardGroupReference") else APIHelper.SKIP
        new_card_group_reference = dictionary.get("NewCardGroupReference") if dictionary.get("NewCardGroupReference") else APIHelper.SKIP
        move_card_references = None
        if dictionary.get('MoveCardReferences') is not None:
            move_card_references = [UpdateCardGroupResponseMoveCardReferencesItems.from_dictionary(x) for x in dictionary.get('MoveCardReferences')]
        else:
            move_card_references = APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(main_reference,
                   update_card_group_reference,
                   new_card_group_reference,
                   move_card_references,
                   error,
                   request_id)