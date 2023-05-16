from flask import Flask, render_template, request, send_file, jsonify
from werkzeug.utils import secure_filename
from tools.gpt import gpt_modify
import os
from cover_letter_creator import generate_cover_letter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        CV = request.files['CV']
        job_url = request.form.get('job_url')
        job_description = request.form.get('job_description')
        special_request = request.form.get('special_request')

        CV.save(CV.filename)
        cover_letter, filename = generate_cover_letter(CV.filename, job_url, job_description, special_request)
        if cover_letter is None:
            return render_template('result.html', cover_letter=None, filename=None)

        os.remove(CV.filename)

        return render_template('result.html', cover_letter=cover_letter, filename=filename)
    return render_template('index.html')

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_file(filename, as_attachment=True)

@app.route('/modify_cover_letter', methods=['POST'])
def modify_cover_letter():
    data = request.json
    chat_input = data.get('chat_input')
    cover_letter = data.get('cover_letter')

    modified_cover_letter = gpt_modify(chat_input, cover_letter)

    return modified_cover_letter




if __name__ == '__main__':
    app.run(debug=True)
