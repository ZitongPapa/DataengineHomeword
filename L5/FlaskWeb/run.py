'''__author__=='Aaron'
    仅写了一个wordcloud示例 
'''

import os
import shutil
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
from echartplot import get_html


UPLOAD_FOLDER = 'static/upload'



# ALLOWED_EXTENSIONS = set(['csv'])
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# upload文件夹路径
file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
# files路径 常用常量文件
constfile_dir= os.path.join(basedir, 'static/files')

@app.route('/', methods=['GET'])
def plotlythml():
    return render_template('pyechart.html')


@app.route('/api/plotly', methods=['POST'], strict_slashes=False)
def plotlys():
    max_words=int(request.form['top'])
    for file in request.files.getlist('myfile'):
        if file:
            filename = secure_filename(file.filename)
            file_in = os.path.join(file_dir, filename)
            file.save(file_in)
            file_out = os.path.join(file_dir, 'wordcloud.html')
            get_html(file_in, file_out,max_words)
            return redirect(url_for('justopen', filename='wordcloud.html'))

@app.route("/open/<path:filename>")
def justopen(filename):
    dirpath = os.path.join(app.root_path,
                           'static/upload')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=False)  # as_attachment=True 一定要写，不然会变成打开，而不是下载



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
