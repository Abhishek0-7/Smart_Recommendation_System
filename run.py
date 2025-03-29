from app import create_app
from pyngrok import ngrok
import os
from config import Config

app = create_app()

if __name__ == "__main__":
    # Load configuration
    ngrok.set_auth_token(os.getenv("NGROK_AUTH_TOKEN")) 
    
    # Start Flask server
    port = 5000
    app.run(host='0.0.0.0', port=port)
    
    # Optional: Ngrok tunneling (for Colab/local testing)
    if os.getenv("ENABLE_NGROK", "False").lower() == "true":
        public_url = ngrok.connect(port)
        print(f"✨ Public URL: {public_url}")
