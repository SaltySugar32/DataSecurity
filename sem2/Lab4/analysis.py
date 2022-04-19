import datetime
from nfstream import NFStreamer

attr = ['src_ip','dst_ip','bidirectional_packets','bidirectional_bytes','application_name','application_category_name'] 

def get_data(pcap_file: str, md_name: str):
    md_file = open(md_name, "w")

    nfs = NFStreamer(source=pcap_file).to_pandas()[attr]
    tab = '     '
    nfs = nfs.astype(str).apply(lambda col: tab + col)

    # 1. Проверка на наличие VPN трафика (application_category_name)
    temp = nfs['application_name'].unique()
    if ('     WireGuard' in temp) or ('     IPsec.Azure' in temp) or ('     OpenVPN.Azure' in temp):
        md_file.write("## 1. VPN found\n---\n")
    else:
        md_file.write("## 1. VPN NOT found\n---\n")

    # Вывод информации о следующих данных:
    # ['src_ip','dst_ip','bidirectional_packets','bidirectional_bytes','application_name','application_category_name']
    md_file.write("## 2. All Info\n")
    md_file.write(nfs.to_string(index=False))

    # вывода для уникальных значений ['src_ip','dst_ip','application_name']
    nfs = nfs[['src_ip', 'dst_ip', 'application_name']].drop_duplicates()
    md_file.write("\n## Unique src_ip, dst_ip, application_name\n")
    md_file.write(nfs.to_string(index=False))

    # 3. Вывод начала и конца захвата трафика
    nfs = NFStreamer(source=pcap_file).to_pandas()[['bidirectional_first_seen_ms', 'bidirectional_last_seen_ms']]
    start = datetime.datetime.fromtimestamp(nfs['bidirectional_first_seen_ms'].min()/1000)
    stop = datetime.datetime.fromtimestamp(nfs['bidirectional_last_seen_ms'].max()/1000)
    md_file.write("\n---\n## 3. Capture start/stop time\n")
    md_file.write(f"\n Start time: {start}\n")
    md_file.write(f"\n Stop time: {stop}\n")

    #4. Вывод полезной информации на основании данных, что есть в трафике
    nfs = NFStreamer(source=pcap_file).to_pandas()[['application_name','application_category_name', 'bidirectional_bytes']]
    nfs = nfs.groupby(['application_name','application_category_name'], sort=True, as_index=False).sum()
    md_file.write("\n---\n## 4. Useful info\n\n")
    nfs = nfs.astype(str).apply(lambda col: tab + col)
    md_file.write(nfs.to_string(index=False))

    md_file.close()
    

def print_all():
    dir = "analysed_md/"
    get_data("data/1/wireguard.pcapng", dir+"1_wireguard.md")
    get_data("data/1/ipsec.pcapng", dir+"1_ipsec.md")
    get_data("data/1/openvpn.pcapng", dir+"1_openvpn.md")

    get_data("data/2/wireguard.pcapng", dir+"2_wireguard.md")
    get_data("data/2/ipsec.pcapng", dir+"2_ipsec.md")
    get_data("data/2/openvpn.pcapng", dir+"2_openvpn.md")

    get_data("data/3/novpn.pcapng", dir+"3_novpn.md")

    get_data("data/4/final.pcapng", dir+"4_final.md")


if __name__ == '__main__':
    print_all()