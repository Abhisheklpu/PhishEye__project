from flask import Flask, render_template, request
import re

app = Flask(__name__)

def is_phishing(url):
    suspicious_keywords = ['login', 'verify', 'update', 'secure', 'account', 'banking']
    if any(keyword in url.lower() for keyword in suspicious_keywords):
        return "⚠️ This URL is likely a phishing site!"
    if re.match(r'^https?://', url) is None:
        return "❌ Invalid URL format. Please include http:// or https://"
    return "✅ This URL appears safe (but always double-check)!"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        url = request.form.get('url')
        result = is_phishing(url)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
