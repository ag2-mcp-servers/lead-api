# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T14:45:46+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity
from fastapi import Header
from pydantic import conint

from models import (
    BadRequestResponse,
    CreateLeadResponse,
    DeleteLeadResponse,
    GetLeadResponse,
    GetLeadsResponse,
    Lead,
    LeadsFilter,
    LeadsSort,
    NotFoundResponse,
    PaymentRequiredResponse,
    UnauthorizedResponse,
    UnexpectedErrorResponse,
    UnprocessableResponse,
    UpdateLeadResponse,
)

app = MCPProxy(
    contact={'email': 'hello@apideck.com', 'url': 'https://developers.apideck.com'},
    description='Welcome to the Lead API.\n\nYou can use this API to access all Lead API endpoints.\n\n## Base URL\n\nThe base URL for all API requests is `https://unify.apideck.com`\n\nWe also provide a [Mock API](https://developers.apideck.com/mock-api) that can be used for testing purposes: `https://mock-api.apideck.com`\n\n## Headers\n\nCustom headers that are expected as part of the request. Note that [RFC7230](https://tools.ietf.org/html/rfc7230) states header names are case insensitive.\n\n| Name                  | Type    | Required | Description                                                                                                                                                    |\n| --------------------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| x-apideck-consumer-id | String  | Yes      | The id of the customer stored inside Apideck Vault. This can be a user id, account id, device id or whatever entity that can have integration within your app. |\n| x-apideck-service-id  | String  | No       | Describe the service you want to call (e.g., pipedrive). Only needed when a customer has activated multiple integrations for the same Unified API.             |\n| x-apideck-raw         | Boolean | No       | Include raw response. Mostly used for debugging purposes.                                                                                                      |\n| x-apideck-app-id      | String  | Yes      | The application id of your Unify application. Available at https://app.apideck.com/unify/api-keys.                                                             |\n| Authorization         | String  | Yes      | Bearer API KEY                                                                                                                                                 |\n\n## Authorization\n\nYou can interact with the API through the authorization methods below.\n\n<!-- ReDoc-Inject: <security-definitions> -->\n\n## Pagination\n\nAll API resources have support for bulk retrieval via list APIs.  Apideck uses cursor-based pagination via the optional `cursor` and `limit` parameters.\n\nTo fetch the first page of results, call the list API without a `cursor` parameter. Afterwards you can fetch subsequent pages by providing a cursor parameter. You will find the next cursor in the response body in `meta.cursors.next`. If `meta.cursors.next` is `null` you\'re at the end of the list.\n\nIn the REST API you can also use the `links` from the response for added convenience. Simply call the URL in `links.next` to get the next page of results.\n\n### Query Parameters\n\n| Name   | Type   | Required | Description                                                                                                        |\n| ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------ |\n| cursor | String | No       | Cursor to start from. You can find cursors for next & previous pages in the meta.cursors property of the response. |\n| limit  | Number | No       | Number of results to return. Minimum 1, Maximum 200, Default 20                                                    |\n\n### Response Body\n\n| Name                  | Type   | Description                                                        |\n| --------------------- | ------ | ------------------------------------------------------------------ |\n| meta.cursors.previous | String | Cursor to navigate to the previous page of results through the API |\n| meta.cursors.current  | String | Cursor to navigate to the current page of results through the API  |\n| meta.cursors.next     | String | Cursor to navigate to the next page of results through the API     |\n| meta.items_on_page    | Number | Number of items returned in the data property of the response      |\n| links.previous        | String | Link to navigate to the previous page of results through the API   |\n| links.current         | String | Link to navigate to the current page of results through the API    |\n| links.next            | String | Link to navigate to the next page of results through the API       |\n\n⚠️ `meta.cursors.previous`/`links.previous` is not available for all connectors.\n\n## SDKs and API Clients\n\nWe currently offer a [Node.js](https://developers.apideck.com/sdks/node), [PHP](https://developers.apideck.com/sdks/php) and [.NET](https://developers.apideck.com/sdks/dot-net) SDK.\nNeed another SDK? [Request the SDK of your choice](https://integrations.apideck.com/request).\n\n## Debugging\n\nBecause of the nature of the abstraction we do in Apideck Unify we still provide the option to the receive raw requests and responses being handled underlying. By including the raw flag `?raw=true` in your requests you can still receive the full request. Please note that this increases the response size and can introduce extra latency.\n\n## Errors\n\nThe API returns standard HTTP response codes to indicate success or failure of the API requests. For errors, we also return a customized error message inside the JSON response. You can see the returned HTTP status codes below.\n\n| Code | Title                | Description                                                                                                                                                                                              |\n| ---- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |\n| 200  | OK                   | The request message has been successfully processed, and it has produced a response. The response message varies, depending on the request method and the requested data.                                |\n| 201  | Created              | The request has been fulfilled and has resulted in one or more new resources being created.                                                                                                              |\n| 204  | No Content           | The server has successfully fulfilled the request and that there is no additional content to send in the response payload body.                                                                          |\n| 400  | Bad Request          | The receiving server cannot understand the request because of malformed syntax. Do not repeat the request without first modifying it; check the request for errors, fix them and then retry the request. |\n| 401  | Unauthorized         | The request has not been applied because it lacks valid authentication credentials for the target resource.                                                                                              |\n| 402  | Payment Required     | Subscription data is incomplete or out of date. You\'ll need to provide payment details to continue.                                                                                                      |\n| 403  | Forbidden            | You do not have the appropriate user rights to access the request. Do not repeat the request.                                                                                                            |\n| 404  | Not Found            | The origin server did not find a current representation for the target resource or is not willing to disclose that one exists.                                                                           |\n| 409  | Conflict             | The request could not be completed due to a conflict with the current state of the target resource.                                                                                                      |\n| 422  | Unprocessable Entity | The server understands the content type of the request entity, and the syntax of the request entity is correct but was unable to process the contained instructions.                                     |\n| 429  | Too Many Requests    | You sent too many requests in a given amount of time ("rate limit"). Try again later                                                                                                                     |\n| 5xx  | Server Errors        | Something went wrong with the Unify API. These errors are logged on our side. You can contact our team to resolve the issue.                                                                             |\n\n### Handling errors\n\nThe Unify API and SDKs can produce errors for many reasons, such as a failed requests due to misconfigured integrations, invalid parameters, authentication errors, and network unavailability.\n\n### Error Types\n\n#### RequestValidationError\n\nRequest is not valid for the current endpoint. The response body will include details on the validation error. Check the spelling and types of your attributes, and ensure you are not passing data that is outside of the specification.\n\n#### UnsupportedFiltersError\n\nFilters in the request are valid, but not supported by the connector. Remove the unsupported filter(s) to get a successful response.\n\n#### UnsupportedSortFieldError\n\nSort field (`sort[by]`) in the request is valid, but not supported by the connector. Replace or remove the sort field to get a successful response.\n\n#### InvalidCursorError\n\nPagination cursor in the request is not valid for the current connector. Make sure to use a cursor returned from the API, for the same connector.\n\n#### ConnectorExecutionError\n\nA Unified API request made via one of our downstream connectors returned an unexpected error. The `status_code` returned is proxied through to error response along with their original response via the error detail.\n\n#### UnauthorizedError\n\nWe were unable to authorize the request as made. This can happen for a number of reasons, from missing header params to passing an incorrect authorization token. Verify your Api Key is being set correctly in the authorization header. ie: `Authorization: \'Bearer sk_live_***\'`\n\n#### ConnectorCredentialsError\n\nA request using a given connector has not been authorized. Ensure the connector you are trying to use has been configured correctly and been authorized for use.\n\n#### ConnectorDisabledError\n\nA request has been made to a connector that has since been disabled. This may be temporary - You can contact our team to resolve the issue.\n\n#### ConnectorRateLimitError\n\nYou sent too many request to a connector. These rate limits vary from connector to connector. You will need to try again later.\n\n#### RequestLimitError\n\nYou have reached the number of requests included in your Free Tier Subscription. You will no be able to make further requests until this limit resets at the end of the month, or talk to us about upgrading your subscription to continue immediately.\n\n#### EntityNotFoundError\n\nYou\'ve made a request for a resource or route that does not exist. Verify your path parameters or any identifiers used to fetch this resource.\n\n#### OAuthCredentialsNotFoundError\n\nWhen adding a connector integration that implements OAuth, both a `client_id` and `client_secret` must be provided before any authorizations can be performed. Verify the integration has been configured properly before continuing.\n\n#### IntegrationNotFoundError\n\nThe requested connector integration could not be found associated to your `application_id`. Verify your `application_id` is correct, and that this connector has been added and configured for your application.\n\n#### ConnectionNotFoundError\n\nA valid connection could not be found associated to your `application_id`. Something _may_ have interrupted the authorization flow. You may need to start the connector authorization process again.\n\n#### ConnectionSettingsError\n\nThe connector has required settings that were not supplied. Verify `connection.settings` contains all required settings for the connector to be callable.\n\n#### ConnectorNotFoundError\n\nA request was made for an unknown connector. Verify your `service_id` is spelled correctly, and that this connector is enabled for your provided `unified_api`.\n\n#### OAuthRedirectUriError\n\nA request was made either in a connector authorization flow, or attempting to revoke connector access without a valid `redirect_uri`. This is the url the user should be returned to on completion of process.\n\n#### OAuthInvalidStateError\n\nThe state param is required and is used to ensure the outgoing authorization state has not been altered before the user is redirected back. It also contains required params needed to identify the connector being used. If this has been altered, the authorization will not succeed.\n\n#### OAuthCodeExchangeError\n\nWhen attempting to exchange the authorization code for an `access_token` during an OAuth flow, an error occurred. This may be temporary. You can reattempt authorization or contact our team to resolve the issue.\n\n#### OAuthConnectorError\n\nIt seems something went wrong on the connector side. It\'s possible this connector is in `beta` or still under development. We\'ve been notified and are working to fix this issue.\n\n#### MappingError\n\nThere was an error attempting to retrieve the mapping for a given attribute. We\'ve been notified and are working to fix this issue.\n\n#### ConnectorMappingNotFoundError\n\nIt seems the implementation for this connector is incomplete. It\'s possible this connector is in `beta` or still under development. We\'ve been notified and are working to fix this issue.\n\n#### ConnectorResponseMappingNotFoundError\n\nWe were unable to retrieve the response mapping for this connector. It\'s possible this connector is in `beta` or still under development. We\'ve been notified and are working to fix this issue.\n\n#### ConnectorOperationMappingNotFoundError\n\nConnector mapping has not been implemented for the requested operation. It\'s possible this connector is in `beta` or still under development. We\'ve been notified and are working to fix this issue.\n\n#### ConnectorWorkflowMappingError\n\nThe composite api calls required for this operation have not been mapped entirely. It\'s possible this connector is in `beta` or still under development. We\'ve been notified and are working to fix this issue.\n\n#### ConnectorOperationUnsupportedError\n\nYou\'re attempting a call that is not supported by the connector. It\'s likely this operation is supported by another connector, but we\'re unable to implement for this one.\n\n#### PaginationNotSupportedError\n\nPagination is not yet supported for this connector, try removing limit and/or cursor from the query. It\'s possible this connector is in `beta` or still under development. We\'ve been notified and are working to fix this issue.\n\n## API Design\n\n### API Styles and data formats\n\n#### REST API\n\nThe API is organized around [REST](https://restfulapi.net/), providing simple and predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. JSON is returned by all API responses, including errors. In all API requests, you must set the content-type HTTP header to application/json. All API requests must be made over HTTPS. Calls made over HTTP will fail.\n\n##### Available HTTP methods\n\nThe Apideck API uses HTTP verbs to understand if you want to read (GET), delete (DELETE) or create (POST) an object. When your web application cannot do a POST or DELETE, we provide the ability to set the method through the query parameter \\_method.\n\n```\nPOST /messages\nGET /messages\nGET /messages/{messageId}\nPATCH /messages/{messageId}\nDELETE /messages/{messageId}\n```\n\nResponse bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise. For some endpoints and use cases we divert from REST to provide a better developer experience.\n\n### Schema\n\nAll API requests and response bodies adhere to a common JSON format representing individual items, collections of items, links to related items and additional meta data.\n\n### Meta\n\nMeta data can be represented as a top level member named “meta”. Any information may be provided in the meta data. It’s most common use is to return the total number of records when requesting a collection of resources.\n\n### Idempotence (upcoming)\n\nTo prevent the creation of duplicate resources, every POST method (such as one that creates a consumer record) must specify a unique value for the X-Unique-Transaction-ID header name. Uniquely identifying each unique POST request ensures that the API processes a given request once and only once.\n\nUniquely identifying new resource-creation POSTs is especially important when the outcome of a response is ambiguous because of a transient service interruption, such as a server-side timeout or network disruption. If a service interruption occurs, then the client application can safely retry the uniquely identified request without creating duplicate operations. (API endpoints that guarantee that every uniquely identified request is processed only once no matter how many times that uniquely identifiable request is made are described as idempotent.)\n\n### Request IDs\n\nEach API request has an associated request identifier. You can find this value in the response headers, under Request-Id. You can also find request identifiers in the URLs of individual request logs in your Dashboard. If you need to contact us about a specific request, providing the request identifier will ensure the fastest possible resolution.\n\n### Fixed field types\n\n#### Dates\n\nThe dates returned by the API are all represented in UTC (ISO8601 format).\n\nThis example\xa0`2019-11-14T00:55:31.820Z`\xa0is defined by the\xa0ISO 8601\xa0standard. The\xa0T\xa0in the middle separates the year-month-day portion from the hour-minute-second portion. The\xa0Z\xa0on the end means UTC, that is, an offset-from-UTC of zero hours-minutes-seconds. The\xa0Z\xa0is pronounced "Zulu" per military/aviation tradition.\n\nThe ISO 8601 standard is more modern. The formats are wisely designed to be easy to parse by machine as well as easy to read by humans across cultures.\n\n#### Prices and Currencies\n\nAll prices returned by the API are represented as integer amounts in a currency’s smallest unit. For example, $5 USD would be returned as 500 (i.e, 500 cents).\n\nFor zero-decimal currencies, amounts will still be provided as an integer but without the need to divide by 100. For example, an amount of ¥5 (JPY) would be returned as 5.\n\nAll currency codes conform to [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217).\n\n## Support\n\nIf you have problems or need help with your case, you can always reach out to our Support.\n\n',
    license={
        'name': 'Apache 2.0',
        'url': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
    title='Lead API',
    version='9.3.0',
    servers=[{'description': 'Production', 'url': 'https://unify.apideck.com'}],
)


@app.get(
    '/lead/leads',
    description=""" List leads """,
    tags=['leads_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def leads_all(
    raw: Optional[bool] = False,
    x_apideck_consumer_id: str = Header(..., alias='x-apideck-consumer-id'),
    x_apideck_app_id: str = Header(..., alias='x-apideck-app-id'),
    x_apideck_service_id: Optional[str] = Header(None, alias='x-apideck-service-id'),
    cursor: Optional[str] = None,
    limit: Optional[conint(ge=1, le=200)] = 20,
    filter: Optional[LeadsFilter] = None,
    sort: Optional[LeadsSort] = None,
    fields: Optional[str] = None,
):
    """
    List leads
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/lead/leads',
    description=""" Create lead """,
    tags=['leads_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def leads_add(
    raw: Optional[bool] = False,
    x_apideck_consumer_id: str = Header(..., alias='x-apideck-consumer-id'),
    x_apideck_app_id: str = Header(..., alias='x-apideck-app-id'),
    x_apideck_service_id: Optional[str] = Header(None, alias='x-apideck-service-id'),
    body: Lead = ...,
):
    """
    Create lead
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/lead/leads/{id}',
    description=""" Delete lead """,
    tags=['leads_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def leads_delete(
    id: str,
    x_apideck_consumer_id: str = Header(..., alias='x-apideck-consumer-id'),
    x_apideck_app_id: str = Header(..., alias='x-apideck-app-id'),
    x_apideck_service_id: Optional[str] = Header(None, alias='x-apideck-service-id'),
    raw: Optional[bool] = False,
):
    """
    Delete lead
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/lead/leads/{id}',
    description=""" Get lead """,
    tags=['leads_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def leads_one(
    id: str,
    x_apideck_consumer_id: str = Header(..., alias='x-apideck-consumer-id'),
    x_apideck_app_id: str = Header(..., alias='x-apideck-app-id'),
    x_apideck_service_id: Optional[str] = Header(None, alias='x-apideck-service-id'),
    raw: Optional[bool] = False,
    fields: Optional[str] = None,
):
    """
    Get lead
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.patch(
    '/lead/leads/{id}',
    description=""" Update lead """,
    tags=['leads_management'],
    security=[
        APIKeyHeader(name="Authorization"),
    ],
)
def leads_update(
    id: str,
    x_apideck_consumer_id: str = Header(..., alias='x-apideck-consumer-id'),
    x_apideck_app_id: str = Header(..., alias='x-apideck-app-id'),
    x_apideck_service_id: Optional[str] = Header(None, alias='x-apideck-service-id'),
    raw: Optional[bool] = False,
    body: Lead = ...,
):
    """
    Update lead
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
