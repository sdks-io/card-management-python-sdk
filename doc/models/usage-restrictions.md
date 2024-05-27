
# Usage Restrictions

## Structure

`UsageRestrictions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `daily_spend` | `float` | Optional | Maximum spend value (amount) allowed per day.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `weekly_spend` | `float` | Optional | Maximum spend value (amount) allowed per week.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `monthly_spend` | `float` | Optional | Maximum spend value (amount) allowed per month.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `per_transaction_spend` | `float` | Optional | Maximum spend value (amount) allowed per transaction.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `daily_volume` | `int` | Optional | Maximum volume (quantity) allowed per day.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `weekly_volume` | `int` | Optional | Maximum volume (quantity) allowed per week.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `monthly_volume` | `int` | Optional | Maximum volume (quantity) allowed per month.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `per_transaction_volume` | `int` | Optional | Maximum volume (quantity) allowed per transaction.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `daily_transaction_count` | `float` | Optional | Maximum number of transactions allowed per day.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `weekly_transaction_count` | `float` | Optional | Maximum number of transactions allowed per week.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `monthly_transaction_count` | `float` | Optional | Maximum number of transactions allowed per month.<br>Optional.<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `annual_spend` | `float` | Optional | Maximum spend value (amount) allowed per annum.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `life_time_spend` | `float` | Optional | Maximum spend value (amount) allowed in card’s life time.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `annual_volume` | `float` | Optional | Maximum volume (quantity) allowed per annum.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `life_time_volume` | `float` | Optional | Maximum volume (quantity) allowed in card’s life time.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `annual_transaction_count` | `float` | Optional | Maximum number of transactions allowed per annum.<br>Optional.<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |
| `life_time_transaction_count` | `float` | Optional | Maximum number of transactions allowed in card’s lifetime.<br>Optional<br>The value ‘0’ represents not set. If Values is passed as null, will be considered as inherited.<br>Valid range: 0 to 9999999999 |

## Example (as JSON)

```json
{
  "DailySpend": 7.72,
  "WeeklySpend": 10.22,
  "MonthlySpend": 48.66,
  "PerTransactionSpend": 17.28,
  "DailyVolume": 122
}
```

