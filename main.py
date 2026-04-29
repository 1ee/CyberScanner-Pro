import argparse
from core.scanner import run_scan

def banner():
    print("""
 ██████╗██╗   ██╗██████╗ ███████╗███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██║   ██║██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║     ██║   ██║██████╔╝█████╗  ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║     ██║   ██║██╔═══╝ ██╔══╝  ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║     ███████╗███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝     ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
    """)

if __name__ == "__main__":
    banner()

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="Target URL")
    parser.add_argument("-p", "--ports", action="store_true", help="Enable port scan")
    parser.add_argument("-o", "--output", default="output/report.json")

    args = parser.parse_args()

    run_scan(args.url, args.ports, args.output)
