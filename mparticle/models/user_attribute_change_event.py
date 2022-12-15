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

from pprint import pformat

from six import iteritems


class UserAttributeChangeEvent(object):

    def __init__(self, timestamp_unixtime_ms=None, event_id=None, source_message_id=None, session_id=None, session_uuid=None, custom_attributes=None, location=None,
                 device_current_state=None, user_attribute_name=None, new=None, old=None, deleted=None, is_new_attribute=None):
        """
        UserAttributeChangeEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'timestamp_unixtime_ms': 'int',
            'event_id': 'int',
            'source_message_id': 'str',
            'session_id': 'int',
            'session_uuid': 'str',
            'custom_attributes': 'dict(str, str)',
            'location': 'GeoLocation',
            'device_current_state': 'DeviceCurrentState',
            'user_attribute_name': 'str',
            'new': 'object',
            'old': 'object',
            'deleted': 'bool',
            'is_new_attribute': 'bool'
        }

        self.attribute_map = {
            'timestamp_unixtime_ms': 'timestamp_unixtime_ms',
            'event_id': 'event_id',
            'source_message_id': 'source_message_id',
            'session_id': 'session_id',
            'session_uuid': 'session_uuid',
            'custom_attributes': 'custom_attributes',
            'location': 'location',
            'device_current_state': 'device_current_state',
            'user_attribute_name': 'user_attribute_name',
            'new': 'new',
            'old': 'old',
            'deleted': 'deleted',
            'is_new_attribute': 'is_new_attribute'
        }

        self._timestamp_unixtime_ms = timestamp_unixtime_ms
        self._event_id = event_id
        self._source_message_id = source_message_id
        self._session_id = session_id
        self._session_uuid = session_uuid
        self._custom_attributes = custom_attributes
        self._location = location
        self._device_current_state = device_current_state
        self._user_attribute_name = user_attribute_name
        self._new = new
        self._old = old
        self._deleted = deleted
        self._is_new_attribute = is_new_attribute

    @property
    def timestamp_unixtime_ms(self):
        """
        Gets the timestamp_unixtime_ms of this UserAttributeChangeEvent.


        :return: The timestamp_unixtime_ms of this UserAttributeChangeEvent.
        :rtype: int
        """
        return self._timestamp_unixtime_ms

    @timestamp_unixtime_ms.setter
    def timestamp_unixtime_ms(self, timestamp_unixtime_ms):
        """
        Sets the timestamp_unixtime_ms of this UserAttributeChangeEvent.


        :param timestamp_unixtime_ms: The timestamp_unixtime_ms of this UserAttributeChangeEvent.
        :type: int
        """

        self._timestamp_unixtime_ms = timestamp_unixtime_ms

    @property
    def event_id(self):
        """
        Gets the event_id of this UserAttributeChangeEvent.


        :return: The event_id of this UserAttributeChangeEvent.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this UserAttributeChangeEvent.


        :param event_id: The event_id of this UserAttributeChangeEvent.
        :type: int
        """

        self._event_id = event_id

    @property
    def source_message_id(self):
        """
        Gets the source_message_id of this UserAttributeChangeEvent.


        :return: The source_message_id of this UserAttributeChangeEvent.
        :rtype: str
        """
        return self._source_message_id

    @source_message_id.setter
    def source_message_id(self, source_message_id):
        """
        Sets the source_message_id of this UserAttributeChangeEvent.


        :param source_message_id: The source_message_id of this UserAttributeChangeEvent.
        :type: str
        """

        self._source_message_id = source_message_id

    @property
    def session_id(self):
        """
        Gets the session_id of this UserAttributeChangeEvent.


        :return: The session_id of this UserAttributeChangeEvent.
        :rtype: int
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this UserAttributeChangeEvent.


        :param session_id: The session_id of this UserAttributeChangeEvent.
        :type: int
        """

        self._session_id = session_id

    @property
    def session_uuid(self):
        """
        Gets the session_uuid of this UserAttributeChangeEvent.


        :return: The session_uuid of this UserAttributeChangeEvent.
        :rtype: str
        """
        return self._session_uuid

    @session_uuid.setter
    def session_uuid(self, session_uuid):
        """
        Sets the session_uuid of this UserAttributeChangeEvent.


        :param session_uuid: The session_uuid of this UserAttributeChangeEvent.
        :type: str
        """

        self._session_uuid = session_uuid

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this UserAttributeChangeEvent.


        :return: The custom_attributes of this UserAttributeChangeEvent.
        :rtype: dict(str, str)
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this UserAttributeChangeEvent.


        :param custom_attributes: The custom_attributes of this UserAttributeChangeEvent.
        :type: dict(str, str)
        """

        self._custom_attributes = custom_attributes

    @property
    def location(self):
        """
        Gets the location of this UserAttributeChangeEvent.


        :return: The location of this UserAttributeChangeEvent.
        :rtype: GeoLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this UserAttributeChangeEvent.


        :param location: The location of this UserAttributeChangeEvent.
        :type: GeoLocation
        """

        self._location = location

    @property
    def device_current_state(self):
        """
        Gets the device_current_state of this UserAttributeChangeEvent.


        :return: The device_current_state of this UserAttributeChangeEvent.
        :rtype: DeviceCurrentState
        """
        return self._device_current_state

    @device_current_state.setter
    def device_current_state(self, device_current_state):
        """
        Sets the device_current_state of this UserAttributeChangeEvent.


        :param device_current_state: The device_current_state of this UserAttributeChangeEvent.
        :type: DeviceCurrentState
        """

        self._device_current_state = device_current_state

    @property
    def user_attribute_name(self):
        """
        Gets the user_attribute_name of this UserAttributeChangeEvent.


        :return: The user_attribute_name of this UserAttributeChangeEvent.
        :rtype: bool
        """
        return self._user_attribute_name

    @user_attribute_name.setter
    def user_attribute_name(self, user_attribute_name):
        """
        Sets the user_attribute_name of this UserAttributeChangeEvent.


        :param user_attribute_name: The user_attribute_name of this UserAttributeChangeEvent.
        :type: bool
        """

        self._user_attribute_name = user_attribute_name

    @property
    def new(self):
        """
        Gets the new property of this UserAttributeChangeEvent.


        :return: The new property of this UserAttributeChangeEvent.
        :rtype: bool
        """
        return self._new

    @new.setter
    def new(self, new):
        """
        Sets the new property of this UserAttributeChangeEvent.


        :param new: The new property of this UserAttributeChangeEvent.
        :type: bool
        """

        self._new = new

    @property
    def old(self):
        """
        Gets the old property of this UserAttributeChangeEvent.


        :return: The old property of this UserAttributeChangeEvent.
        :rtype: bool
        """
        return self._old

    @old.setter
    def old(self, old):
        """
        Sets the old property of this UserAttributeChangeEvent.


        :param old: The old property of this UserAttributeChangeEvent.
        :type: bool
        """

        self._old = old

    @property
    def deleted(self):
        """
        Gets the deleted property of this UserAttributeChangeEvent.


        :return: The deleted property of this UserAttributeChangeEvent.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted property of this UserAttributeChangeEvent.


        :param deleted: The deleted property of this UserAttributeChangeEvent.
        :type: bool
        """

        self._deleted = deleted

    @property
    def is_new_attribute(self):
        """
        Gets the is_new_attribute property of this UserAttributeChangeEvent.


        :return: The is_new_attribute of this UserAttributeChangeEvent.
        :rtype: bool
        """
        return self._is_new_attribute

    @is_new_attribute.setter
    def is_new_attribute(self, is_new_attribute):
        """
        Sets the is_new_attribute property of this UserAttributeChangeEvent.


        :param is_new_attribute: The is_new_attribute of this UserAttributeChangeEvent.
        :type: bool
        """

        self._is_new_attribute = is_new_attribute
        
    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
