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
import re


class DataPlanContext(object):

    def __init__(self, plan_id=None, plan_version=None):
        """
        DataPlanContext - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'plan_id': 'str',
            'plan_version': 'int'
        }

        self.attribute_map = {
            'plan_id': 'plan_id',
            'plan_version': 'plan_version'
        }

        self._plan_id = plan_id
        self._plan_version = plan_version

    @property
    def plan_id(self):
        """
        Gets the plan_id of this DataPlanContext.


        :return: The plan_id of this DataPlanContext.
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """
        Sets the plan_id of this DataPlanContext.


        :param plan_id: The plan_id of this DataPlanContext.
        :type: str
        """

        self._plan_id = plan_id

    @property
    def plan_version(self):
        """
        Gets the plan_version of this DataPlanContext.


        :return: The plan_version of this DataPlanContext.
        :rtype: int
        """
        return self._plan_version

    @plan_version.setter
    def plan_version(self, plan_version):
        """
        Sets the plan_version of this DataPlanContext.


        :param plan_version: The plan_version of this DataPlanContext.
        :type: int
        """

        self._plan_version = plan_version

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
