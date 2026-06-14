import nmap
import netifaces
import ipaddress

TARGET_PORTS = "80,554,1935"

def get_local_subnet():
    iface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    addr = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]
    
    ip = addr['addr']
    netmask = addr['netmask']
    
    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
    return str(network)

def scan_network(subnet):
    print(f"[+] Scanning subnet: {subnet}")
    
    nm = nmap.PortScanner()
    nm.scan(hosts=subnet, arguments=f"-p {TARGET_PORTS} --open -sT -T4")
    
    http_only = []
    rtsp_only = []
    rtmp_only = []
    http_rtsp = []
    all_three = []

    for host in nm.all_hosts():
        ports = []

        if 'tcp' in nm[host]:
            for port in nm[host]['tcp']:
                if nm[host]['tcp'][port]['state'] == 'open':
                    ports.append(port)

        ports = set(ports)

        if ports == {80}:
            http_only.append(host)
        elif ports == {554}:
            rtsp_only.append(host)
        elif ports == {1935}:
            rtmp_only.append(host)
        elif ports == {80, 554}:
            http_rtsp.append(host)
        elif ports == {80, 554, 1935}:
            all_three.append(host)

    return http_only, rtsp_only, rtmp_only, http_rtsp, all_three


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        subnet = sys.argv[1]
    else:
        subnet = get_local_subnet()

    http_only, rtsp_only, rtmp_only, http_rtsp, all_three = scan_network(subnet)

    print("\n====== FILTERED RESULTS ======\n")

    print("HTTP ONLY DEVICES:")
    for ip in http_only:
        print(ip)

    print("\nRTSP ONLY DEVICES:")
    for ip in rtsp_only:
        print(ip)

    print("\nRTMP ONLY DEVICES:")
    for ip in rtmp_only:
        print(ip)

    print("\nHTTP + RTSP DEVICES:")
    for ip in http_rtsp:
        print(ip)

    print("\nALL THREE (HTTP + RTSP + RTMP):")
    for ip in all_three:
        print(ip)
