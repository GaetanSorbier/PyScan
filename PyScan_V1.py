import socket
import concurrent.futures
from tqdm import tqdm
from pystyle import Colors, Colorate 


print(Colorate.Horizontal(Colors.yellow_to_red, """\n██████  ██    ██ ███████  ██████  █████  ███    ██ 
██   ██  ██  ██  ██      ██      ██   ██ ████   ██ 
██████    ████   ███████ ██      ███████ ██ ██  ██ 
██         ██         ██ ██      ██   ██ ██  ██ ██ 
██         ██    ███████  ██████ ██   ██ ██   ████ 
                              V1 By Gaetan Sorbier\n""", 1))

def scan_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    sock.close()
    if result == 0:
        return port

def main():
    print("\nChoisissez la langue / Choose the language:")
    print("\n1. Français")
    print("2. English")
    choice = input("\nChoice (1/2): ")
    
    if choice == "1":
        print("\nLangue sélectionnée: Français")
        target_host = input("\nEntrez l'adresse IP ou le nom d'hôte cible : ")
        max_ports = int(input("\nEntrez le nombre maximum de ports à scanner : "))
        print(f"\nScan en cours sur {target_host}...\n")
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(scan_port, target_host, port) for port in range(1, max_ports + 1)]
            with tqdm(total=max_ports) as pbar:
                for future in concurrent.futures.as_completed(futures):
                    pbar.update(1)
                    port = future.result()
                    if port:
                        open_ports.append(port)
                        print(f"\nPort {port} : Ouvert")
        if not open_ports:
            print(Colors.red + "\nAucun port ouvert trouvé.")
        else:
            print(f"\nPorts ouverts trouvés : {', '.join(map(str, open_ports))}")

    elif choice == "2":
        print("\nSelected language: English")
        target_host = input("\nEnter the target IP address or hostname: ")
        max_ports = int(input("\nEnter the maximum number of ports to scan: "))
        print(f"\nScanning on {target_host}...\n")
        open_ports = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(scan_port, target_host, port) for port in range(1, max_ports + 1)]
            with tqdm(total=max_ports) as pbar:
                for future in concurrent.futures.as_completed(futures):
                    pbar.update(1)
                    port = future.result()
                    if port:
                        open_ports.append(port)
                        print(f"\nPort {port} : Open")
        if not open_ports:
            print(Colors.red + "\nNo open ports found.")
        else:
            print(f"\nOpen ports found: {', '.join(map(str, open_ports))}")

    else:
        print(Colors.yellow + "Choix non valide / Invalid choice.")
    
if __name__ == "__main__":
    main()
