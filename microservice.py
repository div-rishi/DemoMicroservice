from flask import Flask, jsonify
import random
import logging
import sys
sys.path.append('/Users/prag_div/PycharmProjects/CustomLoggerLib')
from CustomLogger import setup_logger

# Set up the custom logger
logger = setup_logger(
    name="MyMicroserviceLogger",
    log_file="microservice.json",  # Save logs in JSON format
    level=logging.DEBUG,
    console_output=True  # Enable console output for debugging
)

# Flask application setup
app = Flask(__name__)

@app.route("/generate", methods=["GET"])
def generate_random_number():
    random_number = random.randint(1, 1000)
    
    # Add extra attributes dynamically in 'additionalData'
    extra_data = {
        "userID": "user_123",  # Custom attribute
        "sessionID": "abc123xyz"  # Another custom attribute
    }
    
    logger.info(f"Generated random number: {random_number}", extra={"eventID": "1570", "extraData": extra_data})
    
    return jsonify({"random_number": random_number})

if __name__ == "__main__":
    logger.debug("Starting the Flask microservice.")
    app.run(port=8002)
