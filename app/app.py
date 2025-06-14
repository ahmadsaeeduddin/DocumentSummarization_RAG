from flask import Flask, request, send_file, jsonify
import os
from Backend.main import summarize_pipeline

UPLOAD_FOLDER = 'Data'
SUMMARY_FOLDER = os.path.join(os.path.dirname(__file__), 'Summaries')

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(SUMMARY_FOLDER, exist_ok=True)

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SUMMARY_FOLDER'] = SUMMARY_FOLDER

@app.route('/')
def index():
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html'))

@app.route('/summarize', methods=['POST'])
def summarize():
    uploaded_file = request.files.get('file')
    if uploaded_file:
        filename = uploaded_file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)

        summary = summarize_pipeline(filepath)

        # Save summary to file
        summary_path = os.path.join(app.config['SUMMARY_FOLDER'], f"{filename}_summary.txt")
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary)

        return jsonify({'filename': filename, 'summary': summary})

    return jsonify({'error': 'No file uploaded'}), 400

@app.route('/download/<filename>')
def download_summary(filename):
    path = os.path.join(app.config['SUMMARY_FOLDER'], f"{filename}_summary.txt")
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
