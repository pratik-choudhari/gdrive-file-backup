import os 
import shutil
import sys
import time
import schedule
from datetime import datetime

from pydrive.drive import GoogleDrive 
from pydrive.auth import GoogleAuth 

def create_zip(path, file_name):
    try:
        shutil.make_archive(f"archive/{file_name}", 'zip', path)
        return True
    except FileNotFoundError as e:
        return False

def google_auth():
    gauth = GoogleAuth() 
    gauth.LocalWebserverAuth()        
    drive = GoogleDrive(gauth) 
    return gauth, drive

def upload_backup(drive, path, file_name):
    f = drive.CreateFile({'title': file_name}) 
    f.SetContentFile(os.path.join(path, file_name)) 
    f.Upload() 
    f = None

def controller():
    path = r"/home/user/Desktop/gdrive-file-backup/backup_me"
    now = datetime.now()
    file_name = "backup " + now.strftime(r"%d/%m/%Y %H:%M:%S").replace('/', '-')

    if  not create_zip(path, file_name):
        sys.exit(0)
    auth, drive = google_auth()
    upload_backup(drive, r"/home/user/Desktop/gdrive-file-backup/archive", file_name+'.zip')

if __name__=="__main__":
    schedule.every().day.at("00:00").do(controller)
    while True:
        schedule.run_pending()
