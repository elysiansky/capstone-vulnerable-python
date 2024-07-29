from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def set_x_frame_options(response):
    ENABLE_X_FRAME_OPTIONS = False  # Set to False to disable
    if ENABLE_X_FRAME_OPTIONS:
        response.headers['X-Frame-Options'] = 'DENY'  # or 'SAMEORIGIN' if you need to allow same origin framing
    return response

@app.route('/')
def home():
    ENABLE_X_FRAME_OPTIONS = False
    if not ENABLE_X_FRAME_OPTIONS:
        import sys
        import platform
        import os

        info = {
            "message": "Hello there Peta. Vulnerability issues found.",
            "python_version": sys.version,
            "platform": platform.platform(),
            "os_name": os.name,
            "release": platform.release(),
            "system": platform.system(),
            "machine": platform.machine(),
            "processor": platform.processor()
        }
        return jsonify(info)
    return 'X-Frame-Options header is enabled. PyInfo is not available. Security Patch Applied! <br/><br/> Your Capstone Project team is doing an amazing job !', 200

if __name__ == '__main__':   
   app.run(host="0.0.0.0", debug=True)