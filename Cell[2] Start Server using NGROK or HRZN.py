#=======================Updated=========================
import codecs
import json
import subprocess, threading, time, socket, urllib.request, portpicker, json
from IPython.display import clear_output, Javascript
from IPython.display import Audio, display

# @title **Cell[2]** Start Server using **NGROK** or **HRZN**
# @markdown This cell will start the server, the first time that you run it will download the models, so it can take a while (~1-2 minutes)

#======================Tunnels===========================

TUNNEL = "NGROK" #@param ["NGROK","HRZN"]

# @markdown ---
# @markdown You'll need a NGROK or HRZN account, but <font color=green>**it's free**</font> and easy to create!
# @markdown ---
# @markdown **1** - Create a <font color=green>**free**</font> account at [ngrok](https://dashboard.ngrok.com/signup) / [hrzn](https://hrzn.run/login) or **login with Google/Github account**\
# @markdown **2** - If you didn't logged in with Google/Github, you will need to **verify your e-mail**!\
# @markdown **3** - Get your [ngrok](https://dashboard.ngrok.com/get-started/your-authtoken) or [hrzn](https://hrzn.run/dashboard) to get your auth token, and place it here:
Token = '2Wu5TirnnuDUDZskugnY9Dhf1pm_2ebvcbeo5Hs3Rcy7Xh7zX' # @param {type:"string"}
# @markdown **4** - *(OPTIONAL FOR NGROK)* Change to a region near to you\
# @markdown `Default Region: ap - Asia/Pacific (Singapore)`
Region = "ap - Asia/Pacific (Singapore)" # @param ["ap - Asia/Pacific (Singapore)", "au - Australia (Sydney)","eu - Europe (Frankfurt)", "in - India (Mumbai)","jp - Japan (Tokyo)","sa - South America (Sao Paulo)", "us - United States (Ohio)"]

#@markdown **5** - *(optional)* Other options:
ClearConsole = True  # @param {type:"boolean"}

# ---------------------------------
# DO NOT TOUCH ANYTHING DOWN BELOW!
# ---------------------------------
if version == "V1(new)":

    PORT = 18888
    if not globals().get('Ready', False):
        print("Go back and run first cells.")
    else:
        if TUNNEL == "NGROK":
            if not globals().get('Ready', False):
                print("Go back and run first and second cells.")
            else:
                from pyngrok import conf, ngrok
                MyConfig = conf.PyngrokConfig()
                MyConfig.auth_token = Token
                MyConfig.region = Region[0:2]
                conf.get_default().authtoken = Token
                conf.get_default().region = Region
                conf.set_default(MyConfig)

                import threading, time, socket
                import json
                from pyngrok import ngrok
                from IPython.display import clear_output

                ngrokConnection = ngrok.connect(PORT)
                public_url = ngrokConnection.public_url

        elif TUNNEL == "HRZN":
            !rm -rf url.txt
            !hrzn login $Token
            os.system(f"hrzn tunnel http://localhost:{PORT} >> url.txt 2>&1 &")
            time.sleep(5)

            with open('url.txt', 'r') as file:
                public_url = file.read()
                public_url = !grep -oE "https://[a-zA-Z0-9.-]+\.hrzn\.run" url.txt
                public_url = public_url[0]

        set_key('.env', "ALLOWED_ORIGINS", json.dumps([public_url]))

        def wait_for_server():
            while True:
                time.sleep(0.5)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('127.0.0.1', PORT))
                if result == 0:
                    break
                sock.close()
            if ClearConsole:
                clear_output()
            print("--------- SERVER READY! ---------")
            print("Your server is available at:")
            print(public_url)
            print("---------------------------------")

        threading.Thread(target=wait_for_server, daemon=True).start()

        !./$path

        clear_output()
        if TUNNEL == "NGROK":
            ngrok.disconnect(ngrokConnection.public_url)
            print("--------- SERVER STOPPED! ---------")
        elif TUNNEL == "HRZN":
            !rm -rf url.txt
            !fuser -k ${PORT}
            print("--------- SERVER STOPPED! ---------")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

