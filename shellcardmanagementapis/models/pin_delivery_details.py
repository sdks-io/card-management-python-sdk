# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class PINDeliveryDetails(object):

    """Implementation of the 'PINDeliveryDetails' model.

    PINDeliverDetails entity. The fields of this entity are described below.
    This is mandatory if PINContactType is 4 else optional and ignored.

    Attributes:
        contact_name (str): Contact Name  Max Length: 50
        contact_title (str): Contact Title  Max Length: 50
        company_name (str): Company Name for PIN delivery.  Max Length: 50
        address_line (str): Address Lines  Max Length: 1024
        zip_code (str): Zip Code  Max Length: 10
        city (str): City  Max Length: 40
        region_id (int): Region
        country_id (int): Country
        phone_number (str): Cardholder phone number for PIN delivery.
        email_address (str): Cardholder email address for PIN delivery  Max
            Length : 90  Example: xxxxxx@example.com <br/>Note:Based on the
            international standard that there can be Max Length 64 before the
            @ (the 'Local part’) =64(minimum of 1) Max Lenth after the (the
            domain) = 88 (Minimum of 2)
        save_pin_reminder (bool): Save PIN Reminder  If SavePINReminder is
            true, the contact address will be saved database for PIN reminder.
            <br/>Only allowed for PIN Advice paper delivery.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "company_name": 'CompanyName',
        "address_line": 'AddressLine',
        "zip_code": 'ZipCode',
        "city": 'City',
        "contact_name": 'ContactName',
        "contact_title": 'ContactTitle',
        "region_id": 'RegionID',
        "country_id": 'CountryID',
        "phone_number": 'PhoneNumber',
        "email_address": 'EmailAddress',
        "save_pin_reminder": 'SavePINReminder'
    }

    _optionals = [
        'contact_name',
        'contact_title',
        'region_id',
        'country_id',
        'phone_number',
        'email_address',
        'save_pin_reminder',
    ]

    _nullables = [
        'contact_name',
        'contact_title',
        'zip_code',
        'region_id',
        'country_id',
        'phone_number',
        'email_address',
    ]

    def __init__(self,
                 company_name=None,
                 address_line=None,
                 zip_code=None,
                 city=None,
                 contact_name=APIHelper.SKIP,
                 contact_title=APIHelper.SKIP,
                 region_id=APIHelper.SKIP,
                 country_id=APIHelper.SKIP,
                 phone_number=APIHelper.SKIP,
                 email_address=APIHelper.SKIP,
                 save_pin_reminder=APIHelper.SKIP):
        """Constructor for the PINDeliveryDetails class"""

        # Initialize members of the class
        if contact_name is not APIHelper.SKIP:
            self.contact_name = contact_name 
        if contact_title is not APIHelper.SKIP:
            self.contact_title = contact_title 
        self.company_name = company_name 
        self.address_line = address_line 
        self.zip_code = zip_code 
        self.city = city 
        if region_id is not APIHelper.SKIP:
            self.region_id = region_id 
        if country_id is not APIHelper.SKIP:
            self.country_id = country_id 
        if phone_number is not APIHelper.SKIP:
            self.phone_number = phone_number 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 
        if save_pin_reminder is not APIHelper.SKIP:
            self.save_pin_reminder = save_pin_reminder 

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
        company_name = dictionary.get("CompanyName") if dictionary.get("CompanyName") else None
        address_line = dictionary.get("AddressLine") if dictionary.get("AddressLine") else None
        zip_code = dictionary.get("ZipCode") if dictionary.get("ZipCode") else None
        city = dictionary.get("City") if dictionary.get("City") else None
        contact_name = dictionary.get("ContactName") if "ContactName" in dictionary.keys() else APIHelper.SKIP
        contact_title = dictionary.get("ContactTitle") if "ContactTitle" in dictionary.keys() else APIHelper.SKIP
        region_id = dictionary.get("RegionID") if "RegionID" in dictionary.keys() else APIHelper.SKIP
        country_id = dictionary.get("CountryID") if "CountryID" in dictionary.keys() else APIHelper.SKIP
        phone_number = dictionary.get("PhoneNumber") if "PhoneNumber" in dictionary.keys() else APIHelper.SKIP
        email_address = dictionary.get("EmailAddress") if "EmailAddress" in dictionary.keys() else APIHelper.SKIP
        save_pin_reminder = dictionary.get("SavePINReminder") if "SavePINReminder" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(company_name,
                   address_line,
                   zip_code,
                   city,
                   contact_name,
                   contact_title,
                   region_id,
                   country_id,
                   phone_number,
                   email_address,
                   save_pin_reminder)