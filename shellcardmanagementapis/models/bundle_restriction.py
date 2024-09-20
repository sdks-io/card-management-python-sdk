# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.day_time_restrictions import DayTimeRestrictions
from shellcardmanagementapis.models.location_restriction import LocationRestriction


class BundleRestriction(object):

    """Implementation of the 'BundleRestriction' model.

    TODO: type model description here.

    Attributes:
        day_time_restriction_action (str): The value indicates what actions to
            be performed with respect to day time restriction.   Mandatory 
            Allowed values –  •    Add: Apply the given restriction on the
            bundle.  •    Default: No Day/Time restriction will be applied on
            the bundle in Gateway.
        location_restriction_action (str): The value indicates what actions to
            be performed with respect to location restriction.   Mandatory 
            Allowed values –  •    Add: Apply the given restriction on the
            bundle.  •    Default: No location restriction will be applied on
            the bundle in Gateway.
        usage_restrictions (object): TODO: type description here.
        day_time_restrictions (DayTimeRestrictions): TODO: type description
            here.
        product_restrictions (object): TODO: type description here.
        location_restrictions (LocationRestriction): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day_time_restriction_action": 'DayTimeRestrictionAction',
        "location_restriction_action": 'LocationRestrictionAction',
        "usage_restrictions": 'UsageRestrictions',
        "day_time_restrictions": 'DayTimeRestrictions',
        "product_restrictions": 'ProductRestrictions',
        "location_restrictions": 'LocationRestrictions'
    }

    _optionals = [
        'day_time_restriction_action',
        'location_restriction_action',
        'usage_restrictions',
        'day_time_restrictions',
        'product_restrictions',
        'location_restrictions',
    ]

    _nullables = [
        'day_time_restriction_action',
        'location_restriction_action',
    ]

    def __init__(self,
                 day_time_restriction_action=APIHelper.SKIP,
                 location_restriction_action=APIHelper.SKIP,
                 usage_restrictions=APIHelper.SKIP,
                 day_time_restrictions=APIHelper.SKIP,
                 product_restrictions=APIHelper.SKIP,
                 location_restrictions=APIHelper.SKIP):
        """Constructor for the BundleRestriction class"""

        # Initialize members of the class
        if day_time_restriction_action is not APIHelper.SKIP:
            self.day_time_restriction_action = day_time_restriction_action 
        if location_restriction_action is not APIHelper.SKIP:
            self.location_restriction_action = location_restriction_action 
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        day_time_restriction_action = dictionary.get("DayTimeRestrictionAction") if "DayTimeRestrictionAction" in dictionary.keys() else APIHelper.SKIP
        location_restriction_action = dictionary.get("LocationRestrictionAction") if "LocationRestrictionAction" in dictionary.keys() else APIHelper.SKIP
        usage_restrictions = dictionary.get("UsageRestrictions") if dictionary.get("UsageRestrictions") else APIHelper.SKIP
        day_time_restrictions = DayTimeRestrictions.from_dictionary(dictionary.get('DayTimeRestrictions')) if 'DayTimeRestrictions' in dictionary.keys() else APIHelper.SKIP
        product_restrictions = dictionary.get("ProductRestrictions") if dictionary.get("ProductRestrictions") else APIHelper.SKIP
        location_restrictions = LocationRestriction.from_dictionary(dictionary.get('LocationRestrictions')) if 'LocationRestrictions' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(day_time_restriction_action,
                   location_restriction_action,
                   usage_restrictions,
                   day_time_restrictions,
                   product_restrictions,
                   location_restrictions)
