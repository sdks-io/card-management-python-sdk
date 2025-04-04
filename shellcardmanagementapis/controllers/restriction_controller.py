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
from shellcardmanagementapis.models.search_card_restriction_res import SearchCardRestrictionRes
from shellcardmanagementapis.models.card_restriction_response import CardRestrictionResponse
from shellcardmanagementapis.models.create_bundle_response import CreateBundleResponse
from shellcardmanagementapis.models.update_bundle_response import UpdateBundleResponse
from shellcardmanagementapis.models.delete_bundle_response import DeleteBundleResponse
from shellcardmanagementapis.models.summaryofbundle_response import SummaryofbundleResponse
from shellcardmanagementapis.models.account_restriction_response import AccountRestrictionResponse
from shellcardmanagementapis.models.search_account_limit_response import SearchAccountLimitResponse
from shellcardmanagementapis.models.bundle_details_response import BundleDetailsResponse
from shellcardmanagementapis.exceptions.api_exception import APIException
from shellcardmanagementapis.exceptions.fleetmanagement_v_2_restriction_searchcard_401_error_exception import FleetmanagementV2RestrictionSearchcard401ErrorException
from shellcardmanagementapis.exceptions.fleetmanagement_v_2_restriction_searchcard_500_error_exception import FleetmanagementV2RestrictionSearchcard500ErrorException


