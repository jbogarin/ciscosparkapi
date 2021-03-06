# -*- coding: utf-8 -*-
"""Cisco Spark Response Codes."""


# Use future for Python v2 and v3 compatibility
from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)
from builtins import *
from past.builtins import basestring


SPARK_RESPONSE_CODES = {
    200: "OK",
    204: "Member deleted.",
    400: "The request was invalid or cannot be otherwise served. An "
         "accompanying error message will explain further.",
    401: "Authentication credentials were missing or incorrect.",
    403: "The request is understood, but it has been refused or access is not "
         "allowed.",
    404: "The URI requested is invalid or the resource requested, such as a "
         "user, does not exist. Also returned when the requested format is "
         "not supported by the requested method.",
    409: "The request could not be processed because it conflicts with some "
         "established rule of the system. For example, a person may not be "
         "added to a room more than once.",
    429: "Too many requests have been sent in a given amount of time and the "
         "request has been rate limited. A Retry-After header should be "
         "present that specifies how many seconds you need to wait before a "
         "successful request can be made.",
    500: "Something went wrong on the server.",
    503: "Server is overloaded with requests. Try again later."
}

RATE_LIMIT_RESPONSE_CODE = 429

EXPECTED_RESPONSE_CODE = {
    'GET': 200,
    'POST': 200,
    'PUT': 200,
    'DELETE': 204
}
