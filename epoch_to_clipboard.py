import time
import subprocess
ts = str(int(time.time()))
subprocess.run(['clip.exe'], input=ts.strip().encode('utf-16'), check=True)
print('epoch timestamp copied to clipboard.')
#input("press anykey to exit.. ")