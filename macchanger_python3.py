#!/usr/bin/env python3

#MAC Address Changer from Learn Python and Ethical Hacking from Scratch course
#by Zaid Al-Quraishi https://zsecurity.org/

import optparse #module for parsing options passed in at command line
import re #regular expression operator module
import subprocess #module for making calls to system commands

def change_mac(interface, newmac):
    print("[+] Changing MAC address for", interface, "to", newmac)
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", newmac])
    subprocess.run(["ifconfig", interface, "up"])

def check_mac(interface):
    #check that MAC address was changed successfully
    ifconfig_result = str(subprocess.check_output(["ifconfig", interface]))
    #python 3 returns subprocess.check_output as bytes like object
    #re operators don't work on bytes like objects so must be converted to str
    mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    #regular expression to return only pattern of MAC address, see pythex for more regex rules
    if mac_search_result:
        #re.search will return multiple groups of results if it finds them
        #returning group 0 only returns the first result, which is all that is needed
        return mac_search_result.group(0)
    else:
        print("[-] MAC address for interface", interface, "not found.")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address of")
    parser.add_option("-m", "--mac", dest="newmac", help="MAC address to change to")
    (options, arguments) = parser.parse_args()
    if not options.interface: #if no interface is given
        parser.error("[-] Please enter an interface, use --help for more information.")
        #parser.error is a function of OptionParser, will show error message you specify then exit
    elif not options.newmac: #if MAC address is not given
        parser.error("[-] Please enter the new MAC address, use --help for more information.")
    return options

def troubleshooting(options):
    print("Variable 'options' captured and is the type: ", type(options))
    #print("Variable 'arguments' captured and is the type: ", type(arguments))
    print("Variable 'options' equals:", options)
    #print("Variable 'arguments' equals:", arguments)

options = get_arguments()

oldmac = check_mac(options.interface)
print("MAC address before changing: ", oldmac)

change_mac(options.interface, options.newmac)
currentmac = check_mac(options.interface)
if currentmac == options.newmac:
    print("[+] MAC for interface", options.interface, "was changed successfully.")
else:
    print("[-] MAC for interface", options.interface, "was NOT changed, check for errors and try again.")
