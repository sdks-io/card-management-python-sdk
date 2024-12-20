# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class UpdateMPayRegStatusResponse(object):

    """Implementation of the 'UpdateMPayRegStatusResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (str): API Request Id
        status (str): API Response Status

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "status": 'Status'
    }

    _optionals = [
        'request_id',
        'status',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the UpdateMPayRegStatusResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        status = dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   status)
