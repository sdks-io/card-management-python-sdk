# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class PINAdviceTypes(object):

    """Implementation of the 'PINAdviceTypes' model.

    TODO: type model description here.

    Attributes:
        pin_advice_type_id (int): Id of of PIN advice type.  Possible Values: 
            1. Paper  2. Email  3. SMS  4. None
        is_card_order_option (bool): Whether the PIN advice type is available
            for card ordering
        is_pin_reminder_option (bool): Whether the PIN advice type is
            available for PIN Reminder

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pin_advice_type_id": 'PINAdviceTypeID',
        "is_card_order_option": 'IsCardOrderOption',
        "is_pin_reminder_option": 'IsPINReminderOption'
    }

    _optionals = [
        'pin_advice_type_id',
        'is_card_order_option',
        'is_pin_reminder_option',
    ]

    _nullables = [
        'pin_advice_type_id',
    ]

    def __init__(self,
                 pin_advice_type_id=APIHelper.SKIP,
                 is_card_order_option=APIHelper.SKIP,
                 is_pin_reminder_option=APIHelper.SKIP):
        """Constructor for the PINAdviceTypes class"""

        # Initialize members of the class
        if pin_advice_type_id is not APIHelper.SKIP:
            self.pin_advice_type_id = pin_advice_type_id 
        if is_card_order_option is not APIHelper.SKIP:
            self.is_card_order_option = is_card_order_option 
        if is_pin_reminder_option is not APIHelper.SKIP:
            self.is_pin_reminder_option = is_pin_reminder_option 

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
        pin_advice_type_id = dictionary.get("PINAdviceTypeID") if "PINAdviceTypeID" in dictionary.keys() else APIHelper.SKIP
        is_card_order_option = dictionary.get("IsCardOrderOption") if "IsCardOrderOption" in dictionary.keys() else APIHelper.SKIP
        is_pin_reminder_option = dictionary.get("IsPINReminderOption") if "IsPINReminderOption" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(pin_advice_type_id,
                   is_card_order_option,
                   is_pin_reminder_option)
