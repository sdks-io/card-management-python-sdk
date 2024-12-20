# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.card_day_time_restrictions import CardDayTimeRestrictions
from shellcardmanagementapis.models.location_restriction import LocationRestriction


class BundleRestrictionUpdate(object):

    """Implementation of the 'BundleRestrictionUpdate' model.

    TODO: type model description here.

    Attributes:
        reset_day_time_restriction (bool): True/False A value indicates if the
            day/time restriction is to be reset for card bundle. Optional
            Default value is False.
        reset_location_restriction (bool): True/False A value indicates if the
            location restriction is to be reset for card bundle. Optional
            Default value is False.
        reset_product_restriction (bool): True/False A value indicates if the
            product restriction is to be reset for card bundle. Optional
            Default value is False.
        usage_restrictions (object): TODO: type description here.
        day_time_restriction_profile_id (str): Identifier of the day/time
            restriction profile to be updated for the bundle in Gateway.
            Optional
        day_time_restrictions (CardDayTimeRestrictions): TODO: type
            description here.
        product_restrictions (object): TODO: type description here.
        location_restriction_profile_id (str): Identifier of the location
            restriction profile to be updated for the bundle in Gateway.
            Optional
        location_restrictions (LocationRestriction): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reset_day_time_restriction": 'ResetDayTimeRestriction',
        "reset_location_restriction": 'ResetLocationRestriction',
        "reset_product_restriction": 'ResetProductRestriction',
        "usage_restrictions": 'UsageRestrictions',
        "day_time_restriction_profile_id": 'DayTimeRestrictionProfileId',
        "day_time_restrictions": 'DayTimeRestrictions',
        "product_restrictions": 'ProductRestrictions',
        "location_restriction_profile_id": 'LocationRestrictionProfileId',
        "location_restrictions": 'LocationRestrictions'
    }

    _optionals = [
        'reset_day_time_restriction',
        'reset_location_restriction',
        'reset_product_restriction',
        'usage_restrictions',
        'day_time_restriction_profile_id',
        'day_time_restrictions',
        'product_restrictions',
        'location_restriction_profile_id',
        'location_restrictions',
    ]

    _nullables = [
        'reset_day_time_restriction',
        'reset_location_restriction',
        'reset_product_restriction',
        'day_time_restriction_profile_id',
    ]

    def __init__(self,
                 reset_day_time_restriction=APIHelper.SKIP,
                 reset_location_restriction=APIHelper.SKIP,
                 reset_product_restriction=APIHelper.SKIP,
                 usage_restrictions=APIHelper.SKIP,
                 day_time_restriction_profile_id=APIHelper.SKIP,
                 day_time_restrictions=APIHelper.SKIP,
                 product_restrictions=APIHelper.SKIP,
                 location_restriction_profile_id=APIHelper.SKIP,
                 location_restrictions=APIHelper.SKIP):
        """Constructor for the BundleRestrictionUpdate class"""

        # Initialize members of the class
        if reset_day_time_restriction is not APIHelper.SKIP:
            self.reset_day_time_restriction = reset_day_time_restriction 
        if reset_location_restriction is not APIHelper.SKIP:
            self.reset_location_restriction = reset_location_restriction 
        if reset_product_restriction is not APIHelper.SKIP:
            self.reset_product_restriction = reset_product_restriction 
        if usage_restrictions is not APIHelper.SKIP:
            self.usage_restrictions = usage_restrictions 
        if day_time_restriction_profile_id is not APIHelper.SKIP:
            self.day_time_restriction_profile_id = day_time_restriction_profile_id 
        if day_time_restrictions is not APIHelper.SKIP:
            self.day_time_restrictions = day_time_restrictions 
        if product_restrictions is not APIHelper.SKIP:
            self.product_restrictions = product_restrictions 
        if location_restriction_profile_id is not APIHelper.SKIP:
            self.location_restriction_profile_id = location_restriction_profile_id 
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
        reset_day_time_restriction = dictionary.get("ResetDayTimeRestriction") if "ResetDayTimeRestriction" in dictionary.keys() else APIHelper.SKIP
        reset_location_restriction = dictionary.get("ResetLocationRestriction") if "ResetLocationRestriction" in dictionary.keys() else APIHelper.SKIP
        reset_product_restriction = dictionary.get("ResetProductRestriction") if "ResetProductRestriction" in dictionary.keys() else APIHelper.SKIP
        usage_restrictions = dictionary.get("UsageRestrictions") if dictionary.get("UsageRestrictions") else APIHelper.SKIP
        day_time_restriction_profile_id = dictionary.get("DayTimeRestrictionProfileId") if "DayTimeRestrictionProfileId" in dictionary.keys() else APIHelper.SKIP
        day_time_restrictions = CardDayTimeRestrictions.from_dictionary(dictionary.get('DayTimeRestrictions')) if 'DayTimeRestrictions' in dictionary.keys() else APIHelper.SKIP
        product_restrictions = dictionary.get("ProductRestrictions") if dictionary.get("ProductRestrictions") else APIHelper.SKIP
        location_restriction_profile_id = dictionary.get("LocationRestrictionProfileId") if dictionary.get("LocationRestrictionProfileId") else APIHelper.SKIP
        location_restrictions = LocationRestriction.from_dictionary(dictionary.get('LocationRestrictions')) if 'LocationRestrictions' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(reset_day_time_restriction,
                   reset_location_restriction,
                   reset_product_restriction,
                   usage_restrictions,
                   day_time_restriction_profile_id,
                   day_time_restrictions,
                   product_restrictions,
                   location_restriction_profile_id,
                   location_restrictions)
