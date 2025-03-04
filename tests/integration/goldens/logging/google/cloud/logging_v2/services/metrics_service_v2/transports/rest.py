# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.auth.transport.requests import AuthorizedSession  # type: ignore
import json  # type: ignore
import grpc  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import retry as retries
from google.api_core import rest_helpers
from google.api_core import rest_streaming
from google.api_core import path_template
from google.api_core import gapic_v1

from requests import __version__ as requests_version
import dataclasses
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple, Union
import warnings

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore


from google.cloud.logging_v2.types import logging_metrics
from google.protobuf import empty_pb2  # type: ignore

from .base import MetricsServiceV2Transport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class MetricsServiceV2RestInterceptor:
    """Interceptor for MetricsServiceV2.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MetricsServiceV2RestTransport.

    .. code-block:: python
        class MyCustomMetricsServiceV2Interceptor(MetricsServiceV2RestInterceptor):
            def pre_create_log_metric(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_log_metric(response):
                logging.log(f"Received response: {response}")

            def pre_delete_log_metric(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_log_metric(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_log_metric(response):
                logging.log(f"Received response: {response}")

            def pre_list_log_metrics(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_log_metrics(response):
                logging.log(f"Received response: {response}")

            def pre_update_log_metric(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_log_metric(response):
                logging.log(f"Received response: {response}")

        transport = MetricsServiceV2RestTransport(interceptor=MyCustomMetricsServiceV2Interceptor())
        client = MetricsServiceV2Client(transport=transport)


    """
    def pre_create_log_metric(self, request: logging_metrics.CreateLogMetricRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[logging_metrics.CreateLogMetricRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for create_log_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetricsServiceV2 server.
        """
        return request, metadata

    def post_create_log_metric(self, response: logging_metrics.LogMetric) -> logging_metrics.LogMetric:
        """Post-rpc interceptor for create_log_metric

        Override in a subclass to manipulate the response
        after it is returned by the MetricsServiceV2 server but before
        it is returned to user code.
        """
        return response

    def pre_delete_log_metric(self, request: logging_metrics.DeleteLogMetricRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[logging_metrics.DeleteLogMetricRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for delete_log_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetricsServiceV2 server.
        """
        return request, metadata

    def pre_get_log_metric(self, request: logging_metrics.GetLogMetricRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[logging_metrics.GetLogMetricRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for get_log_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetricsServiceV2 server.
        """
        return request, metadata

    def post_get_log_metric(self, response: logging_metrics.LogMetric) -> logging_metrics.LogMetric:
        """Post-rpc interceptor for get_log_metric

        Override in a subclass to manipulate the response
        after it is returned by the MetricsServiceV2 server but before
        it is returned to user code.
        """
        return response

    def pre_list_log_metrics(self, request: logging_metrics.ListLogMetricsRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[logging_metrics.ListLogMetricsRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for list_log_metrics

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetricsServiceV2 server.
        """
        return request, metadata

    def post_list_log_metrics(self, response: logging_metrics.ListLogMetricsResponse) -> logging_metrics.ListLogMetricsResponse:
        """Post-rpc interceptor for list_log_metrics

        Override in a subclass to manipulate the response
        after it is returned by the MetricsServiceV2 server but before
        it is returned to user code.
        """
        return response

    def pre_update_log_metric(self, request: logging_metrics.UpdateLogMetricRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[logging_metrics.UpdateLogMetricRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for update_log_metric

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MetricsServiceV2 server.
        """
        return request, metadata

    def post_update_log_metric(self, response: logging_metrics.LogMetric) -> logging_metrics.LogMetric:
        """Post-rpc interceptor for update_log_metric

        Override in a subclass to manipulate the response
        after it is returned by the MetricsServiceV2 server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class MetricsServiceV2RestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MetricsServiceV2RestInterceptor


class MetricsServiceV2RestTransport(MetricsServiceV2Transport):
    """REST backend transport for MetricsServiceV2.

    Service for configuring logs-based metrics.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """
    _STUBS: Dict[str, MetricsServiceV2RestStub] = {}

    def __init__(self, *,
            host: str = 'logging.googleapis.com',
            credentials: ga_credentials.Credentials=None,
            credentials_file: str=None,
            scopes: Sequence[str]=None,
            client_cert_source_for_mtls: Callable[[
                ], Tuple[bytes, bytes]]=None,
            quota_project_id: Optional[str]=None,
            client_info: gapic_v1.client_info.ClientInfo=DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool]=False,
            url_scheme: str='https',
            interceptor: Optional[MetricsServiceV2RestInterceptor] = None,
            session: AuthorizedSession = None,
            ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            session: The requests session to be used by the REST transport to make
                the requests. A new session is created if None.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        maybe_url_match = re.match("^(?P<scheme>http(?:s)?://)?(?P<host>.*)$", host)
        if maybe_url_match is None:
            raise ValueError(f"Unexpected hostname structure: {host}")  # pragma: NO COVER

        url_match_items = maybe_url_match.groupdict()

        host = f"{url_scheme}://{host}" if not url_match_items["scheme"] else host

        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )
        if session:
            self._session = session
        else:
            self._session = AuthorizedSession(
                self._credentials, default_host=self.DEFAULT_HOST)
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or MetricsServiceV2RestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateLogMetric(MetricsServiceV2RestStub):
        def __hash__(self):
            return hash("CreateLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: logging_metrics.CreateLogMetricRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> logging_metrics.LogMetric:
            r"""Call the create log metric method over HTTP.

            Args:
                request (~.logging_metrics.CreateLogMetricRequest):
                    The request object. The parameters to CreateLogMetric.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.logging_metrics.LogMetric:
                    Describes a logs-based metric. The
                value of the metric is the number of log
                entries that match a logs filter in a
                given time interval.
                Logs-based metrics can also be used to
                extract values from logs and create a
                distribution of the values. The
                distribution records the statistics of
                the extracted values along with an
                optional histogram of the values as
                specified by the bucket options.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v2/{parent=projects/*}/metrics',
                'body': 'metric',
            },
            ]
            request, metadata = self._interceptor.pre_create_log_metric(request, metadata)
            request_kwargs = logging_metrics.CreateLogMetricRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            # Jsonify the request body
            body = logging_metrics.LogMetric.to_json(
                logging_metrics.LogMetric(transcoded_request['body']),                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(logging_metrics.CreateLogMetricRequest.to_json(
                logging_metrics.CreateLogMetricRequest(transcoded_request['query_params']),
                including_default_value_fields=False,
                use_integers_for_enums=False
            ))

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = logging_metrics.LogMetric.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_create_log_metric(resp)
            return resp

    class _DeleteLogMetric(MetricsServiceV2RestStub):
        def __hash__(self):
            return hash("DeleteLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: logging_metrics.DeleteLogMetricRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ):
            r"""Call the delete log metric method over HTTP.

            Args:
                request (~.logging_metrics.DeleteLogMetricRequest):
                    The request object. The parameters to DeleteLogMetric.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'delete',
                'uri': '/v2/{metric_name=projects/*/metrics/*}',
            },
            ]
            request, metadata = self._interceptor.pre_delete_log_metric(request, metadata)
            request_kwargs = logging_metrics.DeleteLogMetricRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(logging_metrics.DeleteLogMetricRequest.to_json(
                logging_metrics.DeleteLogMetricRequest(transcoded_request['query_params']),
                including_default_value_fields=False,
                use_integers_for_enums=False
            ))

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _GetLogMetric(MetricsServiceV2RestStub):
        def __hash__(self):
            return hash("GetLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: logging_metrics.GetLogMetricRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> logging_metrics.LogMetric:
            r"""Call the get log metric method over HTTP.

            Args:
                request (~.logging_metrics.GetLogMetricRequest):
                    The request object. The parameters to GetLogMetric.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.logging_metrics.LogMetric:
                    Describes a logs-based metric. The
                value of the metric is the number of log
                entries that match a logs filter in a
                given time interval.
                Logs-based metrics can also be used to
                extract values from logs and create a
                distribution of the values. The
                distribution records the statistics of
                the extracted values along with an
                optional histogram of the values as
                specified by the bucket options.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{metric_name=projects/*/metrics/*}',
            },
            ]
            request, metadata = self._interceptor.pre_get_log_metric(request, metadata)
            request_kwargs = logging_metrics.GetLogMetricRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(logging_metrics.GetLogMetricRequest.to_json(
                logging_metrics.GetLogMetricRequest(transcoded_request['query_params']),
                including_default_value_fields=False,
                use_integers_for_enums=False
            ))

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = logging_metrics.LogMetric.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_get_log_metric(resp)
            return resp

    class _ListLogMetrics(MetricsServiceV2RestStub):
        def __hash__(self):
            return hash("ListLogMetrics")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: logging_metrics.ListLogMetricsRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> logging_metrics.ListLogMetricsResponse:
            r"""Call the list log metrics method over HTTP.

            Args:
                request (~.logging_metrics.ListLogMetricsRequest):
                    The request object. The parameters to ListLogMetrics.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.logging_metrics.ListLogMetricsResponse:
                    Result returned from ListLogMetrics.
            """

            http_options: List[Dict[str, str]] = [{
                'method': 'get',
                'uri': '/v2/{parent=projects/*}/metrics',
            },
            ]
            request, metadata = self._interceptor.pre_list_log_metrics(request, metadata)
            request_kwargs = logging_metrics.ListLogMetricsRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(logging_metrics.ListLogMetricsRequest.to_json(
                logging_metrics.ListLogMetricsRequest(transcoded_request['query_params']),
                including_default_value_fields=False,
                use_integers_for_enums=False
            ))

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = logging_metrics.ListLogMetricsResponse.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_list_log_metrics(resp)
            return resp

    class _UpdateLogMetric(MetricsServiceV2RestStub):
        def __hash__(self):
            return hash("UpdateLogMetric")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: logging_metrics.UpdateLogMetricRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> logging_metrics.LogMetric:
            r"""Call the update log metric method over HTTP.

            Args:
                request (~.logging_metrics.UpdateLogMetricRequest):
                    The request object. The parameters to UpdateLogMetric.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.logging_metrics.LogMetric:
                    Describes a logs-based metric. The
                value of the metric is the number of log
                entries that match a logs filter in a
                given time interval.
                Logs-based metrics can also be used to
                extract values from logs and create a
                distribution of the values. The
                distribution records the statistics of
                the extracted values along with an
                optional histogram of the values as
                specified by the bucket options.

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'put',
                'uri': '/v2/{metric_name=projects/*/metrics/*}',
                'body': 'metric',
            },
            ]
            request, metadata = self._interceptor.pre_update_log_metric(request, metadata)
            request_kwargs = logging_metrics.UpdateLogMetricRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            # Jsonify the request body
            body = logging_metrics.LogMetric.to_json(
                logging_metrics.LogMetric(transcoded_request['body']),                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(logging_metrics.UpdateLogMetricRequest.to_json(
                logging_metrics.UpdateLogMetricRequest(transcoded_request['query_params']),
                including_default_value_fields=False,
                use_integers_for_enums=False
            ))

            query_params.update(self._get_unset_required_fields(query_params))

            # Send the request
            headers = dict(metadata)
            headers['Content-Type'] = 'application/json'
            response = getattr(self._session, method)(
                "{host}{uri}".format(host=self._host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params),
                data=body,
                )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = logging_metrics.LogMetric.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_update_log_metric(resp)
            return resp

    @property
    def create_log_metric(self) -> Callable[
            [logging_metrics.CreateLogMetricRequest],
            logging_metrics.LogMetric]:
        stub = self._STUBS.get("create_log_metric")
        if not stub:
            stub = self._STUBS["create_log_metric"] = self._CreateLogMetric(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def delete_log_metric(self) -> Callable[
            [logging_metrics.DeleteLogMetricRequest],
            empty_pb2.Empty]:
        stub = self._STUBS.get("delete_log_metric")
        if not stub:
            stub = self._STUBS["delete_log_metric"] = self._DeleteLogMetric(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def get_log_metric(self) -> Callable[
            [logging_metrics.GetLogMetricRequest],
            logging_metrics.LogMetric]:
        stub = self._STUBS.get("get_log_metric")
        if not stub:
            stub = self._STUBS["get_log_metric"] = self._GetLogMetric(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def list_log_metrics(self) -> Callable[
            [logging_metrics.ListLogMetricsRequest],
            logging_metrics.ListLogMetricsResponse]:
        stub = self._STUBS.get("list_log_metrics")
        if not stub:
            stub = self._STUBS["list_log_metrics"] = self._ListLogMetrics(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def update_log_metric(self) -> Callable[
            [logging_metrics.UpdateLogMetricRequest],
            logging_metrics.LogMetric]:
        stub = self._STUBS.get("update_log_metric")
        if not stub:
            stub = self._STUBS["update_log_metric"] = self._UpdateLogMetric(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'MetricsServiceV2RestTransport',
)
