# EventData

## Properties

| Name                      | Type                                            | Description | Notes      |
| ------------------------- | ----------------------------------------------- | ----------- | ---------- |
| **timestamp_unixtime_ms** | **int**                                         |             | [optional] |
| **event_id**              | **int**                                         |             | [optional] |
| **source_message_id**     | **str**                                         |             | [optional] |
| **session_id**            | **int**                                         |             | [optional] |
| **session_uuid**          | **str**                                         |             | [optional] |
| **custom_attributes**     | **dict(str, str)**                              |             | [optional] |
| **location**              | [**GeoLocation**](GeoLocation.md)               |             | [optional] |
| **device_current_state**  | [**DeviceCurrentState**](DeviceCurrentState.md) |             | [optional] |
| **custom_flags**          | **dict(str, str)**                              |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
