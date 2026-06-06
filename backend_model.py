from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import os
# AI model file se function import ho raha hai
try:
    from ai_model import restore_audio 
except ImportError:
    def restore_audio(in_p, out_p): return True # Temporary bypass agar file missing ho

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    input_p = "ganda.wav"
    output_p = "saaf.wav"

    # Check karo ki audio file aayi hai ya nahi
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file"}), 400
        
    file = request.files['audio']
    file.save(input_p)
    print(f"File saved: {input_p}")

    # AI Model processing start
    try:
        success = restore_audio(input_p, output_p)
        if success and os.path.exists(output_p):
            return send_file(output_p, as_attachment=True)
        else:
            # Agar AI model fail ho, toh wahi file wapis bhej do demo ke liye
            return send_file(input_p, as_attachment=True)
    except Exception as e:
        print(f"Processing Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
