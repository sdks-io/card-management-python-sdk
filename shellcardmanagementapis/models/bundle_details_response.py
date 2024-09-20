# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.bundled_restrictions_list import BundledRestrictionsList
from shellcardmanagementapis.models.error_status import ErrorStatus


class BundleDetailsResponse(object):

    """Implementation of the 'BundleDetailsResponse' model.

    TODO: type model description here.

    Attributes:
        payer_id (int): Payer Id of the bundles and cards. Example: 123456
        payer_number (str): Payer Number of the bundles and cards. Example:
            GB000000123
        account_id (int): Account ID of the bundle. Example: 123456
        account_number (str): Account Number of the bundle. Example:
            GB000000123
        bundle_id (str): unique identifier for the Card Bundle
        external_bundle_id (str): External system allocated Card Bundle
            identifier for Card Bundle.
        description (str): Card Bundle Description.
        pans (List[str]): List of Card Pans added to the card bundle.
        restriction_currency_code (str): ISO currency code of the country.
            Example: GBP
        restriction_currency_symbol (str): Currency symbol of the country.
            Example: £, $
        restrictions (BundledRestrictionsList): TODO: type description here.
        error (ErrorStatus): TODO: type description here.
        request_id (str): API Request Id

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "bundle_id": 'BundleId',
        "external_bundle_id": 'ExternalBundleId',
        "description": 'Description',
        "pans": 'Pans',
        "restriction_currency_code": 'RestrictionCurrencyCode',
        "restriction_currency_symbol": 'RestrictionCurrencySymbol',
        "restrictions": 'Restrictions',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'payer_id',
        'payer_number',
        'account_id',
        'account_number',
        'bundle_id',
        'external_bundle_id',
        'description',
        'pans',
        'restriction_currency_code',
        'restriction_currency_symbol',
        'restrictions',
        'error',
        'request_id',
    ]

    def __init__(self,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 bundle_id=APIHelper.SKIP,
                 external_bundle_id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 pans=APIHelper.SKIP,
                 restriction_currency_code=APIHelper.SKIP,
                 restriction_currency_symbol=APIHelper.SKIP,
                 restrictions=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the BundleDetailsResponse class"""

        # Initialize members of the class
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if bundle_id is not APIHelper.SKIP:
            self.bundle_id = bundle_id 
        if external_bundle_id is not APIHelper.SKIP:
            self.external_bundle_id = external_bundle_id 
        if description is not APIHelper.SKIP:
            self.description = description 
        if pans is not APIHelper.SKIP:
            self.pans = pans 
        if restriction_currency_code is not APIHelper.SKIP:
            self.restriction_currency_code = restriction_currency_code 
        if restriction_currency_symbol is not APIHelper.SKIP:
            self.restriction_currency_symbol = restriction_currency_symbol 
        if restrictions is not APIHelper.SKIP:
            self.restrictions = restrictions 
        if error is not APIHelper.SKIP:
            self.error = error 
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 

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
        payer_id = dictionary.get("PayerId") if dictionary.get("PayerId") else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if dictionary.get("AccountId") else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if dictionary.get("AccountNumber") else APIHelper.SKIP
        bundle_id = dictionary.get("BundleId") if dictionary.get("BundleId") else APIHelper.SKIP
        external_bundle_id = dictionary.get("ExternalBundleId") if dictionary.get("ExternalBundleId") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        pans = dictionary.get("Pans") if dictionary.get("Pans") else APIHelper.SKIP
        restriction_currency_code = dictionary.get("RestrictionCurrencyCode") if dictionary.get("RestrictionCurrencyCode") else APIHelper.SKIP
        restriction_currency_symbol = dictionary.get("RestrictionCurrencySymbol") if dictionary.get("RestrictionCurrencySymbol") else APIHelper.SKIP
        restrictions = BundledRestrictionsList.from_dictionary(dictionary.get('Restrictions')) if 'Restrictions' in dictionary.keys() else APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(payer_id,
                   payer_number,
                   account_id,
                   account_number,
                   bundle_id,
                   external_bundle_id,
                   description,
                   pans,
                   restriction_currency_code,
                   restriction_currency_symbol,
                   restrictions,
                   error,
                   request_id)
