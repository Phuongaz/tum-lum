import scapy.all as scapy

interface = "eth0"

def process_packet(packet):
    source_ip = packet[scapy.IP].src
    destination_ip = packet[scapy.IP].dst
    protocol = packet[scapy.IP].proto
    payload = packet[scapy.Raw].load

    if "malware" in payload:
        print("Potential malware detected!")
        print(f"Source IP: {source_ip}")
        
    if "suspicious" in payload:
        generate_alert(source_ip, destination_ip, protocol, payload)
    if protocol == 6:  # TCP protocol
        if "GET" in payload or "POST" in payload:
            generate_alert("Potential HTTP traffic", source_ip, destination_ip, protocol, payload)
    if protocol == 17:  # UDP protocol
        if "DNS" in payload:
            generate_alert("Potential DNS traffic", source_ip, destination_ip, protocol, payload)

        if "VoIP" in payload:
            generate_alert("Potential VoIP traffic", source_ip, destination_ip, protocol, payload)
            
def generate_alert(source_ip, destination_ip, protocol, payload):

    print("Alert: Suspicious traffic detected!")
    print(f"Source IP: {source_ip}")
    print(f"Destination IP: {destination_ip}")
    print(f"Protocol: {protocol}")
    print(f"Payload: {payload}")

def start_sniffing():
    scapy.sniff(iface=interface, prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()
