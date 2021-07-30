from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

drive = None

# def auth():
#     gauth = GoogleAuth()
#     gauth.LocalWebserverAuth()
#     drive = GoogleDrive(gauth)
#     drive = drive
#     #return drive


# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()
# drive = GoogleDrive(gauth)
# drive = drive


    

def create_file(title, content):
    """
    [title]: string
    [content]: string
    ------------------
    Creates a file in authenticated user's google drive. 
    """
    file_new = drive.CreateFile({'title': title})
    file_new.SetContentString('Hello')
    file_new.Upload() # Files.insert()


def create_folder(parent_folder_id, subfolder_name):
    """
    [parent_folder_id]: string
    [subfolder_name]: string
    ------------------
    Creates a file in authenticated user's google drive. 
    """
    newFolder = drive.CreateFile({'title': subfolder_name, "parents": [{"kind": "drive#fileLink", "id": \
    parent_folder_id}],"mimeType": "application/vnd.google-apps.folder"})
    newFolder.Upload()
    return newFolder


def folder_browser(folder_list,parent_id):
    browsed=[]
    for element in folder_list:
        if type(element) is dict:
            print (element['title'])
        else:
            print (element)
            print("Enter Name of Folder You Want to Use\nEnter '/' to use current folder\nEnter ':' to create New Folder and use that" )
            inp=input()
            if inp=='/':
                return parent_id
            
            elif inp==':':
                print("Enter Name of Folder You Want to Create")
                inp=input()
                newfolder=create_folder(parent_id,inp)
                if not os.path.exists(HOME_DIRECTORY+ROOT_FOLDER_NAME+os.path.sep+USERNAME):
                    os.makedirs(HOME_DIRECTORY+ROOT_FOLDER_NAME+os.path.sep+USERNAME)
                return newfolder['id']

            else:
                folder_selected=inp
                for element in folder_list:
                    if type(element) is dict:
                        if element["title"]==folder_selected:
                            struc=element["list"]
                            browsed.append(folder_selected)
                            print("Inside "+folder_selected)
                            return folder_browser(struc,element['id'])