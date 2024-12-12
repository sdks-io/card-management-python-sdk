# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.error_status import ErrorStatus
from shellcardmanagementapis.models.purchase_category_1_all_of_0 import PurchaseCategory1AllOf0


class PurchaseCategoryResponse(object):

    """Implementation of the 'PurchaseCategoryResponse' model.

    TODO: type model description here.

    Attributes:
        purchase_categories (List[PurchaseCategory1AllOf0]): TODO: type
            description here.
        error (ErrorStatus): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "purchase_categories": 'PurchaseCategories',
        "error": 'Error'
    }

    _optionals = [
        'purchase_categories',
        'error',
    ]

    def __init__(self,
                 purchase_categories=APIHelper.SKIP,
                 error=APIHelper.SKIP):
        """Constructor for the PurchaseCategoryResponse class"""

        # Initialize members of the class
        if purchase_categories is not APIHelper.SKIP:
            self.purchase_categories = purchase_categories 
        if error is not APIHelper.SKIP:
            self.error = error 

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
        purchase_categories = None
        if dictionary.get('PurchaseCategories') is not None:
            purchase_categories = [PurchaseCategory1AllOf0.from_dictionary(x) for x in dictionary.get('PurchaseCategories')]
        else:
            purchase_categories = APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(purchase_categories,
                   error)
