# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MessagingEndpointProperties(Model):
    """The properties of the Messaging Endpoints used by this IoT Hub.

    :param lock_duration_as_iso8601: The lock duration. Range: 5 Sec (PT5S) -
     5 Min (PT5M).
    :type lock_duration_as_iso8601: timedelta
    :param ttl_as_iso8601: The time to live. Range: 1 Min (PT1M) - 2 Days
     (P2D).
    :type ttl_as_iso8601: timedelta
    :param max_delivery_count: The max delivery count. Range: 1-100.
    :type max_delivery_count: int
    """ 

    _validation = {
        'max_delivery_count': {'maximum': 100, 'minimum': 1},
    }

    _attribute_map = {
        'lock_duration_as_iso8601': {'key': 'lockDurationAsIso8601', 'type': 'duration'},
        'ttl_as_iso8601': {'key': 'ttlAsIso8601', 'type': 'duration'},
        'max_delivery_count': {'key': 'maxDeliveryCount', 'type': 'int'},
    }

    def __init__(self, lock_duration_as_iso8601=None, ttl_as_iso8601=None, max_delivery_count=None):
        self.lock_duration_as_iso8601 = lock_duration_as_iso8601
        self.ttl_as_iso8601 = ttl_as_iso8601
        self.max_delivery_count = max_delivery_count
