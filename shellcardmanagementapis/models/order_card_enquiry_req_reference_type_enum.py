# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class OrderCardEnquiryReqReferenceTypeEnum(object):

    """Implementation of the 'OrderCardEnquiryReqReferenceType' enum.

    Type of the reference number provided.<br />
    Mandatory if ReferenceNumber is provided. Else optional.<br />
    Allowed Values:<br />
    1=Main Reference(Main Order Reference Number returned in the output of
    Card/OrderCard service. <br />
    2=Order Card Reference (Reference number for each individual card in the
    order submitted via Card/OrderCard service. <br />
    3=Bulk Order Card Reference (Reference number returned in the response of
    bulkcardinterface /UploadOrderCardTemplate. )

    Attributes:
        ENUM_1: TODO: type description here.
        ENUM_2: TODO: type description here.
        ENUM_3: TODO: type description here.

    """
    ENUM_1 = 1

    ENUM_2 = 2

    ENUM_3 = 3
