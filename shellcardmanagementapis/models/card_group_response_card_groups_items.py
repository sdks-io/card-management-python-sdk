# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardGroupResponseCardGroupsItems(object):

    """Implementation of the 'CardGroupResponseCardGroupsItems' model.

    Attributes:
        account_id (int): Account Id for the associated card group
        account_number (str): Account number for the associated card group
        account_short_name (str): Account short name for the associated card
            group
        active_cards (int): Total number of active cards for the given search
            criteria
        blocked_cards (int): Total number of cards for the given search
            criteria that are permanently blocked
        cancelled_cards (int): Total number of cards for the given search
            criteria that are cancelled
        card_delivery_point (bool): card delivery point enabled or not
        card_group_id (int): Id of the card group matching the search criteria.
        card_group_name (str): Name of the card group matching the search
            criteria.
        card_type_code (str): Card Type Code
        card_type_id (int): Card Type Id
        card_type_name (str): Card Type Name
        expired_cards (int): Total number of expired cards for the given
            search criteria
        expiry_date (str): Expiry date of the card. Format: yyyyMMdd Note:
            Clients to convert this to appropriate DateTime type.
        print_on_card (bool): PrintOnCard true/false
        renewal_pending_cards (int): Total number of Renewal Pending Cards for
            the given search criteria
        replaced_cards (int): The model property of type int.
        status (str): Status of the card group.
        temporary_block_by_customer (int): Total number of cards for the given
            search criteria that are temporarily blocked by customer
        temporary_block_by_shell (int): Total number of cards for the given
            search criteria that are temporarily blocked by Shell
        terminated_date (str): Terminated Date.   Format: yyyyMMdd  Note:
            Clients to convert this to appropriate Date Time type.
        total_cards (int): Total number of cards for the given search criteria

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "account_short_name": 'AccountShortName',
        "active_cards": 'ActiveCards',
        "blocked_cards": 'BlockedCards',
        "cancelled_cards": 'CancelledCards',
        "card_delivery_point": 'CardDeliveryPoint',
        "card_group_id": 'CardGroupId',
        "card_group_name": 'CardGroupName',
        "card_type_code": 'CardTypeCode',
        "card_type_id": 'CardTypeId',
        "card_type_name": 'CardTypeName',
        "expired_cards": 'ExpiredCards',
        "expiry_date": 'ExpiryDate',
        "print_on_card": 'PrintOnCard',
        "renewal_pending_cards": 'RenewalPendingCards',
        "replaced_cards": 'ReplacedCards',
        "status": 'Status',
        "temporary_block_by_customer": 'TemporaryBlockByCustomer',
        "temporary_block_by_shell": 'TemporaryBlockByShell',
        "terminated_date": 'TerminatedDate',
        "total_cards": 'TotalCards'
    }

    _optionals = [
        'account_id',
        'account_number',
        'account_short_name',
        'active_cards',
        'blocked_cards',
        'cancelled_cards',
        'card_delivery_point',
        'card_group_id',
        'card_group_name',
        'card_type_code',
        'card_type_id',
        'card_type_name',
        'expired_cards',
        'expiry_date',
        'print_on_card',
        'renewal_pending_cards',
        'replaced_cards',
        'status',
        'temporary_block_by_customer',
        'temporary_block_by_shell',
        'terminated_date',
        'total_cards',
    ]

    _nullables = [
        'account_id',
        'account_number',
        'account_short_name',
        'active_cards',
        'blocked_cards',
        'cancelled_cards',
        'card_delivery_point',
        'card_group_id',
        'card_group_name',
        'card_type_code',
        'card_type_id',
        'card_type_name',
        'expired_cards',
        'expiry_date',
        'print_on_card',
        'renewal_pending_cards',
        'replaced_cards',
        'status',
        'temporary_block_by_customer',
        'temporary_block_by_shell',
        'terminated_date',
        'total_cards',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_short_name=APIHelper.SKIP,
                 active_cards=APIHelper.SKIP,
                 blocked_cards=APIHelper.SKIP,
                 cancelled_cards=APIHelper.SKIP,
                 card_delivery_point=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 card_type_code=APIHelper.SKIP,
                 card_type_id=APIHelper.SKIP,
                 card_type_name=APIHelper.SKIP,
                 expired_cards=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP,
                 print_on_card=APIHelper.SKIP,
                 renewal_pending_cards=APIHelper.SKIP,
                 replaced_cards=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 temporary_block_by_customer=APIHelper.SKIP,
                 temporary_block_by_shell=APIHelper.SKIP,
                 terminated_date=APIHelper.SKIP,
                 total_cards=APIHelper.SKIP):
        """Constructor for the CardGroupResponseCardGroupsItems class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_short_name is not APIHelper.SKIP:
            self.account_short_name = account_short_name 
        if active_cards is not APIHelper.SKIP:
            self.active_cards = active_cards 
        if blocked_cards is not APIHelper.SKIP:
            self.blocked_cards = blocked_cards 
        if cancelled_cards is not APIHelper.SKIP:
            self.cancelled_cards = cancelled_cards 
        if card_delivery_point is not APIHelper.SKIP:
            self.card_delivery_point = card_delivery_point 
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if card_type_code is not APIHelper.SKIP:
            self.card_type_code = card_type_code 
        if card_type_id is not APIHelper.SKIP:
            self.card_type_id = card_type_id 
        if card_type_name is not APIHelper.SKIP:
            self.card_type_name = card_type_name 
        if expired_cards is not APIHelper.SKIP:
            self.expired_cards = expired_cards 
        if expiry_date is not APIHelper.SKIP:
            self.expiry_date = expiry_date 
        if print_on_card is not APIHelper.SKIP:
            self.print_on_card = print_on_card 
        if renewal_pending_cards is not APIHelper.SKIP:
            self.renewal_pending_cards = renewal_pending_cards 
        if replaced_cards is not APIHelper.SKIP:
            self.replaced_cards = replaced_cards 
        if status is not APIHelper.SKIP:
            self.status = status 
        if temporary_block_by_customer is not APIHelper.SKIP:
            self.temporary_block_by_customer = temporary_block_by_customer 
        if temporary_block_by_shell is not APIHelper.SKIP:
            self.temporary_block_by_shell = temporary_block_by_shell 
        if terminated_date is not APIHelper.SKIP:
            self.terminated_date = terminated_date 
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
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_short_name = dictionary.get("AccountShortName") if "AccountShortName" in dictionary.keys() else APIHelper.SKIP
        active_cards = dictionary.get("ActiveCards") if "ActiveCards" in dictionary.keys() else APIHelper.SKIP
        blocked_cards = dictionary.get("BlockedCards") if "BlockedCards" in dictionary.keys() else APIHelper.SKIP
        cancelled_cards = dictionary.get("CancelledCards") if "CancelledCards" in dictionary.keys() else APIHelper.SKIP
        card_delivery_point = dictionary.get("CardDeliveryPoint") if "CardDeliveryPoint" in dictionary.keys() else APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if "CardGroupId" in dictionary.keys() else APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if "CardGroupName" in dictionary.keys() else APIHelper.SKIP
        card_type_code = dictionary.get("CardTypeCode") if "CardTypeCode" in dictionary.keys() else APIHelper.SKIP
        card_type_id = dictionary.get("CardTypeId") if "CardTypeId" in dictionary.keys() else APIHelper.SKIP
        card_type_name = dictionary.get("CardTypeName") if "CardTypeName" in dictionary.keys() else APIHelper.SKIP
        expired_cards = dictionary.get("ExpiredCards") if "ExpiredCards" in dictionary.keys() else APIHelper.SKIP
        expiry_date = dictionary.get("ExpiryDate") if "ExpiryDate" in dictionary.keys() else APIHelper.SKIP
        print_on_card = dictionary.get("PrintOnCard") if "PrintOnCard" in dictionary.keys() else APIHelper.SKIP
        renewal_pending_cards = dictionary.get("RenewalPendingCards") if "RenewalPendingCards" in dictionary.keys() else APIHelper.SKIP
        replaced_cards = dictionary.get("ReplacedCards") if "ReplacedCards" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("Status") if "Status" in dictionary.keys() else APIHelper.SKIP
        temporary_block_by_customer = dictionary.get("TemporaryBlockByCustomer") if "TemporaryBlockByCustomer" in dictionary.keys() else APIHelper.SKIP
        temporary_block_by_shell = dictionary.get("TemporaryBlockByShell") if "TemporaryBlockByShell" in dictionary.keys() else APIHelper.SKIP
        terminated_date = dictionary.get("TerminatedDate") if "TerminatedDate" in dictionary.keys() else APIHelper.SKIP
        total_cards = dictionary.get("TotalCards") if "TotalCards" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   account_number,
                   account_short_name,
                   active_cards,
                   blocked_cards,
                   cancelled_cards,
                   card_delivery_point,
                   card_group_id,
                   card_group_name,
                   card_type_code,
                   card_type_id,
                   card_type_name,
                   expired_cards,
                   expiry_date,
                   print_on_card,
                   renewal_pending_cards,
                   replaced_cards,
                   status,
                   temporary_block_by_customer,
                   temporary_block_by_shell,
                   terminated_date,
                   total_cards)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!r}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!r}, '
                f'account_short_name={(self.account_short_name if hasattr(self, "account_short_name") else None)!r}, '
                f'active_cards={(self.active_cards if hasattr(self, "active_cards") else None)!r}, '
                f'blocked_cards={(self.blocked_cards if hasattr(self, "blocked_cards") else None)!r}, '
                f'cancelled_cards={(self.cancelled_cards if hasattr(self, "cancelled_cards") else None)!r}, '
                f'card_delivery_point={(self.card_delivery_point if hasattr(self, "card_delivery_point") else None)!r}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!r}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!r}, '
                f'card_type_code={(self.card_type_code if hasattr(self, "card_type_code") else None)!r}, '
                f'card_type_id={(self.card_type_id if hasattr(self, "card_type_id") else None)!r}, '
                f'card_type_name={(self.card_type_name if hasattr(self, "card_type_name") else None)!r}, '
                f'expired_cards={(self.expired_cards if hasattr(self, "expired_cards") else None)!r}, '
                f'expiry_date={(self.expiry_date if hasattr(self, "expiry_date") else None)!r}, '
                f'print_on_card={(self.print_on_card if hasattr(self, "print_on_card") else None)!r}, '
                f'renewal_pending_cards={(self.renewal_pending_cards if hasattr(self, "renewal_pending_cards") else None)!r}, '
                f'replaced_cards={(self.replaced_cards if hasattr(self, "replaced_cards") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'temporary_block_by_customer={(self.temporary_block_by_customer if hasattr(self, "temporary_block_by_customer") else None)!r}, '
                f'temporary_block_by_shell={(self.temporary_block_by_shell if hasattr(self, "temporary_block_by_shell") else None)!r}, '
                f'terminated_date={(self.terminated_date if hasattr(self, "terminated_date") else None)!r}, '
                f'total_cards={(self.total_cards if hasattr(self, "total_cards") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'account_id={(self.account_id if hasattr(self, "account_id") else None)!s}, '
                f'account_number={(self.account_number if hasattr(self, "account_number") else None)!s}, '
                f'account_short_name={(self.account_short_name if hasattr(self, "account_short_name") else None)!s}, '
                f'active_cards={(self.active_cards if hasattr(self, "active_cards") else None)!s}, '
                f'blocked_cards={(self.blocked_cards if hasattr(self, "blocked_cards") else None)!s}, '
                f'cancelled_cards={(self.cancelled_cards if hasattr(self, "cancelled_cards") else None)!s}, '
                f'card_delivery_point={(self.card_delivery_point if hasattr(self, "card_delivery_point") else None)!s}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!s}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!s}, '
                f'card_type_code={(self.card_type_code if hasattr(self, "card_type_code") else None)!s}, '
                f'card_type_id={(self.card_type_id if hasattr(self, "card_type_id") else None)!s}, '
                f'card_type_name={(self.card_type_name if hasattr(self, "card_type_name") else None)!s}, '
                f'expired_cards={(self.expired_cards if hasattr(self, "expired_cards") else None)!s}, '
                f'expiry_date={(self.expiry_date if hasattr(self, "expiry_date") else None)!s}, '
                f'print_on_card={(self.print_on_card if hasattr(self, "print_on_card") else None)!s}, '
                f'renewal_pending_cards={(self.renewal_pending_cards if hasattr(self, "renewal_pending_cards") else None)!s}, '
                f'replaced_cards={(self.replaced_cards if hasattr(self, "replaced_cards") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'temporary_block_by_customer={(self.temporary_block_by_customer if hasattr(self, "temporary_block_by_customer") else None)!s}, '
                f'temporary_block_by_shell={(self.temporary_block_by_shell if hasattr(self, "temporary_block_by_shell") else None)!s}, '
                f'terminated_date={(self.terminated_date if hasattr(self, "terminated_date") else None)!s}, '
                f'total_cards={(self.total_cards if hasattr(self, "total_cards") else None)!s})')
