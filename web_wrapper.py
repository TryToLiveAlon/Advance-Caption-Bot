import threading
import os

# Bot code run
def run_bot():
    os.system("python3 bot.py") 

# Fake HTTP server to keep service alive
def run_web():
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Bot is running!"

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# Run both in parallel
threading.Thread(target=run_bot).start()
run_web()
