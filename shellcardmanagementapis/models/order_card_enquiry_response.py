# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.order_card_enquiry import OrderCardEnquiry


class OrderCardEnquiryResponse(object):

    """Implementation of the 'OrderCardEnquiryResponse' model.

    TODO: type model description here.

    Attributes:
        request_id (str): TODO: type description here.
        status (str): TODO: type description here.
        data (List[OrderCardEnquiry]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "status": 'Status',
        "data": 'Data'
    }

    _optionals = [
        'request_id',
        'status',
        'data',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 data=APIHelper.SKIP):
        """Constructor for the OrderCardEnquiryResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if data is not APIHelper.SKIP:
            self.data = data 

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
        data = None
        if dictionary.get('Data') is not None:
            data = [OrderCardEnquiry.from_dictionary(x) for x in dictionary.get('Data')]
        else:
            data = APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   status,
                   data)
