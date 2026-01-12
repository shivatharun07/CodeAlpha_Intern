from scapy.all import sniff, IP, TCP, UDP

def packet_analyzer(packet):
    # Check if packet has IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("Source IP      :", src_ip)
        print("Destination IP :", dst_ip)
        print("Protocol       :", protocol)

        # Check for TCP packets
        if packet.haslayer(TCP):
            print("Protocol Type  : TCP")
            print("Source Port    :", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)
            print("Payload        :", bytes(packet[TCP].payload))

        # Check for UDP packets
        elif packet.haslayer(UDP):
            print("Protocol Type  : UDP")
            print("Source Port    :", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)
            print("Payload        :", bytes(packet[UDP].payload))

        print("-" * 60)

# Start sniffing packets
sniff(prn=packet_analyzer, count=10)

