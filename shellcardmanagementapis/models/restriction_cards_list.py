# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.day_time_restrictions import DayTimeRestrictions
from shellcardmanagementapis.models.location_restriction import LocationRestriction


class RestrictionCardsList(object):

    """Implementation of the 'RestrictionCardsList' model.

    Attributes:
        account_id (int): Account ID of the customer.  Optional if
            AccountNumber is passed, else Mandatory.   This input is a search
            criterion, if given.  Example: 123456
        card_id (int): Unique Card Id
        pan (str): Card PAN.  Optional if CardId is given, else mandatory.  
            Example: 7002051006629890645   Note:   •    PAN is ignored if
            CardId is given.  When PAN matches with multiple cards, the
            restriction will be applied on the latest issued card.
        reset_usage_restrictions (bool): True/False.  If true, the usage
            restrictions applied on the card in Gateway will be reset to
            Customer Card Type level max limits, if there are no customer
            level overrides available then OU card type max limits. Else, the
            card restrictions will be updated with the usage restrictions
            provided in the API.   This property is not dependent on
            IsVelocityCeiling or SetDefaultOnVelocityUpdate flags.
        reset_day_time_restrictions (bool): True/False. If true, the Day/Time
            restrictions applied on the card will be deleted. Else, the card
            restrictions will be updated with the day/time restrictions
            provided in the API.
        reset_product_restrictions (bool): True/False. If true, Default
            fuel/non-fuel sets configured at the purchase category level will
            be applied to the card. Else, the card will be applied with
            product restrictions provided in the API.
        reset_location_restrictions (bool): True/False. If true, the location
            restrictions applied on the card will be deleted. Else, the card
            restrictions will be updated with the location restrictions
            provided in the API.
        usage_restrictions (object): The model property of type object.
        day_time_restrictions (DayTimeRestrictions): The model property of
            type DayTimeRestrictions.
        product_restrictions (object): The model property of type object.
        location_restrictions (LocationRestriction): The model property of
            type LocationRestriction.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'AccountId',
        "card_id": 'CardId',
        "pan": 'PAN',
        "reset_usage_restrictions": 'ResetUsageRestrictions',
        "reset_day_time_restrictions": 'ResetDayTimeRestrictions',
        "reset_product_restrictions": 'ResetProductRestrictions',
        "reset_location_restrictions": 'ResetLocationRestrictions',
        "usage_restrictions": 'UsageRestrictions',
        "day_time_restrictions": 'DayTimeRestrictions',
        "product_restrictions": 'ProductRestrictions',
        "location_restrictions": 'LocationRestrictions'
    }

    _optionals = [
        'account_id',
        'card_id',
        'pan',
        'reset_usage_restrictions',
        'reset_day_time_restrictions',
        'reset_product_restrictions',
        'reset_location_restrictions',
        'usage_restrictions',
        'day_time_restrictions',
        'product_restrictions',
        'location_restrictions',
    ]

    _nullables = [
        'account_id',
        'card_id',
        'pan',
        'reset_day_time_restrictions',
        'reset_product_restrictions',
        'reset_location_restrictions',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 reset_usage_restrictions=APIHelper.SKIP,
                 reset_day_time_restrictions=APIHelper.SKIP,
                 reset_product_restrictions=APIHelper.SKIP,
                 reset_location_restrictions=APIHelper.SKIP,
                 usage_restrictions=APIHelper.SKIP,
                 day_time_restrictions=APIHelper.SKIP,
                 product_restrictions=APIHelper.SKIP,
                 location_restrictions=APIHelper.SKIP):
        """Constructor for the RestrictionCardsList class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if reset_usage_restrictions is not APIHelper.SKIP:
            self.reset_usage_restrictions = reset_usage_restrictions 
        if reset_day_time_restrictions is not APIHelper.SKIP:
            self.reset_day_time_restrictions = reset_day_time_restrictions 
        if reset_product_restrictions is not APIHelper.SKIP:
            self.reset_product_restrictions = reset_product_restrictions 
        if reset_location_restrictions is not APIHelper.SKIP:
            self.reset_location_restrictions = reset_location_restrictions 
        if usage_restrictions is not APIHelper.SKIP:
            self.usage_restrictions = usage_restrictions 
        if day_time_restrictions is not APIHelper.SKIP:
            self.day_time_restrictions = day_time_restrictions 
        if product_restrictions is not APIHelper.SKIP:
            self.product_restrictions = product_restrictions 
        if location_restrictions is not APIHelper.SKIP:
            self.location_restrictions = location_restrictions 

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
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        reset_usage_restrictions = dictionary.get("ResetUsageRestrictions") if "ResetUsageRestrictions" in dictionary.keys() else APIHelper.SKIP
        reset_day_time_restrictions = dictionary.get("ResetDayTimeRestrictions") if "ResetDayTimeRestrictions" in dictionary.keys() else APIHelper.SKIP
        reset_product_restrictions = dictionary.get("ResetProductRestrictions") if "ResetProductRestrictions" in dictionary.keys() else APIHelper.SKIP
        reset_location_restrictions = dictionary.get("ResetLocationRestrictions") if "ResetLocationRestrictions" in dictionary.keys() else APIHelper.SKIP
        usage_restrictions = dictionary.get("UsageRestrictions") if dictionary.get("UsageRestrictions") else APIHelper.SKIP
        day_time_restrictions = DayTimeRestrictions.from_dictionary(dictionary.get('DayTimeRestrictions')) if 'DayTimeRestrictions' in dictionary.keys() else APIHelper.SKIP
        product_restrictions = dictionary.get("ProductRestrictions") if dictionary.get("ProductRestrictions") else APIHelper.SKIP
        location_restrictions = LocationRestriction.from_dictionary(dictionary.get('LocationRestrictions')) if 'LocationRestrictions' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   card_id,
                   pan,
                   reset_usage_restrictions,
                   reset_day_time_restrictions,
                   reset_product_restrictions,
                   reset_location_restrictions,
                   usage_restrictions,
                   day_time_restrictions,
                   product_restrictions,
                   location_restrictions)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!r}, '
                f'reset_usage_restrictions={(self.reset_usage_restrictions if hasattr(self, "reset_usage_restrictions") else None)!r}, '
                f'reset_day_time_restrictions={(self.reset_day_time_restrictions if hasattr(self, "reset_day_time_restrictions") else None)!r}, '
                f'reset_product_restrictions={(self.reset_product_restrictions if hasattr(self, "reset_product_restrictions") else None)!r}, '
                f'reset_location_restrictions={(self.reset_location_restrictions if hasattr(self, "reset_location_restrictions") else None)!r}, '
                f'usage_restrictions={(self.usage_restrictions if hasattr(self, "usage_restrictions") else None)!r}, '
                f'day_time_restrictions={(self.day_time_restrictions if hasattr(self, "day_time_restrictions") else None)!r}, '
                f'product_restrictions={(self.product_restrictions if hasattr(self, "product_restrictions") else None)!r}, '
                f'location_restrictions={(self.location_restrictions if hasattr(self, "location_restrictions") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!s}, '
                f'reset_usage_restrictions={(self.reset_usage_restrictions if hasattr(self, "reset_usage_restrictions") else None)!s}, '
                f'reset_day_time_restrictions={(self.reset_day_time_restrictions if hasattr(self, "reset_day_time_restrictions") else None)!s}, '
                f'reset_product_restrictions={(self.reset_product_restrictions if hasattr(self, "reset_product_restrictions") else None)!s}, '
                f'reset_location_restrictions={(self.reset_location_restrictions if hasattr(self, "reset_location_restrictions") else None)!s}, '
                f'usage_restrictions={(self.usage_restrictions if hasattr(self, "usage_restrictions") else None)!s}, '
                f'day_time_restrictions={(self.day_time_restrictions if hasattr(self, "day_time_restrictions") else None)!s}, '
                f'product_restrictions={(self.product_restrictions if hasattr(self, "product_restrictions") else None)!s}, '
                f'location_restrictions={(self.location_restrictions if hasattr(self, "location_restrictions") else None)!s})')
