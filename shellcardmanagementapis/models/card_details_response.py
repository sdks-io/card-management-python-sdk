# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.card_delivery_address import CardDeliveryAddress
from shellcardmanagementapis.models.card_details_response_card_block_schedules_items_all_of_0 import CardDetailsResponseCardBlockSchedulesItemsAllOf0
from shellcardmanagementapis.models.card_details_response_fuel_sets_items import CardDetailsResponseFuelSetsItems
from shellcardmanagementapis.models.card_details_response_non_fuel_sets_items import CardDetailsResponseNonFuelSetsItems
from shellcardmanagementapis.models.error_status import ErrorStatus
from shellcardmanagementapis.models.pin_delivery_address import PINDeliveryAddress


class CardDetailsResponse(object):

    """Implementation of the 'CardDetailsResponse' model.

    TODO: type model description here.

    Attributes:
        payer_id (int): Payer Id (i.e. Customer Id of the Payment Customer in
            the Shell Card Platform) of the selected payer.
        payer_number (str): Payer Number of the selected payer.
        account_id (int): Account Id (i.e. Customer Id of the Customer in the
            Shell Card Platform) of the customer.
        account_number (str): Account Number of the customer.
        account_short_name (str): Account short name.
        col_co_country_code (str): ISO 3166 Alpha-2 Country Code for the
            customer and card owning country.
        local_currency_code (str): ISO 4217 Curreny Code of the local
            currency.
        local_currency_symbol (str): Currency symbol of local currency.
        card_id (int): Unique Card Id in Cards platform.
        pan (str): Card PAN. In the response body the PAN will be masked if
            the option is enabled in the Shell Card Platform.
        status_id (CardDetailsResponseStatusIdEnum): TODO: type description
            here.
        status (str): Possible Id’s and description: * 1  Active * 7  Blocked
            Card * 8  Expired * 9  Cancelled * 10  New * 23  Pending Renewal *
            31  Replaced * 41  Temporary Block (Customer) * 42  Temporary
            Block (Shell) * 43  Fraud * 101 Active (Block in progress) * * 102
            Blocked Card (Unblock in progress) * * 103 Active (Cancel in
            progress) * * 104 Active (Marked as damaged) * * 105 New (Cancel
            as damaged) * * 106 Active(Scheduled for block) ”# * 107 Blocked
            Card(Scheduled for unblock) *# * 108 Blocked Card (Cancel in
            progress) * > Note: •  Items marked with * are intermediate
            statuses  to indicate that there are pending requests in progress.
            , The response can contain these intermediate statuses only if the
            IncludeIntermediateStatus flag is true. •  The placeholder “<Shell
            Card Platform Status>” in the items marked with # will be replaced
            with the Shell Card Platform status description. E.g., “Active
            (Scheduled for block)”
        odometer_prompt (bool): True if odometer input is enabled on the card,
            else false
        fleet_id_prompt (bool): True if fleet id input is enabled, else false
        pin_type (CardDetailsResponsePINTypeEnum): TODO: type description
            here.
        has_pin (bool): True if card has PIN, else false
        is_self_selected_pin (bool): True if card has Self Selected PIN, else
            false
        temporary_block_allowed (bool): True if card can be blocked
            temporarily, else false
        unblock_allowed (bool): True/False True if card can be Unblocked, else
            false
        permanent_block_allowed (bool): True if card can be blocked
            permanently, else false
        issue_number (int): Issue number of the card
        reissue_setting (object): TODO: type description here.
        international_pos_language_id
            (CardDetailsResponseInternationalPOSLanguageIDEnum): TODO: type
            description here.
        international_pos_language_code
            (CardDetailsResponseInternationalPOSLanguageCodeEnum): TODO: type
            description here.
        local_pos_language_id
            (CardDetailsResponseInternationalPOSLanguageIDEnum): TODO: type
            description here.
        local_pos_language_code
            (CardDetailsResponseInternationalPOSLanguageCodeEnum): TODO: type
            description here.
        card_type_code (str): ISO code of the card i.e. first 7 digits of the
            PAN.
        card_type_id (int): Card Type ID
        card_type_name (str): Card Type Name
        token_type_id (int): Token Type ID configured for the Card
        token_type_name (str): Token Type Name configured for the Card
        is_chip_card (bool): True if a chip card, else false
        is_mag_strip_card (bool): True if it is a magnetic stripe card, else
            false
        is_virtual_card (bool): True if it is a virtual card, else false
        purchase_category_code (str): Purchase category code of the card.
        purchase_category_id (int): Purchase category identifier in the Shell
            Card Platform.
        purchase_category_name (str): Purchase category name
        is_crt (bool): True if it is a Commercial Road Transport (CRT) card,
            else false
        is_fleet (bool): True if it is a Fleet card, else false
        is_international (bool): True if it is an international card, else
            false
        is_national (bool): True if it is a national card, else false
        is_partner_sites_included (bool): True if it is allowed at all partner
            sites, else false
        is_shell_sites_only (bool): True if it is only allowed at Shell sites,
            else false
        fuel_sets (List[CardDetailsResponseFuelSetsItems]): List of active
            fuel type product restrictions applied on the card.
        non_fuel_sets (List[CardDetailsResponseNonFuelSetsItems]): List of
            active non-fuel type product restrictions applied on the card.
        issued_date (str): Card issue date.
        expiry_date (str): Expiry date of the card.
        last_used_date (str): Card last used date.
        misuse_date (str): Last misused date of the card.
        temperature (str): Hot-list status
        driver_name (str): Driver name of the card. Note- While ordering card,
            optional when VRN is passed else mandatory.
        vrn (str): Vehicle registration number of the card. Note- While
            ordering card, optional when DriverName is passed else mandatory.
        emboss_text (str): Text printed on the card as account name.
        card_group_id (int): Existing Card Group ID, under which the
            replacement card is to be created. Pass “-1” if the replacement
            card should not be assigned to any card group. Optional.  If not
            provided, the replacement card will be created under the same card
            group as the current card. Example- 156
        card_group_name (str): Card group name. Note- 1. While ordering card
            this field is mandatory when IsNewCardGroup is true.
        renewal_date (str): Renewal date of the card. Applicable if
            ReissueSetting is set to True.
        renewed_card_id (int): Renewed card id.
        renewed_card_status_id (int): Renewed card status id.
        renewed_card_status (str): Renewed card status description.
        renewed_card_expiry_date (str): Renewed card expiry date.
        renewed_card_issue_number (int): Renewed card issue number.
        renewed_card_reissue_setting
            (CardDetailsResponseRenewedCardReissueSettingEnum): TODO: type
            description here.
        creation_date (str): Card Creation Date time
        effective_date (str): Effective date for the Card
        last_modified_date (str): Card last modified date
        bundle_id (str): Bundle Id associated with card in the Gateway. This
            field will have a null value if the card is not associated with
            any bundle in Gateway or the value of IncludeBundleDetails in
            request is false.
        card_delivery_address (CardDeliveryAddress): TODO: type description
            here.
        pin_delivery_address (PINDeliveryAddress): TODO: type description
            here.
        card_block_schedules
            (List[CardDetailsResponseCardBlockSchedulesItemsAllOf0]): TODO:
            type description here.
        error (ErrorStatus): TODO: type description here.
        request_id (str): API Request

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "payer_id": 'PayerId',
        "payer_number": 'PayerNumber',
        "account_id": 'AccountId',
        "account_number": 'AccountNumber',
        "account_short_name": 'AccountShortName',
        "col_co_country_code": 'ColCoCountryCode',
        "local_currency_code": 'LocalCurrencyCode',
        "local_currency_symbol": 'LocalCurrencySymbol',
        "card_id": 'CardId',
        "pan": 'PAN',
        "status_id": 'StatusId',
        "status": 'Status',
        "odometer_prompt": 'OdometerPrompt',
        "fleet_id_prompt": 'FleetIdPrompt',
        "pin_type": 'PINType',
        "has_pin": 'HasPIN',
        "is_self_selected_pin": 'IsSelfSelectedPIN',
        "temporary_block_allowed": 'TemporaryBlockAllowed',
        "unblock_allowed": 'UnblockAllowed',
        "permanent_block_allowed": 'PermanentBlockAllowed',
        "issue_number": 'IssueNumber',
        "reissue_setting": 'ReissueSetting',
        "international_pos_language_id": 'InternationalPOSLanguageID',
        "international_pos_language_code": 'InternationalPOSLanguageCode',
        "local_pos_language_id": 'LocalPOSLanguageID',
        "local_pos_language_code": 'LocalPOSLanguageCode',
        "card_type_code": 'CardTypeCode',
        "card_type_id": 'CardTypeId',
        "card_type_name": 'CardTypeName',
        "token_type_id": 'TokenTypeId',
        "token_type_name": 'TokenTypeName',
        "is_chip_card": 'IsChipCard',
        "is_mag_strip_card": 'IsMagStripCard',
        "is_virtual_card": 'IsVirtualCard',
        "purchase_category_code": 'PurchaseCategoryCode',
        "purchase_category_id": 'PurchaseCategoryId',
        "purchase_category_name": 'PurchaseCategoryName',
        "is_crt": 'IsCRT',
        "is_fleet": 'IsFleet',
        "is_international": 'IsInternational',
        "is_national": 'IsNational',
        "is_partner_sites_included": 'IsPartnerSitesIncluded',
        "is_shell_sites_only": 'IsShellSitesOnly',
        "fuel_sets": 'FuelSets',
        "non_fuel_sets": 'NonFuelSets',
        "issued_date": 'IssuedDate',
        "expiry_date": 'ExpiryDate',
        "last_used_date": 'LastUsedDate',
        "misuse_date": 'MisuseDate',
        "temperature": 'Temperature',
        "driver_name": 'DriverName',
        "vrn": 'VRN',
        "emboss_text": 'EmbossText',
        "card_group_id": 'CardGroupId',
        "card_group_name": 'CardGroupName',
        "renewal_date": 'RenewalDate',
        "renewed_card_id": 'RenewedCardId',
        "renewed_card_status_id": 'RenewedCardStatusId',
        "renewed_card_status": 'RenewedCardStatus',
        "renewed_card_expiry_date": 'RenewedCardExpiryDate',
        "renewed_card_issue_number": 'RenewedCardIssueNumber',
        "renewed_card_reissue_setting": 'RenewedCardReissueSetting',
        "creation_date": 'CreationDate',
        "effective_date": 'EffectiveDate',
        "last_modified_date": 'LastModifiedDate',
        "bundle_id": 'BundleId',
        "card_delivery_address": 'CardDeliveryAddress',
        "pin_delivery_address": 'PINDeliveryAddress',
        "card_block_schedules": 'CardBlockSchedules',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'payer_id',
        'payer_number',
        'account_id',
        'account_number',
        'account_short_name',
        'col_co_country_code',
        'local_currency_code',
        'local_currency_symbol',
        'card_id',
        'pan',
        'status_id',
        'status',
        'odometer_prompt',
        'fleet_id_prompt',
        'pin_type',
        'has_pin',
        'is_self_selected_pin',
        'temporary_block_allowed',
        'unblock_allowed',
        'permanent_block_allowed',
        'issue_number',
        'reissue_setting',
        'international_pos_language_id',
        'international_pos_language_code',
        'local_pos_language_id',
        'local_pos_language_code',
        'card_type_code',
        'card_type_id',
        'card_type_name',
        'token_type_id',
        'token_type_name',
        'is_chip_card',
        'is_mag_strip_card',
        'is_virtual_card',
        'purchase_category_code',
        'purchase_category_id',
        'purchase_category_name',
        'is_crt',
        'is_fleet',
        'is_international',
        'is_national',
        'is_partner_sites_included',
        'is_shell_sites_only',
        'fuel_sets',
        'non_fuel_sets',
        'issued_date',
        'expiry_date',
        'last_used_date',
        'misuse_date',
        'temperature',
        'driver_name',
        'vrn',
        'emboss_text',
        'card_group_id',
        'card_group_name',
        'renewal_date',
        'renewed_card_id',
        'renewed_card_status_id',
        'renewed_card_status',
        'renewed_card_expiry_date',
        'renewed_card_issue_number',
        'renewed_card_reissue_setting',
        'creation_date',
        'effective_date',
        'last_modified_date',
        'bundle_id',
        'card_delivery_address',
        'pin_delivery_address',
        'card_block_schedules',
        'error',
        'request_id',
    ]

    _nullables = [
        'payer_id',
        'payer_number',
        'account_id',
        'account_number',
        'account_short_name',
        'col_co_country_code',
        'local_currency_code',
        'local_currency_symbol',
        'pan',
        'card_type_code',
        'card_type_id',
        'card_type_name',
        'token_type_id',
        'token_type_name',
        'purchase_category_code',
        'purchase_category_name',
        'issued_date',
        'last_used_date',
        'misuse_date',
        'temperature',
        'card_group_id',
        'card_group_name',
        'renewal_date',
        'renewed_card_id',
        'renewed_card_status_id',
        'renewed_card_issue_number',
        'creation_date',
        'effective_date',
        'last_modified_date',
        'bundle_id',
        'card_block_schedules',
    ]

    def __init__(self,
                 payer_id=APIHelper.SKIP,
                 payer_number=APIHelper.SKIP,
                 account_id=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_short_name=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 local_currency_code=APIHelper.SKIP,
                 local_currency_symbol=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 status_id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 odometer_prompt=APIHelper.SKIP,
                 fleet_id_prompt=APIHelper.SKIP,
                 pin_type=APIHelper.SKIP,
                 has_pin=APIHelper.SKIP,
                 is_self_selected_pin=APIHelper.SKIP,
                 temporary_block_allowed=APIHelper.SKIP,
                 unblock_allowed=APIHelper.SKIP,
                 permanent_block_allowed=APIHelper.SKIP,
                 issue_number=APIHelper.SKIP,
                 reissue_setting=APIHelper.SKIP,
                 international_pos_language_id=APIHelper.SKIP,
                 international_pos_language_code=APIHelper.SKIP,
                 local_pos_language_id=APIHelper.SKIP,
                 local_pos_language_code=APIHelper.SKIP,
                 card_type_code=APIHelper.SKIP,
                 card_type_id=APIHelper.SKIP,
                 card_type_name=APIHelper.SKIP,
                 token_type_id=APIHelper.SKIP,
                 token_type_name=APIHelper.SKIP,
                 is_chip_card=APIHelper.SKIP,
                 is_mag_strip_card=APIHelper.SKIP,
                 is_virtual_card=APIHelper.SKIP,
                 purchase_category_code=APIHelper.SKIP,
                 purchase_category_id=APIHelper.SKIP,
                 purchase_category_name=APIHelper.SKIP,
                 is_crt=APIHelper.SKIP,
                 is_fleet=APIHelper.SKIP,
                 is_international=APIHelper.SKIP,
                 is_national=APIHelper.SKIP,
                 is_partner_sites_included=APIHelper.SKIP,
                 is_shell_sites_only=APIHelper.SKIP,
                 fuel_sets=APIHelper.SKIP,
                 non_fuel_sets=APIHelper.SKIP,
                 issued_date=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP,
                 last_used_date=APIHelper.SKIP,
                 misuse_date=APIHelper.SKIP,
                 temperature=APIHelper.SKIP,
                 driver_name=APIHelper.SKIP,
                 vrn=APIHelper.SKIP,
                 emboss_text=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 renewal_date=APIHelper.SKIP,
                 renewed_card_id=APIHelper.SKIP,
                 renewed_card_status_id=APIHelper.SKIP,
                 renewed_card_status=APIHelper.SKIP,
                 renewed_card_expiry_date=APIHelper.SKIP,
                 renewed_card_issue_number=APIHelper.SKIP,
                 renewed_card_reissue_setting=APIHelper.SKIP,
                 creation_date=APIHelper.SKIP,
                 effective_date=APIHelper.SKIP,
                 last_modified_date=APIHelper.SKIP,
                 bundle_id=APIHelper.SKIP,
                 card_delivery_address=APIHelper.SKIP,
                 pin_delivery_address=APIHelper.SKIP,
                 card_block_schedules=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the CardDetailsResponse class"""

        # Initialize members of the class
        if payer_id is not APIHelper.SKIP:
            self.payer_id = payer_id 
        if payer_number is not APIHelper.SKIP:
            self.payer_number = payer_number 
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_short_name is not APIHelper.SKIP:
            self.account_short_name = account_short_name 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if local_currency_code is not APIHelper.SKIP:
            self.local_currency_code = local_currency_code 
        if local_currency_symbol is not APIHelper.SKIP:
            self.local_currency_symbol = local_currency_symbol 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if status_id is not APIHelper.SKIP:
            self.status_id = status_id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if odometer_prompt is not APIHelper.SKIP:
            self.odometer_prompt = odometer_prompt 
        if fleet_id_prompt is not APIHelper.SKIP:
            self.fleet_id_prompt = fleet_id_prompt 
        if pin_type is not APIHelper.SKIP:
            self.pin_type = pin_type 
        if has_pin is not APIHelper.SKIP:
            self.has_pin = has_pin 
        if is_self_selected_pin is not APIHelper.SKIP:
            self.is_self_selected_pin = is_self_selected_pin 
        if temporary_block_allowed is not APIHelper.SKIP:
            self.temporary_block_allowed = temporary_block_allowed 
        if unblock_allowed is not APIHelper.SKIP:
            self.unblock_allowed = unblock_allowed 
        if permanent_block_allowed is not APIHelper.SKIP:
            self.permanent_block_allowed = permanent_block_allowed 
        if issue_number is not APIHelper.SKIP:
            self.issue_number = issue_number 
        if reissue_setting is not APIHelper.SKIP:
            self.reissue_setting = reissue_setting 
        if international_pos_language_id is not APIHelper.SKIP:
            self.international_pos_language_id = international_pos_language_id 
        if international_pos_language_code is not APIHelper.SKIP:
            self.international_pos_language_code = international_pos_language_code 
        if local_pos_language_id is not APIHelper.SKIP:
            self.local_pos_language_id = local_pos_language_id 
        if local_pos_language_code is not APIHelper.SKIP:
            self.local_pos_language_code = local_pos_language_code 
        if card_type_code is not APIHelper.SKIP:
            self.card_type_code = card_type_code 
        if card_type_id is not APIHelper.SKIP:
            self.card_type_id = card_type_id 
        if card_type_name is not APIHelper.SKIP:
            self.card_type_name = card_type_name 
        if token_type_id is not APIHelper.SKIP:
            self.token_type_id = token_type_id 
        if token_type_name is not APIHelper.SKIP:
            self.token_type_name = token_type_name 
        if is_chip_card is not APIHelper.SKIP:
            self.is_chip_card = is_chip_card 
        if is_mag_strip_card is not APIHelper.SKIP:
            self.is_mag_strip_card = is_mag_strip_card 
        if is_virtual_card is not APIHelper.SKIP:
            self.is_virtual_card = is_virtual_card 
        if purchase_category_code is not APIHelper.SKIP:
            self.purchase_category_code = purchase_category_code 
        if purchase_category_id is not APIHelper.SKIP:
            self.purchase_category_id = purchase_category_id 
        if purchase_category_name is not APIHelper.SKIP:
            self.purchase_category_name = purchase_category_name 
        if is_crt is not APIHelper.SKIP:
            self.is_crt = is_crt 
        if is_fleet is not APIHelper.SKIP:
            self.is_fleet = is_fleet 
        if is_international is not APIHelper.SKIP:
            self.is_international = is_international 
        if is_national is not APIHelper.SKIP:
            self.is_national = is_national 
        if is_partner_sites_included is not APIHelper.SKIP:
            self.is_partner_sites_included = is_partner_sites_included 
        if is_shell_sites_only is not APIHelper.SKIP:
            self.is_shell_sites_only = is_shell_sites_only 
        if fuel_sets is not APIHelper.SKIP:
            self.fuel_sets = fuel_sets 
        if non_fuel_sets is not APIHelper.SKIP:
            self.non_fuel_sets = non_fuel_sets 
        if issued_date is not APIHelper.SKIP:
            self.issued_date = issued_date 
        if expiry_date is not APIHelper.SKIP:
            self.expiry_date = expiry_date 
        if last_used_date is not APIHelper.SKIP:
            self.last_used_date = last_used_date 
        if misuse_date is not APIHelper.SKIP:
            self.misuse_date = misuse_date 
        if temperature is not APIHelper.SKIP:
            self.temperature = temperature 
        if driver_name is not APIHelper.SKIP:
            self.driver_name = driver_name 
        if vrn is not APIHelper.SKIP:
            self.vrn = vrn 
        if emboss_text is not APIHelper.SKIP:
            self.emboss_text = emboss_text 
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if renewal_date is not APIHelper.SKIP:
            self.renewal_date = renewal_date 
        if renewed_card_id is not APIHelper.SKIP:
            self.renewed_card_id = renewed_card_id 
        if renewed_card_status_id is not APIHelper.SKIP:
            self.renewed_card_status_id = renewed_card_status_id 
        if renewed_card_status is not APIHelper.SKIP:
            self.renewed_card_status = renewed_card_status 
        if renewed_card_expiry_date is not APIHelper.SKIP:
            self.renewed_card_expiry_date = renewed_card_expiry_date 
        if renewed_card_issue_number is not APIHelper.SKIP:
            self.renewed_card_issue_number = renewed_card_issue_number 
        if renewed_card_reissue_setting is not APIHelper.SKIP:
            self.renewed_card_reissue_setting = renewed_card_reissue_setting 
        if creation_date is not APIHelper.SKIP:
            self.creation_date = creation_date 
        if effective_date is not APIHelper.SKIP:
            self.effective_date = effective_date 
        if last_modified_date is not APIHelper.SKIP:
            self.last_modified_date = last_modified_date 
        if bundle_id is not APIHelper.SKIP:
            self.bundle_id = bundle_id 
        if card_delivery_address is not APIHelper.SKIP:
            self.card_delivery_address = card_delivery_address 
        if pin_delivery_address is not APIHelper.SKIP:
            self.pin_delivery_address = pin_delivery_address 
        if card_block_schedules is not APIHelper.SKIP:
            self.card_block_schedules = card_block_schedules 
        if error is not APIHelper.SKIP:
            self.error = error 
        if request_id is not APIHelper.SKIP:
            self.request_id = request_id 

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
        payer_id = dictionary.get("PayerId") if "PayerId" in dictionary.keys() else APIHelper.SKIP
        payer_number = dictionary.get("PayerNumber") if "PayerNumber" in dictionary.keys() else APIHelper.SKIP
        account_id = dictionary.get("AccountId") if "AccountId" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_short_name = dictionary.get("AccountShortName") if "AccountShortName" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        local_currency_code = dictionary.get("LocalCurrencyCode") if "LocalCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        local_currency_symbol = dictionary.get("LocalCurrencySymbol") if "LocalCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if dictionary.get("CardId") else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        status_id = dictionary.get("StatusId") if dictionary.get("StatusId") else APIHelper.SKIP
        status = dictionary.get("Status") if dictionary.get("Status") else APIHelper.SKIP
        odometer_prompt = dictionary.get("OdometerPrompt") if "OdometerPrompt" in dictionary.keys() else APIHelper.SKIP
        fleet_id_prompt = dictionary.get("FleetIdPrompt") if "FleetIdPrompt" in dictionary.keys() else APIHelper.SKIP
        pin_type = dictionary.get("PINType") if dictionary.get("PINType") else APIHelper.SKIP
        has_pin = dictionary.get("HasPIN") if "HasPIN" in dictionary.keys() else APIHelper.SKIP
        is_self_selected_pin = dictionary.get("IsSelfSelectedPIN") if "IsSelfSelectedPIN" in dictionary.keys() else APIHelper.SKIP
        temporary_block_allowed = dictionary.get("TemporaryBlockAllowed") if "TemporaryBlockAllowed" in dictionary.keys() else APIHelper.SKIP
        unblock_allowed = dictionary.get("UnblockAllowed") if "UnblockAllowed" in dictionary.keys() else APIHelper.SKIP
        permanent_block_allowed = dictionary.get("PermanentBlockAllowed") if "PermanentBlockAllowed" in dictionary.keys() else APIHelper.SKIP
        issue_number = dictionary.get("IssueNumber") if dictionary.get("IssueNumber") else APIHelper.SKIP
        reissue_setting = dictionary.get("ReissueSetting") if dictionary.get("ReissueSetting") else APIHelper.SKIP
        international_pos_language_id = dictionary.get("InternationalPOSLanguageID") if dictionary.get("InternationalPOSLanguageID") else APIHelper.SKIP
        international_pos_language_code = dictionary.get("InternationalPOSLanguageCode") if dictionary.get("InternationalPOSLanguageCode") else APIHelper.SKIP
        local_pos_language_id = dictionary.get("LocalPOSLanguageID") if dictionary.get("LocalPOSLanguageID") else APIHelper.SKIP
        local_pos_language_code = dictionary.get("LocalPOSLanguageCode") if dictionary.get("LocalPOSLanguageCode") else APIHelper.SKIP
        card_type_code = dictionary.get("CardTypeCode") if "CardTypeCode" in dictionary.keys() else APIHelper.SKIP
        card_type_id = dictionary.get("CardTypeId") if "CardTypeId" in dictionary.keys() else APIHelper.SKIP
        card_type_name = dictionary.get("CardTypeName") if "CardTypeName" in dictionary.keys() else APIHelper.SKIP
        token_type_id = dictionary.get("TokenTypeId") if "TokenTypeId" in dictionary.keys() else APIHelper.SKIP
        token_type_name = dictionary.get("TokenTypeName") if "TokenTypeName" in dictionary.keys() else APIHelper.SKIP
        is_chip_card = dictionary.get("IsChipCard") if "IsChipCard" in dictionary.keys() else APIHelper.SKIP
        is_mag_strip_card = dictionary.get("IsMagStripCard") if "IsMagStripCard" in dictionary.keys() else APIHelper.SKIP
        is_virtual_card = dictionary.get("IsVirtualCard") if "IsVirtualCard" in dictionary.keys() else APIHelper.SKIP
        purchase_category_code = dictionary.get("PurchaseCategoryCode") if "PurchaseCategoryCode" in dictionary.keys() else APIHelper.SKIP
        purchase_category_id = dictionary.get("PurchaseCategoryId") if dictionary.get("PurchaseCategoryId") else APIHelper.SKIP
        purchase_category_name = dictionary.get("PurchaseCategoryName") if "PurchaseCategoryName" in dictionary.keys() else APIHelper.SKIP
        is_crt = dictionary.get("IsCRT") if "IsCRT" in dictionary.keys() else APIHelper.SKIP
        is_fleet = dictionary.get("IsFleet") if "IsFleet" in dictionary.keys() else APIHelper.SKIP
        is_international = dictionary.get("IsInternational") if "IsInternational" in dictionary.keys() else APIHelper.SKIP
        is_national = dictionary.get("IsNational") if "IsNational" in dictionary.keys() else APIHelper.SKIP
        is_partner_sites_included = dictionary.get("IsPartnerSitesIncluded") if "IsPartnerSitesIncluded" in dictionary.keys() else APIHelper.SKIP
        is_shell_sites_only = dictionary.get("IsShellSitesOnly") if "IsShellSitesOnly" in dictionary.keys() else APIHelper.SKIP
        fuel_sets = None
        if dictionary.get('FuelSets') is not None:
            fuel_sets = [CardDetailsResponseFuelSetsItems.from_dictionary(x) for x in dictionary.get('FuelSets')]
        else:
            fuel_sets = APIHelper.SKIP
        non_fuel_sets = None
        if dictionary.get('NonFuelSets') is not None:
            non_fuel_sets = [CardDetailsResponseNonFuelSetsItems.from_dictionary(x) for x in dictionary.get('NonFuelSets')]
        else:
            non_fuel_sets = APIHelper.SKIP
        issued_date = dictionary.get("IssuedDate") if "IssuedDate" in dictionary.keys() else APIHelper.SKIP
        expiry_date = dictionary.get("ExpiryDate") if dictionary.get("ExpiryDate") else APIHelper.SKIP
        last_used_date = dictionary.get("LastUsedDate") if "LastUsedDate" in dictionary.keys() else APIHelper.SKIP
        misuse_date = dictionary.get("MisuseDate") if "MisuseDate" in dictionary.keys() else APIHelper.SKIP
        temperature = dictionary.get("Temperature") if "Temperature" in dictionary.keys() else APIHelper.SKIP
        driver_name = dictionary.get("DriverName") if dictionary.get("DriverName") else APIHelper.SKIP
        vrn = dictionary.get("VRN") if dictionary.get("VRN") else APIHelper.SKIP
        emboss_text = dictionary.get("EmbossText") if dictionary.get("EmbossText") else APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if "CardGroupId" in dictionary.keys() else APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if "CardGroupName" in dictionary.keys() else APIHelper.SKIP
        renewal_date = dictionary.get("RenewalDate") if "RenewalDate" in dictionary.keys() else APIHelper.SKIP
        renewed_card_id = dictionary.get("RenewedCardId") if "RenewedCardId" in dictionary.keys() else APIHelper.SKIP
        renewed_card_status_id = dictionary.get("RenewedCardStatusId") if "RenewedCardStatusId" in dictionary.keys() else APIHelper.SKIP
        renewed_card_status = dictionary.get("RenewedCardStatus") if dictionary.get("RenewedCardStatus") else APIHelper.SKIP
        renewed_card_expiry_date = dictionary.get("RenewedCardExpiryDate") if dictionary.get("RenewedCardExpiryDate") else APIHelper.SKIP
        renewed_card_issue_number = dictionary.get("RenewedCardIssueNumber") if "RenewedCardIssueNumber" in dictionary.keys() else APIHelper.SKIP
        renewed_card_reissue_setting = dictionary.get("RenewedCardReissueSetting") if dictionary.get("RenewedCardReissueSetting") else APIHelper.SKIP
        creation_date = dictionary.get("CreationDate") if "CreationDate" in dictionary.keys() else APIHelper.SKIP
        effective_date = dictionary.get("EffectiveDate") if "EffectiveDate" in dictionary.keys() else APIHelper.SKIP
        last_modified_date = dictionary.get("LastModifiedDate") if "LastModifiedDate" in dictionary.keys() else APIHelper.SKIP
        bundle_id = dictionary.get("BundleId") if "BundleId" in dictionary.keys() else APIHelper.SKIP
        card_delivery_address = CardDeliveryAddress.from_dictionary(dictionary.get('CardDeliveryAddress')) if 'CardDeliveryAddress' in dictionary.keys() else APIHelper.SKIP
        pin_delivery_address = PINDeliveryAddress.from_dictionary(dictionary.get('PINDeliveryAddress')) if 'PINDeliveryAddress' in dictionary.keys() else APIHelper.SKIP
        if 'CardBlockSchedules' in dictionary.keys():
            card_block_schedules = [CardDetailsResponseCardBlockSchedulesItemsAllOf0.from_dictionary(x) for x in dictionary.get('CardBlockSchedules')] if dictionary.get('CardBlockSchedules') else None
        else:
            card_block_schedules = APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(payer_id,
                   payer_number,
                   account_id,
                   account_number,
                   account_short_name,
                   col_co_country_code,
                   local_currency_code,
                   local_currency_symbol,
                   card_id,
                   pan,
                   status_id,
                   status,
                   odometer_prompt,
                   fleet_id_prompt,
                   pin_type,
                   has_pin,
                   is_self_selected_pin,
                   temporary_block_allowed,
                   unblock_allowed,
                   permanent_block_allowed,
                   issue_number,
                   reissue_setting,
                   international_pos_language_id,
                   international_pos_language_code,
                   local_pos_language_id,
                   local_pos_language_code,
                   card_type_code,
                   card_type_id,
                   card_type_name,
                   token_type_id,
                   token_type_name,
                   is_chip_card,
                   is_mag_strip_card,
                   is_virtual_card,
                   purchase_category_code,
                   purchase_category_id,
                   purchase_category_name,
                   is_crt,
                   is_fleet,
                   is_international,
                   is_national,
                   is_partner_sites_included,
                   is_shell_sites_only,
                   fuel_sets,
                   non_fuel_sets,
                   issued_date,
                   expiry_date,
                   last_used_date,
                   misuse_date,
                   temperature,
                   driver_name,
                   vrn,
                   emboss_text,
                   card_group_id,
                   card_group_name,
                   renewal_date,
                   renewed_card_id,
                   renewed_card_status_id,
                   renewed_card_status,
                   renewed_card_expiry_date,
                   renewed_card_issue_number,
                   renewed_card_reissue_setting,
                   creation_date,
                   effective_date,
                   last_modified_date,
                   bundle_id,
                   card_delivery_address,
                   pin_delivery_address,
                   card_block_schedules,
                   error,
                   request_id)
