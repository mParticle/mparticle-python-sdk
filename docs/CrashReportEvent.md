# CrashReportEvent

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
**breadcrumbs** | [**list[BreadcrumbEvent]**](BreadcrumbEvent.md) |  | [optional] 
**class_name** | **str** |  | 
**severity** | **str** |  | [optional] 
**message** | **str** |  | 
**stack_trace** | **str** |  | 
**exception_handled** | **bool** |  | 
**topmost_context** | **str** |  | [optional] 
**pl_crash_report_file_base64** | **str** |  | [optional] 
**ios_image_base_address** | **int** |  | [optional] 
**ios_image_size** | **int** |  | [optional] 
**session_number** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


