# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class SummaryOfBundleResponseDataItemsCardBundlesItems(object):

    """Implementation of the 'SummaryOfBundleResponseDataItemsCardBundlesItems' model.

    TODO: type model description here.

    Attributes:
        bundle_id (str): Gateway assigned unique identifier for the Card
            Bundle.
        external_bundle_id (str): External system allocated Card Bundle
            identifier for Card Bundle.
        description (str): Card Bundle Description.
        total_cards (int): No of Card PAN added to the card bundle.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bundle_id": 'BundleId',
        "external_bundle_id": 'ExternalBundleId',
        "description": 'Description',
        "total_cards": 'TotalCards'
    }

    _optionals = [
        'bundle_id',
        'external_bundle_id',
        'description',
        'total_cards',
    ]

    _nullables = [
        'bundle_id',
        'external_bundle_id',
        'description',
        'total_cards',
    ]

    def __init__(self,
                 bundle_id=APIHelper.SKIP,
                 external_bundle_id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 total_cards=APIHelper.SKIP):
        """Constructor for the SummaryOfBundleResponseDataItemsCardBundlesItems class"""

        # Initialize members of the class
        if bundle_id is not APIHelper.SKIP:
            self.bundle_id = bundle_id 
        if external_bundle_id is not APIHelper.SKIP:
            self.external_bundle_id = external_bundle_id 
        if description is not APIHelper.SKIP:
            self.description = description 
        if total_cards is not APIHelper.SKIP:
            self.total_cards = total_cards 

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
        bundle_id = dictionary.get("BundleId") if "BundleId" in dictionary.keys() else APIHelper.SKIP
        external_bundle_id = dictionary.get("ExternalBundleId") if "ExternalBundleId" in dictionary.keys() else APIHelper.SKIP
        description = dictionary.get("Description") if "Description" in dictionary.keys() else APIHelper.SKIP
        total_cards = dictionary.get("TotalCards") if "TotalCards" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(bundle_id,
                   external_bundle_id,
                   description,
                   total_cards)