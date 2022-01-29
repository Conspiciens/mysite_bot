import requests
import wget
import zipfile
import subprocess
import os
from sys import platform
# from win32com.client import Dispatch

def IdentifiyPlatformthenInstallDriver():
    if platform == "darwin":
        installMacDriver()
    elif platform == "win32":
        installWindowDriver()

def installWindowDriver():
    currentDirectory = os.getcwd()

    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall(currentDirectory)

    os.remove(latest_driver_zip)
    os.chmod(currentDirectory + "\\chromedriver.exe", 0o755)

def installMacDriver():
    currentDirectory = os.getcwd()

    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_mac64.zip"

    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall(currentDirectory)

    os.remove(latest_driver_zip)
    os.chmod(currentDirectory + "/chromedriver", 0o755)
