import requests
import wget
import zipfile
import subprocess
import os
from sys import platform
# from win32com.client import Dispatch

def IdentifiyPlatform():
    if platform == "darwin":
        installMacDriver()
    elif platform == "win32":
        installWindowDriver()

def installWindowDriver():
    pass

def installMacDriver():
    # driverVersion = subprocess.check_output("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version", shell=True)
    currentDirectory = os.getcwd()

    url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    response = requests.get(url)
    version_number = response.text

    # driverVersion = driverVersion.decode("utf-8").rstrip()
    # driverVersion = driverVersion.replace("Google Chrome", "").strip()

    # print(driverVersion)

    download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_mac64.zip"

    latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
        zip_ref.extractall(currentDirectory)

    os.remove(latest_driver_zip)
    os.chmod(currentDirectory + "/chromedriver", 0o755)

    # "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version"

installMacDriver()
