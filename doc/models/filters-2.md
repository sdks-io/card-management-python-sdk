
# Filters 2

## Structure

`Filters2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account ID of the customer.<br/> Optional if AccountNumber is passed, else mandatory. <br/> This input is a search criterion, if given. |
| `account_number` | `str` | Optional | Account Number of the customer.<br/> Optional if AccountId is passed, else mandatory.<br/> This input is a search criterion, if given. |
| `col_co_code` | `int` | Optional | Collecting Company Code (Shell Code) of the selected payer. <br /><br>Optional – when ‘ReferenceNumber’ is provided.<br /> |
| `col_co_id` | `int` | Optional | Collecting Company Id (in ) of the selected payer. <br /><br>Optional – when ‘ReferenceNumber’ is provided. Else, either ‘ColCoId’ or ‘ColCoCode’ is mandatory.<br /> |
| `col_co_country_code` | `str` | Optional | ISO 3166 Alpha-2 Country Code for the customer and card owning country. |
| `payer_id` | `int` | Optional | Payer Id (i.e. Customer Id of the Payment Customer) of the selected payer.<br /><br>Optional – when ‘ReferenceNumber’ is provided. Else, either ‘PayerId’ or ‘PayerNumber’ is mandatory. |
| `payer_number` | `str` | Optional | Payer Number of the selected payer.<br /><br>Optional – when ‘ReferenceNumber’ is provided. Else, either ‘PayerId’ or ‘PayerNumber’ is mandatory. |
| `reference_number` | `int` | Optional | Reference number of the Card Order/ Bulk Card Order/ Order Card Request.<br /><br>Mandatory when ColCo and Payer fields are not provided. Else, optional. |
| `reference_type` | [`OrderCardEnquiryReqReferenceTypeEnum`](../../doc/models/order-card-enquiry-req-reference-type-enum.md) | Optional | - |
| `from_date` | `str` | Optional | Card Orders from Date/Time.<br /><br>Optional.<br /><br>Value should be with in last 7 days<br /><br>This field is ignored if ReferenceNumber is provided <br /><br>This field is optional when not provided and ReferenceNumber is null or empty then the value should be set to D-7(Where D is current date)<br /><br>Format: yyyyMMdd |
| `to_date` | `str` | Optional | Card Order to Date/Time<br /><br>Optional<br /><br>Value should be with in last 7 days<br /><br>This field is ignored if ReferenceNumber is provided <br /><br>This field is optional when not provided and ReferenceNumber is null or empty then the value should be set to current date<br /><br>Format: yyyyMMdd |
| `order_request_id` | `str` | Optional | Client provided Unique Id of the original Order Card request, the status of which is enquired by this API |

## Example (as JSON)

```json
{
  "ColCoCountryCode": "PH",
  "OrderRequestId": "ed557f02-c7d7-4c01-b3e5-11bf",
  "AccountId": 174,
  "AccountNumber": "AccountNumber6",
  "ColCoCode": 80,
  "ColCoId": 66
}
```

