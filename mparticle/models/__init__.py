# coding: utf-8

"""
    mParticle

    mParticle Event API

    OpenAPI spec version: 1.0.1
    Contact: support@mparticle.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into model package
from .api_response import ApiResponse
from .api_response_errors import ApiResponseErrors
from .app_event import AppEvent
from .application_information import ApplicationInformation
from .application_state_transition_event import ApplicationStateTransitionEvent
from .attribution_info import AttributionInfo
from .batch import Batch
from .breadcrumb_event import BreadcrumbEvent
from .ccpa_consent_state import CCPAConsentState
from .commerce_event import CommerceEvent
from .consent_state import ConsentState
from .crash_report_event import CrashReportEvent
from .device_current_state import DeviceCurrentState
from .device_information import DeviceInformation
from .event_base import EventBase
from .event_data import EventData
from .first_run_event import FirstRunEvent
from .gdpr_consent_state import GDPRConsentState
from .geo_location import GeoLocation
from .media_info import MediaInfo
from .network_performance_event import NetworkPerformanceEvent
from .opt_out_event import OptOutEvent
from .product import Product
from .product_action import ProductAction
from .product_impression import ProductImpression
from .profile_event import ProfileEvent
from .promotion import Promotion
from .promotion_action import PromotionAction
from .push_message_event import PushMessageEvent
from .push_registration_event import PushRegistrationEvent
from .screen_view_event import ScreenViewEvent
from .session_end_event import SessionEndEvent
from .session_start_event import SessionStartEvent
from .shopping_cart import ShoppingCart
from .source_information import SourceInformation
from .user_identities import UserIdentities
from .batch_context import BatchContext
from .data_plan_context import DataPlanContext
from .user_attribute_change_event import UserAttributeChangeEvent
