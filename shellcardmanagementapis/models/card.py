# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.card_block_schedule import CardBlockSchedule


class Card(object):

    """Implementation of the 'Card' model.

    TODO: type model description here.

    Attributes:
        account_id (int): Account ID
        account_name (str): Account Name
        account_number (str): Account Number
        account_short_name (str): Account Short Name
        bundle_id (str): Bundle Id associated with card in the Gateway.<br /> 
            This field will have null value if the card is not associated with
            any bundle in Gateway or the value of IncludeBundleDetails in
            request is false.
        card_block_schedules (List[CardBlockSchedule]): List of Scheduled Card
            Blocks details<br /> Entity: CardBlockSchedule
        card_group_id (int): Card group ID
        card_group_name (str): Card group name
        card_id (int): Unique Card Id
        card_type_code (str): ISO code of the card i.e. first 7 digits of the
            PAN
        card_type_id (int): Card Type ID Example Id and Description: 1
            -Philippines CRT 7077861 2-Philippines<br /> Fleet 7002861 5-SHELL
            FLEET-HONG KONG 7002821 6-SHELL NHF- HONG KONG 7002821 7-SHELL
            CRT- HONG KONG 7077821
        card_type_name (str): Card Type Name Example Id and Description:
            1-Philippines CRT 7077861 2-Philippines <br /> Fleet 7002861
            5-SHELL FLEET- HONG KONG 7002821 6-SHELL NHF- HONG KONG 7002821
            7-SHELL  CRT- HONG KONG 7077821
        col_co_country_code (str): The 2 character ISO Code for the customer
            and card owning country. <br /> If default card type is not set
            then the first two alphabets of the account ID is returned.
        creation_date (str): Card Creation datetime.<br /> Format: yyyyMMdd
            HH:mm:ss<br /> Note: Clients to convert this to appropriate
            DateTime type.
        driver_name (str): Driver name
        effective_date (str): Effective date for the Card<br /> Format:
            yyyyMMdd<br /> Note: Clients to convert this to appropriate
            DateTime type.
        expiry_date (str): Expiry date of the card.<br /> Format: yyyyMMdd<br
            /> Note: Clients to convert this to appropriate DateTime type.
        fleet_id_input (bool): True/False True if fleet id input is enabled,
            else false
        is_crt (bool): True/False True if it is a CRT type card, else false
        is_fleet (bool): True/False True if it is a Fleet type card, else
            false
        is_international (bool): True/False True if it is an international
            card, else false
        is_national (bool): True/False True if it is a national card, else
            false
        is_partner_sites_included (bool): True/False True if it is allowed at
            all partner sites, else false
        is_shell_sites_only (bool): True/False True if it is only allowed at
            Shell sites, else false
        issue_date (str): Issue date<br /> Format: yyyyMMdd<br /> Note:
            Clients to convert this to appropriate DateTime type.
        is_superseded (bool): True/False True if a new card is issued with the
            same PAN, else false.
        is_virtual_card (bool): True/False True if it is a virtual card, else
            false
        last_modified_date (str): Card last modified date and time<br />
            Format: yyyyMMdd HH:mm:ss<br /> Note: Clients to convert this to
            appropriate DateTime type.
        last_used_date (str): Card last used date .<br /> Note: last used date
            of a card will be calculated based on billed/unbilled sales items 
            of a given card.The query that extracts the last used dates will
            be applied on the        subset of the cards being returned to the
            client.Unbilled sales items is checked        first and for those
            not found in the unbilled table, sales items will be checked      
            (only when the last used date is not found in unbilled table for
            at least a single        card from the result). The transactions
            in last 48 hours are not expected to be  Therefore this field
            gives the correct information up to 48 hours early.<br /> Format:
            yyyyMMdd HH:mm:ss<br /> Note: Clients to convert this to
            appropriate DateTime type
        local_currency_code (str): ISO code of the local currency. <br />
        local_currency_symbol (str): Local currency symbol. <br />
        odometer_input (bool): True/False True if odometer input is enabled on
            the card, else false
        pan (str): Card PAN
        masked_pan (str): Card PAN Mask PAN (Mask all digits except the Last 6
            digits of the PAN)
        panid (float): Card PAN ID.
        purchase_category_code (str): Purchase category code
        purchase_category_id (int): Purchase category Id <br /> Note: Not
            Purchase code.
        purchase_category_name (str): Purchase category name
        reason (str): Card Status reason Example: Lost Stolen Card no longer
            required
        reissue_setting (str): Reissue setting of the card. If the card is
            superseded (i.e. a replacement/new card is issued) then reissue
            setting of the latest card issued. <br /> Values<br /> •True –Card
            will be Reissued when nearing its expiry date <br /> •False –Card
            will not be Reissued
        status_description (str): Status Description (Active, Temporarily
            Blocked, etc.,)<br /> Possible Ids and description: 1 Active 7
            Blocked Card 8 Expired 9 Cancelled 10 New 23 Pending Renewal 31
            Replaced 41<br /> Temporary Block(Customer) 42 Temporary
            Block(Shell) 43 Fraud 101 Active(Block in progress)<br /> * 102
            Blocked Card(Unblock in progress) <br /> * 103 Active(Cancel in
            progress) <br /> * 104 Active(Marked as damaged)<br /> * 105
            New(Cancel in progress) <br /> * 106 { Status}(Scheduled for
            block)<br /> * 107 { Status}(Scheduled for unblock) <br /> *#
            Note: Items marked with* are intermediate statuses  to indicate
            that there are pending requests in progress.<br /> The response
            can contain these intermediate statuses only if the<br />
            IncludeIntermediateStatus flag is true. The placeholder { Status}
            in the items<br /> marked with # will be replaced with the  status
            description. E.g., Active (Scheduled for block)
        status_id (int): Card Status id Possible Ids and description: 1 Active
            7 Blocked Card 8 Expired 9 Cancelled 10 New 23 Pending Renewal 31
            Replaced 41 Temporary Block(Customer) 42 <br /> Temporary
            Block(Shell) 43 Fraud 101 Active(Block in progress) <br /> * 102
            Blocked Card(Unblock in progress)<br /> * 103 Active(Cancel in
            progress) <br /> * 104 Active(Marked as damaged) <br /> * 105
            New(Cancel in progress)<br /> * 106 { Status}(Scheduled for block)
            <br /> # 107 {Status}(Scheduled for unblock)<br /> *# Note: Items
            marked with* are intermediate statuses to indicate that there are
            pending requests in progress.<br /> The response can contain these
            intermediate statuses only if the IncludeIntermediateStatus flag
            is true.<br /> The placeholder { Status} in the items marked with
            # will be replaced with<br /> the status description. E.g., Active
            (Scheduled for block)
        token_type_id (int): Token Type ID configured for the Card E.g. 107
        token_type_name (str): Token Type Name configured for the Card
        vrn (str): Vehicle registration number
        client_reference_id (str): Customer reference number of the card.
        is_emv_contact (bool): Is Europay, MasterCard, and Visa Contact
            enabled or not.
        is_emv_contactless (bool): Is Europay, MasterCard, and Visa
            Contactless enabled or not.
        is_rfid (bool): Whether the card type is enabled for RFID (Radio
            Frequency Identification)
        rfiduid (str): RFIDUID
        emaid (str): EMAID
        ev_printed_number (str): EV Printed Number
        card_media_code (str): Card Media Code.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_id": 'AccountId',
        "account_name": 'AccountName',
        "account_number": 'AccountNumber',
        "account_short_name": 'AccountShortName',
        "bundle_id": 'BundleId',
        "card_block_schedules": 'CardBlockSchedules',
        "card_group_id": 'CardGroupId',
        "card_group_name": 'CardGroupName',
        "card_id": 'CardId',
        "card_type_code": 'CardTypeCode',
        "card_type_id": 'CardTypeId',
        "card_type_name": 'CardTypeName',
        "col_co_country_code": 'ColCoCountryCode',
        "creation_date": 'CreationDate',
        "driver_name": 'DriverName',
        "effective_date": 'EffectiveDate',
        "expiry_date": 'ExpiryDate',
        "fleet_id_input": 'FleetIdInput',
        "is_crt": 'IsCRT',
        "is_fleet": 'IsFleet',
        "is_international": 'IsInternational',
        "is_national": 'IsNational',
        "is_partner_sites_included": 'IsPartnerSitesIncluded',
        "is_shell_sites_only": 'IsShellSitesOnly',
        "issue_date": 'IssueDate',
        "is_superseded": 'IsSuperseded',
        "is_virtual_card": 'IsVirtualCard',
        "last_modified_date": 'LastModifiedDate',
        "last_used_date": 'LastUsedDate',
        "local_currency_code": 'LocalCurrencyCode',
        "local_currency_symbol": 'LocalCurrencySymbol',
        "odometer_input": 'OdometerInput',
        "pan": 'PAN',
        "masked_pan": 'MaskedPAN',
        "panid": 'PANID',
        "purchase_category_code": 'PurchaseCategoryCode',
        "purchase_category_id": 'PurchaseCategoryId',
        "purchase_category_name": 'PurchaseCategoryName',
        "reason": 'Reason',
        "reissue_setting": 'ReissueSetting',
        "status_description": 'StatusDescription',
        "status_id": 'StatusId',
        "token_type_id": 'TokenTypeID',
        "token_type_name": 'TokenTypeName',
        "vrn": 'VRN',
        "client_reference_id": 'ClientReferenceId',
        "is_emv_contact": 'IsEMVContact',
        "is_emv_contactless": 'IsEMVContactless',
        "is_rfid": 'IsRFID',
        "rfiduid": 'RFIDUID',
        "emaid": 'EMAID',
        "ev_printed_number": 'EVPrintedNumber',
        "card_media_code": 'CardMediaCode'
    }

    _optionals = [
        'account_id',
        'account_name',
        'account_number',
        'account_short_name',
        'bundle_id',
        'card_block_schedules',
        'card_group_id',
        'card_group_name',
        'card_id',
        'card_type_code',
        'card_type_id',
        'card_type_name',
        'col_co_country_code',
        'creation_date',
        'driver_name',
        'effective_date',
        'expiry_date',
        'fleet_id_input',
        'is_crt',
        'is_fleet',
        'is_international',
        'is_national',
        'is_partner_sites_included',
        'is_shell_sites_only',
        'issue_date',
        'is_superseded',
        'is_virtual_card',
        'last_modified_date',
        'last_used_date',
        'local_currency_code',
        'local_currency_symbol',
        'odometer_input',
        'pan',
        'masked_pan',
        'panid',
        'purchase_category_code',
        'purchase_category_id',
        'purchase_category_name',
        'reason',
        'reissue_setting',
        'status_description',
        'status_id',
        'token_type_id',
        'token_type_name',
        'vrn',
        'client_reference_id',
        'is_emv_contact',
        'is_emv_contactless',
        'is_rfid',
        'rfiduid',
        'emaid',
        'ev_printed_number',
        'card_media_code',
    ]

    _nullables = [
        'account_id',
        'account_name',
        'account_number',
        'account_short_name',
        'bundle_id',
        'card_group_id',
        'card_group_name',
        'card_id',
        'card_type_code',
        'card_type_id',
        'card_type_name',
        'col_co_country_code',
        'creation_date',
        'driver_name',
        'effective_date',
        'expiry_date',
        'issue_date',
        'last_modified_date',
        'last_used_date',
        'local_currency_code',
        'local_currency_symbol',
        'pan',
        'purchase_category_code',
        'purchase_category_id',
        'purchase_category_name',
        'reason',
        'reissue_setting',
        'status_description',
        'status_id',
        'token_type_id',
        'vrn',
        'client_reference_id',
        'rfiduid',
        'emaid',
        'ev_printed_number',
        'card_media_code',
    ]

    def __init__(self,
                 account_id=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 account_number=APIHelper.SKIP,
                 account_short_name=APIHelper.SKIP,
                 bundle_id=APIHelper.SKIP,
                 card_block_schedules=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 card_group_name=APIHelper.SKIP,
                 card_id=APIHelper.SKIP,
                 card_type_code=APIHelper.SKIP,
                 card_type_id=APIHelper.SKIP,
                 card_type_name=APIHelper.SKIP,
                 col_co_country_code=APIHelper.SKIP,
                 creation_date=APIHelper.SKIP,
                 driver_name=APIHelper.SKIP,
                 effective_date=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP,
                 fleet_id_input=APIHelper.SKIP,
                 is_crt=APIHelper.SKIP,
                 is_fleet=APIHelper.SKIP,
                 is_international=APIHelper.SKIP,
                 is_national=APIHelper.SKIP,
                 is_partner_sites_included=APIHelper.SKIP,
                 is_shell_sites_only=APIHelper.SKIP,
                 issue_date=APIHelper.SKIP,
                 is_superseded=APIHelper.SKIP,
                 is_virtual_card=APIHelper.SKIP,
                 last_modified_date=APIHelper.SKIP,
                 last_used_date=APIHelper.SKIP,
                 local_currency_code=APIHelper.SKIP,
                 local_currency_symbol=APIHelper.SKIP,
                 odometer_input=APIHelper.SKIP,
                 pan=APIHelper.SKIP,
                 masked_pan=APIHelper.SKIP,
                 panid=APIHelper.SKIP,
                 purchase_category_code=APIHelper.SKIP,
                 purchase_category_id=APIHelper.SKIP,
                 purchase_category_name=APIHelper.SKIP,
                 reason=APIHelper.SKIP,
                 reissue_setting=APIHelper.SKIP,
                 status_description=APIHelper.SKIP,
                 status_id=APIHelper.SKIP,
                 token_type_id=APIHelper.SKIP,
                 token_type_name=APIHelper.SKIP,
                 vrn=APIHelper.SKIP,
                 client_reference_id=APIHelper.SKIP,
                 is_emv_contact=APIHelper.SKIP,
                 is_emv_contactless=APIHelper.SKIP,
                 is_rfid=APIHelper.SKIP,
                 rfiduid=APIHelper.SKIP,
                 emaid=APIHelper.SKIP,
                 ev_printed_number=APIHelper.SKIP,
                 card_media_code=APIHelper.SKIP):
        """Constructor for the Card class"""

        # Initialize members of the class
        if account_id is not APIHelper.SKIP:
            self.account_id = account_id 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number 
        if account_short_name is not APIHelper.SKIP:
            self.account_short_name = account_short_name 
        if bundle_id is not APIHelper.SKIP:
            self.bundle_id = bundle_id 
        if card_block_schedules is not APIHelper.SKIP:
            self.card_block_schedules = card_block_schedules 
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        if card_group_name is not APIHelper.SKIP:
            self.card_group_name = card_group_name 
        if card_id is not APIHelper.SKIP:
            self.card_id = card_id 
        if card_type_code is not APIHelper.SKIP:
            self.card_type_code = card_type_code 
        if card_type_id is not APIHelper.SKIP:
            self.card_type_id = card_type_id 
        if card_type_name is not APIHelper.SKIP:
            self.card_type_name = card_type_name 
        if col_co_country_code is not APIHelper.SKIP:
            self.col_co_country_code = col_co_country_code 
        if creation_date is not APIHelper.SKIP:
            self.creation_date = creation_date 
        if driver_name is not APIHelper.SKIP:
            self.driver_name = driver_name 
        if effective_date is not APIHelper.SKIP:
            self.effective_date = effective_date 
        if expiry_date is not APIHelper.SKIP:
            self.expiry_date = expiry_date 
        if fleet_id_input is not APIHelper.SKIP:
            self.fleet_id_input = fleet_id_input 
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
        if issue_date is not APIHelper.SKIP:
            self.issue_date = issue_date 
        if is_superseded is not APIHelper.SKIP:
            self.is_superseded = is_superseded 
        if is_virtual_card is not APIHelper.SKIP:
            self.is_virtual_card = is_virtual_card 
        if last_modified_date is not APIHelper.SKIP:
            self.last_modified_date = last_modified_date 
        if last_used_date is not APIHelper.SKIP:
            self.last_used_date = last_used_date 
        if local_currency_code is not APIHelper.SKIP:
            self.local_currency_code = local_currency_code 
        if local_currency_symbol is not APIHelper.SKIP:
            self.local_currency_symbol = local_currency_symbol 
        if odometer_input is not APIHelper.SKIP:
            self.odometer_input = odometer_input 
        if pan is not APIHelper.SKIP:
            self.pan = pan 
        if masked_pan is not APIHelper.SKIP:
            self.masked_pan = masked_pan 
        if panid is not APIHelper.SKIP:
            self.panid = panid 
        if purchase_category_code is not APIHelper.SKIP:
            self.purchase_category_code = purchase_category_code 
        if purchase_category_id is not APIHelper.SKIP:
            self.purchase_category_id = purchase_category_id 
        if purchase_category_name is not APIHelper.SKIP:
            self.purchase_category_name = purchase_category_name 
        if reason is not APIHelper.SKIP:
            self.reason = reason 
        if reissue_setting is not APIHelper.SKIP:
            self.reissue_setting = reissue_setting 
        if status_description is not APIHelper.SKIP:
            self.status_description = status_description 
        if status_id is not APIHelper.SKIP:
            self.status_id = status_id 
        if token_type_id is not APIHelper.SKIP:
            self.token_type_id = token_type_id 
        if token_type_name is not APIHelper.SKIP:
            self.token_type_name = token_type_name 
        if vrn is not APIHelper.SKIP:
            self.vrn = vrn 
        if client_reference_id is not APIHelper.SKIP:
            self.client_reference_id = client_reference_id 
        if is_emv_contact is not APIHelper.SKIP:
            self.is_emv_contact = is_emv_contact 
        if is_emv_contactless is not APIHelper.SKIP:
            self.is_emv_contactless = is_emv_contactless 
        if is_rfid is not APIHelper.SKIP:
            self.is_rfid = is_rfid 
        if rfiduid is not APIHelper.SKIP:
            self.rfiduid = rfiduid 
        if emaid is not APIHelper.SKIP:
            self.emaid = emaid 
        if ev_printed_number is not APIHelper.SKIP:
            self.ev_printed_number = ev_printed_number 
        if card_media_code is not APIHelper.SKIP:
            self.card_media_code = card_media_code 

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
        account_name = dictionary.get("AccountName") if "AccountName" in dictionary.keys() else APIHelper.SKIP
        account_number = dictionary.get("AccountNumber") if "AccountNumber" in dictionary.keys() else APIHelper.SKIP
        account_short_name = dictionary.get("AccountShortName") if "AccountShortName" in dictionary.keys() else APIHelper.SKIP
        bundle_id = dictionary.get("BundleId") if "BundleId" in dictionary.keys() else APIHelper.SKIP
        card_block_schedules = None
        if dictionary.get('CardBlockSchedules') is not None:
            card_block_schedules = [CardBlockSchedule.from_dictionary(x) for x in dictionary.get('CardBlockSchedules')]
        else:
            card_block_schedules = APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if "CardGroupId" in dictionary.keys() else APIHelper.SKIP
        card_group_name = dictionary.get("CardGroupName") if "CardGroupName" in dictionary.keys() else APIHelper.SKIP
        card_id = dictionary.get("CardId") if "CardId" in dictionary.keys() else APIHelper.SKIP
        card_type_code = dictionary.get("CardTypeCode") if "CardTypeCode" in dictionary.keys() else APIHelper.SKIP
        card_type_id = dictionary.get("CardTypeId") if "CardTypeId" in dictionary.keys() else APIHelper.SKIP
        card_type_name = dictionary.get("CardTypeName") if "CardTypeName" in dictionary.keys() else APIHelper.SKIP
        col_co_country_code = dictionary.get("ColCoCountryCode") if "ColCoCountryCode" in dictionary.keys() else APIHelper.SKIP
        creation_date = dictionary.get("CreationDate") if "CreationDate" in dictionary.keys() else APIHelper.SKIP
        driver_name = dictionary.get("DriverName") if "DriverName" in dictionary.keys() else APIHelper.SKIP
        effective_date = dictionary.get("EffectiveDate") if "EffectiveDate" in dictionary.keys() else APIHelper.SKIP
        expiry_date = dictionary.get("ExpiryDate") if "ExpiryDate" in dictionary.keys() else APIHelper.SKIP
        fleet_id_input = dictionary.get("FleetIdInput") if "FleetIdInput" in dictionary.keys() else APIHelper.SKIP
        is_crt = dictionary.get("IsCRT") if "IsCRT" in dictionary.keys() else APIHelper.SKIP
        is_fleet = dictionary.get("IsFleet") if "IsFleet" in dictionary.keys() else APIHelper.SKIP
        is_international = dictionary.get("IsInternational") if "IsInternational" in dictionary.keys() else APIHelper.SKIP
        is_national = dictionary.get("IsNational") if "IsNational" in dictionary.keys() else APIHelper.SKIP
        is_partner_sites_included = dictionary.get("IsPartnerSitesIncluded") if "IsPartnerSitesIncluded" in dictionary.keys() else APIHelper.SKIP
        is_shell_sites_only = dictionary.get("IsShellSitesOnly") if "IsShellSitesOnly" in dictionary.keys() else APIHelper.SKIP
        issue_date = dictionary.get("IssueDate") if "IssueDate" in dictionary.keys() else APIHelper.SKIP
        is_superseded = dictionary.get("IsSuperseded") if "IsSuperseded" in dictionary.keys() else APIHelper.SKIP
        is_virtual_card = dictionary.get("IsVirtualCard") if "IsVirtualCard" in dictionary.keys() else APIHelper.SKIP
        last_modified_date = dictionary.get("LastModifiedDate") if "LastModifiedDate" in dictionary.keys() else APIHelper.SKIP
        last_used_date = dictionary.get("LastUsedDate") if "LastUsedDate" in dictionary.keys() else APIHelper.SKIP
        local_currency_code = dictionary.get("LocalCurrencyCode") if "LocalCurrencyCode" in dictionary.keys() else APIHelper.SKIP
        local_currency_symbol = dictionary.get("LocalCurrencySymbol") if "LocalCurrencySymbol" in dictionary.keys() else APIHelper.SKIP
        odometer_input = dictionary.get("OdometerInput") if "OdometerInput" in dictionary.keys() else APIHelper.SKIP
        pan = dictionary.get("PAN") if "PAN" in dictionary.keys() else APIHelper.SKIP
        masked_pan = dictionary.get("MaskedPAN") if dictionary.get("MaskedPAN") else APIHelper.SKIP
        panid = dictionary.get("PANID") if dictionary.get("PANID") else APIHelper.SKIP
        purchase_category_code = dictionary.get("PurchaseCategoryCode") if "PurchaseCategoryCode" in dictionary.keys() else APIHelper.SKIP
        purchase_category_id = dictionary.get("PurchaseCategoryId") if "PurchaseCategoryId" in dictionary.keys() else APIHelper.SKIP
        purchase_category_name = dictionary.get("PurchaseCategoryName") if "PurchaseCategoryName" in dictionary.keys() else APIHelper.SKIP
        reason = dictionary.get("Reason") if "Reason" in dictionary.keys() else APIHelper.SKIP
        reissue_setting = dictionary.get("ReissueSetting") if "ReissueSetting" in dictionary.keys() else APIHelper.SKIP
        status_description = dictionary.get("StatusDescription") if "StatusDescription" in dictionary.keys() else APIHelper.SKIP
        status_id = dictionary.get("StatusId") if "StatusId" in dictionary.keys() else APIHelper.SKIP
        token_type_id = dictionary.get("TokenTypeID") if "TokenTypeID" in dictionary.keys() else APIHelper.SKIP
        token_type_name = dictionary.get("TokenTypeName") if dictionary.get("TokenTypeName") else APIHelper.SKIP
        vrn = dictionary.get("VRN") if "VRN" in dictionary.keys() else APIHelper.SKIP
        client_reference_id = dictionary.get("ClientReferenceId") if "ClientReferenceId" in dictionary.keys() else APIHelper.SKIP
        is_emv_contact = dictionary.get("IsEMVContact") if "IsEMVContact" in dictionary.keys() else APIHelper.SKIP
        is_emv_contactless = dictionary.get("IsEMVContactless") if "IsEMVContactless" in dictionary.keys() else APIHelper.SKIP
        is_rfid = dictionary.get("IsRFID") if "IsRFID" in dictionary.keys() else APIHelper.SKIP
        rfiduid = dictionary.get("RFIDUID") if "RFIDUID" in dictionary.keys() else APIHelper.SKIP
        emaid = dictionary.get("EMAID") if "EMAID" in dictionary.keys() else APIHelper.SKIP
        ev_printed_number = dictionary.get("EVPrintedNumber") if "EVPrintedNumber" in dictionary.keys() else APIHelper.SKIP
        card_media_code = dictionary.get("CardMediaCode") if "CardMediaCode" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(account_id,
                   account_name,
                   account_number,
                   account_short_name,
                   bundle_id,
                   card_block_schedules,
                   card_group_id,
                   card_group_name,
                   card_id,
                   card_type_code,
                   card_type_id,
                   card_type_name,
                   col_co_country_code,
                   creation_date,
                   driver_name,
                   effective_date,
                   expiry_date,
                   fleet_id_input,
                   is_crt,
                   is_fleet,
                   is_international,
                   is_national,
                   is_partner_sites_included,
                   is_shell_sites_only,
                   issue_date,
                   is_superseded,
                   is_virtual_card,
                   last_modified_date,
                   last_used_date,
                   local_currency_code,
                   local_currency_symbol,
                   odometer_input,
                   pan,
                   masked_pan,
                   panid,
                   purchase_category_code,
                   purchase_category_id,
                   purchase_category_name,
                   reason,
                   reissue_setting,
                   status_description,
                   status_id,
                   token_type_id,
                   token_type_name,
                   vrn,
                   client_reference_id,
                   is_emv_contact,
                   is_emv_contactless,
                   is_rfid,
                   rfiduid,
                   emaid,
                   ev_printed_number,
                   card_media_code)
