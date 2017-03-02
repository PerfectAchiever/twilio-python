# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.exceptions import TwilioException
from twilio.http.response import Response


class AvailablePhoneNumberCountryTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .available_phone_numbers.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json',
        ))

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "countries": [
                    {
                        "beta": false,
                        "country": "Denmark",
                        "country_code": "DK",
                        "subresource_uris": {
                            "local": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/DK/Local.json"
                        },
                        "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/DK.json"
                    }
                ],
                "end": 1,
                "first_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/DK.json?PageSize=50&Page=0",
                "last_page_uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/DK.json?PageSize=50&Page=0",
                "next_page_uri": null,
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .available_phone_numbers.list()

        self.assertIsNotNone(actual)

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "countries": [],
                "end": 1,
                "first_page_uri": null,
                "last_page_uri": null,
                "next_page_uri": null,
                "num_pages": 1,
                "page": 0,
                "page_size": 50,
                "previous_page_uri": null,
                "start": 0,
                "total": 1,
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .available_phone_numbers.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                 .available_phone_numbers(country_code="US").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://api.twilio.com/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US.json',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "beta": null,
                "country": "United States",
                "country_code": "US",
                "subresource_uris": {
                    "local": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/Local.json",
                    "toll_free": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US/TollFree.json"
                },
                "uri": "/2010-04-01/Accounts/ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/AvailablePhoneNumbers/US.json"
            }
            '''
        ))

        actual = self.client.api.v2010.accounts(sid="ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                                      .available_phone_numbers(country_code="US").fetch()

        self.assertIsNotNone(actual)
