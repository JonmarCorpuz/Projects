# Fetch system information
echo System information: > C:\Windows\Temp\Oops.txt
systeminfo >> C:\Windows\Temp\Oops.txt

# Fetch current local user and their privileges
echo Current user information: >> C:\Windows\Temp\Oops.txt
echo '' >> C:\Windows\Temp\Oops.txt
whoami >> C:\Windows\Temp\Oops.txt
whoami /priv >> C:\Windows\Temp\Oops.txt

# Fetch a list of users on the machine
echo List of users present on the machine: >> C:\Windows\Temp\Oops.txt
wmic useraccount list >> C:\Windows\Temp\Oops.txt

# Test code (Remove later)
# Notepad.exe C:\Windows\Temp\Oops.txt

 
