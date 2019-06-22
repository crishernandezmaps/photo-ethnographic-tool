import sys
import shutil
import datetime
import os, glob
from flask import Flask, render_template, send_from_directory, request, json
from PIL import Image, ExifTags
from iptcinfo3 import IPTCInfo
from geojson import Point, Feature, FeatureCollection, dump

__author__ = 'ibininja'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# @app.route("/")
# def index():
#     return render_template("upload.html")

# @app.route("/upload", methods=["POST"])
# def upload():
#     target = os.path.join(APP_ROOT, 'images/')
#     print(target)
#     if not os.path.isdir(target):
#             os.mkdir(target)
#     else:
#         print("Couldn't create upload directory: {}".format(target))
#     print(request.files.getlist("file"))
#     for upload in request.files.getlist("file"):
#         print(upload)
#         print("{} is the file name".format(upload.filename))
#         filename = upload.filename
#         destination = "/".join([target, filename])
#         print ("Accept incoming file:", filename)
#         print ("Save it to:", destination)
#         upload.save(destination)
    
#     shutil.rmtree(target)
    
#     # return send_from_directory("images", filename, as_attachment=True)
#     return render_template("gallery.html", image_name=filename)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

@app.route('/')
def get_gallery():
    return 'Caca'    

# @app.route('/gallery')
# def get_gallery():
#     image_names = os.listdir('./images')
#     print(image_names)
#     return render_template("complete_display_image.html", image_names=image_names)



# # initialization
# app = Flask(__name__)
# app.config.update(
#     DEBUG = True,
# )

# # base variables #
# d = str(datetime.datetime.now())
# timeStamp = d.split(' ')[0].strip()

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# # controllers #
# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

# #####################
# @app.route("/upload", methods=['GET','POST'])
# def upload():
#     target = os.path.join(APP_ROOT, 'images/')
#     print(target)
#     if not os.path.isdir(target):
#             os.mkdir(target)
#     else:
#         print("Couldn't create upload directory: {}".format(target))
#     print(request.files.getlist("file"))
#     for upload in request.files.getlist("file"):
#         print(upload)
#         print("{} is the file name".format(upload.filename))
#         filename = upload.filename
#         destination = "/".join([target, filename])
#         print ("Accept incoming file:", filename)
#         print ("Save it to:", destination)
#         upload.save(destination)

#     # return send_from_directory("images", filename, as_attachment=True)
#     return render_template("complete.html", image_name=filename)

# @app.route('/upload/<filename>')
# def send_image(filename):
#     return send_from_directory("images", filename)

# @app.route('/gallery')
# def get_gallery():
#     image_names = os.listdir('./images')
#     print(image_names)
#     return render_template("gallery.html", image_names=image_names)
# #####################   

# @app.route("/")
# def index():
#     return render_template('index.html')
#     # return render_template('upload.html')


# launch #
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)