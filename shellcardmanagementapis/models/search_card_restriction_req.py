# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.accounts import Accounts
from shellcardmanagementapis.models.search_card_restriction import SearchCardRestriction


class SearchCardRestrictionReq(object):

    """Implementation of the 'SearchCardRestrictionReq' model.

    TODO: type model description here.

    Attributes:
        col_co_id (int): Collecting Company Id of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86 for Philippines  5
            for UK
        payer_id (int): Payer Id (i.e. Customer Id of the Payment Customer) of
            the selected payer.  Optional if PayerNumber is passed else
            Mandatory  Example: 123456
        payer_number (str): Payer Number of the selected payer.  Optional if
            PayerId is passed else Mandatory  Example: GB000000123
        accounts (Accounts): TODO: type description here.
        bundle_id (str): Identifier of the Card bundle  Optional if cards list
            is given, else mandatory.  This input is a search criterion, if
            given.
        cards (SearchCardRestriction): TODO: type description here.
        include_location_restrictions (bool): True/False  Whether to include
            location restriction of the cards in the response.  Optional 
            Default ‘false’
        include_bundle_details (bool): Default value is False,  When the value
            is True, API will return bundle Id associated with cards in the
            response, if available.   Note: Use ‘Null’ or ‘False’ for optimum
            performance. A delay in response is expected when set to ‘True’.
        include_inherited_limits (bool): Default value is True,  When True:
            service will return the inherited values for the usage limits
            (from card-program or account as available) when it is not
            overridden on the card.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "accounts": 'Accounts',
        "bundle_id": 'BundleId',
        "cards": 'Cards',
        "include_location_restrictions": 'IncludeLocationRestrictions',
        "include_bundle_details": 'IncludeBundleDetails',
        "include_inherited_limits": 'IncludeInheritedLimits'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'accounts',
        'bundle_id',
        'cards',
        'include_location_restrictions',
        'include_bundle_details',
        'include_inherited_limits',
    ]

    _nullables = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'bundle_id',
        'include_location_restrictions',
        'include_bundle_details',
        'include_inherited_limits',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 accounts=APIHelper.SKIP,
                 bundle_id=APIHelper.SKIP,
                 cards=APIHelper.SKIP,
                 include_location_restrictions=APIHelper.SKIP,
                 include_bundle_details=APIHelper.SKIP,
                 include_inherited_limits=APIHelper.SKIP):
        """Constructor for the SearchCardRestrictionReq class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 
        if bundle_id is not APIHelper.SKIP:
            self.bundle_id = bundle_id 
        if cards is not APIHelper.SKIP:
            self.cards = cards 
        if include_location_restrictions is not APIHelper.SKIP:
            self.include_location_restrictions = include_location_restrictions 
        if include_bundle_details is not APIHelper.SKIP:
            self.include_bundle_details = include_bundle_details 
        if include_inherited_limits is not APIHelper.SKIP:
            self.include_inherited_limits = include_inherited_limits 

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
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else APIHelper.SKIP
        accounts = Accounts.from_dictionary(dictionary.get('Accounts')) if 'Accounts' in dictionary.keys() else APIHelper.SKIP
        bundle_id = dictionary.get("BundleId") if "BundleId" in dictionary.keys() else APIHelper.SKIP
        cards = SearchCardRestriction.from_dictionary(dictionary.get('Cards')) if 'Cards' in dictionary.keys() else APIHelper.SKIP
        include_location_restrictions = dictionary.get("IncludeLocationRestrictions") if "IncludeLocationRestrictions" in dictionary.keys() else APIHelper.SKIP
        include_bundle_details = dictionary.get("IncludeBundleDetails") if "IncludeBundleDetails" in dictionary.keys() else APIHelper.SKIP
        include_inherited_limits = dictionary.get("IncludeInheritedLimits") if "IncludeInheritedLimits" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   accounts,
                   bundle_id,
                   cards,
                   include_location_restrictions,
                   include_bundle_details,
                   include_inherited_limits)