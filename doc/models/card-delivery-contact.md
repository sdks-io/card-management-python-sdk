
# Card Delivery Contact

Request entity object for CardDeliveryContact
Mandatory when CardDeliveryType is 2 else ignored.

## Structure

`CardDeliveryContact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `delivery_contact_title` | `str` | Optional | Title of the contact person <br /><br>Optional<br>Max field length: 10<br>**Constraints**: *Maximum Length*: `10` |
| `delivery_contact_name` | `str` | Required | Name of the contact person <br /><br>Mandatory  <br /><br>Max field length: 50<br>**Constraints**: *Maximum Length*: `50` |
| `delivery_company_name` | `str` | Required | Company name <br /><br>Mandatory  <br /><br>Max field length: 50<br>**Constraints**: *Maximum Length*: `50` |
| `delivery_address_line_1` | `str` | Required | Address line 1 <br /><br>Mandatory<br /><br>Max field length: 40<br>**Constraints**: *Maximum Length*: `40` |
| `delivery_address_line_2` | `str` | Optional | Address line 2 <br /><br>Optional <br /><br>Max field length: 40  <br /><br>Optional<br>**Constraints**: *Maximum Length*: `40` |
| `delivery_address_line_3` | `str` | Optional | Address line 3 <br /><br>Optional <br /><br>Max field length: 40  <br /><br>Optional<br>**Constraints**: *Maximum Length*: `40` |
| `delivery_zip_code` | `str` | Required | ZIP code <br /><br>Mandatory  <br /><br>Max field length: 10  <br /><br>Optional<br>**Constraints**: *Maximum Length*: `10` |
| `delivery_city` | `str` | Required | City  <br /><br>Mandatory  <br /><br>Max field length: 40<br>**Constraints**: *Maximum Length*: `40` |
| `delivery_region_id` | `int` | Optional | Region Id  <br /><br>Optional |
| `delivery_region` | `str` | Optional | Region  <br /><br>Optional<br /><br>When region is passed |
| `delivery_country` | `str` | Required | The ISO code of the country.<br /> |
| `phone_number` | `str` | Optional | Phone number for courier delivery.<br /><br>Optional.<br /><br>Max field length: 20<br>**Constraints**: *Maximum Length*: `20` |
| `email_address` | `str` | Optional | Email address for courier delivery.<br /><br>Optional.<br /><br>Max field length: 90 <br/>Note:Based on the international standard that there can be Max Length 64 before the @ (the 'Local part’) =64(minimum of 1) Max Lenth after the (the domain) = 88 (Minimum of 2)<br>**Constraints**: *Maximum Length*: `90` |
| `save_for_card_reissue` | `bool` | Optional | If this is specified, the contact address will be saved in cards platform for card reissue processing.<br /><br>Optional |

## Example (as JSON)

```json
{
  "DeliveryContactTitle": "DeliveryContactTitle0",
  "DeliveryContactName": "DeliveryContactName6",
  "DeliveryCompanyName": "DeliveryCompanyName4",
  "DeliveryAddressLine1": "DeliveryAddressLine14",
  "DeliveryAddressLine2": "DeliveryAddressLine26",
  "DeliveryAddressLine3": "DeliveryAddressLine38",
  "DeliveryZipCode": "DeliveryZipCode6",
  "DeliveryCity": "DeliveryCity8",
  "DeliveryRegionId": 216,
  "DeliveryRegion": "DeliveryRegion2",
  "DeliveryCountry": "DeliveryCountry6"
}
```

