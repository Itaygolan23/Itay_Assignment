import argparse
import subprocess
import threading


# Run the command on all the IP addresses in the list in Multithreading
def run_command(ip,command):
    ssh = subprocess.Popen(["ssh", "root@%s" % ip, command],)
    print(ssh.stdout)

def main():
    # Parse the arguments
    parser = argparse.ArgumentParser()
    # List of IP addresses
    parser.add_argument('-l', '--list',
                        type=str, nargs='+', action='store',
                        dest='list',
                        help='<Required> List of IP addresses',
                        required=True)

    # Linux Command
    parser.add_argument("-c", type=str, help="<Required> User Linux Command")
    
    args = parser.parse_args()

    # Chceking the format of the IP address
    for ip in args.list:
        if not ip.count('.') == 3:
            print("Invalid IP address")
            return

    IP_list = []
    # Create a thread for each IP address
    for ip in args.list:
        t = threading.Thread(target=run_command, args=(ip,args.c))
        IP_list.append(t)
        t.start()
        
    # Wait for all the threads to finish
    for i in IP_list:
        i.join()

    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())

if __name__ == '__main__':
    main()

