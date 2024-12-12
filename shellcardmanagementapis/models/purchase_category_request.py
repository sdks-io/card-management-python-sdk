# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class PurchaseCategoryRequest(object):

    """Implementation of the 'PurchaseCategoryRequest' model.

    TODO: type model description here.

    Attributes:
        request_id (str): Mandatory UUID (according to RFC 4122 standards) for
            requests and responses. This will be played back in the response
            from the request.
        col_co_code (int): Collecting Company Code (Shell Code).
        col_co_id (int): Collecting Company Id (in Shell Cards Platform).
        card_type_id (int): Card type Id
        purchase_category_id (int): Purchase category Id Optional. Example:
            123, 124, etc.,
        language_code (str): Language code for the Title and Description. 
            Language codes should be same as SFH supported language  
            Optional.  Default: en-GB  Example:  en-GB – English (UK)  nl-NL –
            Dutch (Netherlands)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "request_id": 'RequestId',
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "card_type_id": 'CardTypeId',
        "purchase_category_id": 'PurchaseCategoryId',
        "language_code": 'LanguageCode'
    }

    _optionals = [
        'request_id',
        'col_co_code',
        'col_co_id',
        'card_type_id',
        'purchase_category_id',
        'language_code',
    ]

    _nullables = [
        'col_co_code',
        'col_co_id',
        'card_type_id',
    ]

    def __init__(self,
                 request_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 card_type_id=APIHelper.SKIP,
                 purchase_category_id=APIHelper.SKIP,
                 language_code=APIHelper.SKIP):
        """Constructor for the PurchaseCategoryRequest class"""

        # Initialize members of the class
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if card_type_id is not APIHelper.SKIP:
            self.card_type_id = card_type_id 
        if purchase_category_id is not APIHelper.SKIP:
            self.purchase_category_id = purchase_category_id 
        if language_code is not APIHelper.SKIP:
            self.language_code = language_code 

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
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        card_type_id = dictionary.get("CardTypeId") if "CardTypeId" in dictionary.keys() else APIHelper.SKIP
        purchase_category_id = dictionary.get("PurchaseCategoryId") if dictionary.get("PurchaseCategoryId") else APIHelper.SKIP
        language_code = dictionary.get("LanguageCode") if dictionary.get("LanguageCode") else APIHelper.SKIP
        # Return an object of this model
        return cls(request_id,
                   col_co_code,
                   col_co_id,
                   card_type_id,
                   purchase_category_id,
                   language_code)
