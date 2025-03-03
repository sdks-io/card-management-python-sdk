# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.error_details import ErrorDetails
from shellcardmanagementapis.models.submitted_card import SubmittedCard


class CancelCardResponse(object):

    """Implementation of the 'CancelCardResponse' model.

    Attributes:
        request_id (str): Unique request identifier passed from end user. This
            identifier helps in tracing a transaction
        main_reference (int): Cancel card reference number for tracking the
            execution of the request.
        order_replacement_reference (int): Order replacement reference number
            for tracking the execution of the order replacement cards request.
        status (str): Indicates overall status of the request. Allowed values:
            SUCCESS, FAILED, PARTIAL_SUCCESS
        data (List[SubmittedCard]): The model property of type
            List[SubmittedCard].
        errors (List[ErrorDetails]): The model property of type
            List[ErrorDetails].

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "main_reference": 'MainReference',
        "order_replacement_reference": 'OrderReplacementReference',
        "status": 'Status',
        "data": 'Data',
        "errors": 'Errors'
    }

    _optionals = [
        'request_id',
        'main_reference',
        'order_replacement_reference',
        'status',
        'data',
        'errors',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 main_reference=APIHelper.SKIP,
                 order_replacement_reference=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 data=APIHelper.SKIP,
                 errors=APIHelper.SKIP):
        """Constructor for the CancelCardResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if main_reference is not APIHelper.SKIP:
            self.main_reference = main_reference 
        if order_replacement_reference is not APIHelper.SKIP:
            self.order_replacement_reference = order_replacement_reference 
        if status is not APIHelper.SKIP:
            self.status = status 
        if data is not APIHelper.SKIP:
            self.data = data 
        if errors is not APIHelper.SKIP:
            self.errors = errors 

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
        main_reference = dictionary.get("MainReference") if dictionary.get("MainReference") else APIHelper.SKIP
        order_replacement_reference = dictionary.get("OrderReplacementReference") if dictionary.get("OrderReplacementReference") else APIHelper.SKIP
        status = dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        data = None
        if dictionary.get('Data') is not None:
            data = [SubmittedCard.from_dictionary(x) for x in dictionary.get('Data')]
        else:
            data = APIHelper.SKIP
        errors = None
        if dictionary.get('Errors') is not None:
            errors = [ErrorDetails.from_dictionary(x) for x in dictionary.get('Errors')]
        else:
            errors = APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   main_reference,
                   order_replacement_reference,
                   status,
                   data,
                   errors)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!r}, '
                f'main_reference={(self.main_reference if hasattr(self, "main_reference") else None)!r}, '
                f'order_replacement_reference={(self.order_replacement_reference if hasattr(self, "order_replacement_reference") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'data={(self.data if hasattr(self, "data") else None)!r}, '
                f'errors={(self.errors if hasattr(self, "errors") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s}, '
                f'main_reference={(self.main_reference if hasattr(self, "main_reference") else None)!s}, '
                f'order_replacement_reference={(self.order_replacement_reference if hasattr(self, "order_replacement_reference") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'data={(self.data if hasattr(self, "data") else None)!s}, '
                f'errors={(self.errors if hasattr(self, "errors") else None)!s})')
