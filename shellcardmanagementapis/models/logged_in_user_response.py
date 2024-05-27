# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.models.account_access import AccountAccess
from shellcardmanagementapis.models.col_co_access import ColCoAccess
from shellcardmanagementapis.models.eid_access import EIDAccess
from shellcardmanagementapis.models.error_status import ErrorStatus
from shellcardmanagementapis.models.payer_access import PayerAccess
from shellcardmanagementapis.models.role import Role


class LoggedInUserResponse(object):

    """Implementation of the 'LoggedInUserResponse' model.

    TODO: type model description here.

    Attributes:
        user_name (str): Logged in User Identifier
        display_name (str): Name of the logged in user.
        id_mssoid (str): Single Sign On/Unique Identifier of the User in
            Identity Management system
        preferred_language (str): ISO culture code/ Language chosen by the
            logged in user
        is_super_admin (bool): Whether the user is a super administrator
        date_format (str): Preferred Date format for the logged in user
        time_format (str): Preferred Time format for the logged in user
        week_begins (int): Preferred Day to Begin the Week. The value will be
            between 1 to 7 or null.
        display_week (bool): Preferred Display Week on Fuel Prices
            configuration for the logged in User.
        csv_separator (str): Preferred CSV Separator for the logged in user.
        decimal_separator (str): Preferred Decimal separator configured for
            the logged in user  Note: - Colco default value (configured at
            Microservices) is returned when the user is not provided or does
            not exist.
        report_format (str): Preferred report format configured for the logged
            in user
        has_api_access (bool): True/False  True, if user has access to the
            requested API. This is validated based on the role Vs API access
            matrix and client Vs API access matrix.
        roles (List[Role]): List of roles the user have access to
        payers (List[PayerAccess]): List of payers which the user has access
            to.  • It will return 250 payers only and it is configurable. If
            the user has more than that, the remaining will be ignored.  • The
            payer which is marked as default will be the first item in the
            output.    Note: This list will be empty for users mapped with
            roles which has either IsShellAdmin or IsServiceAccount set to
            true as their access level is controlled at ColCo level only.
        accounts (List[AccountAccess]): List of accounts which the user has
            access to.  Note: This list will be empty for users mapped with
            roles which has either IsCustomerAdmin, IsShellAdmin or
            IsServiceAccount set to true as their access level is controller
            at either ColCo or payer level only.
        collecting_companies (List[ColCoAccess]): List of collecting companies
            to which the user has access to   Note: This list will be empty
            for users mapped with roles which has either IsCustomerAdmin or
            IsCustomerUser set to true as their access level is controller at
            Payer or Account level.
        eid_access_details (List[EIDAccess]): List of Electronic Invoice Data
            configured for the user.  Note: This list will be empty if the
            value of EIDDetails is set to false or empty in the request.
        user_classification_by_system (str): User classification by system.
        user_classification_by_shell (str): User classification by Shell.
        payer_count (int): Count of payers accessible to the user at the time
            when user was created or last updated.   Note:  Count may vary
            based on customer operations hence it may not be an up to date
            value.
        account_count (int): Count of accounts at the time when the user was
            created or last updated.   Note:  Count may vary based on customer
            operations hence it may not be an up to date value.
        card_count (int): Count of cards at the time when the user was created
            or last updated.  Note:   Count may vary based on customer
            operations hence it may not be an up to date value.
        error (ErrorStatus): TODO: type description here.
        request_id (str): Request Id of the API call

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "user_name": 'UserName',
        "display_name": 'DisplayName',
        "id_mssoid": 'IdMSSOID',
        "preferred_language": 'PreferredLanguage',
        "is_super_admin": 'IsSuperAdmin',
        "date_format": 'DateFormat',
        "time_format": 'TimeFormat',
        "week_begins": 'WeekBegins',
        "display_week": 'DisplayWeek',
        "csv_separator": 'CSVSeparator',
        "decimal_separator": 'DecimalSeparator',
        "report_format": 'ReportFormat',
        "has_api_access": 'HasAPIAccess',
        "roles": 'Roles',
        "payers": 'Payers',
        "accounts": 'Accounts',
        "collecting_companies": 'CollectingCompanies',
        "eid_access_details": 'EIDAccessDetails',
        "user_classification_by_system": 'UserClassificationBySystem',
        "user_classification_by_shell": 'UserClassificationByShell',
        "payer_count": 'PayerCount',
        "account_count": 'AccountCount',
        "card_count": 'CardCount',
        "error": 'Error',
        "request_id": 'RequestId'
    }

    _optionals = [
        'user_name',
        'display_name',
        'id_mssoid',
        'preferred_language',
        'is_super_admin',
        'date_format',
        'time_format',
        'week_begins',
        'display_week',
        'csv_separator',
        'decimal_separator',
        'report_format',
        'has_api_access',
        'roles',
        'payers',
        'accounts',
        'collecting_companies',
        'eid_access_details',
        'user_classification_by_system',
        'user_classification_by_shell',
        'payer_count',
        'account_count',
        'card_count',
        'error',
        'request_id',
    ]

    _nullables = [
        'user_name',
        'display_name',
        'id_mssoid',
        'preferred_language',
        'date_format',
        'time_format',
        'week_begins',
        'csv_separator',
        'decimal_separator',
        'report_format',
        'user_classification_by_system',
        'user_classification_by_shell',
        'payer_count',
        'account_count',
        'card_count',
    ]

    def __init__(self,
                 user_name=APIHelper.SKIP,
                 display_name=APIHelper.SKIP,
                 id_mssoid=APIHelper.SKIP,
                 preferred_language=APIHelper.SKIP,
                 is_super_admin=False,
                 date_format=APIHelper.SKIP,
                 time_format=APIHelper.SKIP,
                 week_begins=APIHelper.SKIP,
                 display_week=True,
                 csv_separator=APIHelper.SKIP,
                 decimal_separator=APIHelper.SKIP,
                 report_format=APIHelper.SKIP,
                 has_api_access=True,
                 roles=APIHelper.SKIP,
                 payers=APIHelper.SKIP,
                 accounts=APIHelper.SKIP,
                 collecting_companies=APIHelper.SKIP,
                 eid_access_details=APIHelper.SKIP,
                 user_classification_by_system=APIHelper.SKIP,
                 user_classification_by_shell=APIHelper.SKIP,
                 payer_count=APIHelper.SKIP,
                 account_count=APIHelper.SKIP,
                 card_count=APIHelper.SKIP,
                 error=APIHelper.SKIP,
                 request_id=APIHelper.SKIP):
        """Constructor for the LoggedInUserResponse class"""

        # Initialize members of the class
        if user_name is not APIHelper.SKIP:
            self.user_name = user_name 
        if display_name is not APIHelper.SKIP:
            self.display_name = display_name 
        if id_mssoid is not APIHelper.SKIP:
            self.id_mssoid = id_mssoid 
        if preferred_language is not APIHelper.SKIP:
            self.preferred_language = preferred_language 
        self.is_super_admin = is_super_admin 
        if date_format is not APIHelper.SKIP:
            self.date_format = date_format 
        if time_format is not APIHelper.SKIP:
            self.time_format = time_format 
        if week_begins is not APIHelper.SKIP:
            self.week_begins = week_begins 
        self.display_week = display_week 
        if csv_separator is not APIHelper.SKIP:
            self.csv_separator = csv_separator 
        if decimal_separator is not APIHelper.SKIP:
            self.decimal_separator = decimal_separator 
        if report_format is not APIHelper.SKIP:
            self.report_format = report_format 
        self.has_api_access = has_api_access 
        if roles is not APIHelper.SKIP:
            self.roles = roles 
        if payers is not APIHelper.SKIP:
            self.payers = payers 
        if accounts is not APIHelper.SKIP:
            self.accounts = accounts 
        if collecting_companies is not APIHelper.SKIP:
            self.collecting_companies = collecting_companies 
        if eid_access_details is not APIHelper.SKIP:
            self.eid_access_details = eid_access_details 
        if user_classification_by_system is not APIHelper.SKIP:
            self.user_classification_by_system = user_classification_by_system 
        if user_classification_by_shell is not APIHelper.SKIP:
            self.user_classification_by_shell = user_classification_by_shell 
        if payer_count is not APIHelper.SKIP:
            self.payer_count = payer_count 
        if account_count is not APIHelper.SKIP:
            self.account_count = account_count 
        if card_count is not APIHelper.SKIP:
            self.card_count = card_count 
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
        user_name = dictionary.get("UserName") if "UserName" in dictionary.keys() else APIHelper.SKIP
        display_name = dictionary.get("DisplayName") if "DisplayName" in dictionary.keys() else APIHelper.SKIP
        id_mssoid = dictionary.get("IdMSSOID") if "IdMSSOID" in dictionary.keys() else APIHelper.SKIP
        preferred_language = dictionary.get("PreferredLanguage") if "PreferredLanguage" in dictionary.keys() else APIHelper.SKIP
        is_super_admin = dictionary.get("IsSuperAdmin") if dictionary.get("IsSuperAdmin") else False
        date_format = dictionary.get("DateFormat") if "DateFormat" in dictionary.keys() else APIHelper.SKIP
        time_format = dictionary.get("TimeFormat") if "TimeFormat" in dictionary.keys() else APIHelper.SKIP
        week_begins = dictionary.get("WeekBegins") if "WeekBegins" in dictionary.keys() else APIHelper.SKIP
        display_week = dictionary.get("DisplayWeek") if dictionary.get("DisplayWeek") else True
        csv_separator = dictionary.get("CSVSeparator") if "CSVSeparator" in dictionary.keys() else APIHelper.SKIP
        decimal_separator = dictionary.get("DecimalSeparator") if "DecimalSeparator" in dictionary.keys() else APIHelper.SKIP
        report_format = dictionary.get("ReportFormat") if "ReportFormat" in dictionary.keys() else APIHelper.SKIP
        has_api_access = dictionary.get("HasAPIAccess") if dictionary.get("HasAPIAccess") else True
        roles = None
        if dictionary.get('Roles') is not None:
            roles = [Role.from_dictionary(x) for x in dictionary.get('Roles')]
        else:
            roles = APIHelper.SKIP
        payers = None
        if dictionary.get('Payers') is not None:
            payers = [PayerAccess.from_dictionary(x) for x in dictionary.get('Payers')]
        else:
            payers = APIHelper.SKIP
        accounts = None
        if dictionary.get('Accounts') is not None:
            accounts = [AccountAccess.from_dictionary(x) for x in dictionary.get('Accounts')]
        else:
            accounts = APIHelper.SKIP
        collecting_companies = None
        if dictionary.get('CollectingCompanies') is not None:
            collecting_companies = [ColCoAccess.from_dictionary(x) for x in dictionary.get('CollectingCompanies')]
        else:
            collecting_companies = APIHelper.SKIP
        eid_access_details = None
        if dictionary.get('EIDAccessDetails') is not None:
            eid_access_details = [EIDAccess.from_dictionary(x) for x in dictionary.get('EIDAccessDetails')]
        else:
            eid_access_details = APIHelper.SKIP
        user_classification_by_system = dictionary.get("UserClassificationBySystem") if "UserClassificationBySystem" in dictionary.keys() else APIHelper.SKIP
        user_classification_by_shell = dictionary.get("UserClassificationByShell") if "UserClassificationByShell" in dictionary.keys() else APIHelper.SKIP
        payer_count = dictionary.get("PayerCount") if "PayerCount" in dictionary.keys() else APIHelper.SKIP
        account_count = dictionary.get("AccountCount") if "AccountCount" in dictionary.keys() else APIHelper.SKIP
        card_count = dictionary.get("CardCount") if "CardCount" in dictionary.keys() else APIHelper.SKIP
        error = ErrorStatus.from_dictionary(dictionary.get('Error')) if 'Error' in dictionary.keys() else APIHelper.SKIP
        request_id = dictionary.get("RequestId") if dictionary.get("RequestId") else APIHelper.SKIP
        # Return an object of this model
        return cls(user_name,
                   display_name,
                   id_mssoid,
                   preferred_language,
                   is_super_admin,
                   date_format,
                   time_format,
                   week_begins,
                   display_week,
                   csv_separator,
                   decimal_separator,
                   report_format,
                   has_api_access,
                   roles,
                   payers,
                   accounts,
                   collecting_companies,
                   eid_access_details,
                   user_classification_by_system,
                   user_classification_by_shell,
                   payer_count,
                   account_count,
                   card_count,
                   error,
                   request_id)
