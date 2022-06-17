The parking project is an automated Python script that allows the user to add & remove a vehicle from the University of Maryland parking portal. It has functionality to bypass Duo push 2FA and register/deregister a vehicle from the parking portal. In order to do so, you must generate preauthorized bypass codes from your password portal and paste them into "bypasscodes.txt" with no extra lines.

In each of the Python scripts, enter your login information as well as vehicle credentials. You can then set your machine (local or cloud) to run the script at predetermined times, therefore automatically adding and removing your vehicle from the UMD parking portal. Run "addvehicle.py" when you want your vehicle added to the portal, and "removevehicle.py" to erase it from the portal. 

Utilizes chromewebdriver.exe (Selenium browser access, Windows version) which is specified in a PATH vairable at the top of both scripts. Update the PATH for your system specifically.

This prototype is designed to circumvent the expensive UMD parking passes. Using this script allows users to pay for a significantly cheaper commuter pass (versus an overnight pass) and park their vehicle on campus full time.

Disclaimer: This is merely code I wrote as a personal project. I currently do not nor have in the past used this script to circumvent UMD parking rules.  Anyone who utilizes this script does so of their own volition and assumes any consequences. This script was solely designed as a way to practice automation via Python. 