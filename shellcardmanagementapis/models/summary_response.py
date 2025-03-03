# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class SummaryResponse(object):

    """Implementation of the 'SummaryResponse' model.

    Encapsulates the details of a Summary response.

    Attributes:
        active_cards (int): Total number of active cards for the given search
            criteria
        blocked_cards (int): Total number of cards for the given search
            criteria that are permanently blocked (Blocked)
        cancelled_cards (int): Total number of cards for the given search
            criteria that are cancelled (at cancelled status) blocked by
            customer
        expired_cards (int): Total number of expired cards for the given
            search criteria
        expiring_cards (int): Cards that are active and expiring in X days, X
            should be configurable
        fraud_cards (int): Totalnumber of Cards in Fraud status for the given
            search criteria.
        new_cards (int): Total number of cards in New status for the given
            search criteria.
        renewal_pending_cards (int): Total number of Renewal Pending cards for
            the given search criteria
        replaced_cards (int): Cards with status Replaced
        temporary_block_by_customer (int): Total number of cards for the given
            search criteria that are temporarily blocked by customer
        temporary_block_by_shell (int): Total number of cards for the given
            search criteria that are temporarily blocked by Shell
        total_cards (int): Total number of cards for the given search criteria

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "active_cards": 'ActiveCards',
        "blocked_cards": 'BlockedCards',
        "cancelled_cards": 'CancelledCards',
        "expired_cards": 'ExpiredCards',
        "expiring_cards": 'ExpiringCards',
        "fraud_cards": 'FraudCards',
        "new_cards": 'NewCards',
        "renewal_pending_cards": 'RenewalPendingCards',
        "replaced_cards": 'ReplacedCards',
        "temporary_block_by_customer": 'TemporaryBlockByCustomer',
        "temporary_block_by_shell": 'TemporaryBlockByShell',
        "total_cards": 'TotalCards'
    }

    _optionals = [
        'active_cards',
        'blocked_cards',
        'cancelled_cards',
        'expired_cards',
        'expiring_cards',
        'fraud_cards',
        'new_cards',
        'renewal_pending_cards',
        'replaced_cards',
        'temporary_block_by_customer',
        'temporary_block_by_shell',
        'total_cards',
    ]

    _nullables = [
        'active_cards',
        'blocked_cards',
        'cancelled_cards',
        'expired_cards',
        'expiring_cards',
        'fraud_cards',
        'new_cards',
        'renewal_pending_cards',
        'replaced_cards',
        'temporary_block_by_customer',
        'temporary_block_by_shell',
        'total_cards',
    ]

    def __init__(self,
                 active_cards=APIHelper.SKIP,
                 blocked_cards=APIHelper.SKIP,
                 cancelled_cards=APIHelper.SKIP,
                 expired_cards=APIHelper.SKIP,
                 expiring_cards=APIHelper.SKIP,
                 fraud_cards=APIHelper.SKIP,
                 new_cards=APIHelper.SKIP,
                 renewal_pending_cards=APIHelper.SKIP,
                 replaced_cards=APIHelper.SKIP,
                 temporary_block_by_customer=APIHelper.SKIP,
                 temporary_block_by_shell=APIHelper.SKIP,
                 total_cards=APIHelper.SKIP):
        """Constructor for the SummaryResponse class"""

        # Initialize members of the class
        if active_cards is not APIHelper.SKIP:
            self.active_cards = active_cards 
        if blocked_cards is not APIHelper.SKIP:
            self.blocked_cards = blocked_cards 
        if cancelled_cards is not APIHelper.SKIP:
            self.cancelled_cards = cancelled_cards 
        if expired_cards is not APIHelper.SKIP:
            self.expired_cards = expired_cards 
        if expiring_cards is not APIHelper.SKIP:
            self.expiring_cards = expiring_cards 
        if fraud_cards is not APIHelper.SKIP:
            self.fraud_cards = fraud_cards 
        if new_cards is not APIHelper.SKIP:
            self.new_cards = new_cards 
        if renewal_pending_cards is not APIHelper.SKIP:
            self.renewal_pending_cards = renewal_pending_cards 
        if replaced_cards is not APIHelper.SKIP:
            self.replaced_cards = replaced_cards 
        if temporary_block_by_customer is not APIHelper.SKIP:
            self.temporary_block_by_customer = temporary_block_by_customer 
        if temporary_block_by_shell is not APIHelper.SKIP:
            self.temporary_block_by_shell = temporary_block_by_shell 
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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        active_cards = dictionary.get("ActiveCards") if "ActiveCards" in dictionary.keys() else APIHelper.SKIP
        blocked_cards = dictionary.get("BlockedCards") if "BlockedCards" in dictionary.keys() else APIHelper.SKIP
        cancelled_cards = dictionary.get("CancelledCards") if "CancelledCards" in dictionary.keys() else APIHelper.SKIP
        expired_cards = dictionary.get("ExpiredCards") if "ExpiredCards" in dictionary.keys() else APIHelper.SKIP
        expiring_cards = dictionary.get("ExpiringCards") if "ExpiringCards" in dictionary.keys() else APIHelper.SKIP
        fraud_cards = dictionary.get("FraudCards") if "FraudCards" in dictionary.keys() else APIHelper.SKIP
        new_cards = dictionary.get("NewCards") if "NewCards" in dictionary.keys() else APIHelper.SKIP
        renewal_pending_cards = dictionary.get("RenewalPendingCards") if "RenewalPendingCards" in dictionary.keys() else APIHelper.SKIP
        replaced_cards = dictionary.get("ReplacedCards") if "ReplacedCards" in dictionary.keys() else APIHelper.SKIP
        temporary_block_by_customer = dictionary.get("TemporaryBlockByCustomer") if "TemporaryBlockByCustomer" in dictionary.keys() else APIHelper.SKIP
        temporary_block_by_shell = dictionary.get("TemporaryBlockByShell") if "TemporaryBlockByShell" in dictionary.keys() else APIHelper.SKIP
        total_cards = dictionary.get("TotalCards") if "TotalCards" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(active_cards,
                   blocked_cards,
                   cancelled_cards,
                   expired_cards,
                   expiring_cards,
                   fraud_cards,
                   new_cards,
                   renewal_pending_cards,
                   replaced_cards,
                   temporary_block_by_customer,
                   temporary_block_by_shell,
                   total_cards)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'active_cards={(self.active_cards if hasattr(self, "active_cards") else None)!r}, '
                f'blocked_cards={(self.blocked_cards if hasattr(self, "blocked_cards") else None)!r}, '
                f'cancelled_cards={(self.cancelled_cards if hasattr(self, "cancelled_cards") else None)!r}, '
                f'expired_cards={(self.expired_cards if hasattr(self, "expired_cards") else None)!r}, '
                f'expiring_cards={(self.expiring_cards if hasattr(self, "expiring_cards") else None)!r}, '
                f'fraud_cards={(self.fraud_cards if hasattr(self, "fraud_cards") else None)!r}, '
                f'new_cards={(self.new_cards if hasattr(self, "new_cards") else None)!r}, '
                f'renewal_pending_cards={(self.renewal_pending_cards if hasattr(self, "renewal_pending_cards") else None)!r}, '
                f'replaced_cards={(self.replaced_cards if hasattr(self, "replaced_cards") else None)!r}, '
                f'temporary_block_by_customer={(self.temporary_block_by_customer if hasattr(self, "temporary_block_by_customer") else None)!r}, '
                f'temporary_block_by_shell={(self.temporary_block_by_shell if hasattr(self, "temporary_block_by_shell") else None)!r}, '
                f'total_cards={(self.total_cards if hasattr(self, "total_cards") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'active_cards={(self.active_cards if hasattr(self, "active_cards") else None)!s}, '
                f'blocked_cards={(self.blocked_cards if hasattr(self, "blocked_cards") else None)!s}, '
                f'cancelled_cards={(self.cancelled_cards if hasattr(self, "cancelled_cards") else None)!s}, '
                f'expired_cards={(self.expired_cards if hasattr(self, "expired_cards") else None)!s}, '
                f'expiring_cards={(self.expiring_cards if hasattr(self, "expiring_cards") else None)!s}, '
                f'fraud_cards={(self.fraud_cards if hasattr(self, "fraud_cards") else None)!s}, '
                f'new_cards={(self.new_cards if hasattr(self, "new_cards") else None)!s}, '
                f'renewal_pending_cards={(self.renewal_pending_cards if hasattr(self, "renewal_pending_cards") else None)!s}, '
                f'replaced_cards={(self.replaced_cards if hasattr(self, "replaced_cards") else None)!s}, '
                f'temporary_block_by_customer={(self.temporary_block_by_customer if hasattr(self, "temporary_block_by_customer") else None)!s}, '
                f'temporary_block_by_shell={(self.temporary_block_by_shell if hasattr(self, "temporary_block_by_shell") else None)!s}, '
                f'total_cards={(self.total_cards if hasattr(self, "total_cards") else None)!s})')
