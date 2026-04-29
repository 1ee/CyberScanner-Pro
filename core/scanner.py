import asyncio
from core.headers import check_headers
from core.vuln import test_vulns
from core.ports import port_scan
from core.reporter import save_report

async def run_scan(url, port_flag, output):

    report = {
        "target": url,
        "headers": {},
        "vulnerabilities": [],
        "open_ports": []
    }

    print(f"\n[+] Scanning target: {url}\n")

    # headers check
    report["headers"] = check_headers(url)

    # vuln test async
    report["vulnerabilities"] = await test_vulns(url)

    # optional port scan
    if port_flag:
        report["open_ports"] = port_scan(url)

    save_report(report, output)

    print("\n[+] Scan completed. Report saved.\n")