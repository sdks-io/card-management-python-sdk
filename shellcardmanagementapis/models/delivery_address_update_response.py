# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.delivery_address_update_references import DeliveryAddressUpdateReferences
from shellcardmanagementapis.models.error_status import ErrorStatus


class DeliveryAddressUpdateResponse(object):

    """Implementation of the 'DeliveryAddressUpdateResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (str): Request ID to which was passed on the API request.
        service_reference (int): Service reference number for tracking.
        delivery_address_update_references
            (List[DeliveryAddressUpdateReferences]): TODO: type description
            here.
        error (ErrorStatus): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "service_reference": 'ServiceReference',
        "delivery_address_update_references": 'DeliveryAddressUpdateReferences',
        "error": 'Error'
    }

    _optionals = [
        'request_id',
        'service_reference',
        'delivery_address_update_references',
        'error',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 service_reference=APIHelper.SKIP,
                 delivery_address_update_references=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the DeliveryAddressUpdateResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if service_reference is not APIHelper.SKIP:
            self.service_reference = service_reference 
        if delivery_address_update_references is not APIHelper.SKIP:
            self.delivery_address_update_references = delivery_address_update_references 
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        service_reference = dictionary.get("ServiceReference") if dictionary.get("ServiceReference") else APIHelper.SKIP
        delivery_address_update_references = None
        if dictionary.get('DeliveryAddressUpdateReferences') is not None:
            delivery_address_update_references = [DeliveryAddressUpdateReferences.from_dictionary(x) for x in dictionary.get('DeliveryAddressUpdateReferences')]
        else:
            delivery_address_update_references = APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   service_reference,
                   delivery_address_update_references,
                   error)