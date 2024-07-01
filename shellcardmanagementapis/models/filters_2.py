# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class Filters2(object):

    """Implementation of the 'Filters2' model.

    TODO: type model description here.

    Attributes:
        account_id (int): Account ID of the customer.<br/> Optional if
            AccountNumber is passed, else mandatory. <br/> This input is a
            search criterion, if given.
        account_number (str): Account Number of the customer.<br/> Optional if
            AccountId is passed, else mandatory.<br/> This input is a search
            criterion, if given.
        col_co_code (int): Collecting Company Code (Shell Code) of the
            selected payer. <br /> Optional – when ‘ReferenceNumber’ is
            provided.<br />
        col_co_id (int): Collecting Company Id (in ) of the selected payer.
            <br /> Optional – when ‘ReferenceNumber’ is provided. Else, either
            ‘ColCoId’ or ‘ColCoCode’ is mandatory.<br />
        col_co_country_code (str): ISO 3166 Alpha-2 Country Code for the
            customer and card owning country.
        payer_id (int): Payer Id (i.e. Customer Id of the Payment Customer) of
            the selected payer.<br /> Optional – when ‘ReferenceNumber’ is
            provided. Else, either ‘PayerId’ or ‘PayerNumber’ is mandatory.
        payer_number (str): Payer Number of the selected payer.<br /> Optional
            – when ‘ReferenceNumber’ is provided. Else, either ‘PayerId’ or
            ‘PayerNumber’ is mandatory.
        reference_number (int): Reference number of the Card Order/ Bulk Card
            Order/ Order Card Request.<br /> Mandatory when ColCo and Payer
            fields are not provided. Else, optional.
        reference_type (OrderCardEnquiryReqReferenceTypeEnum): TODO: type
            description here.
        from_date (str): Card Orders from Date/Time.<br /> Optional.<br />
            Value should be with in last 7 days<br /> This field is ignored if
            ReferenceNumber is provided <br /> This field is optional when not
            provided and ReferenceNumber is null or empty then the value
            should be set to D-7(Where D is current date)<br /> Format:
            yyyyMMdd
        to_date (str): Card Order to Date/Time<br /> Optional<br /> Value
            should be with in last 7 days<br /> This field is ignored if
            ReferenceNumber is provided <br /> This field is optional when not
            provided and ReferenceNumber is null or empty then the value
            should be set to current date<br /> Format: yyyyMMdd
        order_request_id (str): Client provided Unique Id of the original
            Order Card request, the status of which is enquired by this API

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "col_co_code": 'ColCoCode',
        "col_co_id": 'ColCoId',
        "col_co_country_code": 'ColCoCountryCode',
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "reference_number": 'ReferenceNumber',
        "reference_type": 'ReferenceType',
        "from_date": 'FromDate',
        "to_date": 'ToDate',
        "order_request_id": 'OrderRequestId'
    }

    _optionals = [
        'account_id',
        'account_number',
        'col_co_code',
        'col_co_id',
        'col_co_country_code',
        'payer_id',
        'payer_number',
        'reference_number',
        'reference_type',
        'from_date',
        'to_date',
        'order_request_id',
    ]

    _nullables = [
        'account_id',
        'account_number',
        'col_co_code',
        'col_co_id',
        'col_co_country_code',
        'payer_id',
        'payer_number',
        'from_date',
        'to_date',
        'order_request_id',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 col_co_code=APIHelper.SKIP,
                 col_co_id=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 reference_number=APIHelper.SKIP,
                 reference_type=APIHelper.SKIP,
                 from_date=APIHelper.SKIP,
                 to_date=APIHelper.SKIP,
                 order_request_id=APIHelper.SKIP):
        """Constructor for the Filters2 class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if col_co_code is not APIHelper.SKIP:
            self.col_co_code = col_co_code 
        if col_co_id is not APIHelper.SKIP:
            self.col_co_id = col_co_id 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if reference_number is not APIHelper.SKIP:
            self.reference_number = reference_number 
        if reference_type is not APIHelper.SKIP:
            self.reference_type = reference_type 
        if from_date is not APIHelper.SKIP:
            self.from_date = from_date 
        if to_date is not APIHelper.SKIP:
            self.to_date = to_date 
        if order_request_id is not APIHelper.SKIP:
            self.order_request_id = order_request_id 

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
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        col_co_code = dictionary.get("ColCoCode") if "ColCoCode" in dictionary.keys() else APIHelper.SKIP
        col_co_id = dictionary.get("ColCoId") if "ColCoId" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        reference_number = dictionary.get("ReferenceNumber") if dictionary.get("ReferenceNumber") else APIHelper.SKIP
        reference_type = dictionary.get("ReferenceType") if dictionary.get("ReferenceType") else APIHelper.SKIP
        from_date = dictionary.get("FromDate") if "FromDate" in dictionary.keys() else APIHelper.SKIP
        to_date = dictionary.get("ToDate") if "ToDate" in dictionary.keys() else APIHelper.SKIP
        order_request_id = dictionary.get("OrderRequestId") if "OrderRequestId" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   account_number,
                   col_co_code,
                   col_co_id,
                   col_co_country_code,
                   payer_id,
                   payer_number,
                   reference_number,
                   reference_type,
                   from_date,
                   to_date,
                   order_request_id)
