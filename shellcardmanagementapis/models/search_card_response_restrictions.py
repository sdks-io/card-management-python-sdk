# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.day_time_restrictions import DayTimeRestrictions
from shellcardmanagementapis.models.location_restrictions import LocationRestrictions
from shellcardmanagementapis.models.search_product_restriction import SearchProductRestriction
from shellcardmanagementapis.models.usage_restrictions import UsageRestrictions


class SearchCardResponseRestrictions(object):

    """Implementation of the 'SearchCardResponseRestrictions' model.

    TODO: type model description here.

    Attributes:
        day_time_restrictions (DayTimeRestrictions): Day/time restrictions
            such as weekdays and time range to be applied on the bundle. 
            Mandatory if respective action is set as “Add”.  The details of
            DayTimeRestriction entity is given below.
        location_restrictions (LocationRestrictions): Location restrictions to
            be applied on the bundle which either allows or restricts using
            the cards, which are under the bundle, in the specified locations.
            Mandatory if respective action is set as “Add”.  Details of
            location restrictions are given below.
        product_restrictions (SearchProductRestriction): TODO: type
            description here.
        usage_restrictions (UsageRestrictions): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "day_time_restrictions": 'DayTimeRestrictions',
        "location_restrictions": 'LocationRestrictions',
        "product_restrictions": 'ProductRestrictions',
        "usage_restrictions": 'UsageRestrictions'
    }

    _optionals = [
        'day_time_restrictions',
        'location_restrictions',
        'product_restrictions',
        'usage_restrictions',
    ]

    def __init__(self,
                 day_time_restrictions=APIHelper.SKIP,
                 location_restrictions=APIHelper.SKIP,
                 product_restrictions=APIHelper.SKIP,
                 usage_restrictions=APIHelper.SKIP):
        """Constructor for the SearchCardResponseRestrictions class"""

        # Initialize members of the class
        if day_time_restrictions is not APIHelper.SKIP:
            self.day_time_restrictions = day_time_restrictions 
        if location_restrictions is not APIHelper.SKIP:
            self.location_restrictions = location_restrictions 
        if product_restrictions is not APIHelper.SKIP:
            self.product_restrictions = product_restrictions 
        if usage_restrictions is not APIHelper.SKIP:
            self.usage_restrictions = usage_restrictions 

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
        day_time_restrictions = DayTimeRestrictions.from_dictionary(dictionary.get('DayTimeRestrictions')) if 'DayTimeRestrictions' in dictionary.keys() else APIHelper.SKIP
        location_restrictions = LocationRestrictions.from_dictionary(dictionary.get('LocationRestrictions')) if 'LocationRestrictions' in dictionary.keys() else APIHelper.SKIP
        product_restrictions = SearchProductRestriction.from_dictionary(dictionary.get('ProductRestrictions')) if 'ProductRestrictions' in dictionary.keys() else APIHelper.SKIP
        usage_restrictions = UsageRestrictions.from_dictionary(dictionary.get('UsageRestrictions')) if 'UsageRestrictions' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(day_time_restrictions,
                   location_restrictions,
                   product_restrictions,
                   usage_restrictions)