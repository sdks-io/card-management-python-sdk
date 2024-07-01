# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class PartnerSiteRestriction(object):

    """Implementation of the 'PartnerSiteRestriction' model.

    TODO: type model description here.

    Attributes:
        network_code (str): Gateway network codes, typically 7 or 10 digits,
            where sites and site groups belong to.  Example: 0002003250
        sites (List[str]): A list of Site IDs in this network which needs to
            be either restricted or allowed.  For example, 97123, 97155  A
            list of values must be passed for either Sites or SiteGroups or
            both.  Max 10 sites are allowed for the Partner site Restriction.
        site_groups (List[str]): A list of site group ids in this network
            which needs to be either restricted or allowed.  For example,
            83649200  A list of values must be passed for either Sites or
            SiteGroups or both.  Max 10 sites groups are allowed for the
            Partner site Restriction.
        exclusive (bool): Flag indicates whether the profile is inclusive or
            exclusive.  Mandatory  Example: False - (inclusive), i.e. the
            “Sites” & “SiteGroups” properties lists the sites & site groups
            where the transaction will be allowed.  True - (exclusive), i.e.
            the “Sites” & “SiteGroups” properties lists the sites and site
            groups where the transactions will be declined.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "network_code": 'NetworkCode',
        "sites": 'Sites',
        "site_groups": 'SiteGroups',
        "exclusive": 'Exclusive'
    }

    _optionals = [
        'network_code',
        'sites',
        'site_groups',
        'exclusive',
    ]

    def __init__(self,
                 network_code=APIHelper.SKIP,
                 sites=APIHelper.SKIP,
                 site_groups=APIHelper.SKIP,
                 exclusive=APIHelper.SKIP):
        """Constructor for the PartnerSiteRestriction class"""

        # Initialize members of the class
        if network_code is not APIHelper.SKIP:
            self.network_code = network_code 
        if sites is not APIHelper.SKIP:
            self.sites = sites 
        if site_groups is not APIHelper.SKIP:
            self.site_groups = site_groups 
        if exclusive is not APIHelper.SKIP:
            self.exclusive = exclusive 

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
        network_code = dictionary.get("NetworkCode") if dictionary.get("NetworkCode") else APIHelper.SKIP
        sites = dictionary.get("Sites") if dictionary.get("Sites") else APIHelper.SKIP
        site_groups = dictionary.get("SiteGroups") if dictionary.get("SiteGroups") else APIHelper.SKIP
        exclusive = dictionary.get("Exclusive") if "Exclusive" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(network_code,
                   sites,
                   site_groups,
                   exclusive)