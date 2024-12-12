
# Update Card

Request entity object for UpdateCardRequest  list

## Structure

`UpdateCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `caller` | `str` | Optional | The caller to be notified with the status of the update card status request. <br /><br>The caller will also be notified with the status of the replacement card order request, if any.<br /><br>Mandatory, if NotifyCaller is true. <br /><br>Maximum field length: 20<br /><br>Allowed values:<br /><br><br>- NextGenUI: This value to be used by next gen UI application.<br /><br>- Motix: This value to be used by MOTiX application.<br /><br>- FleetHubUILifeTime: This value to be used by Fleet Hub UI application for life time restriction cards.<br /><br>  Note: The values passed in this field are case insensitive. |
| `is_replacement_chargeable` | `bool` | Optional | True/False<br /><br>Optional<br /><br>When not provided will considered as default value as True.<br /><br>If passed True, the replacement card will be chargeable, else replacement card will not be charged. |
| `notify_caller` | `bool` | Optional | True/False.<br /><br>Optional.<br /><br>Default: False<br /><br>If true, the caller would be notified back with the status as success or failure after the update card status request is processed.<br>Notification API subscription required to use this feature , please refer API documetation for more details |
| `notify_caller_on_sync` | `bool` | Optional | True/False.<br /><br>Optional.<br /><br>Default: False<br /><br>If true, the caller would be notified back with the status as success or failed after the replacement card is synced with Gateway, if a replacement card was requested. |
| `order_card_replacement` | `bool` | Optional | True/False.<br /><br>Pass True if a replacement order card request is to be placed, else False.<br /><br>Optional.Default value False.<br /><br>Replacement of a card is only applicable when the target status requested is either permanently Block or Damaged for the existing card.<br /><br>Request for Replacement card will be placed only when the Block card or Block damaged card request is successfully placed.<br /><br>The Replacement card request will be processed only when the permanent Block card request is successfully processed. <br /><br>In case of damaged card request, the replacement card request will be processed immediately. |
| `card_settings` | [`CardSettings`](../../doc/models/card-settings.md) | Optional | - |
| `account_id` | `int` | Optional | Account Id of the customer.<br /><br>Optional if AccountNumber is passed, else Mandatory. |
| `account_number` | `str` | Optional | Account Number of the customer.<br /><br>Optional if AccountId is passed, else Mandatory. |
| `card_expiry_date` | `str` | Optional | Expiry date of the card.<br /><br>Mandatory if PAN is passed, else optional.<br /><br>Format: yyyyMMdd |
| `card_id` | `int` | Optional | Card Id of the card.<br /><br>Optional if PAN is passed, else Mandatory. |
| `col_co_code` | `int` | Optional | Collecting company code of the customer. <br /><br>Optional if ColCoId is passed, else Mandatory.<br /> |
| `col_co_id` | `int` | Optional | Collecting company id of the customer. <br /><br>Optional if ColCoCode is passed, else Mandatory.<br /> |
| `pan` | `str` | Optional | PAN of the card.<br /><br>Optional if CardId is passed, else Mandatory.<br /> |
| `panid` | `float` | Optional | PANID of the card |
| `payer_id` | `int` | Optional | Payer id of the customer.<br /><br>Optional if PayerNumber is passed, else Mandatory. |
| `payer_number` | `str` | Optional | PayerNumber of the customer.<br /><br>Optional if PayerId is passed, else Mandatory. |

## Example (as JSON)

```json
{
  "Caller": "Caller6",
  "IsReplacementChargeable": false,
  "NotifyCaller": false,
  "NotifyCallerOnSync": false,
  "OrderCardReplacement": false
}
```

