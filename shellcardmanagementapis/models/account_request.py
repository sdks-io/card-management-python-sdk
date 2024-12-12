# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.accounts import Accounts


class AccountRequest(object):

    """Implementation of the 'AccountRequest' model.

    TODO: type model description here.

    Attributes:
        status (str): Account Status. Optional if StatusList is passed, else
            mandatory. Ignored if StatusList is passed. Allowed values: •   
            ALL •    ACTIVE •    BLOCKED •    CANCELLED •    CREDITLOCK •   
            DELINQUENCYLOCK
        include_card_summary (bool): Include card summary details in the
            response.   When passed as false, the card summary related
            parameters on response will be set to null.   Optional – default
            value: true.
        payer_id (int): Payer id of the customer. Optional if PayerNumber is
            passed, else Mandatory.
        payer_number (str): PayerNumber of the customer. Optional if PayerId
            is passed, else Mandatory.
        page_size (int): Page Size – Number of records to show on a page.
            Optional Default value 50
        request_id (str): API Request Id
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer.   ColCoCode or ColCoCountryCode  is Mandatory for
            serviced OUs such as Romania, Latvia, Lithuania, Estonia, Ukraine
            etc. It is optional for other countries if ColCoID is provided.
        col_co_country_code (str): The 2-character ISO Code for the customer
            and card owning country. ColCoCode or ColCoCountryCode  is
            Mandatory for serviced OUs such as Romania, Latvia, Lithuania,
            Estonia, Ukraine etc. It is optional for other countries if
            ColCoID is provided.
        current_page (int): Page Number (as shown to the users) Optional
            Default value 1
        invoice_points_only (bool): Optional – default value: false. When
            passed as true, the API will return accounts that are configured
            as Invoice Point only.
        col_co_id (int): Collecting Company Id (in GFN) of the selected payer.
            Optional if ColCoCode or ColCoCountryCode  is passed else
            Mandatory.
        return_tolls_customer_id (bool): Return e-Toll Customer details When
            True.
        accounts (List[Accounts]): TODO: type description here.
        account_name (str): Account Name of the customer.  Optional.   Minimum
            of 4 characters should be provided else not considered.  Accounts
            those have the entered value at any part of the Name will be
            returned.
        status_list (List[str]): Account Statuses.  Optional   Multiple
            statuses are allowed to be included in the search criteria. 
            Allowed values:  •    ACTIVE  •    BLOCKED  •    CANCELLED  •   
            CREDITLOCK  •    DELINQUENCYLOCK

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'Status',
        "include_card_summary": 'IncludeCardSummary',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "page_size": 'PageSize',
        "request_id": 'RequestId',
        "col_co_code": 'ColCoCode',
        "col_co_country_code": 'ColCoCountryCode',
        "current_page": 'CurrentPage',
        "invoice_points_only": 'InvoicePointsOnly',
        "col_co_id": 'ColCoId',
        "return_tolls_customer_id": 'ReturnTollsCustomerId',
        "accounts": 'Accounts',
        "account_name": 'AccountName',
        "status_list": 'StatusList'
    }

    _optionals = [
        'status',
        'include_card_summary',
        'payer_id',
        'payer_number',
        'page_size',
        'request_id',
        'col_co_code',
        'col_co_country_code',
        'current_page',
        'invoice_points_only',
        'col_co_id',
        'return_tolls_customer_id',
        'accounts',
        'account_name',
        'status_list',
    ]

    _nullables = [
        'status',
        'payer_id',
        'payer_number',
        'page_size',
        'request_id',
        'col_co_code',
        'col_co_country_code',
        'current_page',
        'invoice_points_only',
        'col_co_id',
        'account_name',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 include_card_summary=True,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 page_size=APIHelper.SKIP,
                 request_id=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 invoice_points_only=False,
                 col_co_id=APIHelper.SKIP,
                 return_tolls_customer_id=APIHelper.SKIP,
                 accounts=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 status_list=APIHelper.SKIP):
        """Constructor for the AccountRequest class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        self.include_card_summary = include_card_summary 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if page_size is not APIHelper.SKIP:
            self.page_size = page_size 
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        self.invoice_points_only = invoice_points_only 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if return_tolls_customer_id is not APIHelper.SKIP:
            self.return_tolls_customer_id = return_tolls_customer_id 
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if status_list is not APIHelper.SKIP:
            self.status_list = status_list 

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
        status = dictionary.get("Status") if "Status" in dictionary.keys() else APIHelper.SKIP
        include_card_summary = dictionary.get("IncludeCardSummary") if dictionary.get("IncludeCardSummary") else True
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        page_size = dictionary.get("PageSize") if "PageSize" in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if "RequestId" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        current_page = dictionary.get("CurrentPage") if "CurrentPage" in dictionary.keys() else APIHelper.SKIP
        invoice_points_only = dictionary.get("InvoicePointsOnly") if dictionary.get("InvoicePointsOnly") else False
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        return_tolls_customer_id = dictionary.get("ReturnTollsCustomerId") if "ReturnTollsCustomerId" in dictionary.keys() else APIHelper.SKIP
        accounts = None
        if dictionary.get('Accounts') is not None:
            accounts = [Accounts.from_dictionary(x) for x in dictionary.get('Accounts')]
        else:
            accounts = APIHelper.SKIP
        account_name = dictionary.get("AccountName") if "AccountName" in dictionary.keys() else APIHelper.SKIP
        status_list = dictionary.get("StatusList") if dictionary.get("StatusList") else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   include_card_summary,
                   payer_id,
                   payer_number,
                   page_size,
                   request_id,
                   col_co_code,
                   col_co_country_code,
                   current_page,
                   invoice_points_only,
                   col_co_id,
                   return_tolls_customer_id,
                   accounts,
                   account_name,
                   status_list)
