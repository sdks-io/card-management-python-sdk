# -*- coding: utf-8 -*-

"""
shellcardmanagementapis

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from shellcardmanagementapis.api_helper import APIHelper
from shellcardmanagementapis.configuration import Server
from shellcardmanagementapis.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from shellcardmanagementapis.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from shellcardmanagementapis.models.logged_in_user_response import LoggedInUserResponse
from shellcardmanagementapis.models.payer_response import PayerResponse
from shellcardmanagementapis.models.customer_detail_response import CustomerDetailResponse
from shellcardmanagementapis.models.account_response import AccountResponse
from shellcardmanagementapis.models.card_type_response import CardTypeResponse
from shellcardmanagementapis.models.card_group_response import CardGroupResponse
from shellcardmanagementapis.models.audit_response import AuditResponse
from shellcardmanagementapis.models.create_card_group_response import CreateCardGroupResponse
from shellcardmanagementapis.models.update_card_group_response import UpdateCardGroupResponse
from shellcardmanagementapis.exceptions.default_error_exception import DefaultErrorException
from shellcardmanagementapis.exceptions.error_user_access_error_1_exception import ErrorUserAccessError1Exception


class CustomerController(BaseController):

    """A Controller to access Endpoints in the shellcardmanagementapis API."""
    def __init__(self, config):
        super(CustomerController, self).__init__(config)

    def loggedin_user(self,
                      apikey,
                      request_id,
                      body=None):
        """Does a POST request to /fleetmanagement/v1/user/loggedinuser.

        This API allows querying the user data of the logged in user.</br>
        This API will return the user access details such as payers and/or
        accounts. </br>
        This API will also validate that logged in user has access to the
        requested API, on failure it will return HasAPIAccess flag as false in
        response.</br>

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (LoggedInUserRequest, optional): Logged in user request body

        Returns:
            LoggedInUserResponse: Response from the API. The http status code
                200 and the Error.Code "0000" in the response body would
                indicate the API call is successful. The http status code 200
                with Error Code other than "0000" in the response body would
                indicate there is a failure in the API call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/user/loggedinuser')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(LoggedInUserResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def payers(self,
               apikey,
               request_id,
               body=None):
        """Does a POST request to /fleetmanagement/v1/customer/payers.

        This API allows querying the payer accounts details from the Shell
        Cards
        Platform. It provides flexible search criteria for searching payer
        information and supports paging. 
        Paging is applicable only when all the
        payers passed in the input are from the same ColCo. 
        However, paging will
        be ignored and the API will return all the matching data by merging
        the
        data queried from each ColCo when payers passed in the input are from
        multiple ColCos.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (PayerRequest, optional): Serach payers request body

        Returns:
            PayerResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/customer/payers')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PayerResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def customer(self,
                 apikey,
                 request_id,
                 body=None):
        """Does a POST request to /fleetmanagement/v1/customer/customer.

        This API allows querying the card delivery addresses of a given
        account from the Shell Cards Platform. 
        Only active delivery addresses will be returned.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (CustomerDetailRequest, optional): Customerdetails request
                body

        Returns:
            CustomerDetailResponse: Response from the API. List of fuel cards.
                The http status code 200 and the Error.Code "0000" in the
                response body would indicate the API call is successful. The
                http status code 200 with Error Code other than "0000" in the
                response body would indicate there is a failure in the API
                call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/customer/customer')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CustomerDetailResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def accounts(self,
                 apikey,
                 request_id,
                 body=None):
        """Does a POST request to /fleetmanagement/v1/customer/accounts.

        This API allows querying the customer account details from the Shell
        Cards Platform. 
        It provides a flexible search criterion and supports paging".

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (AccountRequest, optional): TODO: type description here.

        Returns:
            AccountResponse: Response from the API. List of fuel cards. The
                http status code 200 and the Error.Code "0000" in the response
                body would indicate the API call is successful. The http
                status code 200 with Error Code other than "0000" in the
                response body would indicate there is a failure in the API
                call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/customer/accounts')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def card_type(self,
                  apikey,
                  request_id,
                  body=None):
        """Does a POST request to /fleetmanagement/v2/customer/cardtype.

        This operation allows querying card types that are associated to the
        given account and are allowed to be shown to users.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (CardTypeRequest, optional): Get CardType Request Body

        Returns:
            CardTypeResponse: Response from the API. The http status code 200
                and the Error.Code "0000" in the response body would indicate
                the API call is successful. The http status code 200 with
                Error Code other than "0000" in the response body would
                indicate there is a failure in the API call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v2/customer/cardtype')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CardTypeResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def card_groups(self,
                    apikey,
                    request_id,
                    body=None):
        """Does a POST request to /fleetmanagement/v1/customer/cardgroups.

        This operation allows querying the card group details . It provides
        flexible search criteria and supports paging.\
        When the card group type is configured as ‘Vertical’ in cards
        platform, this operation will return all card groups from the given
        account or if no account is passed in the input, then will return card
        groups from all the accounts under the payer.
        When the card group type is configured as ‘Horizontal’ in cards
        platform, this API will return all card groups configured directly
        under the payer.
        Accounts with cancelled status will not be considered for cardgroups
        search for the configured (E.g., SFH) set of client apps.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (CardGroupRequest, optional): Request Body

        Returns:
            CardGroupResponse: Response from the API. The http status code 200
                and the Error.Code "0000" in the response body would indicate
                the API call is successful. The http status code 200 with
                Error Code other than "0000" in the response body would
                indicate there is a failure in the API call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/customer/cardgroups')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CardGroupResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def audit_report(self,
                     apikey,
                     request_id,
                     body=None):
        """Does a POST request to /fleetmanagement/v1/customer/auditreport.

        This operation allows users to fetch audit data of account or card
        operations performed by users of a given customer
        The audit data includes details of below API operations
        * Order Card 
        * Create Card Group 
        * PIN reminder 
        * Move Cards 
        * Update Card Status 
        * Update Card Group 
        * Auto renew 
        * Bulk card order 
        * Bulk card block 
        * Bulk Card Order (Multi Account) 
        * BCOSummary 
        * BCOMultiAccountSummary 
        * BCBSummary 
        * Mobile Payment 
        * Registration 
        * Fund Transfer (Scheduled & Realtime) 
        * Delivery Address Update.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (AuditRequest, optional): request body

        Returns:
            AuditResponse: Response from the API. The http status code 200 and
                the Error.Code "0000" in the response body would indicate the
                API call is successful. The http status code 200 with Error
                Code other than "0000" in the response body would indicate
                there is a failure in the API call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/customer/auditreport')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AuditResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def create_card_group(self,
                          apikey,
                          request_id,
                          body=None):
        """Does a POST request to /fleetmanagement/v1/customer/createcardgroup.

        This API allows creating a new Card Group in the Shell Cards Platform.
        It will
        also allow moving of cards (up to 500 cards) into the newly created
        card-group. 
        ### Move Card requests are queued after passing the below validations
                * Given PAN matches with only one card. 
        * Card is allowed to be moved to the Target Card Group and/or
        * Target account requested. 
        * There is no pending Move Card request for the same card in the queue
        which is submitted on the same date
          and is yet to be processed or has been processed
        successfully

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (CreateCardGroupRequest, optional): CreateCardGroup request
                body

        Returns:
            CreateCardGroupResponse: Response from the API. List of fuel
                cards. The http status code 200 and the Error.Code "0000" in
                the response body would indicate the API call is successful.
                The http status code 200 with Error Code other than "0000" in
                the response body would indicate there is a failure in the API
                call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/customer/createcardgroup')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CreateCardGroupResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()

    def update_card_group(self,
                          apikey,
                          request_id,
                          body=None):
        """Does a POST request to /fleetmanagement/v1/customer/updatecardgroup.

        This API allows updating or removing a Card Group in the Shell Cards
        Platform.
        It also allows moving of cards out of a card group or from one card
        group to another existing card group.
        The request for updating or removing of the card group, creationg of a
        new card group (where-applicable) and moving of card into another card
        group will be queued at Microservices after passing the basic
        validations. 

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (UpdateCardGroupRequest, optional): request body of customer
                card group

        Returns:
            UpdateCardGroupResponse: Response from the API. List of fuel
                cards. The http status code 200 and the Error.Code "0000" in
                the response body would indicate the API call is successful.
                The http status code 200 with Error Code other than "0000" in
                the response body would indicate there is a failure in the API
                call.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/fleetmanagement/v1/customer/updatecardgroup')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('apikey')
                          .value(apikey))
            .header_param(Parameter()
                          .key('RequestId')
                          .value(request_id))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UpdateCardGroupResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', DefaultErrorException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.\r\n', DefaultErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.\r\n', ErrorUserAccessError1Exception)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.\r\n', DefaultErrorException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.\r\n', DefaultErrorException)
        ).execute()