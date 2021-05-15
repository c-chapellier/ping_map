import os
import sys
import subprocess
import random

from ip2geotools.databases.noncommercial import DbIpCity

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ping_the_world:

    def __init__(self, saving_file='locations.csv'):
        self.__saving_file = saving_file
        self.__init_locations_saving_file()

    def __init_locations_saving_file(self):
        if not os.path.exists(self.__saving_file):
            if os.path.isdir(self.__saving_file):
                print('./locations.csv must be a file', file=sys.stderr)
                exit(1)
            with open(self.__saving_file, 'a+') as f:
                f.write('ip,city,region,country,latitude,longitude,rtt\n')

    @staticmethod
    def random_ip():
        # Return a random IPV4 address.
        ip = str(random.randrange(256))
        for _ in range(3):
            ip += '.' + str(random.randrange(256))
        return ip

    @staticmethod
    def __ping(ip):
        # Try to ping an ip.
        # Return the round-trip time (RTT) on success.
        # Throw an error on failure.
        output = subprocess.check_output(['ping', '-c', '1', '-t', '1', ip])
        return float(output.splitlines()[1].split()[-2][5:])

    def __call__(self, ip):
        # Try to ping an ip.
        # Save infos about the IP address and the round-trip time (RTT) on success.
        try:
            rtt = self.__ping(ip)
            print('ping[' + bcolors.OKGREEN + ip + bcolors.ENDC + ']')
            # Request infos about an IP address.
            ip_infos = DbIpCity.get(ip, api_key='free')
            print(ip_infos.to_json(), rtt)
            with open(self.__saving_file, 'a+') as f:
                f.write(ip_infos.to_csv(',') + ',' + str(rtt) + '\n')
        except Exception as e:
            print('ping[' + bcolors.FAIL + ip + bcolors.ENDC + ']')
            # Check if the error was throw by the ping request.
            if e.__class__ != subprocess.CalledProcessError:
                print(e.__class__, file=sys.stderr)


def main():
    ptw = ping_the_world()

    # If arguments are provided, ping each one of theses IP adresses.
    if (len(sys.argv) > 1):
        for ip in sys.argv:
            ptw(ip)
        exit(0)

    # If no arguments are provided, ping random IP adresses.
    while True:
        ptw(ptw.random_ip())

if __name__ == '__main__':
    # Handle ctrl-C
    try:
       main()
    except KeyboardInterrupt:
        print('\n\n[Process completed]')
        exit(1)