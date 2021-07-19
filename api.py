from flask import Flask
from gdrive import *
import json
from flask import jsonify

from flask_cors import CORS, cross_origin



app = Flask(__name__)
cors = CORS(app)

drive = ""

@app.route("/auth")
def api_auth():
    drive = auth()
    print(drive)
    return {"Drive": "success"}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/listall")
def list_all():
    """
    ------------------
    [returns]: All files from root directory
    """
    all_files = []
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    for file1 in file_list:
        file_obj = {
            "title": file1['title'],
            "id": file1['id'],
            "type": file1['mimeType']
        }
        all_files.append(json.dumps(file_obj))
    return {"Success" : all_files}



@app.route("/listall/<parent_folder_id>")
def list_subfolders(parent_folder_id):
    """
    [parent_folder_id]: string
    ------------------
    [returns]: All Files under an ID. If ID does not refer to a folder, then returns empty list.
    """
    all_subjects = []
    foldered_list=drive.ListFile({'q':  "'"+parent_folder_id+"' in parents and trashed=false"}).GetList()
    for file in foldered_list:
        print(file.keys())
        subject = {
            "subject": file['title'], 
            "id": file['id'],
            "type": file['mimeType']
        }
        all_subjects.append(json.dumps(subject))
    return {"Success" : all_subjects}


@app.route("/createDoc", methods=["POST"])
def create_google_doc(title):
    file1 = drive.CreateFile({'title': title})
    file1.SetContentString('Hello')
    file1.Upload() # Files.insert()