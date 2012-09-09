#!/usr/bin/python
# Update script for Backtrack 5 R2/R3. 
# Author: sickness
# Thanks goes to: g0tmi1k
# #########################################
#
# Depending on how you run the script it may cause issues with your Backtrack installation. 
# DO NOT RUN IT UNLESS YOU KNOW WHAT YOU ARE DOING.
# Further more I am not responsable if your Backtrack OS starts encountering issues.
#
###########################################

# Imports
import sys, urllib2, subprocess, argparse, os
from time import sleep
from argparse import RawTextHelpFormatter

GREEN = '\033[92m'
END = '\033[0m'
RED = '\033[31m'

# Update Functions
def internet_check(): 
	try: 
		urllib2.urlopen("http://www.google.com", timeout=1)
		print "\n"
		print GREEN + "[>] Internet connection: available!" + END
		sleep(0.1)
	except: 
		print "\n"
		print RED + "[>] Internet connection: unavailable!" + END
		sys.exit()

def backtrack_update():
    print GREEN + "[>] Updating & cleaning Backtrack, please wait...\n" + END
    if subprocess.Popen("ls -l /pentest/web/scanners/ 2>/dev/null | grep -q 0",shell=True).wait() == 0:
	subprocess.Popen("rm -rf /pentest/web/scanners/",shell=True).wait()
    if subprocess.Popen("apt-get update && apt-get -y dist-upgrade",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Backtrack updated & cleaned successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Backtrack\n" + END
        sleep(2)

def exploit_db():
    print GREEN + "[>] Updating Exploit-DB, please wait...\n" + END

    if subprocess.Popen("cd /pentest/exploits/exploitdb/ && svn up",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Exploit-DB updated successfully!" + END
    else:
        print RED + "[>] Exploit-DB's SVN didn't work. Updating manually. Please wait...\n" + END
        if subprocess.Popen("wget http://www.exploit-db.com/archive.tar.bz2",shell=True).wait() == 0: 
            subprocess.Popen("tar xvfj archive.tar.bz2 > /dev/null", shell=True).wait()
            subprocess.Popen("rm -rf /pentest/exploits/exploitdb/platforms/",shell=True).wait() 
            subprocess.Popen("mv -f platforms/ files.csv /pentest/exploits/exploitdb/",shell=True).wait()
            subprocess.Popen("rm -rf archive.tar.bz2*",shell=True).wait()
            print "\n"
            print GREEN + "[>] Exploit-DB updated successfully!" + END
        else:
            print "\n"
            print RED + "[>] Failed to update Exploit-DB\n" + END
            sleep(2)

def s_e_t():
    print GREEN + "[>] Updating SET, please wait...\n" + END

    if subprocess.Popen("cd /pentest/exploits/set/ && ./set-update",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] SET updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update SET\n" + END
        sleep(2)

def warvox():
    print RED + "[>] The following software has been completely integrated within Metasploit, update might fail!" + END
    print GREEN + "[>] Updating Warvox, please wait...\n" + END

    if subprocess.Popen("cd /pentest/telephony/warvox/ && svn up",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Warvox updated successfully!" + END
    elif subprocess.Popen("apt-get remove warvox -y && rm -rf /pentest/telephony/warvox/ && svn checkout http://www.metasploit.com/svn/warvox/trunk/ /pentest/telephony/warvox/",shell=True).wait() == 0:
    #elif subprocess.Popen("svn checkout http://www.metasploit.com/svn/warvox/trunk/ /pentest/telephony/warvox/",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Warvox updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Warvox\n" + END
        sleep(2)

def giskismet():
    print GREEN + "[>] Updating Giskismet, please wait...\n" + END

    if subprocess.Popen("cd /pentest/wireless/giskismet/ && svn up",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Giskismet updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Giskismet\n" + END
        sleep(2)

def dedected():
    print GREEN + "[>] Updating Dedected, please wait...\n" + END

    if subprocess.Popen("cd /pentest/telephony/dedected/ && svn up",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Dedected updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Dedected\n" + END
        sleep(2)

def msf():
    print GREEN + "[>] Updating Metasploit, please wait...\n" + END

    if subprocess.Popen("msfupdate",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Metasploit updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Metasploit\n" + END
        sleep(2)

def w3af():
    print GREEN + "[>] Updating W3AF, please wait...\n" + END

    if subprocess.Popen("cd /pentest/web/w3af/ && svn up",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] W3AF updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update W3AF\n" + END
        sleep(2)

def nikto():
    print RED + "[>] The following software hasn't been updated for an extensive period of time, update might fail!" + END
    print GREEN + "[>] Updating Nikto, please wait...\n" + END

    if subprocess.Popen("cd /pentest/web/nikto/ && ./nikto.pl -update",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Nikto updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Nikto\n" + END
        sleep(2)

def fasttrack():
    print GREEN + "[>] Updating Fast-track, please wait...\n" + END
    if subprocess.Popen("cd /pentest/exploits/fasttrack/ && ./fast-track.py -c 1",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Fast-track updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Fast-track\n" + END
        sleep(2)

def pyrit():
    print GREEN + "[>] Checking to see if Pyrit is installed" + END

    if subprocess.Popen("pyrit > /dev/null",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Pyrit installed!" + END
    else:
        print GREEN + "[>] Installing Pyrit, please wait...\n" + END
        subprocess.Popen("apt-get -y install libssl-dev scapy python-dev",shell=True).wait()
        subprocess.Popen("svn checkout http://pyrit.googlecode.com/svn/trunk/ pyrit_svn",shell=True).wait()
        subprocess.Popen("cd pyrit_svn/pyrit && python setup.py build && python setup.py install",shell=True).wait()
        subprocess.Popen("rm -rf pyrit_svn",shell=True).wait()
        print "\n"
        print GREEN + "[>] Pyrit installed successfully!" + END
        sleep(2)

def nmap():
    print GREEN + "[>] Updating Nmap fingerprint, please wait...\n" + END

    if subprocess.Popen("wget http://nmap.org/svn/nmap-os-db -O /usr/local/share/nmap/nmap-os-db",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] Nmap fingerprint updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update nmap fingerprint\n" + END
        sleep(2)

def fimap():
    print GREEN + "[>] Updating Fimap & installing MSF plugin, please wait...\n" + END

    if subprocess.Popen("cd /pentest/web/fimap/ && ./fimap.py --update-def",shell=True).wait() == 1:
        print "\n"
        print GREEN + "[>] Fimap updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update Fimap\n" + END
        sleep(2)

def wpscan():
    print GREEN + "[>] Updating WPScan, please wait...\n" + END
    
    if subprocess.Popen("gem list nokogiri | grep -q nokogiri",shell=True).wait() == 1: 
        print GREEN + "[>] Installing the required ruby gem, please wait...\n" + END
        if subprocess.Popen("gem install --user-install nokogiri",shell=True).wait() == 0: 
            print GREEN + "[>] Ruby gem installed successfully!" + END
        else: 
            print RED + "[>] Failed to install ruby gem\n" + END 

    if subprocess.Popen("cd /pentest/web/wpscan/ && svn up ",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] WPScan updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update WPScan\n" + END
        sleep(2)

def joomscan():
    print GREEN + "[>] Updating JoomScan, please wait...\n" + END

    if subprocess.Popen("cd /pentest/web/joomscan/ && perl joomscan.pl update",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] JoomScan updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update JoomScan\n" + END
        sleep(2)

def sqlmap():
    print GREEN + "[>] Updating SQLMap, please wait...\n" + END

    if subprocess.Popen("cd /pentest/database/sqlmap/ && python sqlmap.py --update",shell=True).wait() == 1:
        print "\n"
        print GREEN + "[>] SQLMap updated successfully!" + END
    elif subprocess.Popen("cd /pentest/database/sqlmap/ && svn update",shell=True).wait() == 1:
        print "\n"
        print GREEN + "[>] SQLMap updated successfully!" + END
    #elif subprocess.Popen("apt-get remove sqlmap && rm -rf /pentest/database/sqlmap/ && svn checkout https://svn.sqlmap.org/sqlmap/trunk/sqlmap /pentest/database/sqlmap/",shell=True).wait() == 1:
    elif subprocess.Popen("svn checkout https://svn.sqlmap.org/sqlmap/trunk/sqlmap /pentest/database/sqlmap/",shell=True).wait() == 1:
        print "\n"
        print GREEN + "[>] SQLMap updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update SQLMap\n" + END
        sleep(2)

def hexorbase():
    print GREEN + "[>] Updating HexorBase please wait...\n" + END

    if subprocess.Popen("cd /pentest/database/hexorbase/ && svn update",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] HexorBase updated successfully!" + END
    #elif subprocess.Popen("apt-get remove hexorbase && rm -rf /pentest/database/hexorbase/ && svn checkout http://hexorbase.googlecode.com/svn/ /pentest/database/hexorbase/",shell=True).wait() == 1:
    elif subprocess.Popen("svn checkout http://hexorbase.googlecode.com/svn/ /pentest/database/hexorbase/",shell=True).wait() == 1:
        print "\n"
        print GREEN + "[>] HexorBase updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update HexorBase\n" + END
        sleep(2)

def sqlninja():
    print GREEN + "[>] Updating SQLNinja, please wait...\n" + END

    if subprocess.Popen("apt-get remove sqlninja -y && rm -rf /pentest/database/sqlninja && svn co https://sqlninja.svn.sourceforge.net/svnroot/sqlninja /pentest/database/sqlninja",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] SQLNinja updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update SQLNinja\n" + END
        sleep(2)

def openvas():
    print GREEN + "[>] Updating OpenVAS, please wait...\n" + END

    if subprocess.Popen("openvas-nvt-sync",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] OpenVAS updated successfully!" + END

    else:
        print "\n"
        print RED + "[>] Failed to update OpenVAS\n" + END
        sleep(2)

def aircrack():
    print GREEN + "[>] Updating AirCrack-NG & Airodump, please wait...\n" + END

    subprocess.Popen("apt-get install libssl-dev",shell=True).wait()
    if subprocess.Popen("cd /pentest/wireless/aircrack-ng/ && svn up",shell=True).wait() == 0:
        subprocess.Popen("cd /pentest/wireless/aircrack-ng/scripts/ && chmod a+x airodump-ng-oui-update && ./airodump-ng-oui-update",shell=True).wait()
        print "\n"
        print GREEN + "[>] AirCrack-NG & Airodump updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update AirCrack-ng\n" + END
        sleep(2)
        
def webhandler():
    print GREEN + "[>] Updating WebHandler, please wait...\n" + END

    if subprocess.Popen("cd /pentest/backdoors/web/webhandler/ && python webhandler.py --update",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] WebHandler updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update WebHandler\n" + END
        sleep(2)
        
def beef():
    print GREEN + "[>] Updating BeEF, please wait...\n" + END

    if subprocess.Popen("cd /pentest/web/beef/ && ./update-beef",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] BeEF updated successfully!" + END
    else:
        print RED + "[>] Unable to update BeEF normally. Downloading a fresh copy, please wait...\n" + END
        if subprocess.Popen("mv -f /pentest/web/beef{,_old} && cd /pentest/web/ && git clone git://github.com/beefproject/beef.git && cd /pentest/web/beef/ && ./update-beef",shell=True).wait() == 0:
            print "\n"
            print GREEN + "[>] BeEF updated successfully!" + END
        else:
            print "\n"
            print RED + "[>] Failed to update BeEF\n" + END
            sleep(2)
        
def wifite():
    print GREEN + "[>] Updating WiFite, please wait...\n" + END

    if subprocess.Popen("cd /pentest/wireless/wifite/ && python wifite.py -upgrade",shell=True).wait() == 0:
        print "\n"
        print GREEN + "[>] WiFite updated successfully!" + END
    else:
        print "\n"
        print RED + "[>] Failed to update WiFite\n" + END
        sleep(2)
        
def system():
    backtrack_update()

def tools():
    exploit_db()
    s_e_t ()
    warvox()
    giskismet()
    dedected()
    msf()
    w3af()
    nikto()
    fasttrack()
    pyrit()
    nmap()
    fimap()
    wpscan()
    joomscan()
    sqlmap()
    hexorbase()
    sqlninja()
    openvas()
    aircrack()
    webhandler()
    beef()
    wifite()
    
def all(): 
    system()
    tools()
   
def tryharder():
    print "\n"
    print RED + "[>] Wrong choice, possible choices are: system, tools, all\n" + END

def complete():
    print GREEN + "[>] Cleaning up, please wait...\n" + END
    subprocess.Popen("rm fimap.log",shell=True).wait()
    subprocess.Popen("apt-get -y autoremove && apt-get clean",shell=True).wait()
    print GREEN + "[>] Cleaned successfully!" + END
    print "\n"
    print GREEN + "[>] Backtrack update completed successfully!\n" + END
    sys.exit()

# Main
if __name__ == "__main__": 
	parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description='''[>] Update script for Backtrack 5 R2/R3\n[>] Author: sickness \n[>] Version: 2.0''')
	parser.add_argument('--update', help="Select what to update: system, tools, all")

	args = parser.parse_args()
	if len(sys.argv) > 4: 
		parser.print_help()
		sys.exit()
	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit()

	internet_check()

	if args.update == "system":
		system()
		complete()
	elif args.update == "tools":
		tools()
		complete()
	elif args.update == "all":
		all()
		complete()
	else:
		tryharder()
