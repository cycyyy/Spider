import subprocess
import time

while True:
    subprocess.call('python spider.py wenzinvliumang',shell=True)
    subprocess.call('python spider.py shibasui',shell=True)
    subprocess.call('python spider.py woaigif',shell=True)
    time.sleep(3600)
