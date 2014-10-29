#!/usr/bin/env python
#-*-coding:utf-8-*-
#Python nginx cut log
import subprocess
def mkdir():
        subprocess.call('mkdir -pv /usr/local/nginx/logs/$(date -d "yesterday" +"%Y")/$(date -d "yesterday" +"%m")/',shell=True)
def mv():
        subprocess.call('mv /usr/local/nginx/logs/access.log /usr/local/nginx/logs/$(date -d "yesterday" +"%Y")/$(date -d "yesterday" +"%m")/access_$(date -d "yesterda
y" +"%Y%m%d").log',shell=True)
def kill():
        pid = open("/usr/local/nginx/logs/nginx.pid","r")
        f = pid.read()
        f = f.strip()
        pid.close()
        kill = "kill"
        kill_usage = "-USR1"
        subprocess.call([kill,kill_usage,f])
def main():
        mkdir()
        mv()
        kill()
if __name__ == "__main__":
        main()