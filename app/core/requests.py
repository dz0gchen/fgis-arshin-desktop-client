import asyncio

import aiohttp
from marshmallow import Schema, ValidationError, fields
from requests import codes as http_codes  # type: ignore
from tenacity import RetryError, retry, retry_if_result, stop_after_attempt, wait_fixed

from app.core.config import get_config


class ItemSchema(Schema):
    vri_id = fields.String(
        required=True,
    )
    org_title = fields.String(
        required=True,
    )
    mit_number = fields.String(
        required=True,
    )
    mit_title = fields.String(
        required=True,
    )
    mit_notation = fields.String(
        required=True,
    )
    mi_modification = fields.String(
        required=True,
    )
    mi_number = fields.String(
        required=True,
    )
    verification_date = fields.String(
        required=True,
    )
    valid_date = fields.String(
        required=True,
    )
    result_docnum = fields.String(
        required=True,
    )
    applicability = fields.Boolean(
        required=True,
    )


class ResultItemSchema(Schema):
    count = fields.Integer(
        required=True,
    )
    start = fields.Integer(
        required=True,
    )
    rows = fields.Integer(
        required=True,
    )
    items = fields.List(
        fields.Nested(ItemSchema, required=True),
    )


class ResultSchema(Schema):
    result = fields.Nested(ResultItemSchema, required=True)


class FGISArshinAPI:
    def __init__(self) -> None:
        self.cfg = get_config()
        self.host = self.cfg.api.host
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        self.request = retry(  # type: ignore[method-assign]
            stop=stop_after_attempt(self.cfg.api.request_retries),
            wait=wait_fixed(self.cfg.api.request_retries),
            retry=retry_if_result(lambda x: not x),
        )(self.request)

    def request(self, params: dict, method: str = "get") -> dict:
        async def _async_request(method: str, params: dict) -> dict:
            async with aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.cfg.api.request_retries)
            ) as session:
                async with getattr(session, method)(
                    url=f"https://{self.host}/fundmetrology/eapi/vri?mi_number="
                    f"{params['number']}&verification_date={params['date']}",
                    json=params,
                    headers=self.headers,
                ) as resp:
                    response = await resp.json()
                    if resp.status == http_codes.ok:
                        return response
                    return {}

        try:
            result = asyncio.run(_async_request(method=method, params=params))
        except (
            aiohttp.client_exceptions.ClientConnectorError,
            aiohttp.client_exceptions.ServerDisconnectedError,
            asyncio.TimeoutError,
        ):
            return {}
        return result

    def send(self, params: dict) -> dict:
        try:
            response = self.request(params=params)
        except RetryError:
            return {}
        schema = ResultSchema()
        try:
            schema.load(response)
        except ValidationError:
            return {}
        return response
