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

import os
import sys
import unittest

import mparticle
from mparticle.rest import ApiException
from mparticle.models.commerce_event import CommerceEvent


class TestCommerceEvent(unittest.TestCase):
    """ CommerceEvent unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommerceEvent(self):
        event = mparticle.models.commerce_event.CommerceEvent(
            product_action={})
        pass

    def testCommerceEventAttributeValues(self):
        with self.assertRaises(ValueError):
            event = mparticle.models.commerce_event.CommerceEvent(product_action={},
                                                                  custom_attributes={
                                                                      'example attribute key': ['something']}
                                                                  )

        event = mparticle.models.commerce_event.CommerceEvent(
            product_action={})

        with self.assertRaises(ValueError):
            event.custom_attributes = {'example attribute key': ['something']}
        pass

    def testCommerceEventCustomAttributes(self):
        custom_flags = {
            "foo": 'bar',
            'answer': 42,
            'arrays': [
                'foo', 'bar', 'baz'
            ]
        }

        event = mparticle.models.commerce_event.CommerceEvent(
            product_action='test',
            custom_flags=custom_flags)

        event_dict = event.to_dict()

        self.assertEqual("bar", event_dict["custom_flags"]["foo"])
        self.assertEqual(42, event_dict["custom_flags"]["answer"])
        self.assertEqual(
            ['foo', 'bar', 'baz'],
            event_dict["custom_flags"]["arrays"])


if __name__ == '__main__':
    unittest.main()
