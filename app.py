import sys
import shutil
import datetime
import os, glob
from flask import Flask, render_template, send_from_directory, request, json
from PIL import Image, ExifTags
from iptcinfo3 import IPTCInfo
from geojson import Point, Feature, FeatureCollection, dump

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

def getFileWithExt(extension,pathFolder):
    cd = os.chdir(pathFolder)
    filesEXT = []
    ext = ''.join(['*.',extension])
    for f in glob.glob(ext):
        filesEXT.append(f)
    return filesEXT 

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    if(os.path.isdir(target)):
        shutil.rmtree(target)
        os.mkdir(target)
    else:
        os.mkdir(target)

    for upload in request.files.getlist("file"):
        filename = upload.filename
        destination = "".join([target, filename])
        upload.save(destination)
    
    collection = []
    lisOfBigImages = getFileWithExt('jpg',target)
    for i in lisOfBigImages:
        try:
            openSmall = Image.open(i)
            exif = { ExifTags.TAGS[k]: v for k, v in openSmall._getexif().items() if k in ExifTags.TAGS }
            dateTime = exif['DateTime'][0:10].replace(':','-').strip()
            lat = [float(x)/float(y) for x, y in exif['GPSInfo'][2]]
            lon = [float(x)/float(y) for x, y in exif['GPSInfo'][4]]
            latref = exif['GPSInfo'][1]
            lonref = exif['GPSInfo'][3]
            lat = lat[0] + lat[1]/60 + lat[2]/3600
            lon = lon[0] + lon[1]/60 + lon[2]/3600
            if latref == 'S':
                lat = -lat
            if lonref == 'W':
                lon = -lon

            info = IPTCInfo(i,force=True)
            kw = []
            for x in info['keywords']:
                kw.append(x.decode("utf-8") ) 
            
            o = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [lon,lat]
                },
                "properties": {
                    "name": i,
                    "date": dateTime,
                    "tags": kw,
                    "image": "",
                    "author": "FONDECYT N1171554, INVI - U. of Chile, 2018/9"
                }
            } 
            
            collection.append(o) 
        except:
            pass
    
    data = {
        "type": "FeatureCollection",
        "features": collection
    }

    r = app.response_class(
        response=json.dumps(data,indent=4),
        mimetype='application/json'
    )

    shutil.rmtree(target)
    return r

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

# @app.route('/')
# def get_gallery():
#     return 'Caca'    

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