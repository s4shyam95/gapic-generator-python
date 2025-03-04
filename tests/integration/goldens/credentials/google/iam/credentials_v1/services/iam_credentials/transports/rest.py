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


from google.iam.credentials_v1.types import common

from .base import IAMCredentialsTransport, DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=requests_version,
)


class IAMCredentialsRestInterceptor:
    """Interceptor for IAMCredentials.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the IAMCredentialsRestTransport.

    .. code-block:: python
        class MyCustomIAMCredentialsInterceptor(IAMCredentialsRestInterceptor):
            def pre_generate_access_token(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_access_token(response):
                logging.log(f"Received response: {response}")

            def pre_generate_id_token(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_id_token(response):
                logging.log(f"Received response: {response}")

            def pre_sign_blob(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_sign_blob(response):
                logging.log(f"Received response: {response}")

            def pre_sign_jwt(request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_sign_jwt(response):
                logging.log(f"Received response: {response}")

        transport = IAMCredentialsRestTransport(interceptor=MyCustomIAMCredentialsInterceptor())
        client = IAMCredentialsClient(transport=transport)


    """
    def pre_generate_access_token(self, request: common.GenerateAccessTokenRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[common.GenerateAccessTokenRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for generate_access_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IAMCredentials server.
        """
        return request, metadata

    def post_generate_access_token(self, response: common.GenerateAccessTokenResponse) -> common.GenerateAccessTokenResponse:
        """Post-rpc interceptor for generate_access_token

        Override in a subclass to manipulate the response
        after it is returned by the IAMCredentials server but before
        it is returned to user code.
        """
        return response

    def pre_generate_id_token(self, request: common.GenerateIdTokenRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[common.GenerateIdTokenRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for generate_id_token

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IAMCredentials server.
        """
        return request, metadata

    def post_generate_id_token(self, response: common.GenerateIdTokenResponse) -> common.GenerateIdTokenResponse:
        """Post-rpc interceptor for generate_id_token

        Override in a subclass to manipulate the response
        after it is returned by the IAMCredentials server but before
        it is returned to user code.
        """
        return response

    def pre_sign_blob(self, request: common.SignBlobRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[common.SignBlobRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for sign_blob

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IAMCredentials server.
        """
        return request, metadata

    def post_sign_blob(self, response: common.SignBlobResponse) -> common.SignBlobResponse:
        """Post-rpc interceptor for sign_blob

        Override in a subclass to manipulate the response
        after it is returned by the IAMCredentials server but before
        it is returned to user code.
        """
        return response

    def pre_sign_jwt(self, request: common.SignJwtRequest, metadata: Sequence[Tuple[str, str]]) -> Tuple[common.SignJwtRequest, Sequence[Tuple[str, str]]]:
        """Pre-rpc interceptor for sign_jwt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the IAMCredentials server.
        """
        return request, metadata

    def post_sign_jwt(self, response: common.SignJwtResponse) -> common.SignJwtResponse:
        """Post-rpc interceptor for sign_jwt

        Override in a subclass to manipulate the response
        after it is returned by the IAMCredentials server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class IAMCredentialsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: IAMCredentialsRestInterceptor


class IAMCredentialsRestTransport(IAMCredentialsTransport):
    """REST backend transport for IAMCredentials.

    A service account is a special type of Google account that
    belongs to your application or a virtual machine (VM), instead
    of to an individual end user. Your application assumes the
    identity of the service account to call Google APIs, so that the
    users aren't directly involved.

    Service account credentials are used to temporarily assume the
    identity of the service account. Supported credential types
    include OAuth 2.0 access tokens, OpenID Connect ID tokens,
    self-signed JSON Web Tokens (JWTs), and more.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """
    _STUBS: Dict[str, IAMCredentialsRestStub] = {}

    def __init__(self, *,
            host: str = 'iamcredentials.googleapis.com',
            credentials: ga_credentials.Credentials=None,
            credentials_file: str=None,
            scopes: Sequence[str]=None,
            client_cert_source_for_mtls: Callable[[
                ], Tuple[bytes, bytes]]=None,
            quota_project_id: Optional[str]=None,
            client_info: gapic_v1.client_info.ClientInfo=DEFAULT_CLIENT_INFO,
            always_use_jwt_access: Optional[bool]=False,
            url_scheme: str='https',
            interceptor: Optional[IAMCredentialsRestInterceptor] = None,
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
        self._interceptor = interceptor or IAMCredentialsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _GenerateAccessToken(IAMCredentialsRestStub):
        def __hash__(self):
            return hash("GenerateAccessToken")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: common.GenerateAccessTokenRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> common.GenerateAccessTokenResponse:
            r"""Call the generate access token method over HTTP.

            Args:
                request (~.common.GenerateAccessTokenRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.common.GenerateAccessTokenResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/serviceAccounts/*}:generateAccessToken',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_generate_access_token(request, metadata)
            request_kwargs = common.GenerateAccessTokenRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            # Jsonify the request body
            body = common.GenerateAccessTokenRequest.to_json(
                common.GenerateAccessTokenRequest(transcoded_request['body']),                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(common.GenerateAccessTokenRequest.to_json(
                common.GenerateAccessTokenRequest(transcoded_request['query_params']),
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
            resp = common.GenerateAccessTokenResponse.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_generate_access_token(resp)
            return resp

    class _GenerateIdToken(IAMCredentialsRestStub):
        def __hash__(self):
            return hash("GenerateIdToken")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: common.GenerateIdTokenRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> common.GenerateIdTokenResponse:
            r"""Call the generate id token method over HTTP.

            Args:
                request (~.common.GenerateIdTokenRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.common.GenerateIdTokenResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/serviceAccounts/*}:generateIdToken',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_generate_id_token(request, metadata)
            request_kwargs = common.GenerateIdTokenRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            # Jsonify the request body
            body = common.GenerateIdTokenRequest.to_json(
                common.GenerateIdTokenRequest(transcoded_request['body']),                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(common.GenerateIdTokenRequest.to_json(
                common.GenerateIdTokenRequest(transcoded_request['query_params']),
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
            resp = common.GenerateIdTokenResponse.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_generate_id_token(resp)
            return resp

    class _SignBlob(IAMCredentialsRestStub):
        def __hash__(self):
            return hash("SignBlob")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: common.SignBlobRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> common.SignBlobResponse:
            r"""Call the sign blob method over HTTP.

            Args:
                request (~.common.SignBlobRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.common.SignBlobResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/serviceAccounts/*}:signBlob',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_sign_blob(request, metadata)
            request_kwargs = common.SignBlobRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            # Jsonify the request body
            body = common.SignBlobRequest.to_json(
                common.SignBlobRequest(transcoded_request['body']),                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(common.SignBlobRequest.to_json(
                common.SignBlobRequest(transcoded_request['query_params']),
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
            resp = common.SignBlobResponse.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_sign_blob(resp)
            return resp

    class _SignJwt(IAMCredentialsRestStub):
        def __hash__(self):
            return hash("SignJwt")

        __REQUIRED_FIELDS_DEFAULT_VALUES: Dict[str, str] =  {
        }

        @classmethod
        def _get_unset_required_fields(cls, message_dict):
            return {k: v for k, v in cls.__REQUIRED_FIELDS_DEFAULT_VALUES.items() if k not in message_dict}

        def __call__(self,
                request: common.SignJwtRequest, *,
                retry: OptionalRetry=gapic_v1.method.DEFAULT,
                timeout: float=None,
                metadata: Sequence[Tuple[str, str]]=(),
                ) -> common.SignJwtResponse:
            r"""Call the sign jwt method over HTTP.

            Args:
                request (~.common.SignJwtRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, str]]): Strings which should be
                    sent along with the request as metadata.

            Returns:
                ~.common.SignJwtResponse:

            """

            http_options: List[Dict[str, str]] = [{
                'method': 'post',
                'uri': '/v1/{name=projects/*/serviceAccounts/*}:signJwt',
                'body': '*',
            },
            ]
            request, metadata = self._interceptor.pre_sign_jwt(request, metadata)
            request_kwargs = common.SignJwtRequest.to_dict(request)
            transcoded_request = path_template.transcode(
                http_options, **request_kwargs)

            # Jsonify the request body
            body = common.SignJwtRequest.to_json(
                common.SignJwtRequest(transcoded_request['body']),                including_default_value_fields=False,
                use_integers_for_enums=False
            )
            uri = transcoded_request['uri']
            method = transcoded_request['method']

            # Jsonify the query params
            query_params = json.loads(common.SignJwtRequest.to_json(
                common.SignJwtRequest(transcoded_request['query_params']),
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
            resp = common.SignJwtResponse.from_json(
                response.content,
                ignore_unknown_fields=True
            )
            resp = self._interceptor.post_sign_jwt(resp)
            return resp

    @property
    def generate_access_token(self) -> Callable[
            [common.GenerateAccessTokenRequest],
            common.GenerateAccessTokenResponse]:
        stub = self._STUBS.get("generate_access_token")
        if not stub:
            stub = self._STUBS["generate_access_token"] = self._GenerateAccessToken(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def generate_id_token(self) -> Callable[
            [common.GenerateIdTokenRequest],
            common.GenerateIdTokenResponse]:
        stub = self._STUBS.get("generate_id_token")
        if not stub:
            stub = self._STUBS["generate_id_token"] = self._GenerateIdToken(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def sign_blob(self) -> Callable[
            [common.SignBlobRequest],
            common.SignBlobResponse]:
        stub = self._STUBS.get("sign_blob")
        if not stub:
            stub = self._STUBS["sign_blob"] = self._SignBlob(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def sign_jwt(self) -> Callable[
            [common.SignJwtRequest],
            common.SignJwtResponse]:
        stub = self._STUBS.get("sign_jwt")
        if not stub:
            stub = self._STUBS["sign_jwt"] = self._SignJwt(self._session, self._host, self._interceptor)

        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return stub # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__=(
    'IAMCredentialsRestTransport',
)
