from flask import Flask, jsonify, render_template_string
from flask.templating import render_template
from gdrive import *
import json

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

drive = None


@app.route("/auth")
def api_auth():
    global drive 

    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive_created = GoogleDrive(gauth)
    drive = drive_created
    return {"Message": "Done"}

@app.route("/test")
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
    print(file_list)
    for file1 in file_list:
        file_obj = {
            "title": file1['title'],
            "id": file1['id'],
            "type": file1['mimeType']
        }
        all_files.append(file_obj)
        print(all_files)
    return jsonify(all_files)

    #     return render_template_string('''
    #     <table>
    #             <tr>
    #                 <td> Name </td> 
    #                 <td> Status </td>
    #             </tr>

    #     {% for label in labels %}
    #         {% for id, title in label.items() %}

    #                 <tr>
    #                     <td>{{ id }}</td> 
    #                     <td>{{ title }}</td>
    #                 </tr>

    #         {% endfor %}
    #     {% endfor %}


    #     </table>
    # ''', labels=all_files)



@app.route("/listall/<parent_folder_id>")
def list_subfolders(parent_folder_id):
    """
    [parent_folder_id]: string of parent folder ID given by api
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
    return jsonify(all_subjects)


@app.route("/createDoc", methods=["POST"])
def create_google_doc(title):
    file1 = drive.CreateFile({'title': title})
    file1.SetContentString('Hello')
    file1.Upload() # Files.insert()
