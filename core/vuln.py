import aiohttp
import asyncio

xss_payloads = [
    "<script>alert(1)</script>",
    "\"><img src=x onerror=alert(1)>"
]

sql_payloads = [
    "' OR '1'='1",
    "' OR 1=1--"
]

async def fetch(session, url):
    try:
        async with session.get(url, timeout=5) as r:
            return await r.text()
    except:
        return ""

async def test_vulns(url):

    print("[*] Testing vulnerabilities...")

    findings = []

    async with aiohttp.ClientSession() as session:

        for payload in xss_payloads:
            res = await fetch(session, url + "?q=" + payload)
            if payload in res:
                findings.append("Possible XSS")

        for payload in sql_payloads:
            res = await fetch(session, url + "?id=" + payload)
            if "sql" in res.lower() or "error" in res.lower():
                findings.append("Possible SQL Injection")

    return list(set(findings))