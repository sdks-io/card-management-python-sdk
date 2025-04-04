# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class ReplaceCardSettings(object):

    """Implementation of the 'ReplaceCardSettings' model.

    Request entity object for ReplaceCardSettings

    Attributes:
        self_selected_encrypted_pin (str): The encrypted value of
            self-selected PIN.<br /> Optional – When not provided, the PIN
            will be auto generated(if the card token type supports PIN) and
            delivered based on the given PIN delivery option.<br /> Max
            Length: 256
        self_selected_pin_key_id (str): KeyId of the PIN encrypted value.<br
            /> Mandatory, if opted for self-selected PIN else optional.<br />
            Max Length: 30
        self_selected_pin_session_key (str): Encoded message of the TCS form
            which is used for encrypting the PIN of this card.<br /> The
            encode message forms are provided to clients by another API
            (“TCS”).<br /> Instructions to encrypt the PIN is covered in the
            related API specifications document.<br /> Mandatory –If opted for
            self-selected PIN else optional. Max Length: 1024
        validate_fleet_id (bool): True/False.<br /> Optional <br /> Default:
            False<br /> For cards ordered with Validate Fleet Id parameter set
            to true, CFGW will be notified to enable this validation for the
            card.<br /> Note: When “FleetIdInputRequired” is not set on the
            card, validate fleet id will be considered false regardless of the
            value passed on this parameter.
        card_group_id (int): Existing Card Group ID, under which the
            replacement card is to be created.<br /> Pass “-1” if the
            replacement card should not be assigned to any card group.<br />
            Optional <br /> If not provided, the replacement card will be
            created under the same card group as the current card.
        card_delivery_type (int): Card delivery type.<br /> Mandatory <br />
            Allowed Value: <br /> 1.    Customer Address(Default) <br /> 2.   
            New Delivery Address <br /> 3.    Old Card Address
        delivery_contact_title (str): Title of the contact person. <br />
            Optional<br /> Max field length: 10
        delivery_contact_name (str): Name of the contact person <br />
            Mandatory - If CardDeliveryType  is 2 and OrderCardReplacement is
            passed as true.<br /> Max field length: 50
        delivery_company_name (str): Company name <br /> Mandatory - If
            CardDeliveryType  is 2 and OrderCardReplacement is passed as true.
            Max field length: 50
        delivery_address_line_1 (str): Address line 1 <br /> Mandatory - If
            CardDeliveryType  is 2 and OrderCardReplacement is passed as
            true.<br /> Max field length: 40
        delivery_address_line_2 (str): Address line 2 <br /> Optional <br />
            Max field length: 40
        delivery_address_line_3 (str): Address line 3 <br /> Optional<br />
            Max field length: 40
        delivery_zip_code (str): ZIP code <br /> Mandatory - If
            CardDeliveryType  is 2 and OrderCardReplacement is passed as
            true.<br /> Max field length: 10
        delivery_city (str): City  <br /> Mandatory - If CardDeliveryType  is
            2 and OrderCardReplacement is passed as true.<br /> Max field
            length: 40
        delivery_region_id (int): Region Id  <br /> Optional
        delivery_region (str): Region  <br /> Optional<br /> When region is
            passed
        delivery_country (str): The ISO code of the country.<br /> Mandatory -
            If CardDeliveryType  is 2 and OrderCardReplacement is passed as
            true
        delivery_country_id (int): The countryId of gicen country.<br />
        phone_number (str): Phone number for to send SMS. <br /> Optional<br
            /> Max field length: 20
        email_address (str): Email address for to send email.<br /> Mandatory
            if PINAdviceType is email else optional.<br /> Max field length: 90
        pin_delivery_address_type (int): PIN delivery address type
            selection.<br /> Optional<br /> Allowed Values:<br /> 1.   
            Customer Address(Default)<br /> 2.    Card Address<br /> 3.    New
            Delivery Address
        pin_advice_type (int): PIN delivery method.<br /> Mandatory when
            OrderReplacement Is true.<br /> Allowed Values:<br /> 1.   
            Paper<br /> 2.    Email<br /> 3.    SMS<br /> 4.    None
        pin_delivery_contact_title (str): Title of the contact person.<br />
            Optional <br /> Max field length: 10
        pin_delivery_contact_name (str): Name of the contact person.<br />
            Mandatory - If PINAdviceType is paper else optional.<br /> Max
            field length: 50
        pin_delivery_company_name (str): Company name.<br /> Mandatory - If
            PINAdviceType is paper else optional.<br /> Max field length: 50
        pin_delivery_address_line_1 (str): Address line 1.<br /> Mandatory -
            If PINAdviceType is paper else optional.<br /> Max field length: 40
        pin_delivery_address_line_2 (str): Address line 2.<br /> Optional <br
            /> Max field length: 40
        pin_delivery_address_line_3 (str): Address line 3.<br /> Optional <br
            /> Max field length: 40
        pin_delivery_zip_code (str): ZIP code.<br /> Mandatory - if
            PINAdviceType is paper else optional. <br /> Max field length: 10
        pin_delivery_city (str): City.<br /> Mandatory - If PINAdviceType is
            paper else optional. <br /> Max field length: 40
        pin_delivery_region_id (int): Region Id.<br /> Optional
        pin_delivery_region (str): Region.<br /> When region is passed
        pin_delivery_country (str): The ISO code of the country.<br />
            Mappings for ISO code <br /> Mandatory if PINAdviceType is paper
            else optional.
        pin_delivery_country_id (int): The countryId of the country.<br />
            Mappings for ISO code<br /> This is not an input parameter.
        pin_phone_number (str): Phone number for to send SMS of the PIN in
            case PINAdviceType is SMS.<br /> Mandatory if PINAdviceType is SMS
            else optional.<br /> Max field length: 20
        pin_email_address (str): Email address for to send email of the PIN in
            case PINAdviceType is Email.<br /> Mandatory if PINAdviceType is
            email else optional.<br /> Max field length: 90
        save_for_pin_reminder (bool): The given address will be used for
            sending PIN reminders in future when requested.<br />  PIN Advice
            type should be Paper   Optional
        save_for_card_reissue (bool): If this is specified, the contact
            address will be saved in cards platform for card reissue
            processing.<br /> Optional
        expiry_date (str): Expiry Date for newly created card to be update in
            cards plot form.<br />  Optional <br />  Format: MMyy <br /> 
            Eg:1221 <br />  If not apply the default Expiry Date.<br /> 
            Note:<br />  There is a limit to the ExpiryDate which the user can
            choose for the Card.   If the user chooses a later ExpiryDate than
            the allowed value for the CardType of the OU,   the background
            service logs the respective error code and description

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "card_delivery_type": 'CardDeliveryType',
        "self_selected_encrypted_pin": 'SelfSelectedEncryptedPIN',
        "self_selected_pin_key_id": 'SelfSelectedPINKeyID',
        "self_selected_pin_session_key": 'SelfSelectedPINSessionKey',
        "validate_fleet_id": 'ValidateFleetId',
        "card_group_id": 'CardGroupId',
        "delivery_contact_title": 'DeliveryContactTitle',
        "delivery_contact_name": 'DeliveryContactName',
        "delivery_company_name": 'DeliveryCompanyName',
        "delivery_address_line_1": 'DeliveryAddressLine1',
        "delivery_address_line_2": 'DeliveryAddressLine2',
        "delivery_address_line_3": 'DeliveryAddressLine3',
        "delivery_zip_code": 'DeliveryZipCode',
        "delivery_city": 'DeliveryCity',
        "delivery_region_id": 'DeliveryRegionId',
        "delivery_region": 'DeliveryRegion',
        "delivery_country": 'DeliveryCountry',
        "delivery_country_id": 'DeliveryCountryId',
        "phone_number": 'PhoneNumber',
        "email_address": 'EmailAddress',
        "pin_delivery_address_type": 'PINDeliveryAddressType',
        "pin_advice_type": 'PINAdviceType',
        "pin_delivery_contact_title": 'PINDeliveryContactTitle',
        "pin_delivery_contact_name": 'PINDeliveryContactName',
        "pin_delivery_company_name": 'PINDeliveryCompanyName',
        "pin_delivery_address_line_1": 'PINDeliveryAddressLine1',
        "pin_delivery_address_line_2": 'PINDeliveryAddressLine2',
        "pin_delivery_address_line_3": 'PINDeliveryAddressLine3',
        "pin_delivery_zip_code": 'PINDeliveryZipCode',
        "pin_delivery_city": 'PINDeliveryCity',
        "pin_delivery_region_id": 'PINDeliveryRegionId',
        "pin_delivery_region": 'PINDeliveryRegion',
        "pin_delivery_country": 'PINDeliveryCountry',
        "pin_delivery_country_id": 'PINDeliveryCountryId',
        "pin_phone_number": 'PINPhoneNumber',
        "pin_email_address": 'PINEmailAddress',
        "save_for_pin_reminder": 'SaveForPINReminder',
        "save_for_card_reissue": 'SaveForCardReissue',
        "expiry_date": 'ExpiryDate'
    }

    _optionals = [
        'self_selected_encrypted_pin',
        'self_selected_pin_key_id',
        'self_selected_pin_session_key',
        'validate_fleet_id',
        'card_group_id',
        'delivery_contact_title',
        'delivery_contact_name',
        'delivery_company_name',
        'delivery_address_line_1',
        'delivery_address_line_2',
        'delivery_address_line_3',
        'delivery_zip_code',
        'delivery_city',
        'delivery_region_id',
        'delivery_region',
        'delivery_country',
        'delivery_country_id',
        'phone_number',
        'email_address',
        'pin_delivery_address_type',
        'pin_advice_type',
        'pin_delivery_contact_title',
        'pin_delivery_contact_name',
        'pin_delivery_company_name',
        'pin_delivery_address_line_1',
        'pin_delivery_address_line_2',
        'pin_delivery_address_line_3',
        'pin_delivery_zip_code',
        'pin_delivery_city',
        'pin_delivery_region_id',
        'pin_delivery_region',
        'pin_delivery_country',
        'pin_delivery_country_id',
        'pin_phone_number',
        'pin_email_address',
        'save_for_pin_reminder',
        'save_for_card_reissue',
        'expiry_date',
    ]

    _nullables = [
        'self_selected_encrypted_pin',
        'self_selected_pin_key_id',
        'self_selected_pin_session_key',
        'card_group_id',
        'card_delivery_type',
        'delivery_contact_title',
        'delivery_contact_name',
        'delivery_company_name',
        'delivery_address_line_1',
        'delivery_address_line_2',
        'delivery_address_line_3',
        'delivery_zip_code',
        'delivery_city',
        'delivery_region_id',
        'delivery_region',
        'delivery_country',
        'delivery_country_id',
        'email_address',
        'pin_delivery_address_type',
        'pin_advice_type',
        'pin_delivery_contact_title',
        'pin_delivery_contact_name',
        'pin_delivery_company_name',
        'pin_delivery_address_line_1',
        'pin_delivery_address_line_2',
        'pin_delivery_address_line_3',
        'pin_delivery_zip_code',
        'pin_delivery_city',
        'pin_delivery_region_id',
        'pin_delivery_region',
        'pin_delivery_country',
        'pin_delivery_country_id',
        'pin_phone_number',
        'pin_email_address',
        'expiry_date',
    ]

    def __init__(self,
                 card_delivery_type=None,
                 self_selected_encrypted_pin=APIHelper.SKIP,
                 self_selected_pin_key_id=APIHelper.SKIP,
                 self_selected_pin_session_key=APIHelper.SKIP,
                 validate_fleet_id=APIHelper.SKIP,
                 card_group_id=APIHelper.SKIP,
                 delivery_contact_title=APIHelper.SKIP,
                 delivery_contact_name=APIHelper.SKIP,
                 delivery_company_name=APIHelper.SKIP,
                 delivery_address_line_1=APIHelper.SKIP,
                 delivery_address_line_2=APIHelper.SKIP,
                 delivery_address_line_3=APIHelper.SKIP,
                 delivery_zip_code=APIHelper.SKIP,
                 delivery_city=APIHelper.SKIP,
                 delivery_region_id=APIHelper.SKIP,
                 delivery_region=APIHelper.SKIP,
                 delivery_country=APIHelper.SKIP,
                 delivery_country_id=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 pin_delivery_address_type=APIHelper.SKIP,
                 pin_advice_type=APIHelper.SKIP,
                 pin_delivery_contact_title=APIHelper.SKIP,
                 pin_delivery_contact_name=APIHelper.SKIP,
                 pin_delivery_company_name=APIHelper.SKIP,
                 pin_delivery_address_line_1=APIHelper.SKIP,
                 pin_delivery_address_line_2=APIHelper.SKIP,
                 pin_delivery_address_line_3=APIHelper.SKIP,
                 pin_delivery_zip_code=APIHelper.SKIP,
                 pin_delivery_city=APIHelper.SKIP,
                 pin_delivery_region_id=APIHelper.SKIP,
                 pin_delivery_region=APIHelper.SKIP,
                 pin_delivery_country=APIHelper.SKIP,
                 pin_delivery_country_id=APIHelper.SKIP,
                 pin_phone_number=APIHelper.SKIP,
                 pin_email_address=APIHelper.SKIP,
                 save_for_pin_reminder=APIHelper.SKIP,
                 save_for_card_reissue=APIHelper.SKIP,
                 expiry_date=APIHelper.SKIP):
        """Constructor for the ReplaceCardSettings class"""

        # Initialize members of the class
        if self_selected_encrypted_pin is not APIHelper.SKIP:
            self.self_selected_encrypted_pin = self_selected_encrypted_pin 
        if self_selected_pin_key_id is not APIHelper.SKIP:
            self.self_selected_pin_key_id = self_selected_pin_key_id 
        if self_selected_pin_session_key is not APIHelper.SKIP:
            self.self_selected_pin_session_key = self_selected_pin_session_key 
        if validate_fleet_id is not APIHelper.SKIP:
            self.validate_fleet_id = validate_fleet_id 
        if card_group_id is not APIHelper.SKIP:
            self.card_group_id = card_group_id 
        self.card_delivery_type = card_delivery_type 
        if delivery_contact_title is not APIHelper.SKIP:
            self.delivery_contact_title = delivery_contact_title 
        if delivery_contact_name is not APIHelper.SKIP:
            self.delivery_contact_name = delivery_contact_name 
        if delivery_company_name is not APIHelper.SKIP:
            self.delivery_company_name = delivery_company_name 
        if delivery_address_line_1 is not APIHelper.SKIP:
            self.delivery_address_line_1 = delivery_address_line_1 
        if delivery_address_line_2 is not APIHelper.SKIP:
            self.delivery_address_line_2 = delivery_address_line_2 
        if delivery_address_line_3 is not APIHelper.SKIP:
            self.delivery_address_line_3 = delivery_address_line_3 
        if delivery_zip_code is not APIHelper.SKIP:
            self.delivery_zip_code = delivery_zip_code 
        if delivery_city is not APIHelper.SKIP:
            self.delivery_city = delivery_city 
        if delivery_region_id is not APIHelper.SKIP:
            self.delivery_region_id = delivery_region_id 
        if delivery_region is not APIHelper.SKIP:
            self.delivery_region = delivery_region 
        if delivery_country is not APIHelper.SKIP:
            self.delivery_country = delivery_country 
        if delivery_country_id is not APIHelper.SKIP:
            self.delivery_country_id = delivery_country_id 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if pin_delivery_address_type is not APIHelper.SKIP:
            self.pin_delivery_address_type = pin_delivery_address_type 
        if pin_advice_type is not APIHelper.SKIP:
            self.pin_advice_type = pin_advice_type 
        if pin_delivery_contact_title is not APIHelper.SKIP:
            self.pin_delivery_contact_title = pin_delivery_contact_title 
        if pin_delivery_contact_name is not APIHelper.SKIP:
            self.pin_delivery_contact_name = pin_delivery_contact_name 
        if pin_delivery_company_name is not APIHelper.SKIP:
            self.pin_delivery_company_name = pin_delivery_company_name 
        if pin_delivery_address_line_1 is not APIHelper.SKIP:
            self.pin_delivery_address_line_1 = pin_delivery_address_line_1 
        if pin_delivery_address_line_2 is not APIHelper.SKIP:
            self.pin_delivery_address_line_2 = pin_delivery_address_line_2 
        if pin_delivery_address_line_3 is not APIHelper.SKIP:
            self.pin_delivery_address_line_3 = pin_delivery_address_line_3 
        if pin_delivery_zip_code is not APIHelper.SKIP:
            self.pin_delivery_zip_code = pin_delivery_zip_code 
        if pin_delivery_city is not APIHelper.SKIP:
            self.pin_delivery_city = pin_delivery_city 
        if pin_delivery_region_id is not APIHelper.SKIP:
            self.pin_delivery_region_id = pin_delivery_region_id 
        if pin_delivery_region is not APIHelper.SKIP:
            self.pin_delivery_region = pin_delivery_region 
        if pin_delivery_country is not APIHelper.SKIP:
            self.pin_delivery_country = pin_delivery_country 
        if pin_delivery_country_id is not APIHelper.SKIP:
            self.pin_delivery_country_id = pin_delivery_country_id 
        if pin_phone_number is not APIHelper.SKIP:
            self.pin_phone_number = pin_phone_number 
        if pin_email_address is not APIHelper.SKIP:
            self.pin_email_address = pin_email_address 
        if save_for_pin_reminder is not APIHelper.SKIP:
            self.save_for_pin_reminder = save_for_pin_reminder 
        if save_for_card_reissue is not APIHelper.SKIP:
            self.save_for_card_reissue = save_for_card_reissue 
        if expiry_date is not APIHelper.SKIP:
            self.expiry_date = expiry_date 

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
        card_delivery_type = dictionary.get("CardDeliveryType") if dictionary.get("CardDeliveryType") else None
        self_selected_encrypted_pin = dictionary.get("SelfSelectedEncryptedPIN") if "SelfSelectedEncryptedPIN" in dictionary.keys() else APIHelper.SKIP
        self_selected_pin_key_id = dictionary.get("SelfSelectedPINKeyID") if "SelfSelectedPINKeyID" in dictionary.keys() else APIHelper.SKIP
        self_selected_pin_session_key = dictionary.get("SelfSelectedPINSessionKey") if "SelfSelectedPINSessionKey" in dictionary.keys() else APIHelper.SKIP
        validate_fleet_id = dictionary.get("ValidateFleetId") if "ValidateFleetId" in dictionary.keys() else APIHelper.SKIP
        card_group_id = dictionary.get("CardGroupId") if "CardGroupId" in dictionary.keys() else APIHelper.SKIP
        delivery_contact_title = dictionary.get("DeliveryContactTitle") if "DeliveryContactTitle" in dictionary.keys() else APIHelper.SKIP
        delivery_contact_name = dictionary.get("DeliveryContactName") if "DeliveryContactName" in dictionary.keys() else APIHelper.SKIP
        delivery_company_name = dictionary.get("DeliveryCompanyName") if "DeliveryCompanyName" in dictionary.keys() else APIHelper.SKIP
        delivery_address_line_1 = dictionary.get("DeliveryAddressLine1") if "DeliveryAddressLine1" in dictionary.keys() else APIHelper.SKIP
        delivery_address_line_2 = dictionary.get("DeliveryAddressLine2") if "DeliveryAddressLine2" in dictionary.keys() else APIHelper.SKIP
        delivery_address_line_3 = dictionary.get("DeliveryAddressLine3") if "DeliveryAddressLine3" in dictionary.keys() else APIHelper.SKIP
        delivery_zip_code = dictionary.get("DeliveryZipCode") if "DeliveryZipCode" in dictionary.keys() else APIHelper.SKIP
        delivery_city = dictionary.get("DeliveryCity") if "DeliveryCity" in dictionary.keys() else APIHelper.SKIP
        delivery_region_id = dictionary.get("DeliveryRegionId") if "DeliveryRegionId" in dictionary.keys() else APIHelper.SKIP
        delivery_region = dictionary.get("DeliveryRegion") if "DeliveryRegion" in dictionary.keys() else APIHelper.SKIP
        delivery_country = dictionary.get("DeliveryCountry") if "DeliveryCountry" in dictionary.keys() else APIHelper.SKIP
        delivery_country_id = dictionary.get("DeliveryCountryId") if "DeliveryCountryId" in dictionary.keys() else APIHelper.SKIP
        phone_number = dictionary.get("PhoneNumber") if dictionary.get("PhoneNumber") else APIHelper.SKIP
        email_address = dictionary.get("EmailAddress") if "EmailAddress" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_address_type = dictionary.get("PINDeliveryAddressType") if "PINDeliveryAddressType" in dictionary.keys() else APIHelper.SKIP
        pin_advice_type = dictionary.get("PINAdviceType") if "PINAdviceType" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_contact_title = dictionary.get("PINDeliveryContactTitle") if "PINDeliveryContactTitle" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_contact_name = dictionary.get("PINDeliveryContactName") if "PINDeliveryContactName" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_company_name = dictionary.get("PINDeliveryCompanyName") if "PINDeliveryCompanyName" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_address_line_1 = dictionary.get("PINDeliveryAddressLine1") if "PINDeliveryAddressLine1" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_address_line_2 = dictionary.get("PINDeliveryAddressLine2") if "PINDeliveryAddressLine2" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_address_line_3 = dictionary.get("PINDeliveryAddressLine3") if "PINDeliveryAddressLine3" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_zip_code = dictionary.get("PINDeliveryZipCode") if "PINDeliveryZipCode" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_city = dictionary.get("PINDeliveryCity") if "PINDeliveryCity" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_region_id = dictionary.get("PINDeliveryRegionId") if "PINDeliveryRegionId" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_region = dictionary.get("PINDeliveryRegion") if "PINDeliveryRegion" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_country = dictionary.get("PINDeliveryCountry") if "PINDeliveryCountry" in dictionary.keys() else APIHelper.SKIP
        pin_delivery_country_id = dictionary.get("PINDeliveryCountryId") if "PINDeliveryCountryId" in dictionary.keys() else APIHelper.SKIP
        pin_phone_number = dictionary.get("PINPhoneNumber") if "PINPhoneNumber" in dictionary.keys() else APIHelper.SKIP
        pin_email_address = dictionary.get("PINEmailAddress") if "PINEmailAddress" in dictionary.keys() else APIHelper.SKIP
        save_for_pin_reminder = dictionary.get("SaveForPINReminder") if "SaveForPINReminder" in dictionary.keys() else APIHelper.SKIP
        save_for_card_reissue = dictionary.get("SaveForCardReissue") if "SaveForCardReissue" in dictionary.keys() else APIHelper.SKIP
        expiry_date = dictionary.get("ExpiryDate") if "ExpiryDate" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(card_delivery_type,
                   self_selected_encrypted_pin,
                   self_selected_pin_key_id,
                   self_selected_pin_session_key,
                   validate_fleet_id,
                   card_group_id,
                   delivery_contact_title,
                   delivery_contact_name,
                   delivery_company_name,
                   delivery_address_line_1,
                   delivery_address_line_2,
                   delivery_address_line_3,
                   delivery_zip_code,
                   delivery_city,
                   delivery_region_id,
                   delivery_region,
                   delivery_country,
                   delivery_country_id,
                   phone_number,
                   email_address,
                   pin_delivery_address_type,
                   pin_advice_type,
                   pin_delivery_contact_title,
                   pin_delivery_contact_name,
                   pin_delivery_company_name,
                   pin_delivery_address_line_1,
                   pin_delivery_address_line_2,
                   pin_delivery_address_line_3,
                   pin_delivery_zip_code,
                   pin_delivery_city,
                   pin_delivery_region_id,
                   pin_delivery_region,
                   pin_delivery_country,
                   pin_delivery_country_id,
                   pin_phone_number,
                   pin_email_address,
                   save_for_pin_reminder,
                   save_for_card_reissue,
                   expiry_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'self_selected_encrypted_pin={(self.self_selected_encrypted_pin if hasattr(self, "self_selected_encrypted_pin") else None)!r}, '
                f'self_selected_pin_key_id={(self.self_selected_pin_key_id if hasattr(self, "self_selected_pin_key_id") else None)!r}, '
                f'self_selected_pin_session_key={(self.self_selected_pin_session_key if hasattr(self, "self_selected_pin_session_key") else None)!r}, '
                f'validate_fleet_id={(self.validate_fleet_id if hasattr(self, "validate_fleet_id") else None)!r}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!r}, '
                f'card_delivery_type={self.card_delivery_type!r}, '
                f'delivery_contact_title={(self.delivery_contact_title if hasattr(self, "delivery_contact_title") else None)!r}, '
                f'delivery_contact_name={(self.delivery_contact_name if hasattr(self, "delivery_contact_name") else None)!r}, '
                f'delivery_company_name={(self.delivery_company_name if hasattr(self, "delivery_company_name") else None)!r}, '
                f'delivery_address_line_1={(self.delivery_address_line_1 if hasattr(self, "delivery_address_line_1") else None)!r}, '
                f'delivery_address_line_2={(self.delivery_address_line_2 if hasattr(self, "delivery_address_line_2") else None)!r}, '
                f'delivery_address_line_3={(self.delivery_address_line_3 if hasattr(self, "delivery_address_line_3") else None)!r}, '
                f'delivery_zip_code={(self.delivery_zip_code if hasattr(self, "delivery_zip_code") else None)!r}, '
                f'delivery_city={(self.delivery_city if hasattr(self, "delivery_city") else None)!r}, '
                f'delivery_region_id={(self.delivery_region_id if hasattr(self, "delivery_region_id") else None)!r}, '
                f'delivery_region={(self.delivery_region if hasattr(self, "delivery_region") else None)!r}, '
                f'delivery_country={(self.delivery_country if hasattr(self, "delivery_country") else None)!r}, '
                f'delivery_country_id={(self.delivery_country_id if hasattr(self, "delivery_country_id") else None)!r}, '
                f'phone_number={(self.phone_number if hasattr(self, "phone_number") else None)!r}, '
                f'email_address={(self.email_address if hasattr(self, "email_address") else None)!r}, '
                f'pin_delivery_address_type={(self.pin_delivery_address_type if hasattr(self, "pin_delivery_address_type") else None)!r}, '
                f'pin_advice_type={(self.pin_advice_type if hasattr(self, "pin_advice_type") else None)!r}, '
                f'pin_delivery_contact_title={(self.pin_delivery_contact_title if hasattr(self, "pin_delivery_contact_title") else None)!r}, '
                f'pin_delivery_contact_name={(self.pin_delivery_contact_name if hasattr(self, "pin_delivery_contact_name") else None)!r}, '
                f'pin_delivery_company_name={(self.pin_delivery_company_name if hasattr(self, "pin_delivery_company_name") else None)!r}, '
                f'pin_delivery_address_line_1={(self.pin_delivery_address_line_1 if hasattr(self, "pin_delivery_address_line_1") else None)!r}, '
                f'pin_delivery_address_line_2={(self.pin_delivery_address_line_2 if hasattr(self, "pin_delivery_address_line_2") else None)!r}, '
                f'pin_delivery_address_line_3={(self.pin_delivery_address_line_3 if hasattr(self, "pin_delivery_address_line_3") else None)!r}, '
                f'pin_delivery_zip_code={(self.pin_delivery_zip_code if hasattr(self, "pin_delivery_zip_code") else None)!r}, '
                f'pin_delivery_city={(self.pin_delivery_city if hasattr(self, "pin_delivery_city") else None)!r}, '
                f'pin_delivery_region_id={(self.pin_delivery_region_id if hasattr(self, "pin_delivery_region_id") else None)!r}, '
                f'pin_delivery_region={(self.pin_delivery_region if hasattr(self, "pin_delivery_region") else None)!r}, '
                f'pin_delivery_country={(self.pin_delivery_country if hasattr(self, "pin_delivery_country") else None)!r}, '
                f'pin_delivery_country_id={(self.pin_delivery_country_id if hasattr(self, "pin_delivery_country_id") else None)!r}, '
                f'pin_phone_number={(self.pin_phone_number if hasattr(self, "pin_phone_number") else None)!r}, '
                f'pin_email_address={(self.pin_email_address if hasattr(self, "pin_email_address") else None)!r}, '
                f'save_for_pin_reminder={(self.save_for_pin_reminder if hasattr(self, "save_for_pin_reminder") else None)!r}, '
                f'save_for_card_reissue={(self.save_for_card_reissue if hasattr(self, "save_for_card_reissue") else None)!r}, '
                f'expiry_date={(self.expiry_date if hasattr(self, "expiry_date") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'self_selected_encrypted_pin={(self.self_selected_encrypted_pin if hasattr(self, "self_selected_encrypted_pin") else None)!s}, '
                f'self_selected_pin_key_id={(self.self_selected_pin_key_id if hasattr(self, "self_selected_pin_key_id") else None)!s}, '
                f'self_selected_pin_session_key={(self.self_selected_pin_session_key if hasattr(self, "self_selected_pin_session_key") else None)!s}, '
                f'validate_fleet_id={(self.validate_fleet_id if hasattr(self, "validate_fleet_id") else None)!s}, '
                f'card_group_id={(self.card_group_id if hasattr(self, "card_group_id") else None)!s}, '
                f'card_delivery_type={self.card_delivery_type!s}, '
                f'delivery_contact_title={(self.delivery_contact_title if hasattr(self, "delivery_contact_title") else None)!s}, '
                f'delivery_contact_name={(self.delivery_contact_name if hasattr(self, "delivery_contact_name") else None)!s}, '
                f'delivery_company_name={(self.delivery_company_name if hasattr(self, "delivery_company_name") else None)!s}, '
                f'delivery_address_line_1={(self.delivery_address_line_1 if hasattr(self, "delivery_address_line_1") else None)!s}, '
                f'delivery_address_line_2={(self.delivery_address_line_2 if hasattr(self, "delivery_address_line_2") else None)!s}, '
                f'delivery_address_line_3={(self.delivery_address_line_3 if hasattr(self, "delivery_address_line_3") else None)!s}, '
                f'delivery_zip_code={(self.delivery_zip_code if hasattr(self, "delivery_zip_code") else None)!s}, '
                f'delivery_city={(self.delivery_city if hasattr(self, "delivery_city") else None)!s}, '
                f'delivery_region_id={(self.delivery_region_id if hasattr(self, "delivery_region_id") else None)!s}, '
                f'delivery_region={(self.delivery_region if hasattr(self, "delivery_region") else None)!s}, '
                f'delivery_country={(self.delivery_country if hasattr(self, "delivery_country") else None)!s}, '
                f'delivery_country_id={(self.delivery_country_id if hasattr(self, "delivery_country_id") else None)!s}, '
                f'phone_number={(self.phone_number if hasattr(self, "phone_number") else None)!s}, '
                f'email_address={(self.email_address if hasattr(self, "email_address") else None)!s}, '
                f'pin_delivery_address_type={(self.pin_delivery_address_type if hasattr(self, "pin_delivery_address_type") else None)!s}, '
                f'pin_advice_type={(self.pin_advice_type if hasattr(self, "pin_advice_type") else None)!s}, '
                f'pin_delivery_contact_title={(self.pin_delivery_contact_title if hasattr(self, "pin_delivery_contact_title") else None)!s}, '
                f'pin_delivery_contact_name={(self.pin_delivery_contact_name if hasattr(self, "pin_delivery_contact_name") else None)!s}, '
                f'pin_delivery_company_name={(self.pin_delivery_company_name if hasattr(self, "pin_delivery_company_name") else None)!s}, '
                f'pin_delivery_address_line_1={(self.pin_delivery_address_line_1 if hasattr(self, "pin_delivery_address_line_1") else None)!s}, '
                f'pin_delivery_address_line_2={(self.pin_delivery_address_line_2 if hasattr(self, "pin_delivery_address_line_2") else None)!s}, '
                f'pin_delivery_address_line_3={(self.pin_delivery_address_line_3 if hasattr(self, "pin_delivery_address_line_3") else None)!s}, '
                f'pin_delivery_zip_code={(self.pin_delivery_zip_code if hasattr(self, "pin_delivery_zip_code") else None)!s}, '
                f'pin_delivery_city={(self.pin_delivery_city if hasattr(self, "pin_delivery_city") else None)!s}, '
                f'pin_delivery_region_id={(self.pin_delivery_region_id if hasattr(self, "pin_delivery_region_id") else None)!s}, '
                f'pin_delivery_region={(self.pin_delivery_region if hasattr(self, "pin_delivery_region") else None)!s}, '
                f'pin_delivery_country={(self.pin_delivery_country if hasattr(self, "pin_delivery_country") else None)!s}, '
                f'pin_delivery_country_id={(self.pin_delivery_country_id if hasattr(self, "pin_delivery_country_id") else None)!s}, '
                f'pin_phone_number={(self.pin_phone_number if hasattr(self, "pin_phone_number") else None)!s}, '
                f'pin_email_address={(self.pin_email_address if hasattr(self, "pin_email_address") else None)!s}, '
                f'save_for_pin_reminder={(self.save_for_pin_reminder if hasattr(self, "save_for_pin_reminder") else None)!s}, '
                f'save_for_card_reissue={(self.save_for_card_reissue if hasattr(self, "save_for_card_reissue") else None)!s}, '
                f'expiry_date={(self.expiry_date if hasattr(self, "expiry_date") else None)!s})')
