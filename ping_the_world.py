import os
import platform
import subprocess
import random

from ip2geotools.databases.noncommercial import DbIpCity

def ping(ip, fnull):
    command = ['ping', '-c', '1', '-t', '1', ip]
    try:
        output = subprocess.check_output(command)
    except:
        return -1
    return float(output.splitlines()[1].split()[-2][5:])

fnull = open(os.devnull, 'w')

while True:
    ip = str(random.randrange(256)) + '.' + str(random.randrange(256)) + '.' + str(random.randrange(256)) + '.' + str(random.randrange(256))
    time = ping(ip, fnull)
    if time != -1:
        try:
            response = DbIpCity.get(ip, api_key='free')
        except:
            print("API error")
            continue
        print(response.to_json())
        f = open("locations.csv", "a+")
        f.write(response.to_csv(',') + ',' + str(time) + '\n')
        f.close()