import http.server
import socketserver
import webbrowser
import os

# --- CONFIGURATION ---
PORT = 8000
FILENAME = "sprite_studio.html" 

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        return

def start_server():
    if not os.path.exists(FILENAME):
        print(f"Error: '{FILENAME}' not found. Keep both files in the same folder.")
        return

    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/{FILENAME}"
            print("\n" + "!"*40)
            print("   SPRITE STUDIO v1.2")
            print("!"*40)
            print(f"Server: {url}")
            print("Status: Universal Sprite Mode Active")
            print("-" * 40)
            print("1. Drag any sprite into the browser.")
            print("2. Click the background to remove it.")
            print("3. Export as a clean PNG for your Java engine.")
            print("-" * 40)
            print("Press CTRL+C to close.")
            
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError:
        print(f"Error: Port {PORT} is busy. Close other instances first.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    start_server()