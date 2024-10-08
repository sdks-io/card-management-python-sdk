# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CardDetailsResponseReissueSettingEnum(object):

    """Implementation of the 'CardDetailsResponseReissueSetting' enum.

    Reissue setting of the card. If the card is superseded (i.e. a
    replacement/new card is issued) then reissue setting of the latest card
    issued. Reissue setting:
      * `True` - Card will be Reissued when nearing its expiry date
      * `False` - Card will not be Reissued

    Attributes:
        TRUE: TODO: type description here.
        FALSE: TODO: type description here.

    """
    ENUM_TRUE = 'True'

    ENUM_FALSE = 'False'