elif version == "V1(ori)":

    # Check if Run_Cell
    PORT = portpicker.pick_unused_port()
    if 'Run_Cell' not in globals():
        print("No, Go back to the first cell and run it")
    else:
        if Run_Cell == 0:
            print("No, Go back to the first cell and run it")
        else:
            if TUNNEL == "NGROK":
              from pyngrok import conf, ngrok
              MyConfig = conf.PyngrokConfig()
              MyConfig.auth_token = Token
              MyConfig.region = Region[0:2]
              conf.set_default(MyConfig)
              ngrokConnection = ngrok.connect(PORT)
              public_url = ngrokConnection.public_url
            elif TUNNEL == "HRZN":
              !rm -rf url.txt
              !hrzn login $Token
              os.system(f"hrzn tunnel http://localhost:{PORT} >> url.txt 2>&1 &")
              time.sleep(5)

              with open('url.txt', 'r') as file:
                public_url = file.read()
                public_url = !grep -oE "https://[a-zA-Z0-9.-]+\.hrzn\.run" url.txt
                public_url = public_url[0]

            def wait_for_server():
                while True:
                    time.sleep(0.5)
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(('127.0.0.1', PORT))
                    if result == 0:
                        break
                    sock.close()
                if ClearConsole:
                    clear_output()
                print("--------- SERVER READY! ---------")
                print("Your server is available at:")
                print(public_url)
                print("---------------------------------")

            threading.Thread(target=wait_for_server, daemon=True).start()

            mainpy = codecs.decode('ZZIPFreireFVB.cl', 'rot_13')
            mainname = codecs.decode('ZZIPFreireFVB', 'rot_13')
            !mv {mainpy} HVoice.py
            !sed -i "s/MMVCServerSIO/HVoice/" HVoice.py
            !python3 HVoice.py \
              -p {PORT} \
              --https False \
              --content_vec_500 pretrain/checkpoint_best_legacy_500.pt \
              --content_vec_500_onnx pretrain/content_vec_500.onnx \
              --content_vec_500_onnx_on false \
              --hubert_base pretrain/hubert_base.pt \
              --hubert_base_jp pretrain/rinna_hubert_base_jp.pt \
              --hubert_soft pretrain/hubert/hubert-soft-0d54a1f4.pt \
              --nsf_hifigan pretrain/nsf_hifigan/model \
              --crepe_onnx_full pretrain/crepe_onnx_full.onnx \
              --crepe_onnx_tiny pretrain/crepe_onnx_tiny.onnx \
              --rmvpe pretrain/rmvpe.pt \
              --model_dir model_dir \
              --samples samples.json \
              --allowed-origins {public_url}

            clear_output()
            if TUNNEL == "NGROK":
              ngrok.disconnect(ngrokConnection.public_url)
              print("--------- SERVER STOPPED! ---------")
            elif TUNNEL == "HRZN":
              !rm -rf url.txt
              !fuser -k ${PORT}
              print("--------- SERVER STOPPED! ---------")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

elif version == "V2":

    import time
    from IPython.display import clear_output, display, Javascript
    PORT = portpicker.pick_unused_port()
    LOG_FILE = f"/content/LOG_FILE_{PORT}"

    # Start
    if mode == "elf":
        get_ipython().system_raw(f'LD_LIBRARY_PATH=/usr/lib64-nvidia:/usr/lib/x86_64-linux-gnu ./vcclient_latest_for_colab cui --port {PORT} --no_cui true >{LOG_FILE} 2>&1 &')
    elif mode == "zip":
        !LD_LIBRARY_PATH=/usr/lib64-nvidia:/usr/lib/x86_64-linux-gnu ./main cui --port {PORT} --no_cui true &

    # Tunggu sampai server dimulai
    print('\033[31m\033[1m\033[3mTunggu sampai server dimulai\033[0m')
    time.sleep(130)

    if TUNNEL == "NGROK":

        from pyngrok import ngrok
        Close_Ngrok = True
        Open_New_Tab = True

        from pyngrok import conf, ngrok
        MyConfig = conf.PyngrokConfig()
        MyConfig.auth_token = Token
        MyConfig.region = Region[0:2]
        conf.set_default(MyConfig)
        ngrokConnection = ngrok.connect(PORT)
        public_url = ngrokConnection.public_url
        clear_output()

        if Open_New_Tab:
            display(Javascript(f'window.open("{public_url}", "_blank");'))

        print("--------- SERVER LINK ---------")
        print('\033[32m\033[1m\033[3mServer Sudah Berjalan\033[0m')
        print("PUBLIC URL:", public_url)
        print("---------------------------------")

    elif TUNNEL == "HRZN":
        !rm -rf url.txt
        !hrzn login $Token
        os.system(f"hrzn tunnel http://localhost:{PORT} >> url.txt 2>&1 &")
        time.sleep(5)

        with open('url.txt', 'r') as file:
          public_url = file.read()
          public_url = !grep -oE "https://[a-zA-Z0-9.-]+\.hrzn\.run" url.txt
          public_url = public_url[0]

        print("--------- SERVER LINK ---------")
        print('\033[32m\033[1m\033[3mServer Sudah Berjalan\033[0m')
        print("PUBLIC URL:", public_url)
        print("---------------------------------")
