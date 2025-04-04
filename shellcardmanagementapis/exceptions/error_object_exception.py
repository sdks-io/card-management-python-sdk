# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.models.error_details import ErrorDetails


class ErrorObjectException(APIException):
    def __init__(self, reason, response):
        """Constructor for the ErrorObjectException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(ErrorObjectException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.text)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else None
        self.status = dictionary.get("Status") if dictionary.get("Status") else None
        self.errors = None
        if dictionary.get('Errors') is not None:
            self.errors = [ErrorDetails.from_dictionary(x) for x in dictionary.get('Errors')]
        else:
            self.errors = None

    def __str__(self):
        base_str = super().__str__()
        return (f'{self.__class__.__name__}('
                f'{base_str[base_str.find("(") + 1:-1]}, '
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'errors={(self.errors if hasattr(self, "errors") else None)!s})')
