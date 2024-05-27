# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class UpdateCardGroupRequest(object):

    """Implementation of the 'UpdateCardGroupRequest' model.

    TODO: type model description here.

    Attributes:
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86-Philippines  5-UK
        col_co_id (int): Collecting Company Id  of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example: 
            1-Philippines  5-UK
        payer_number (str): Payer Number of the selected payer.  Optional if
            PayerId is passed else Mandatory
        payer_id (int): Payer Id (i.e., Customer Id of the Payment Customer)
            of the selected payer.  Optional if PayerNumber is passed else
            Mandatory  Example: 123456
        account_id (int): Account ID of the card-group to be
            updated/terminated.
        account_number (str): Account Number of the card-group to be
            updated/terminated.
        card_group_id (int): Unique Id of the card group that needs to be
            updated or terminated.
        card_group_name (str): New name for the card group if it needs to be
            updated. Set this field to ‘null’ if no change required to the
            current card group name.    Optional    Minimum length: 1
            (Configurable)  Maximum length: 40 (Configurable)  Allowed
            characters (Configurable) are: - A-Z 0-9, / ‘. & Ä Ö Ü Å Æ É Ø 
            Note: The card group name has to be unique for customer. Else an
            error with error code 9015 is returned.
        print_on_card (bool): Whether to emboss the card group name on the
            cards.   Populate this field only if the value needs to be
            updated. Otherwise set to ‘null’.
        card_type_id (int): Card Type ID of the card group.   Populate this
            field if the value needs to be updated. Otherwise set to ‘null’. 
            Optional  Note:   1) If a card type is passed, the cardgorup will
            allow cards with same card type to be moved in to the card group. 
            2) Pass ‘-1’ to remove the card type from the card group.
        terminate_card_group (bool): Whether to terminate the card group. 
            When set to true, the card group will be terminated by setting
            current date as it’s termination date.  Optional, False by default
            .
        move_cards (bool): Whether to move the cards from this CardGroup in to
            a different or a new CardGroup.  Optional  When the value is set
            to ‘False’ or ‘null’, the cards that are currently in the
            card-group will remain under the same card-group.
        target_account_id (int): Account ID of the new/target card-group. 
            Either TargetAccountId or TargetAccountNumber is mandatory when
            MoveCards is set to True.
        target_account_number (str): Account Number of the new/target
            card-group.  Either TargetAccountId or TargetAccountNumber is
            mandatory when MoveCards is set to True.
        target_new_card_group_name (str): Name of the new card group if the
            cards in the existing card-group have to be moved to a new
            card-group.    Mandatory when MoveCards parameter is True and
            TargetCardGroupId is null.    Minimum length: 1 (Configurable) 
            Maximum length: 30 (Configurable)
        target_card_group_id (int): ID of the card group if the cards in the
            existing card-group have to be moved to another existing
            card-group.  Mandatory when MoveCards parameter is True and
            TargetNewCardGroupName is null.  If the value is “-1” then the
            cards will be moved out of the current CardGroup.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "payer_number": 'PayerNumber',
        "payer_id": 'PayerId',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "card_group_id": 'CardGroupId',
        "card_group_name": 'CardGroupName',
        "print_on_card": 'PrintOnCard',
        "card_type_id": 'CardTypeId',
        "terminate_card_group": 'TerminateCardGroup',
        "move_cards": 'MoveCards',
        "target_account_id": 'TargetAccountId',
        "target_account_number": 'TargetAccountNumber',
        "target_new_card_group_name": 'TargetNewCardGroupName',
        "target_card_group_id": 'TargetCardGroupId'
    }

    _optionals = [
        'col_co_code',
        'col_co_id',
        'payer_number',
        'payer_id',
        'account_id',
        'account_number',
        'card_group_id',
        'card_group_name',
        'print_on_card',
        'card_type_id',
        'terminate_card_group',
        'move_cards',
        'target_account_id',
        'target_account_number',
        'target_new_card_group_name',
        'target_card_group_id',
    ]

    def __init__(self,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 print_on_card=APIHelper.SKIP,
                 card_type_id=APIHelper.SKIP,
                 terminate_card_group=APIHelper.SKIP,
                 move_cards=APIHelper.SKIP,
                 target_account_id=APIHelper.SKIP,
                 target_account_number=APIHelper.SKIP,
                 target_new_card_group_name=APIHelper.SKIP,
                 target_card_group_id=APIHelper.SKIP):
        """Constructor for the UpdateCardGroupRequest class"""

        # Initialize members of the class
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if print_on_card is not APIHelper.SKIP:
            self.print_on_card = print_on_card 
        if card_type_id is not APIHelper.SKIP:
            self.card_type_id = card_type_id 
        if terminate_card_group is not APIHelper.SKIP:
            self.terminate_card_group = terminate_card_group 
        if move_cards is not APIHelper.SKIP:
            self.move_cards = move_cards 
        if target_account_id is not APIHelper.SKIP:
            self.target_account_id = target_account_id 
        if target_account_number is not APIHelper.SKIP:
            self.target_account_number = target_account_number 
        if target_new_card_group_name is not APIHelper.SKIP:
            self.target_new_card_group_name = target_new_card_group_name 
        if target_card_group_id is not APIHelper.SKIP:
            self.target_card_group_id = target_card_group_id 

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
        col_co_code = dictionary.get("ColCoCode") if dictionary.get("ColCoCode") else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if dictionary.get("ColCoId") else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if dictionary.get("PayerNumber") else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if dictionary.get("PayerId") else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if dictionary.get("AccountId") else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if dictionary.get("AccountNumber") else APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if dictionary.get("CardGroupId") else APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if dictionary.get("CardGroupName") else APIHelper.SKIP
        print_on_card = dictionary.get("PrintOnCard") if "PrintOnCard" in dictionary.keys() else APIHelper.SKIP
        card_type_id = dictionary.get("CardTypeId") if dictionary.get("CardTypeId") else APIHelper.SKIP
        terminate_card_group = dictionary.get("TerminateCardGroup") if "TerminateCardGroup" in dictionary.keys() else APIHelper.SKIP
        move_cards = dictionary.get("MoveCards") if "MoveCards" in dictionary.keys() else APIHelper.SKIP
        target_account_id = dictionary.get("TargetAccountId") if dictionary.get("TargetAccountId") else APIHelper.SKIP
        target_account_number = dictionary.get("TargetAccountNumber") if dictionary.get("TargetAccountNumber") else APIHelper.SKIP
        target_new_card_group_name = dictionary.get("TargetNewCardGroupName") if dictionary.get("TargetNewCardGroupName") else APIHelper.SKIP
        target_card_group_id = dictionary.get("TargetCardGroupId") if dictionary.get("TargetCardGroupId") else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_code,
                   col_co_id,
                   payer_number,
                   payer_id,
                   account_id,
                   account_number,
                   card_group_id,
                   card_group_name,
                   print_on_card,
                   card_type_id,
                   terminate_card_group,
                   move_cards,
                   target_account_id,
                   target_account_number,
                   target_new_card_group_name,
                   target_card_group_id)
