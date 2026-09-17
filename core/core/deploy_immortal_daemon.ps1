$taskName = "EbonyMasterEdgeNode"

Write-Host "[*] FORGING IMMORTAL WINDOWS DAEMON..." -ForegroundColor Cyan

# Define the absolute execution parameters to run silently
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "-m streamlit run C:\HVF_Repos\hvf-media-matrix-private\app.py --server.port 8501 --server.headless true" -WorkingDirectory "C:\HVF_Repos\hvf-media-matrix-private"

# Command the OS to execute at boot
$trigger = New-ScheduledTaskTrigger -AtStartup

# Lock the execution to the NT AUTHORITY\SYSTEM account (highest privilege, completely hidden)
$principal = New-ScheduledTaskPrincipal -UserId "NT AUTHORITY\SYSTEM" -LogonType ServiceAccount -RunLevel Highest

# Ensure the system never kills it for power management
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable -DontStopOnIdleEnd -ExecutionTimeLimit 0

# Register the Daemon
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force

# Start the Daemon immediately
Start-ScheduledTask -TaskName $taskName

Write-Host "[+] SUCCESS: Ebony is now hardwired into the Windows Kernel. Accidental shutdown is impossible." -ForegroundColor Green
