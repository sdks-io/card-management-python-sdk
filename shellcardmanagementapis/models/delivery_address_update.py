# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.update_card_renewal_address_2 import UpdateCardRenewalAddress2


class DeliveryAddressUpdate(object):

    """Implementation of the 'DeliveryAddressUpdate' model.

    List of cards for delivery address update. Maximum number of cards that
    can be provided in the list is 50

    Attributes:
        card_id (int): Card Id of the card. Optional if  PAN is passed, else
            Mandatory.
        pan (str): PAN of the card.  Optional if CardId is passed, else
            Mandatory.     Note: -  PAN & ExpiryDate parameters will be
            considered only if CardId & PANID are not provided.
        card_expiry_date (str): Expiry date of the card. Mandatory if PAN is
            passed, else optional. Format: yyyyMMdd
        use_customer_default_address (bool): Whether to use the default
            delivery address configured at customer (or card group) level as
            the delivery address for this card. Mandatory Note: If value is
            false then ‘UpdateCardRenewalAddress’ is mandatory. If value set
            to ‘True’ then ‘UpdateCardRenewalAddress’ may be null/empty. It
            will be ignored if provided.
        update_card_renewal_address (UpdateCardRenewalAddress2): The model
            property of type UpdateCardRenewalAddress2.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "use_customer_default_address": 'UseCustomerDefaultAddress',
        "card_id": 'CardId',
        "pan": 'PAN',
        "card_expiry_date": 'CardExpiryDate',
        "update_card_renewal_address": 'UpdateCardRenewalAddress'
    }

    _optionals = [
        'card_id',
        'pan',
        'card_expiry_date',
        'update_card_renewal_address',
    ]

    def __init__(self,
                 use_customer_default_address=None,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 card_expiry_date=APIHelper.SKIP,
                 update_card_renewal_address=APIHelper.SKIP):
        """Constructor for the DeliveryAddressUpdate class"""

        # Initialize members of the class
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if card_expiry_date is not APIHelper.SKIP:
            self.card_expiry_date = card_expiry_date 
        self.use_customer_default_address = use_customer_default_address 
        if update_card_renewal_address is not APIHelper.SKIP:
            self.update_card_renewal_address = update_card_renewal_address 

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
        use_customer_default_address = dictionary.get("UseCustomerDefaultAddress") if "UseCustomerDefaultAddress" in dictionary.keys() else None
        card_id = dictionary.get("CardId") if dictionary.get("CardId") else APIHelper.SKIP
        pan = dictionary.get("PAN") if dictionary.get("PAN") else APIHelper.SKIP
        card_expiry_date = dictionary.get("CardExpiryDate") if dictionary.get("CardExpiryDate") else APIHelper.SKIP
        update_card_renewal_address = UpdateCardRenewalAddress2.from_dictionary(dictionary.get('UpdateCardRenewalAddress')) if 'UpdateCardRenewalAddress' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(use_customer_default_address,
                   card_id,
                   pan,
                   card_expiry_date,
                   update_card_renewal_address)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!r}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!r}, '
                f'card_expiry_date={(self.card_expiry_date if hasattr(self, "card_expiry_date") else None)!r}, '
                f'use_customer_default_address={self.use_customer_default_address!r}, '
                f'update_card_renewal_address={(self.update_card_renewal_address if hasattr(self, "update_card_renewal_address") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'card_id={(self.card_id if hasattr(self, "card_id") else None)!s}, '
                f'pan={(self.pan if hasattr(self, "pan") else None)!s}, '
                f'card_expiry_date={(self.card_expiry_date if hasattr(self, "card_expiry_date") else None)!s}, '
                f'use_customer_default_address={self.use_customer_default_address!s}, '
                f'update_card_renewal_address={(self.update_card_renewal_address if hasattr(self, "update_card_renewal_address") else None)!s})')
