# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class CardDeliveryContact(object):

    """Implementation of the 'CardDeliveryContact' model.

    Request entity object for CardDeliveryContact
    Mandatory when CardDeliveryType is 2 else ignored.

    Attributes:
        delivery_contact_title (str): Title of the contact person <br />
            Optional Max field length: 10
        delivery_contact_name (str): Name of the contact person <br />
            Mandatory  <br /> Max field length: 50
        delivery_company_name (str): Company name <br /> Mandatory  <br /> Max
            field length: 50
        delivery_address_line_1 (str): Address line 1 <br /> Mandatory<br />
            Max field length: 40
        delivery_address_line_2 (str): Address line 2 <br /> Optional <br />
            Max field length: 40  <br /> Optional
        delivery_address_line_3 (str): Address line 3 <br /> Optional <br />
            Max field length: 40  <br /> Optional
        delivery_zip_code (str): ZIP code <br /> Mandatory  <br /> Max field
            length: 10  <br /> Optional
        delivery_city (str): City  <br /> Mandatory  <br /> Max field length:
            40
        delivery_region_id (int): Region Id  <br /> Optional
        delivery_region (str): Region  <br /> Optional<br /> When region is
            passed
        delivery_country (str): The ISO code of the country.<br />
        phone_number (str): Phone number for courier delivery.<br />
            Optional.<br /> Max field length: 20
        email_address (str): Email address for courier delivery.<br />
            Optional.<br /> Max field length: 90 <br/>Note:Based on the
            international standard that there can be Max Length 64 before the
            @ (the 'Local part’) =64(minimum of 1) Max Lenth after the (the
            domain) = 88 (Minimum of 2)
        save_for_card_reissue (bool): If this is specified, the contact
            address will be saved in cards platform for card reissue
            processing.<br /> Optional

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_contact_name": 'DeliveryContactName',
        "delivery_company_name": 'DeliveryCompanyName',
        "delivery_address_line_1": 'DeliveryAddressLine1',
        "delivery_zip_code": 'DeliveryZipCode',
        "delivery_city": 'DeliveryCity',
        "delivery_country": 'DeliveryCountry',
        "delivery_contact_title": 'DeliveryContactTitle',
        "delivery_address_line_2": 'DeliveryAddressLine2',
        "delivery_address_line_3": 'DeliveryAddressLine3',
        "delivery_region_id": 'DeliveryRegionId',
        "delivery_region": 'DeliveryRegion',
        "phone_number": 'PhoneNumber',
        "email_address": 'EmailAddress',
        "save_for_card_reissue": 'SaveForCardReissue'
    }

    _optionals = [
        'delivery_contact_title',
        'delivery_address_line_2',
        'delivery_address_line_3',
        'delivery_region_id',
        'delivery_region',
        'phone_number',
        'email_address',
        'save_for_card_reissue',
    ]

    _nullables = [
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
        'phone_number',
        'email_address',
    ]

    def __init__(self,
                 delivery_contact_name=None,
                 delivery_company_name=None,
                 delivery_address_line_1=None,
                 delivery_zip_code=None,
                 delivery_city=None,
                 delivery_country=None,
                 delivery_contact_title=APIHelper.SKIP,
                 delivery_address_line_2=APIHelper.SKIP,
                 delivery_address_line_3=APIHelper.SKIP,
                 delivery_region_id=APIHelper.SKIP,
                 delivery_region=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 save_for_card_reissue=APIHelper.SKIP):
        """Constructor for the CardDeliveryContact class"""

        # Initialize members of the class
        if delivery_contact_title is not APIHelper.SKIP:
            self.delivery_contact_title = delivery_contact_title 
        self.delivery_contact_name = delivery_contact_name 
        self.delivery_company_name = delivery_company_name 
        self.delivery_address_line_1 = delivery_address_line_1 
        if delivery_address_line_2 is not APIHelper.SKIP:
            self.delivery_address_line_2 = delivery_address_line_2 
        if delivery_address_line_3 is not APIHelper.SKIP:
            self.delivery_address_line_3 = delivery_address_line_3 
        self.delivery_zip_code = delivery_zip_code 
        self.delivery_city = delivery_city 
        if delivery_region_id is not APIHelper.SKIP:
            self.delivery_region_id = delivery_region_id 
        if delivery_region is not APIHelper.SKIP:
            self.delivery_region = delivery_region 
        self.delivery_country = delivery_country 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if save_for_card_reissue is not APIHelper.SKIP:
            self.save_for_card_reissue = save_for_card_reissue 

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
        delivery_contact_name = dictionary.get("DeliveryContactName") if dictionary.get("DeliveryContactName") else None
        delivery_company_name = dictionary.get("DeliveryCompanyName") if dictionary.get("DeliveryCompanyName") else None
        delivery_address_line_1 = dictionary.get("DeliveryAddressLine1") if dictionary.get("DeliveryAddressLine1") else None
        delivery_zip_code = dictionary.get("DeliveryZipCode") if dictionary.get("DeliveryZipCode") else None
        delivery_city = dictionary.get("DeliveryCity") if dictionary.get("DeliveryCity") else None
        delivery_country = dictionary.get("DeliveryCountry") if dictionary.get("DeliveryCountry") else None
        delivery_contact_title = dictionary.get("DeliveryContactTitle") if "DeliveryContactTitle" in dictionary.keys() else APIHelper.SKIP
        delivery_address_line_2 = dictionary.get("DeliveryAddressLine2") if "DeliveryAddressLine2" in dictionary.keys() else APIHelper.SKIP
        delivery_address_line_3 = dictionary.get("DeliveryAddressLine3") if "DeliveryAddressLine3" in dictionary.keys() else APIHelper.SKIP
        delivery_region_id = dictionary.get("DeliveryRegionId") if "DeliveryRegionId" in dictionary.keys() else APIHelper.SKIP
        delivery_region = dictionary.get("DeliveryRegion") if "DeliveryRegion" in dictionary.keys() else APIHelper.SKIP
        phone_number = dictionary.get("PhoneNumber") if "PhoneNumber" in dictionary.keys() else APIHelper.SKIP
        email_address = dictionary.get("EmailAddress") if "EmailAddress" in dictionary.keys() else APIHelper.SKIP
        save_for_card_reissue = dictionary.get("SaveForCardReissue") if "SaveForCardReissue" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(delivery_contact_name,
                   delivery_company_name,
                   delivery_address_line_1,
                   delivery_zip_code,
                   delivery_city,
                   delivery_country,
                   delivery_contact_title,
                   delivery_address_line_2,
                   delivery_address_line_3,
                   delivery_region_id,
                   delivery_region,
                   phone_number,
                   email_address,
                   save_for_card_reissue)
