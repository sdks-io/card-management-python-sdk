# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CardDetailsResponseStatusIdEnum(object):

    """Implementation of the 'CardDetailsResponseStatusId' enum.

    Possible Id’s and description:
    * 1  Active
    * 7  Blocked Card
    * 8  Expired
    * 9  Cancelled
    * 10  New
    * 23  Pending Renewal
    * 31  Replaced
    * 41  Temporary Block (Customer)
    * 42  Temporary Block (Shell)
    * 43  Fraud
    * 101 Active (Block in progress) *
    * 102 Blocked Card (Unblock in progress) *
    * 103 Active (Cancel in progress) *
    * 104 Active (Marked as damaged) *
    * 105 New (Cancel as damaged) *
    * 106 Active(Scheduled for block) ”#
    * 107 Blocked Card(Scheduled for unblock)*#
    * 108 Blocked Card (Cancel in progress) *
    > Note:
    •  Items marked with * are intermediate statuses  to indicate that there
    are pending requests in progress. , The response can contain these
    intermediate statuses only if the IncludeIntermediateStatus flag is true.
    •  The placeholder “<Shell Card Platform Status>” in the items marked with
    # will be replaced with the Shell Card Platform status description. E.g.,
    “Active (Scheduled for block)”

    Attributes:
        ENUM_1: TODO: type description here.
        ENUM_7: TODO: type description here.
        ENUM_8: TODO: type description here.
        ENUM_9: TODO: type description here.
        ENUM_10: TODO: type description here.
        ENUM_23: TODO: type description here.
        ENUM_31: TODO: type description here.
        ENUM_41: TODO: type description here.
        ENUM_42: TODO: type description here.
        ENUM_43: TODO: type description here.
        ENUM_101: TODO: type description here.
        ENUM_102: TODO: type description here.
        ENUM_103: TODO: type description here.
        ENUM_104: TODO: type description here.
        ENUM_105: TODO: type description here.
        ENUM_106: TODO: type description here.
        ENUM_107: TODO: type description here.
        ENUM_108: TODO: type description here.

    """
    ENUM_1 = 1

    ENUM_7 = 7

    ENUM_8 = 8

    ENUM_9 = 9

    ENUM_10 = 10

    ENUM_23 = 23

    ENUM_31 = 31

    ENUM_41 = 41

    ENUM_42 = 42

    ENUM_43 = 43

    ENUM_101 = 101

    ENUM_102 = 102

    ENUM_103 = 103

    ENUM_104 = 104

    ENUM_105 = 105

    ENUM_106 = 106

    ENUM_107 = 107

    ENUM_108 = 108

