#!/bin/bash
 
## Ensure that the user has entered one positional argument.

if [ $# -ne 1 ]; then
	echo "[ERROR] Usage: ./Scanning.sh <TARGET IP>"
	exit
fi

## Ensure that the target host is reachable
if ping $1 -c 3 &>/dev/null; then
	echo " "
else
	echo " " 
	echo "[ERROR] The target host is unreachable."
	exit
fi

Banner="
      ___                        ___                         ___       ___     
     /  /\           ___        /  /\          ___          /  /\     /  /\    
    /  /::\         /__/\      /  /::|        /  /\        /  /:/    /  /::\   
   /__/:/\:\        \__\:\    /  /:|:|       /  /::\      /  /:/    /  /:/\:\  
  _\_ \:\ \:\       /  /::\  /  /:/|:|__    /  /:/\:\    /  /:/    /  /::\ \:\ 
 /__/\ \:\ \:\   __/  /:/\/ /__/:/_|::::\  /  /::\ \:\  /__/:/    /__/:/\:\ \: 
 \  \:\ \:\_\/  /__/\/:/~~  \__\/  /~~/:/ /__/:/\:\_\:\ \  \:\    \  \:\ \:\_\/
  \  \:\_\:\    \  \::/           /  /:/  \__\/  \:\/:/  \  \:\    \  \:\ \:\  
   \  \:\/:/     \  \:\          /  /:/        \  \::/    \  \:\    \  \:\_\/  
    \  \::/       \__\/         /__/:/          \__\/      \  \:\    \  \:\    
     \__\/                      \__\/                       \__\/     \__\/    
      ___           ___           ___           ___           ___              
     /  /\         /  /\         /  /\         /  /\         /  /\             
    /  /::\       /  /::\       /  /::\       /  /::\       /  /::|            
   /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:/\:\     /  /:|:|            
  /  /::\ \:\   /  /::\ \:\   /  /:/  \:\   /  /:/  \:\   /  /:/|:|__          
 /__/:/\:\_\:\ /__/:/\:\ \:\ /__/:/ \  \:\ /__/:/ \__\:\ /__/:/ |:| /\         
 \__\/~|::\/:/ \  \:\ \:\_\/ \  \:\  \__\/ \  \:\ /  /:/ \__\/  |:|/:/         
    |  |:|::/   \  \:\ \:\    \  \:\        \  \:\  /:/      |  |:/:/          
    |  |:|\/     \  \:\_\/     \  \:\        \  \:\/:/       |__|::/           
    |__|:|~       \  \:\        \  \:\        \  \::/        /__/:/            
     \__\|         \__\/         \__\/         \__\/         \__\/             


by Jonmar Corpuz

"
echo "$Banner"
echo " "
echo "[*] Starting the program."
echo " "

## Ensure that the required tools are installed on the system that we are running this script on.

if (type nmap &>/dev/null); then
	echo "[*] Network Mapper (nmap) is already installed."
else	
	echo "[*] Installing Network Mapper (nmap)."
	sudo apt install nmap
fi

if (type gobuster &>/dev/null); then
	echo "[*] GoBuster is akready installed."
else
	echo "[*] Installing GoBuster."
	sudo apt install gobuster
fi

echo " "
echo "[*] The required tools are all installed and ready to be used."

## Download wordlists.
echo " "
if (type wordlists &>/dev/null); then
	echo "[*] Wordlists are already installed."
else	
	echo "[*] Installing wordlists"
	sudo apt install wordlists
	
	
	echo " "
	echo "[*] Unizpping the rockyou.txt.tar.gz archive."
	echo "Y" | wordlists
	cd ~
	
	echo " "
	echo "[*] The required wordlists are all installed and ready to be used."
fi

## Use nmap to scan for open ports.
echo " "
echo "[*] Starting Network Mapper (nmap)"
echo "[*] Beginning port scan on ports 1 to 1000"
echo "[*] Running 'nmap -sC -sV -A $1'"
echo " " > Scanning_Results.txt
echo "############## PORT SCAN ##############" >> Scanning_Results.txt
echo " " >> Scanning_Results.txt
nmap -sC -sV -A $1 >> Scanning_Results.txt
echo " "
echo "[*] Port scan complete."


## Use GoBuster to scan for hidden directories and files
#echo " "
#echo "[*] Starting Gobuster"
#echo "[*] Running 'gobuster dir --url http://$1 --wordlist /usr/share/wordlists/rockyou.txt --threads 50 --quiet'"
#echo "  " >> Scanning_Results.txt
#echo "  " >> Scanning_Results.txt
#echo " ----------------------" >> Scanning_Results.txt
#echo "GoBuster scan:" >> Scanning_Results.txt
#echo " ----------------------" >> Scanning_Results.txt
#gobuster dir --url http://$1 --wordlist /usr/share/wordlists/rockyou.txt --threads 50 --quiet >> Scanning_Results.txt 
#echo " "
#echo "[*] GoBuster scan complete."

## Use DIrb to scan for hidden directories
echo " "
echo "[*] Starting Dirb"
echo "[*] Beginning web directory enumeration"
echo " " >> Scanning_Results.txt
echo " " >> Scanning_Results.txt
echo "############## HIDDEN WEB FILE AND DIRECTORY SCAN ##############" >> Scanning_Results.txt
dirb http://$1 /usr/share/dirb/wordlists/small.txt -r -S >> Scanning_Results.txt

echo " "
echo "[*] Beginning file enumeration"

### Create file extensions wordlist containing the type of files that we're looking for.
echo ".txt" > ExtensionsWordlist.txt
echo ".php" >> ExtensionsWordlist.txt
echo ".html" >> ExtensionsWordlist.txt
echo ".xml" >> ExtensionsWordlist.txt
echo ".css" >> ExtensionsWordlist.txt
echo ".js" >> ExtensionsWordlist.txt
echo ".bak" >> ExtensionsWordlist.txt

dirb http://$1 /usr/share/dirb/wordlists/small.txt -R -S -x ExtensionsWordlist.txt >> Scannin_Results.txt

rm ExtensionsWordlist.txt

echo " "
echo "[*] Web directory and file scan complete."

echo " "
echo "[*] The scan results were saved in Scanning_Results.txt"
echo "[*] Now exiting the program."

exit
