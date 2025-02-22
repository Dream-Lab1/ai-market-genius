from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Function: Generate AI Business Report
def generate_business_report(business_name, industry):
    strategies = [
        f"📈 Growth Strategy for {business_name}:\n- Focus on digital marketing and SEO.\n- Collaborate with influencers.\n- Engage in {industry}-related forums.",
        f"🏆 Competitive Edge for {business_name}:\n- Provide outstanding customer service.\n- Innovate with AI-driven features.\n- Optimize pricing for higher conversions.",
        f"💰 Revenue Plan for {business_name}:\n- Implement a subscription model.\n- Use upselling strategies.\n- Expand internationally with localization."
    ]
    return random.choice(strategies)

@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.json
    business_name = data.get("business_name")
    industry = data.get("industry")

    if not business_name or not industry:
        return jsonify({"error": "Missing data"}), 400

    report = generate_business_report(business_name, industry)
    return jsonify({"report": report})

if __name__ == '__main__':
    app.run(debug=True)
