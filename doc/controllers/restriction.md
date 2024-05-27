# Restriction

APIs for Retrieve and Update restriction on cards

```python
restriction_controller = client.restriction
```

## Class Name

`RestrictionController`

## Methods

* [Restriction Bundle Create](../../doc/controllers/restriction.md#restriction-bundle-create)
* [Restriction Bundle Update](../../doc/controllers/restriction.md#restriction-bundle-update)
* [Restriction Bundle Delete](../../doc/controllers/restriction.md#restriction-bundle-delete)
* [Restriction Bundle Summary](../../doc/controllers/restriction.md#restriction-bundle-summary)
* [Card Restriction](../../doc/controllers/restriction.md#card-restriction)
* [Account Restriction](../../doc/controllers/restriction.md#account-restriction)
* [Search Account Limit](../../doc/controllers/restriction.md#search-account-limit)
* [Search Card Restriction](../../doc/controllers/restriction.md#search-card-restriction)


# Restriction Bundle Create

This API enables clients to create a new card bundle and apply restrictions.

#### Supported operations

* Create bundle and include mandatory -
  * Usage, day/time, product and location restrictions
  * List of cards to add to bundle
* Create bundle and include optional identifier of bundle in external system

#### Validation rules

The following are the key validation rules with the associated error codes for failed validation-

* `7012` - At least one card must be added to the bundle
* `7011` - The total number of cards passed in the input must be 500 or less.
* `7014` - All the cards passed in the input are part of the selected account.
* `7013` - At least one restriction must be applied to the bundle i.e. either of usage, day/time, location or product restriction.
* `7005` - Day time restriction cannot be set to restrict the use of a card on all days of the week.
* `7000` - Usage restriction of the bundle is not open ended i.e. all the limits within the usage restriction must not be set to 0/null.
* `7004` - In the usage restrictions, the limits per transaction should be less than or equal to Daily, Daily should be less than or equal to Weekly, Weekly should be less than or equal to Monthly. Exception being 0/blank will be skipped, i.e. Daily value should be less than equal to Monthly value if Weekly value is 0/blank.
* `0007` - Error returned if request parameters fail validation e.g. mandatory check.

```python
def restriction_bundle_create(self,
                             request_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`CreateBundleRequest`](../../doc/models/create-bundle-request.md) | Body, Optional | Create Bundle Request body |

## Response Type

[`CreateBundleResponse`](../../doc/models/create-bundle-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = CreateBundleRequest(
    description='',
    cards=[
        '7077141000589242081',
        '7077141000589242099'
    ],
    col_co_id=14,
    payer_id=22884,
    account_id=22884,
    external_bundle_id='SIT3Bundle04FEB-2',
    restrictions=CreateBundleRequestRestrictions(
        usage_restriction_action='None',
        day_time_restriction_action='Add',
        location_restriction_action='Add',
        day_time_restrictions=DayTimeRestrictions(
            friday=True,
            monday=False,
            saturday=True,
            sunday=True,
            thursday=False,
            time_from='03:10:00',
            time_to='12:00:00',
            tuesday=False,
            wednesday=False
        ),
        location_restrictions=LocationRestrictions(),
        product_restrictions=ProductRestrictions(
            products=[
                '010',
                '011'
            ]
        ),
        usage_restrictions=UsageRestrictions(
            daily_spend=1000,
            monthly_spend=14000,
            per_transaction_spend=800,
            daily_volume=10,
            weekly_volume=100,
            monthly_volume=1000,
            per_transaction_volume=10,
            daily_transaction_count=3,
            weekly_transaction_count=9,
            monthly_transaction_count=20
        )
    )
)

result = restriction_controller.restriction_bundle_create(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "254745ea-7573-4eed-e714-f2a42506dba0",
  "Status": "Success",
  "Data": [
    {
      "BundleId": "31183",
      "Cards": null,
      "DayTimeRestrictionProfileId": "33395",
      "LocationRestrictionProfileId": "32326",
      "ProductRestrictionProfileId": "38029"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Restriction Bundle Update

This API enables clients to update an existing card bundle and its associated restrictions.

#### Supported operations

* Add new cards to an existing bundle
* Remove cards from existing bundle
* Update restrictions applied to existing bundle

The following are the key validation rules with the associated error codes for failed validation-

#### Validation rules

* `9007` - The cards must exist in the cards platform for adding or removing cards.
* `7014` - All the cards passed in the input are part of the selected account.
* `7018` - All the cards passed in the input are part of the selected bundle.
* `7011` - The total number of cards passed in the input must be 500 or less.
* `7012` - The action to remove cards should not result in removing all the cards from the bundle.
* `7016` - At least one restriction must be modified for â€œUpdateâ€ request action.
* `7013` - All restrictions cannot be marked for â€œResetâ€ for â€œUpdateâ€ request action.
* `7005` - Day time restriction cannot be set to restrict the use of a card on all days of the week. This validation is applicable for Update request action.
* `7000` - Usage restriction of the bundle is not open ended i.e., all the limits within the usage restriction must not be set to 0/null. This validation is applicable for Update request action.
* `7004` - In the usage restrictions, the limits per transaction should be less than or equal to Daily, Daily should be less than or equal to Weekly, Weekly should be less than or equal to Monthly. Exception being 0/blank will be skipped, i.e., Daily value should be less than equal to Monthly value if Weekly value is 0/blank. This validation is applicable for Update request action.
* `0007` - Error returned if request parameters fail validation e.g. at least one card must be provided in the input.

```python
def restriction_bundle_update(self,
                             request_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`UpdateBundleRequest`](../../doc/models/update-bundle-request.md) | Body, Optional | Update Bundle Request body |

## Response Type

[`UpdateBundleResponse`](../../doc/models/update-bundle-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = UpdateBundleRequest(
    bundle_id='2207',
    request_action='Add',
    col_co_id=32,
    payer_id=1223,
    account_id=1223,
    cards=[
        '7077327290224797344'
    ],
    usage_restriction_action='Update',
    restrictions=BundleRestriction()
)

result = restriction_controller.restriction_bundle_update(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "13cb37b6-991f-4f37-c8c2-f4b29c916735",
  "Status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Restriction Bundle Delete

This API enables clients to delete an existing card bundle in the Shell Card Platform. Once the card bundle is deleted the usage and product restrictions of the cards that were present in the bundle will be reset based on the request.

#### Supported operations

* Delete card bundle by bundle Id

#### Validation rules

The following are the key validation rules with the associated error codes for failed validation-

* `7019` - The given card bundle is not available in the Shell Card Platform.
* `0007` - Error returned if request parameters fail validation e.g. mandatory check.

```python
def restriction_bundle_delete(self,
                             request_id,
                             body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`DeleteBundleRequest`](../../doc/models/delete-bundle-request.md) | Body, Optional | Delete Bundle Request body |

## Response Type

[`DeleteBundleResponse`](../../doc/models/delete-bundle-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = DeleteBundleRequest(
    bundle_id='31189',
    col_co_id=14,
    payer_id=22884,
    account_id=22884
)

result = restriction_controller.restriction_bundle_delete(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "13cb37b6-991f-4f37-c8c2-f4b29c916735",
  "Status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Restriction Bundle Summary

This API allows clients to get a summary of card bundles associated with Payer/Account. This API will return the basic bundle details including card and restriction details. Optionally the API will also include a count of cards that are not associated with the bundle but returned by the search criteria.

Note - to include count of cards of an account that are not associated with any bundles, in the input parameter SearchCardBundles either pass all the bundles of the account in the list or pass only account with bundle id left blank/null.

#### Supported operations

* Get summary of bundles by list of bundle Ids

```python
def restriction_bundle_summary(self,
                              request_id,
                              body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`SummaryOfBundleRequest`](../../doc/models/summary-of-bundle-request.md) | Body, Optional | Summary Bundle Request body |

## Response Type

[`SummaryOfBundleResponse`](../../doc/models/summary-of-bundle-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = SummaryOfBundleRequest(
    filters=SummaryofBundle(
        bundle_id=[
            '2343'
        ],
        col_co_id=5,
        payer_number='GB00000235',
        payer_id=291,
        account_id=291,
        account_number='GB00000235'
    )
)

result = restriction_controller.restriction_bundle_summary(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "cf142c58-bdfa-4414-81c5-f099c0c829d7",
  "Status": "Success",
  "Data": [
    {
      "PayerId": 291,
      "PayerNumber": "GB00000235",
      "AccountId": 291,
      "AccountNumber": "GB00000235",
      "CountOfCardsNotInBundle": 205,
      "CardBundles": [
        {
          "BundleId": "1234",
          "ExternalBundleId": "2343",
          "Description": "CardBundle1",
          "TotalCards": 1250
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Card Restriction

This API allows to set or update the restrictions for existing cards or newly ordered cards under the same payer.

#### Supported operations

* Set or reset usage restrictions for cards
* Set or reset day/time restrictions for cards
* Set or reset product restrictions for cards
* Set or reset location restrictions for cards

```python
def card_restriction(self,
                    request_id,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`RestrictionCardRequest`](../../doc/models/restriction-card-request.md) | Body, Optional | Summary Bundle Request body |

## Response Type

[`RestrictionCardResponse`](../../doc/models/restriction-card-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = RestrictionCardRequest(
    col_co_id=5,
    payer_number='GB00000235',
    payer_id=291,
    cards=[
        RestrictionCardRequestCardsItems(
            account_number='GB00000235',
            account_id=291,
            pan='7002057035956000019',
            card_id=205113,
            reset_usage_restrictions=False,
            reset_day_time_restrictions=False,
            reset_product_restrictions=False,
            reset_location_restrictions=False,
            day_time_restrictions=DayTimeRestrictions(
                friday=True,
                monday=True,
                saturday=False,
                sunday=False,
                thursday=True,
                time_from='01:00:00',
                time_to='10:00:00',
                tuesday=True,
                wednesday=True
            ),
            location_restrictions=LocationRestrictions(
                shell_site_restrictions=[
                    LocationRestrictionsShellSiteRestrictionsItems()
                ],
                partner_site_restrictions=[
                    LocationRestrictionsPartnerSiteRestrictionsItems(
                        network_code='0452301643'
                    )
                ]
            ),
            product_restrictions=ProductRestrictions(),
            usage_restrictions=UsageRestrictions(
                daily_spend=1010,
                weekly_spend=1620,
                monthly_spend=15020,
                per_transaction_spend=920,
                daily_volume=10,
                weekly_volume=100,
                monthly_volume=1000,
                per_transaction_volume=10,
                daily_transaction_count=6,
                weekly_transaction_count=18,
                monthly_transaction_count=32
            )
        )
    ]
)

result = restriction_controller.card_restriction(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "MainReference": 1234,
  "RequestId": "cf142c58-bdfa-4414-81c5-f099c0c829d7",
  "Status": "Success",
  "Data": [
    {
      "AccountId": 291,
      "AccountNumber": "GB00000235",
      "CardId": 205113,
      "CardProductReference": null,
      "DayTimeRestrictionDescription": "0000 - Success",
      "DayTimeRestrictionStatus": "Success",
      "LocationRestrictionDescription": "0000 - Success",
      "LocationRestrictionStatus": "Success",
      "PAN": "7002057035956000019",
      "ProductRestrictionDescription": "0000 - Success",
      "ProductRestrictionStatus": "Success",
      "UsageRestrictionDescription": "0000 - Success",
      "UsageRestrictionStatus": "Success",
      "ValidationErrorCode": null,
      "ValidationErrorDescription": null
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Account Restriction

This operation allows setting or updating the usage restrictions of an existing account.

#### Validation rules

* The account exists.
* Day time restriction cannot be set to restrict the use of a card, under the account, on all days of the week.
* Either of the usage, daytime or location is either marked for reset or new restriction values provided for the account.
* In usage restrictions, the limits per transaction should be less than or equal to Daily, Daily should be less than or equal to Weekly, Weekly should be less than or equal to Monthly. Exception being 0/blank will be skipped, i.e., Daily value should be less than equal to Monthly value if Weekly value is 0/blank.

```python
def account_restriction(self,
                       request_id,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`AccountRestrictionRequest`](../../doc/models/account-restriction-request.md) | Body, Optional | Summary Bundle Request body |

## Response Type

[`AccountRestrictionResponse`](../../doc/models/account-restriction-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = AccountRestrictionRequest(
    col_co_id=32,
    col_co_code=3,
    payer_number='CZ00000927',
    account_number='CZ00000928',
    reset_usage_restrictions=False,
    usage_restrictions=UsageRestrictions(
        daily_spend=10,
        weekly_spend=30,
        monthly_spend=100,
        per_transaction_spend=3,
        daily_volume=10,
        weekly_volume=146,
        monthly_volume=625,
        per_transaction_volume=5,
        daily_transaction_count=5,
        weekly_transaction_count=15,
        monthly_transaction_count=20,
        annual_spend=500,
        life_time_spend=50000,
        annual_volume=1000,
        life_time_volume=5000,
        annual_transaction_count=50,
        life_time_transaction_count=100
    )
)

result = restriction_controller.account_restriction(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "18c955d1-b3ec-4dc0-95da-76e67afb891a",
  "Status": "SUCCESS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Search Account Limit

This operation will allow user to get account level limits for the given account.
It returns the velocity limits if its overridden at the account else the values will be null/empty.

```python
def search_account_limit(self,
                        request_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`SearchAccountLimitRequest`](../../doc/models/search-account-limit-request.md) | Body, Optional | Summary Bundle Request body |

## Response Type

[`SearchAccountLimitResponse`](../../doc/models/search-account-limit-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = SearchAccountLimitRequest(
    filters=SearchAccountLimitRequestFilters(
        col_co_id=14,
        col_co_code=14,
        payer_id=1234,
        payer_number='GB99215176',
        account_id=29484,
        account_number='GB99215176'
    )
)

result = restriction_controller.search_account_limit(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "27ec111b-0310-425d-b2a0-0fc2b1bfabb7",
  "Status": "SUCCESS",
  "Data": {
    "AccountId": 29484,
    "AccountNumber": "GB99215176",
    "ReferenceProduct": "021",
    "RestrictionCondition": "DECLINE_ALERT",
    "VelocityLimits": [
      {
        "Type": "VALUE",
        "Period": "DAILY",
        "Limit": 1500.55,
        "Accumulation": 1100.55,
        "Balance": 400.55,
        "Override": true,
        "ProductGroup": "RoadSvc",
        "Threshold": 50.55
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |


# Search Card Restriction

This API will allows querying card details including the day/time and product restrictions.

#### Supported operations

* Search by list of cards or bundle
* Include card bundle details (optional)

```python
def search_card_restriction(self,
                           request_id,
                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Header, Required | Mandatory UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `body` | [`RestrictionSearchCardRequest`](../../doc/models/restriction-search-card-request.md) | Body, Optional | Summary Bundle Request body |

## Response Type

[`RestrictionSearchCardResponse`](../../doc/models/restriction-search-card-response.md)

## Example Usage

```python
request_id = 'RequestId8'

body = RestrictionSearchCardRequest(
    filters=RestrictionSearchCardRequestFilters(
        col_co_code=32,
        col_co_id=32,
        payer_number='CZ00000923',
        payer_id=1223,
        bundle_id='BundleId8',
        cards=[
            RestrictionSearchCardRequestFiltersCardsItems(
                pan='7077327290223419353',
                card_id=459629
            )
        ],
        include_location_restrictions=True,
        include_inherited_limits=True,
        include_bundle_details=True
    )
)

result = restriction_controller.search_card_restriction(
    request_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "RequestId": "cf142c58-bdfa-4414-81c5-f099c0c829d7",
  "Status": "Success",
  "Data": [
    {
      "BundleId": 100,
      "Restrictions": {
        "DayTimeRestrictions": {
          "Friday": true,
          "Monday": true,
          "Saturday": false,
          "Sunday": false,
          "Thursday": true,
          "TimeFrom": "01:00:00",
          "TimeTo": "10:00:00",
          "Tuesday": true,
          "Wednesday": true
        },
        "LocationRestrictions": {
          "CountryRestrictions": {
            "Countries": [
              "203"
            ],
            "Exclusive": true
          },
          "NetworkRestrictions": [
            {
              "Country": "826",
              "Exclusive": false,
              "Networks": [
                "0002003826"
              ]
            }
          ],
          "PartnerSiteRestrictions": [
            {
              "Exclusive": false,
              "NetworkCode": "0452301643",
              "SiteGroups": [
                "P1"
              ],
              "Sites": []
            }
          ],
          "ShellSiteRestrictions": [
            {
              "Country": "276",
              "Exclusive": true,
              "SiteGroups": [
                "P2"
              ],
              "Sites": []
            }
          ]
        },
        "ProductRestrictions": {
          "FuelSetId": 0,
          "FuelSetName": null,
          "NonFuelSets": null,
          "ProductGroups": [
            {
              "IsDefault": true,
              "IsFuelType": true,
              "Name": "Premium Diesel",
              "ProductGroupId": "P103",
              "Products": [
                {
                  "Description": "High Performance Diesel",
                  "GlobalProductCode": "033"
                }
              ],
              "ReferenceId": 100
            }
          ],
          "Products": [],
          "PurchaseCategoryCode": "",
          "PurchaseCategoryId": 0
        },
        "UsageRestrictions": {
          "AnnualSpend": 9999999999.99,
          "AnnualSpendAccumulated": 0,
          "AnnualSpendBalance": 9999999999.99,
          "AnnualTransactionAccumulated": 0,
          "AnnualTransactionBalance": 999999999999,
          "AnnualTransactionCount": 999999999999,
          "AnnualVolume": 9999999999.99,
          "AnnualVolumeAccumulated": 0,
          "AnnualVolumeBalance": 9999999999.99,
          "DailySpend": 1010,
          "DailySpendAccumulated": 0,
          "DailySpendBalance": 1010,
          "DailyTransactionAccumulated": 0,
          "DailyTransactionBalance": 6,
          "DailyTransactionCount": 6,
          "DailyVolume": 10,
          "DailyVolumeAccumulated": 0,
          "DailyVolumeBalance": 10,
          "Level": "Card",
          "LifeTimeSpend": null,
          "LifeTimeSpendAccumulated": null,
          "LifeTimeSpendBalance": null,
          "LifeTimeTransactionAccumulated": null,
          "LifeTimeTransactionBalance": null,
          "LifeTimeTransactionCount": null,
          "LifeTimeVolume": null,
          "LifeTimeVolumeAccumulated": null,
          "LifeTimeVolumeBalance": null,
          "MonthlySpend": 15020,
          "MonthlySpendAccumulated": 0,
          "MonthlySpendBalance": 15020,
          "MonthlyTransactionAccumulated": 0,
          "MonthlyTransactionBalance": 32,
          "MonthlyTransactionCount": 32,
          "MonthlyVolume": 1000,
          "MonthlyVolumeAccumulated": 0,
          "MonthlyVolumeBalance": 1000,
          "PerTransactionSpend": 920,
          "PerTransactionVolume": 10,
          "WeeklySpend": 1620,
          "WeeklySpendAccumulated": 0,
          "WeeklySpendBalance": 1620,
          "WeeklyTransactionAccumulated": 0,
          "WeeklyTransactionBalance": 18,
          "WeeklyTransactionCount": 18,
          "WeeklyVolume": 100,
          "WeeklyVolumeAccumulated": 0,
          "WeeklyVolumeBalance": 100,
          "AnnualSpendOverride": false,
          "DailySpendOverride": true,
          "LifeTimeSpendOverride": false,
          "MonthlySpendOverride": true,
          "PerTransactionSpendOverride": true,
          "WeeklySpendOverride": true,
          "DailyVolumeOverride": true,
          "WeeklyVolumeOverride": true,
          "MonthlyVolumeOverride": true,
          "PerTransactionVolumeOverride": true,
          "AnnualVolumeOverride": false,
          "LifeTimeVolumeOverride": false,
          "DailyTransactionOverride": true,
          "WeeklyTransactionOverride": true,
          "MonthlyTransactionOverride": true,
          "AnnualTransactionOverride": false,
          "LifeTimeTransactionOverride": false
        }
      },
      "RestrictionCurrencyCode": "CZK",
      "RestrictionCurrencySymbol": "Kč",
      "AccountId": 1223,
      "AccountName": "NewtestPandB",
      "AccountNumber": "CZ00000923",
      "AccountShortName": "NewtestPandB",
      "CardId": 459629,
      "CardTypeCode": "7077327",
      "CardTypeId": 105,
      "CardTypeName": "CZ CRT INT MUL R7",
      "ColCoCurrencyCode": "CZK",
      "ColCoCurrencySymbol": "Kč",
      "CurrencyCode": "EUR",
      "CurrencySymbol": "€",
      "DriverName": "XYZ 1504",
      "ExpiryDate": "20240731",
      "IsCRT": true,
      "IsFleet": false,
      "IsInternational": true,
      "IsNational": false,
      "IsPartnerSitesIncluded": true,
      "IsShellSitesOnly": false,
      "IssueDate": "20200722",
      "IssueNumber": 1,
      "IsSuperseded": false,
      "IsVirtualCard": false,
      "PAN": "7077327290223419353",
      "PurchaseCategoryCode": "0",
      "PurchaseCategoryId": 100,
      "PurchaseCategoryName": "0 - Diesel Products and TMF",
      "StatusDescription": "Active",
      "StatusId": 1,
      "VRN": "ABC 1504",
      "MediumTypeID": 5,
      "MediumType": "Key fob"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing). | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 401 | The request has not been applied because it lacks valid  authentication credentials for the target resource. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 403 | Forbidden | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 404 | The origin server did not find a current representation  for the target resource or is not willing to disclose  that one exists. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |
| 500 | The server encountered an unexpected condition that  prevented it from fulfilling the request. | [`ErrorObjectException`](../../doc/models/error-object-exception.md) |

