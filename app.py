# Python Auto-Start Ollama 

import subprocess
import requests
import time

def ensure_ollama_running():
    try:
        # Check if Ollama API is already up
        requests.get("http://localhost:11434", timeout=2)
        print("✅ Ollama is already running.")
    except requests.exceptions.ConnectionError:
        print("🚀 Starting Ollama server...")
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # Wait until it’s up
        for i in range(10):
            try:
                time.sleep(1)
                requests.get("http://localhost:11434", timeout=2)
                print("✅ Ollama is now running.")
                break
            except requests.exceptions.ConnectionError:
                pass
        else:
            raise RuntimeError("❌ Ollama failed to start.")

# Call before your app runs
ensure_ollama_running()