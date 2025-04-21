from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Membaca file CSV menggunakan Pandas
        data = pd.read_csv(file_path)
        
        # Melakukan analisis statistik dasar
        summary = data.describe().to_html(classes='table table-striped', index=True)
        
        return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)