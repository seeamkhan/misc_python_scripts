import subprocess
import pandas as pd
import time

ts = (str(pd.to_datetime(int(time.time()),unit='s'))).replace(':','-')

subprocess.run(['clip.exe'], input=ts.strip().encode('utf-16'), check=True)
print('timestamp copied to clipboard.')
