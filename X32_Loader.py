from pythonosc import udp_client
import socket

# Define the IP address and port of the X32 console
X32_IP = '192.168.0.56'
X32_PORT = 10023

# Define the scene number to load (scene indexing starts at zero)
SCENE_NUMBER = 15

def check_udp_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2)
        sock.sendto(b'', (ip, port))
        sock.close()
        return True
    except Exception as e:
        print(f"UDP port check failed: {e}")
        return False

def load_scene(ip, port, scene_number):
    try:
        # Check if the IP address is reachable via UDP
        print(f"Attempting to connect to {ip}:{port}...")
        if not check_udp_port(ip, port):
            print(f"Cannot reach {ip}:{port}. Please check the IP address and port.")
            return
        print(f"Successfully connected to {ip}:{port}.")
        
        # Create an OSC client
        client = udp_client.SimpleUDPClient(ip, port)
        
        # Send the OSC message to load the scene using the correct path
        print(f"Sending OSC message to load scene {scene_number + 1}...")
        client.send_message("/-action/goscene", [scene_number])
        print(f"Sent OSC message: /-action/goscene with argument: {scene_number}")
        
        # Verify if the message was sent
        print(f"Scene {scene_number + 1} load command sent to {ip}:{port}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Load the scene
load_scene(X32_IP, X32_PORT, SCENE_NUMBER)