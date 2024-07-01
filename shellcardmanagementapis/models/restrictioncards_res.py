# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class RestrictioncardsRes(object):

    """Implementation of the 'RestrictioncardsRes' model.

    TODO: type model description here.

    Attributes:
        account_id (int): Account Id of the customer.  Example: 123456
        account_number (str): Account Number of the customer.  Example:
            GB000000123
        card_id (str): Unique Card Id  Example: 275549
        pan (str): Card PAN.  Example: 7002051006629890645
        usage_restriction_status (str): Status of the card usage restriction
            submitted. Based on the response the value will be set as either
            “Success” or “Failed”.
        usage_restriction_description (str): Response for the usage
            restriction in case of an error. This field will have a value only
            when “UsageRestrictionStatus” is “Failed”.
        day_time_restriction_status (str): Status of the card day/time
            restriction submitted. Based on the response from Gateway value
            will be set as either “Success” or “Failed”.
        day_time_restriction_description (str): Response for the day/time
            restriction in case of an error. This field will have a value only
            when “DayTimeRestrictionStatus” is “Failed”.
        product_restriction_status (str): Status of the card product
            restriction submitted. Based on the response  the value will be
            set  either as “Success” or “Failed”.
        product_restriction_description (str): Response for the product
            restriction in case of an error. This field will have a value only
            when “ProductRestrictionStatus” is “Failed”.
        location_restriction_status (str): Card Location restriction
            submitted, based on response value set as “Success” or “Failed”.
        location_restriction_status_description (str): Response for the
            location restriction in case of an error. This field will have a
            value only when “LocationRestrictionStatus” is “Failed”.
        validation_error_code (str): Error code for validation failure.
        validation_error_description (str): Description of validation
            failure.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "card_id": 'CardId',
        "pan": 'PAN',
        "usage_restriction_status": 'UsageRestrictionStatus',
        "usage_restriction_description": 'UsageRestrictionDescription',
        "day_time_restriction_status": 'DayTimeRestrictionStatus',
        "day_time_restriction_description": 'DayTimeRestrictionDescription',
        "product_restriction_status": 'ProductRestrictionStatus',
        "product_restriction_description": 'ProductRestrictionDescription',
        "location_restriction_status": 'LocationRestrictionStatus',
        "location_restriction_status_description": 'LocationRestrictionStatusDescription',
        "validation_error_code": 'ValidationErrorCode',
        "validation_error_description": 'ValidationErrorDescription'
    }

    _optionals = [
        'account_id',
        'account_number',
        'card_id',
        'pan',
        'usage_restriction_status',
        'usage_restriction_description',
        'day_time_restriction_status',
        'day_time_restriction_description',
        'product_restriction_status',
        'product_restriction_description',
        'location_restriction_status',
        'location_restriction_status_description',
        'validation_error_code',
        'validation_error_description',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 usage_restriction_status=APIHelper.SKIP,
                 usage_restriction_description=APIHelper.SKIP,
                 day_time_restriction_status=APIHelper.SKIP,
                 day_time_restriction_description=APIHelper.SKIP,
                 product_restriction_status=APIHelper.SKIP,
                 product_restriction_description=APIHelper.SKIP,
                 location_restriction_status=APIHelper.SKIP,
                 location_restriction_status_description=APIHelper.SKIP,
                 validation_error_code=APIHelper.SKIP,
                 validation_error_description=APIHelper.SKIP):
        """Constructor for the RestrictioncardsRes class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if usage_restriction_status is not APIHelper.SKIP:
            self.usage_restriction_status = usage_restriction_status 
        if usage_restriction_description is not APIHelper.SKIP:
            self.usage_restriction_description = usage_restriction_description 
        if day_time_restriction_status is not APIHelper.SKIP:
            self.day_time_restriction_status = day_time_restriction_status 
        if day_time_restriction_description is not APIHelper.SKIP:
            self.day_time_restriction_description = day_time_restriction_description 
        if product_restriction_status is not APIHelper.SKIP:
            self.product_restriction_status = product_restriction_status 
        if product_restriction_description is not APIHelper.SKIP:
            self.product_restriction_description = product_restriction_description 
        if location_restriction_status is not APIHelper.SKIP:
            self.location_restriction_status = location_restriction_status 
        if location_restriction_status_description is not APIHelper.SKIP:
            self.location_restriction_status_description = location_restriction_status_description 
        if validation_error_code is not APIHelper.SKIP:
            self.validation_error_code = validation_error_code 
        if validation_error_description is not APIHelper.SKIP:
            self.validation_error_description = validation_error_description 

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
        account_id = dictionary.get("AccountId") if dictionary.get("AccountId") else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if dictionary.get("AccountNumber") else APIHelper.SKIP
        card_id = dictionary.get("CardId") if dictionary.get("CardId") else APIHelper.SKIP
        pan = dictionary.get("PAN") if dictionary.get("PAN") else APIHelper.SKIP
        usage_restriction_status = dictionary.get("UsageRestrictionStatus") if dictionary.get("UsageRestrictionStatus") else APIHelper.SKIP
        usage_restriction_description = dictionary.get("UsageRestrictionDescription") if dictionary.get("UsageRestrictionDescription") else APIHelper.SKIP
        day_time_restriction_status = dictionary.get("DayTimeRestrictionStatus") if dictionary.get("DayTimeRestrictionStatus") else APIHelper.SKIP
        day_time_restriction_description = dictionary.get("DayTimeRestrictionDescription") if dictionary.get("DayTimeRestrictionDescription") else APIHelper.SKIP
        product_restriction_status = dictionary.get("ProductRestrictionStatus") if dictionary.get("ProductRestrictionStatus") else APIHelper.SKIP
        product_restriction_description = dictionary.get("ProductRestrictionDescription") if dictionary.get("ProductRestrictionDescription") else APIHelper.SKIP
        location_restriction_status = dictionary.get("LocationRestrictionStatus") if dictionary.get("LocationRestrictionStatus") else APIHelper.SKIP
        location_restriction_status_description = dictionary.get("LocationRestrictionStatusDescription") if dictionary.get("LocationRestrictionStatusDescription") else APIHelper.SKIP
        validation_error_code = dictionary.get("ValidationErrorCode") if dictionary.get("ValidationErrorCode") else APIHelper.SKIP
        validation_error_description = dictionary.get("ValidationErrorDescription") if dictionary.get("ValidationErrorDescription") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   account_number,
                   card_id,
                   pan,
                   usage_restriction_status,
                   usage_restriction_description,
                   day_time_restriction_status,
                   day_time_restriction_description,
                   product_restriction_status,
                   product_restriction_description,
                   location_restriction_status,
                   location_restriction_status_description,
                   validation_error_code,
                   validation_error_description)