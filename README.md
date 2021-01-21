# gdrive-file-backup

![](https://img.shields.io/badge/MadeWith-Python-green)
[![](https://img.shields.io/badge/BuiltFor-MLH(LHD)-yellow)](https://www.mlh.io)


Script to automate folder backups on google drive.

### Learn about the entire process from start to end in this blog: 
https://pratik-choudhari.medium.com/automate-google-drive-backup-using-python-105f57e2151

## Set up:
1. `pip3 install -r requirements.txt`
2. This project uses Google drive API which requires a client secret, [follow step-1 only from this procedure](https://developers.google.com/drive/api/v3/quickstart/python). Save the secret file as `client_secrets.json` and place in project folder.
3. Execute `python3 automate_backup.py`

## Info:
1. This file is set to run everyday at 12:00 am.
2. Zip file is uploaded to `My Drive`.
3. Local backup is srored in `archive` folder.
4. By default  `backup_me` is set as backup folder

## Leave a star, if it helped you in anyway :)
