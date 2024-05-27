# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class LoggedInUserRequest(object):

    """Implementation of the 'LoggedInUserRequest' model.

    This entity models the data that is sent in the http request body for
    Logged In User operation. This class inherits RequestBase class.

    Attributes:
        include_payer_group (bool): True/False. The output will include the
            payer group information only when true is passed.
        include_eid_details (bool): True/False. The output will include the
            EID (Electronic Invoice data) information only when true is
            passed..
        requested_api_name (str): Name of the API on which user access needs
            to be validated Optional.
        payer_id (int): Payer id of the customer.</br> Optional.</br> This
            input is a search criterion.</br> Note: If PayerId or PayerNumber
            is provided in the input, the given payer will be available in the
            output if the user has access to the given payer.
        payer_number (str): PayerNumber of the customer.</br> Optional</br>
            This input is a search criterion.</br> Note: If Payerid or
            PayerNumber is provided in the input, the given payer will be
            available in the output if the user has access to the given
            payer.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "include_payer_group": 'IncludePayerGroup',
        "include_eid_details": 'IncludeEIDDetails',
        "requested_api_name": 'RequestedAPIName',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber'
    }

    _optionals = [
        'include_payer_group',
        'include_eid_details',
        'requested_api_name',
        'payer_id',
        'payer_number',
    ]

    _nullables = [
        'requested_api_name',
        'payer_id',
        'payer_number',
    ]

    def __init__(self,
                 include_payer_group=False,
                 include_eid_details=False,
                 requested_api_name=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP):
        """Constructor for the LoggedInUserRequest class"""

        # Initialize members of the class
        self.include_payer_group = include_payer_group 
        self.include_eid_details = include_eid_details 
        if requested_api_name is not APIHelper.SKIP:
            self.requested_api_name = requested_api_name 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 

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
        include_payer_group = dictionary.get("IncludePayerGroup") if dictionary.get("IncludePayerGroup") else False
        include_eid_details = dictionary.get("IncludeEIDDetails") if dictionary.get("IncludeEIDDetails") else False
        requested_api_name = dictionary.get("RequestedAPIName") if "RequestedAPIName" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(include_payer_group,
                   include_eid_details,
                   requested_api_name,
                   payer_id,
                   payer_number)
