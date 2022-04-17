from nfstream import NFStreamer

attr = ['src_ip','dst_ip','bidirectional_packets','bidirectional_bytes','application_name','application_category_name'] 

def get_data(pcap_file: str, md_name: str):
    md_file = open(md_name, "w")

    nfs = NFStreamer(source=pcap_file).to_pandas()[attr]

    if "VPN" in nfs['application_category_name'].unique():
        md_file.write("## 1. VPN found\n---\n")
    else:
        md_file.write("## 1. VPN NOT found\n---\n")

    md_file.write("## 2. All info\n")
    md_file.write(nfs.head(nfs.size).to_string(index=False))
    

if __name__ == '__main__':
    dir = "analysed_md/"
    get_data("data/1/wireguard.pcapng", dir+"1_wireguard.md")
    get_data("data/1/ipsec.pcapng", dir+"1_ipsec.md")
    get_data("data/1/openvpn.pcapng", dir+"1_openvpn.md")

    get_data("data/2/wireguard.pcapng", dir+"2_wireguard.md")
    get_data("data/2/ipsec.pcapng", dir+"2_ipsec.md")
    get_data("data/2/openvpn.pcapng", dir+"2_openvpn.md")

    get_data("data/3/novpn.pcapng", dir+"3_novpn.md")

    get_data("data/4/final.pcapng", dir+"4_final.md")