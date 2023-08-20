# Fetch system information
echo System information: > C:\Windows\Temp\Oops.txt
echo 'systeminfo' | PowerShell.exe >> C:\Windows\Temp\Oops.txt

# Fetch current local user and their privileges
echo Current user information: >> C:\Windows\Temp\Oops.txt
echo '' >> C:\Windows\Temp\Oops.txt
echo 'whoami' | PowerShell.exe >> C:\Windows\Temp\Oops.txt
echo 'whoami /priv' | PowerShell.exe >> C:\Windows\Temp\Oops.txt

# Fetch a list of users on the machine
echo List of users present on the machine: >> C:\Windows\Temp\Oops.txt
echo 'wmic useraccount list' | PowerShell.exe >> C:\Windows\Temp\Oops.txt

# Test code (Remove later)
# Notepad.exe C:\Windows\Temp\Oops.txt

 