class RestrictionController(BaseController):

    """A Controller to access Endpoints in the shellcardmanagementapis API."""
    def __init__(self, config):
        super(RestrictionController, self).__init__(config)

    def search_card_restriction(self,
                                apikey,
                                request_id,
                                body=None):
        """Does a POST request to /fleetmanagement/v2/restriction/searchcard.

        This API will allows querying card details including the day/time and
        product restrictions.
        #### Supported operations
          * Search by list of cards or bundle
          * Include card bundle details (optional)

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (SearchCardRestrictionReq, optional): Restriction search card
                request body

        Returns:
            SearchCardRestrictionRes: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v2/restriction/searchcard')
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
            .deserialize_into(SearchCardRestrictionRes.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', FleetmanagementV2RestrictionSearchcard401ErrorException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', FleetmanagementV2RestrictionSearchcard500ErrorException)
        ).execute()

    def apply_restriction(self,
                          apikey,
                          request_id,
                          body=None):
        """Does a POST request to /fleetmanagement/v2/restriction/card.

        The Card Limit and Restriction API is REST-based and employs Basic and
        ApiKey authentication. The API endpoints accept JSON-encoded request
        bodies, return JSON-encoded responses and use standard HTTP response
        codes. 
        All resources are located in the Shell Card Platform.  The Shell Card
        Platform is the overall platform that encompasses all the internal
        Shell systems used to manage resources. The internal workings of the
        platform are not important when interacting with the API. However, it
        is worth noting that the platform uses a microservice architecture to
        communicate with various backend systems and some API calls are
        processed asynchronously.
        All endpoints use the `POST` verb for retrieving, updating, creating
        and deleting resources in the Shell Card Platform. The endpoints that
        retrieve resources from the Shell Card Platform allow flexible search
        parameters in the API request body.
        **Important Note** - This operation allows setting or updating the
        restrictions on existing cards. (For up to 3 cards in a single call).
        All restrictions of the cards are submitted and executed after
        successful below condition.
        •    The card exists.
        •    Day time restriction cannot be set to restrict the use of a card
        on all days of the week i.e., the values for all the days in the
        restriction cannot be set to false.
        •    Either of the usage, daytime, location or product restriction
        ‘Reset’ is set to ‘True’ or applied on the card.
        •    All the limits in the usage restriction profile for a card is not
        set to ‘0’/null.
        •    If IsVelocityCeiling is ‘true’, API will validate below condition:
        Usage restrictions for a card are lower than Customer Card Type level
        limits, if there are no customer level overrides available then lower
        than OU card type limits.
        •    In usage restrictions, the limits per transaction should be less
        than or equal to Daily, Daily should be less than or equal to Weekly,
        Weekly should be less than or equal to Monthly, Monthly should be less
        than or equal to Yearly (Annually). Exception being null/blank will be
        skipped. i.e., Daily value should be less than equal to Monthly value
        if Weekly value is null/blank. Lifetime limit is not considered for
        usage restrictions limits validation.
        •    Apply the card type limit to Gateway when a value is NULL in the
        input. However, if the card type limit is NULL for the same field,
        then no limit will be applied in Gateway.
        •    If ‘SetDefaultOnVelocityUpdate’ is ‘true’ then the operation will
        apply customer cardtype or OU level velocity limits on existing cards
        when restrictions are modified without providing custom values for all
        fields.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (CardRestrictionReq, optional): Card Restriction request body

        Returns:
            CardRestrictionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v2/restriction/card')
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
            .deserialize_into(CardRestrictionResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()

    def create_bundle(self,
                      apikey,
                      request_id,
                      body=None):
        """Does a POST request to /fleetmanagement/v1/restriction/createbundle.

        This API enables clients to create a new card bundle and apply
        restrictions.
        #### Supported operations
          * Create bundle and include mandatory -
            * Usage, day/time, product and location restrictions
            * List of cards to add to bundle
          * Create bundle and include optional identifier of bundle in
        external system
        #### Validation rules
          The following are the key validation rules with the associated error
        codes for failed validation-
          * `7012` - At least one card must be added to the bundle
          *  `7011` - The total number of cards passed in the input must be
        500 or less.
          *  `7014` - All the cards passed in the input are part of the
        selected account.
          *  `7013` - At least one restriction must be applied to the bundle
        i.e. either of usage, day/time, location or product restriction.
          *  `7005` - Day time restriction cannot be set to restrict the use
        of a card on all days of the week.
          *  `7000` - Usage restriction of the bundle is not open ended i.e.
        all the limits within the usage restriction must not be set to 0/null.
          *  `7004` - In the usage restrictions, the limits per transaction
        should be less than or equal to Daily, Daily should be less than or
        equal to Weekly, Weekly should be less than or equal to Monthly.
        Exception being 0/blank will be skipped, i.e. Daily value should be
        less than equal to Monthly value if Weekly value is 0/blank. 
          *  `0007` - Error returned if request parameters fail validation
        e.g. mandatory check.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (CreateBundleRequest, optional): CreateBundle request body

        Returns:
            CreateBundleResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v1/restriction/createbundle')
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
            .deserialize_into(CreateBundleResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()

    def update_bundle(self,
                      apikey,
                      request_id,
                      body=None):
        """Does a POST request to /fleetmanagement/v1/restriction/updatebundle.

        This API enables clients to update an existing card bundle and its
        associated restrictions.
        #### Supported operations
          * Add new cards to an existing bundle
          * Remove cards from existing bundle
          * Update restrictions applied to existing bundle
          The following are the key validation rules with the associated error
        codes for failed validation-      
        #### Validation rules
          *  `9007` - The cards must exist in the cards platform for adding or
        removing cards.
          *  `7014` - All the cards passed in the input are part of the
        selected account.
          *  `7018` - All the cards passed in the input are part of the
        selected bundle.
          *  `7011` - The total number of cards passed in the input must be
        500 or less.
          *  `7012` - The action to remove cards should not result in removing
        all the cards from the bundle.
          *  `7016` - At least one restriction must be modified for
        â€œUpdateâ€ request action.
          *  `7013` - All restrictions cannot be marked for â€œResetâ€ for
        â€œUpdateâ€ request action.
          *  `7005` - Day time restriction cannot be set to restrict the use
        of a card on all days of the week. This validation is applicable for
        Update request action.
          *  `7000` - Usage restriction of the bundle is not open ended i.e.,
        all the limits within the usage restriction must not be set to 0/null.
        This validation is applicable for Update request action.
          *  `7004` - In the usage restrictions, the limits per transaction
        should be less than or equal to Daily, Daily should be less than or
        equal to Weekly, Weekly should be less than or equal to Monthly.
        Exception being 0/blank will be skipped, i.e., Daily value should be
        less than equal to Monthly value if Weekly value is 0/blank. This
        validation is applicable for Update request action.
          *  `0007` - Error returned if request parameters fail validation
        e.g. at least one card must be provided in the input.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (UpdateBundleRequest, optional): Update Bundle request body

        Returns:
            UpdateBundleResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v1/restriction/updatebundle')
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
            .deserialize_into(UpdateBundleResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()

    def delete_bundle(self,
                      apikey,
                      request_id,
                      body=None):
        """Does a POST request to /fleetmanagement/v1/restriction/deletebundle.

        This API enables clients to delete an existing card bundle in the
        Shell Card Platform. Once the card bundle is deleted the usage and
        product restrictions of the cards that were present in the bundle will
        be reset based on the request.
        #### Supported operations
          * Delete card bundle by bundle Id
        #### Validation rules
          The following are the key validation rules with the associated error
        codes for failed validation-
          *  `7019` - The given card bundle is not available in the Shell Card
        Platform. 
          *  `0007` - Error returned if request parameters fail validation
        e.g. mandatory check.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (DeleteBundleRequest, optional): Update Bundle request body

        Returns:
            DeleteBundleResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v1/restriction/deletebundle')
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
            .deserialize_into(DeleteBundleResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()

    def summary_of_bundles(self,
                           apikey,
                           request_id,
                           body=None):
        """Does a POST request to /fleetmanagement/v1/restriction/summaryofbundles.

        This API allows clients to get a summary of card bundles associated
        with Payer/Account. This API will return the basic bundle details
        including card and restriction details. Optionally the API will also
        include a count of cards that are not associated with the bundle but
        returned by the search criteria.
        Note - to include count of cards of an account that are not associated
        with any bundles, in the input parameter SearchCardBundles either pass
        all the bundles of the account in the list or pass only account with
        bundle id left blank/null.
        #### Supported operations
          * Get summary of bundles by list of bundle Ids

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (SummaryofbundlerRequest, optional): Summary of Bundle
                request body

        Returns:
            SummaryofbundleResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v1/restriction/summaryofbundles')
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
            .deserialize_into(SummaryofbundleResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()

    def restriction_account(self,
                            apikey,
                            request_id,
                            body=None):
        """Does a POST request to /fleetmanagement/v1/restriction/account.

        This API allows setting or updating the usage restrictions of an
        existing account. 
        Then validation rules applied for this API.
        •    The account exists.
        •    Day time restriction cannot be set to restrict the use of a card,
        under the account, on all days of the week.
        •    Either of the usage, daytime or location is either marked for
        reset or new restriction values provided for the account.
        •    In usage restrictions, the limits per transaction should be less
        than or equal to Daily, Daily should be less than or equal to Weekly,
        Weekly should be less than or equal to Monthly. Exception being
        0/blank will be skipped, i.e., Daily value should be less than equal
        to Monthly value if Weekly value is 0/blank.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (AccountRestrictionRequest, optional): Account Restriction
                request body

        Returns:
            AccountRestrictionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v1/restriction/account')
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
            .auth(Single('BearerToken'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(AccountRestrictionResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()

    def search_account_limit(self,
                             apikey,
                             request_id,
                             body=None):
        """Does a POST request to /fleetmanagement/v1/restriction/searchaccountlimit.

        This API will allow user to get account level limits for the given
        account. It returns the velocity limits if its overridden at the
        account else the values will be null/empty.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (SearchAccountLimitRequest, optional): Search Account Limit
                RequestBody

        Returns:
            SearchAccountLimitResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v1/restriction/searchaccountlimit')
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
            .deserialize_into(SearchAccountLimitResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()

    def bundle_details(self,
                       apikey,
                       request_id,
                       body=None):
        """Does a POST request to /fleetmanagement/v1/restriction/bundledetails.

        This API allows to get the details of a specific card bundle. It
        returns the bundle basic details along with the cards in the bundle
        and restrictions applied on them.

        Args:
            apikey (str): This is the API key of the specific environment
                which needs to be passed by the client.
            request_id (str): Mandatory UUID (according to RFC 4122 standards)
                for requests and responses. This will be played back in the
                response from the request.
            body (BudleDetailsRequest, optional): Bundle Details Request body

        Returns:
            BundleDetailsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SHELL)
            .path('/fleetmanagement/v1/restriction/bundledetails')
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
            .deserialize_into(BundleDetailsResponse.from_dictionary)
            .local_error('400', 'The server cannot or will not process the request  due to something that is perceived to be a client\r\n error (e.g., malformed request syntax, invalid \r\n request message framing, or deceptive request routing).', APIException)
            .local_error('401', 'The request has not been applied because it lacks valid  authentication credentials for the target resource.', APIException)
            .local_error('403', 'The server understood the request but refuses to authorize it.', APIException)
            .local_error('404', 'The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists.', APIException)
            .local_error('500', 'The server encountered an unexpected condition the prevented it from fulfilling the request.', APIException)
        ).execute()
