# ApplicationStateTransitionEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp_unixtime_ms** | **int** |  | [optional] 
**event_id** | **int** |  | [optional] 
**source_message_id** | **str** |  | [optional] 
**session_id** | **int** |  | [optional] 
**session_uuid** | **str** |  | [optional] 
**custom_attributes** | **dict(str, str)** |  | [optional] 
**location** | [**GeoLocation**](GeoLocation.md) |  | [optional] 
**device_current_state** | [**DeviceCurrentState**](DeviceCurrentState.md) |  | [optional] 
**successfully_closed** | **bool** |  | [optional] 
**is_first_run** | **bool** |  | [optional] 
**is_upgrade** | **bool** |  | [optional] 
**push_notification_payload** | **str** |  | [optional] 
**application_transition_type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


