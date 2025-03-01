from flask import Flask, request, jsonify
import openai
from report_generator import generate_cosmic_report
from pdf_generator import generate_pdf

app = Flask(__name__)

# Replace with your OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/", methods=["GET"])
def home():
    return "Cosmic Destiny API is running!"

@app.route("/generate_report", methods=["POST"])
def generate_report():
    try:
        data = request.json
        name = data.get("name")
        birthdate = data.get("birthdate")
        location = data.get("location")

        if not name or not birthdate or not location:
            return jsonify({"error": "Missing required fields"}), 400

        # Generate report content using OpenAI
        report_text = generate_cosmic_report(name, birthdate, location)

        # Convert report to PDF
        pdf_path = generate_pdf(name, report_text)

        return jsonify({"message": "Report generated successfully", "pdf_url": pdf_path})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
