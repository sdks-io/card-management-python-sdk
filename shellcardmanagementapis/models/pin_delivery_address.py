# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper


class PINDeliveryAddress(object):

    """Implementation of the 'PINDeliveryAddress' model.

    TODO: type model description here.

    Attributes:
        contact_fore_name (str): Fore name of the contact person
        contact_middle_name (str): Middle name of the contact person
        contact_last_name (str): Last name of the contact person
        contact_title (str): Title of the contact person Optional Max field
            length- 10 Note- If the Shell Card Platform configuration is set
            to clear the personal details captured on card orders, this value
            will be cleared from the record after processing the request.
        company_name (str): Company name Mandatory if IsNewDeliveryAddress and
            OrderReplacement are passed. True, Note- If the Shell Card
            Platform configuration is set to clear the personal details
            captured on card orders, this value will be cleared from the
            record after processing the request.
        address_id (int): Address Id in cards platform.
        address_line_1 (str): Address line 1 Mandatory if IsNewDeliveryAddress
            and OrderReplacement are passed True. Max field length- 40 Note-
            If the Shell Card Platform configuration is set to clear the
            personal details captured on card orders, this value will be
            cleared from the record after processing the request.
        address_line_2 (str): Address line 2 Optional Max field length- 40
            Note- If the Shell Card Platform configuration is set to clear the
            personal details captured on card orders, this value will be
            cleared from the record after processing the request.
        address_line_3 (str): Address line Optional Max field length- 40 Note-
            If the Shell Card Platform configuration is set to clear the
            personal details captured on card orders, this value will be
            cleared from the record after processing the request.
        zip_code (str): ZIP code Mandatory if IsNewDeliveryAddress and
            OrderReplacement are passed. True, Max field length- 10 Note- If
            the Shell Card Platform configuration is set to clear the personal
            details captured on card orders, this value will be cleared from
            the record after processing the request.
        city (str): City Max field length- 40 Note- If the Shell Card Platform
            configuration is set to clear the personal details captured on
            card orders, this value will be cleared from the record after
            processing the request.
        region_id (int): Region Id
        region (str): Region Optional When region is passed, Shell Card
            Platform will look up for the region id for the given region.  If
            the option to clear personal details is set in the Shell Card
            Platform, then this value will be cleared from the record after
            processing the request .
        country_id (int): Country Id in cards platform.
        country_iso_code (str): The ISO code of the country. Mandatory if
            IsNewDeliveryAddress and OrderReplacement are passed. If the
            option to clear personal details is set in the Shell Card
            Platform, then this value will be cleared from the record after
            processing the request .
        country (str): Country name.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "company_name": 'CompanyName',
        "address_id": 'AddressId',
        "address_line_1": 'AddressLine1',
        "zip_code": 'ZipCode',
        "country_id": 'CountryId',
        "country_iso_code": 'CountryISOCode',
        "country": 'Country',
        "contact_fore_name": 'ContactForeName',
        "contact_middle_name": 'ContactMiddleName',
        "contact_last_name": 'ContactLastName',
        "contact_title": 'ContactTitle',
        "address_line_2": 'AddressLine2',
        "address_line_3": 'AddressLine3',
        "city": 'City',
        "region_id": 'RegionId',
        "region": 'Region'
    }

    _optionals = [
        'contact_fore_name',
        'contact_middle_name',
        'contact_last_name',
        'contact_title',
        'address_line_2',
        'address_line_3',
        'city',
        'region_id',
        'region',
    ]

    _nullables = [
        'contact_fore_name',
        'contact_middle_name',
        'contact_last_name',
        'contact_title',
        'region_id',
    ]

    def __init__(self,
                 company_name=None,
                 address_id=None,
                 address_line_1=None,
                 zip_code=None,
                 country_id=None,
                 country_iso_code=None,
                 country=None,
                 contact_fore_name=APIHelper.SKIP,
                 contact_middle_name=APIHelper.SKIP,
                 contact_last_name=APIHelper.SKIP,
                 contact_title=APIHelper.SKIP,
                 address_line_2=APIHelper.SKIP,
                 address_line_3=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 region_id=APIHelper.SKIP,
                 region=APIHelper.SKIP):
        """Constructor for the PINDeliveryAddress class"""

        # Initialize members of the class
        if contact_fore_name is not APIHelper.SKIP:
            self.contact_fore_name = contact_fore_name 
        if contact_middle_name is not APIHelper.SKIP:
            self.contact_middle_name = contact_middle_name 
        if contact_last_name is not APIHelper.SKIP:
            self.contact_last_name = contact_last_name 
        if contact_title is not APIHelper.SKIP:
            self.contact_title = contact_title 
        self.company_name = company_name 
        self.address_id = address_id 
        self.address_line_1 = address_line_1 
        if address_line_2 is not APIHelper.SKIP:
            self.address_line_2 = address_line_2 
        if address_line_3 is not APIHelper.SKIP:
            self.address_line_3 = address_line_3 
        self.zip_code = zip_code 
        if city is not APIHelper.SKIP:
            self.city = city 
        if region_id is not APIHelper.SKIP:
            self.region_id = region_id 
        if region is not APIHelper.SKIP:
            self.region = region 
        self.country_id = country_id 
        self.country_iso_code = country_iso_code 
        self.country = country 

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
        company_name = dictionary.get("CompanyName") if dictionary.get("CompanyName") else None
        address_id = dictionary.get("AddressId") if dictionary.get("AddressId") else None
        address_line_1 = dictionary.get("AddressLine1") if dictionary.get("AddressLine1") else None
        zip_code = dictionary.get("ZipCode") if dictionary.get("ZipCode") else None
        country_id = dictionary.get("CountryId") if dictionary.get("CountryId") else None
        country_iso_code = dictionary.get("CountryISOCode") if dictionary.get("CountryISOCode") else None
        country = dictionary.get("Country") if dictionary.get("Country") else None
        contact_fore_name = dictionary.get("ContactForeName") if "ContactForeName" in dictionary.keys() else APIHelper.SKIP
        contact_middle_name = dictionary.get("ContactMiddleName") if "ContactMiddleName" in dictionary.keys() else APIHelper.SKIP
        contact_last_name = dictionary.get("ContactLastName") if "ContactLastName" in dictionary.keys() else APIHelper.SKIP
        contact_title = dictionary.get("ContactTitle") if "ContactTitle" in dictionary.keys() else APIHelper.SKIP
        address_line_2 = dictionary.get("AddressLine2") if dictionary.get("AddressLine2") else APIHelper.SKIP
        address_line_3 = dictionary.get("AddressLine3") if dictionary.get("AddressLine3") else APIHelper.SKIP
        city = dictionary.get("City") if dictionary.get("City") else APIHelper.SKIP
        region_id = dictionary.get("RegionId") if "RegionId" in dictionary.keys() else APIHelper.SKIP
        region = dictionary.get("Region") if dictionary.get("Region") else APIHelper.SKIP
        # Return an object of this model
        return cls(company_name,
                   address_id,
                   address_line_1,
                   zip_code,
                   country_id,
                   country_iso_code,
                   country,
                   contact_fore_name,
                   contact_middle_name,
                   contact_last_name,
                   contact_title,
                   address_line_2,
                   address_line_3,
                   city,
                   region_id,
                   region)
