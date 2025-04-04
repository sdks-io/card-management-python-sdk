# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.error_status import ErrorStatus


class UpdateBundleResponse(object):

    """Implementation of the 'UpdateBundleResponse' model.

    Attributes:
        request_id (str): Request Id of the API call
        request_action_status (ErrorStatus): The model property of type
            ErrorStatus.
        day_time_restriction_status (ErrorStatus): The model property of type
            ErrorStatus.
        location_restriction_status (ErrorStatus): The model property of type
            ErrorStatus.
        product_restriction_status (ErrorStatus): The model property of type
            ErrorStatus.
        usage_restriction_status (ErrorStatus): The model property of type
            ErrorStatus.
        error (ErrorStatus): The model property of type ErrorStatus.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "request_action_status": 'RequestActionStatus',
        "day_time_restriction_status": 'DayTimeRestrictionStatus',
        "location_restriction_status": 'LocationRestrictionStatus',
        "product_restriction_status": 'ProductRestrictionStatus',
        "usage_restriction_status": 'UsageRestrictionStatus',
        "error": 'Error'
    }

    _optionals = [
        'request_id',
        'request_action_status',
        'day_time_restriction_status',
        'location_restriction_status',
        'product_restriction_status',
        'usage_restriction_status',
        'error',
    ]

    _nullables = [
        'request_id',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 request_action_status=APIHelper.SKIP,
                 day_time_restriction_status=APIHelper.SKIP,
                 location_restriction_status=APIHelper.SKIP,
                 product_restriction_status=APIHelper.SKIP,
                 usage_restriction_status=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the UpdateBundleResponse class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if request_action_status is not APIHelper.SKIP:
            self.request_action_status = request_action_status 
        if day_time_restriction_status is not APIHelper.SKIP:
            self.day_time_restriction_status = day_time_restriction_status 
        if location_restriction_status is not APIHelper.SKIP:
            self.location_restriction_status = location_restriction_status 
        if product_restriction_status is not APIHelper.SKIP:
            self.product_restriction_status = product_restriction_status 
        if usage_restriction_status is not APIHelper.SKIP:
            self.usage_restriction_status = usage_restriction_status 
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
        request_id = dictionary.get("RequestId") if "RequestId" in dictionary.keys() else APIHelper.SKIP
        request_action_status = ErrorStatus.from_dictionary(dictionary.get('RequestActionStatus')) if 'RequestActionStatus' in dictionary.keys() else APIHelper.SKIP
        day_time_restriction_status = ErrorStatus.from_dictionary(dictionary.get('DayTimeRestrictionStatus')) if 'DayTimeRestrictionStatus' in dictionary.keys() else APIHelper.SKIP
        location_restriction_status = ErrorStatus.from_dictionary(dictionary.get('LocationRestrictionStatus')) if 'LocationRestrictionStatus' in dictionary.keys() else APIHelper.SKIP
        product_restriction_status = ErrorStatus.from_dictionary(dictionary.get('ProductRestrictionStatus')) if 'ProductRestrictionStatus' in dictionary.keys() else APIHelper.SKIP
        usage_restriction_status = ErrorStatus.from_dictionary(dictionary.get('UsageRestrictionStatus')) if 'UsageRestrictionStatus' in dictionary.keys() else APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   request_action_status,
                   day_time_restriction_status,
                   location_restriction_status,
                   product_restriction_status,
                   usage_restriction_status,
                   error)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!r}, '
                f'request_action_status={(self.request_action_status if hasattr(self, "request_action_status") else None)!r}, '
                f'day_time_restriction_status={(self.day_time_restriction_status if hasattr(self, "day_time_restriction_status") else None)!r}, '
                f'location_restriction_status={(self.location_restriction_status if hasattr(self, "location_restriction_status") else None)!r}, '
                f'product_restriction_status={(self.product_restriction_status if hasattr(self, "product_restriction_status") else None)!r}, '
                f'usage_restriction_status={(self.usage_restriction_status if hasattr(self, "usage_restriction_status") else None)!r}, '
                f'error={(self.error if hasattr(self, "error") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'request_id={(self.request_id if hasattr(self, "request_id") else None)!s}, '
                f'request_action_status={(self.request_action_status if hasattr(self, "request_action_status") else None)!s}, '
                f'day_time_restriction_status={(self.day_time_restriction_status if hasattr(self, "day_time_restriction_status") else None)!s}, '
                f'location_restriction_status={(self.location_restriction_status if hasattr(self, "location_restriction_status") else None)!s}, '
                f'product_restriction_status={(self.product_restriction_status if hasattr(self, "product_restriction_status") else None)!s}, '
                f'usage_restriction_status={(self.usage_restriction_status if hasattr(self, "usage_restriction_status") else None)!s}, '
                f'error={(self.error if hasattr(self, "error") else None)!s})')
