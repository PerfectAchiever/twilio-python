# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio import deserialize
from twilio import values
from twilio.instance_context import InstanceContext
from twilio.instance_resource import InstanceResource
from twilio.list_resource import ListResource
from twilio.page import Page
from twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension import InstalledAddOnExtensionList


class InstalledAddOnList(ListResource):

    def __init__(self, version):
        """
        Initialize the InstalledAddOnList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnList
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnList
        """
        super(InstalledAddOnList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/InstalledAddOns'.format(**self._solution)

    def create(self, available_add_on_sid, accept_terms_of_service,
               configuration=values.unset, unique_name=values.unset):
        """
        Create a new InstalledAddOnInstance

        :param unicode available_add_on_sid: A string that uniquely identifies the Add-on to install
        :param bool accept_terms_of_service: A boolean reflecting your acceptance of the Terms of Service
        :param dict configuration: The JSON object representing the configuration
        :param unicode unique_name: The string that uniquely identifies this Add-on installation

        :returns: Newly created InstalledAddOnInstance
        :rtype: twilio.rest.preview.twilio.com.marketplace.installed_add_on.InstalledAddOnList
        """
        data = values.of({
            'AvailableAddOnSid': available_add_on_sid,
            'AcceptTermsOfService': accept_terms_of_service,
            'Configuration': configuration,
            'UniqueName': unique_name,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return InstalledAddOnInstance(
            self._version,
            payload,
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams InstalledAddOnInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists InstalledAddOnInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of InstalledAddOnInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InstalledAddOnInstance
        :rtype: Page
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return InstalledAddOnPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a InstalledAddOnContext

        :param sid: The unique Installed Add-on Sid

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        return InstalledAddOnContext(
            self._version,
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a InstalledAddOnContext

        :param sid: The unique Installed Add-on Sid

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        return InstalledAddOnContext(
            self._version,
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.InstalledAddOnList>'


class InstalledAddOnPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the InstalledAddOnPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnPage
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnPage
        """
        super(InstalledAddOnPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InstalledAddOnInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        return InstalledAddOnInstance(
            self._version,
            payload,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.InstalledAddOnPage>'


class InstalledAddOnContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the InstalledAddOnContext

        :param Version version: Version that contains the resource
        :param sid: The unique Installed Add-on Sid

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        super(InstalledAddOnContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'sid': sid,
        }
        self._uri = '/InstalledAddOns/{sid}'.format(**self._solution)

        # Dependents
        self._extensions = None

    def delete(self):
        """
        Deletes the InstalledAddOnInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a InstalledAddOnInstance

        :returns: Fetched InstalledAddOnInstance
        :rtype: twilio.rest.preview.twilio.com.marketplace.installed_add_on.InstalledAddOnList
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return InstalledAddOnInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    def update(self, configuration=values.unset, unique_name=values.unset):
        """
        Update the InstalledAddOnInstance

        :param dict configuration: The JSON object representing the configuration
        :param unicode unique_name: The string that uniquely identifies this Add-on installation

        :returns: Updated InstalledAddOnInstance
        :rtype: twilio.rest.preview.twilio.com.marketplace.installed_add_on.InstalledAddOnList
        """
        data = values.of({
            'Configuration': configuration,
            'UniqueName': unique_name,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return InstalledAddOnInstance(
            self._version,
            payload,
            sid=self._solution['sid'],
        )

    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.preview.marketplace.installed_add_on_extension.InstalledAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.installed_add_on_extension.InstalledAddOnExtensionList
        """
        if self._extensions is None:
            self._extensions = InstalledAddOnExtensionList(
                self._version,
                installed_add_on_sid=self._solution['sid'],
            )
        return self._extensions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.InstalledAddOnContext {}>'.format(context)


class InstalledAddOnInstance(InstanceResource):

    def __init__(self, version, payload, sid=None):
        """
        Initialize the InstalledAddOnInstance

        :returns: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnInstance
        """
        super(InstalledAddOnInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'friendly_name': payload['friendly_name'],
            'description': payload['description'],
            'configuration': payload['configuration'],
            'unique_name': payload['unique_name'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: InstalledAddOnContext for this InstalledAddOnInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.InstalledAddOnContext
        """
        if self._context is None:
            self._context = InstalledAddOnContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Add-on installation
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The Account id that has installed this Add-on
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def friendly_name(self):
        """
        :returns: A description of this Add-on installation
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def description(self):
        """
        :returns: A short description of the Add-on functionality
        :rtype: unicode
        """
        return self._properties['description']

    @property
    def configuration(self):
        """
        :returns: The JSON object representing the current configuration
        :rtype: dict
        """
        return self._properties['configuration']

    @property
    def unique_name(self):
        """
        :returns: The string that uniquely identifies this Add-on installation
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def date_created(self):
        """
        :returns: The date this Add-on installation was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Add-on installation was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def delete(self):
        """
        Deletes the InstalledAddOnInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a InstalledAddOnInstance

        :returns: Fetched InstalledAddOnInstance
        :rtype: twilio.rest.preview.twilio.com.marketplace.installed_add_on.InstalledAddOnList
        """
        return self._proxy.fetch()

    def update(self, configuration=values.unset, unique_name=values.unset):
        """
        Update the InstalledAddOnInstance

        :param dict configuration: The JSON object representing the configuration
        :param unicode unique_name: The string that uniquely identifies this Add-on installation

        :returns: Updated InstalledAddOnInstance
        :rtype: twilio.rest.preview.twilio.com.marketplace.installed_add_on.InstalledAddOnList
        """
        return self._proxy.update(
            configuration=configuration,
            unique_name=unique_name,
        )

    @property
    def extensions(self):
        """
        Access the extensions

        :returns: twilio.rest.preview.marketplace.installed_add_on_extension.InstalledAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.installed_add_on_extension.InstalledAddOnExtensionList
        """
        return self._proxy.extensions

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.InstalledAddOnInstance {}>'.format(context)
