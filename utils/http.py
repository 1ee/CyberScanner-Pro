import requests
import aiohttp
import asyncio

# =========================
# Sync HTTP (requests)
# =========================

def get(url, timeout=5, headers=None):
    try:
        r = requests.get(url, timeout=timeout, headers=headers)
        return {
            "status": r.status_code,
            "text": r.text,
            "headers": dict(r.headers)
        }
    except Exception as e:
        return {
            "error": str(e)
        }


def post(url, data=None, json=None, timeout=5, headers=None):
    try:
        r = requests.post(url, data=data, json=json, timeout=timeout, headers=headers)
        return {
            "status": r.status_code,
            "text": r.text
        }
    except Exception as e:
        return {
            "error": str(e)
        }

# =========================
# Async HTTP (aiohttp)
# =========================

async def async_get(url, timeout=5, headers=None):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=timeout, headers=headers) as r:
                text = await r.text()
                return {
                    "status": r.status,
                    "text": text
                }
    except Exception as e:
        return {
            "error": str(e)
        }


async def async_post(url, data=None, json=None, timeout=5, headers=None):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=data, json=json, timeout=timeout, headers=headers) as r:
                text = await r.text()
                return {
                    "status": r.status,
                    "text": text
                }
    except Exception as e:
        return {
            "error": str(e)
        }