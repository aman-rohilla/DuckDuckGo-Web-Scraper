import sys, os

platform = sys.platform
if platform != 'mac' and platform != 'linux':
  platform = 'win64'

chromium_urls = {
  'linux': 'https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/1048450/chrome-linux.zip',
  'mac': 'https://storage.googleapis.com/chromium-browser-snapshots/Mac/1048450/chrome-mac.zip',
  'win64': 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/1048450/chrome-win.zip'
}

chromium_executables = {
  'linux': 'chrome-linux/chrome',
  'mac': 'chrome-mac/Chromium.app/Contents/MacOS/Chromium',
  'win64': 'chrome-win/chrome.exe',
}

chromium = chromium_urls[platform]
chromium_exe = chromium_executables[platform]
zip_file = chromium.split('/')[-1]

def chromium_downloader():
  print('\nDownloading chromium, please wait... ', end='')
  import requests
  import shutil

  with requests.get(chromium, stream=True) as req:
    with open(zip_file, 'wb') as file:
      shutil.copyfileobj(req.raw, file)
      
  print('Done',end='')
  print('\nUnpacking Zip... ', end='')
  shutil.unpack_archive(zip_file)
  os.remove(zip_file)
  print('Done\n')
