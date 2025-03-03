# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.accounts import Accounts


class CardGroupRequest(object):

    """Implementation of the 'CardGroupRequest' model.

    Attributes:
        col_co_id (int): Collecting Company Id of the selected payer.  
            Optional if ColCoCode is passed else Mandatory.  Example:  1 for
            Philippines  5 for UK
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   Mandatory for serviced OUs such as Romania,
            Latvia, Lithuania, Estonia, Ukraine etc. It is optional for other
            countries if ColCoID is provided.  Example:  86 for Philippines  5
            for UK
        payer_id (int): Payer id of the customer. Optional if PayerNumber is
            passed, else Mandatory. This input is a search criterion. Example:
            123456
        payer_number (str): PayerNumber of the customer.  Optional if PayerId
            is passed, else Mandatory.   This input is a search criterion. 
            Example: GB00123456
        account (List[Accounts]): The model property of type List[Accounts].
        card_group_name (str): Card Group Name   Optional.   Minimum of 2
            characters should be provided else not considered.  CardGroups
            those have the entered value at any part
        status (str): Card Group Status Mandatory Allowed values: •    ALL •  
            TERMINATED •    ACTIVE
        current_page (int): Page Number (as shown to the users) Optional
            Default value 1
        page_size (int): Page Size – Number of records to show on a page.
            Optional Default value 50. Return all rows if -1 is supplied as
            page size.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "col_co_id": 'ColCoId',
        "col_co_code": 'ColCoCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "account": 'Account',
        "card_group_name": 'CardGroupName',
        "status": 'Status',
        "current_page": 'CurrentPage',
        "page_size": 'PageSize'
    }

    _optionals = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'account',
        'card_group_name',
        'status',
        'current_page',
        'page_size',
    ]

    _nullables = [
        'col_co_id',
        'col_co_code',
        'payer_id',
        'payer_number',
        'card_group_name',
        'status',
    ]

    def __init__(self,
                 col_co_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 account=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 page_size=APIHelper.SKIP):
        """Constructor for the CardGroupRequest class"""

        # Initialize members of the class
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if account is not APIHelper.SKIP:
            self.account = account 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if status is not APIHelper.SKIP:
            self.status = status 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if page_size is not APIHelper.SKIP:
            self.page_size = page_size 

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
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        account = None
        if dictionary.get('Account') is not None:
            account = [Accounts.from_dictionary(x) for x in dictionary.get('Account')]
        else:
            account = APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if "CardGroupName" in dictionary.keys() else APIHelper.SKIP
        status = dictionary.get("Status") if "Status" in dictionary.keys() else APIHelper.SKIP
        current_page = dictionary.get("CurrentPage") if dictionary.get("CurrentPage") else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if dictionary.get("PageSize") else APIHelper.SKIP
        # Return an object of this model
        return cls(col_co_id,
                   col_co_code,
                   payer_id,
                   payer_number,
                   account,
                   card_group_name,
                   status,
                   current_page,
                   page_size)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!r}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!r}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!r}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!r}, '
                f'account={(self.account if hasattr(self, "account") else None)!r}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!r}, '
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!r}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'col_co_id={(self.col_co_id if hasattr(self, "col_co_id") else None)!s}, '
                f'col_co_code={(self.col_co_code if hasattr(self, "col_co_code") else None)!s}, '
                f'payer_id={(self.payer_id if hasattr(self, "payer_id") else None)!s}, '
                f'payer_number={(self.payer_number if hasattr(self, "payer_number") else None)!s}, '
                f'account={(self.account if hasattr(self, "account") else None)!s}, '
                f'card_group_name={(self.card_group_name if hasattr(self, "card_group_name") else None)!s}, '
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'current_page={(self.current_page if hasattr(self, "current_page") else None)!s}, '
                f'page_size={(self.page_size if hasattr(self, "page_size") else None)!s})')
