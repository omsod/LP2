print(" Welcome to the Help Desk Expert System!")
print("What issue are you facing?")
print("1. Internet Issue")
print("2. Computer Not Turn On")
print("3. Slow Performance")
print("4. Software Installation Problem")

choice = input("Enter your choice (1-4): ")

if choice == '1':
    wifi = input("Is Wi-Fi turned on? (yes/no): ")
    if wifi == 'yes':
        others = input("Are other devices connected? (yes/no): ")
        if others == 'yes':
            print(" Restart your computer.")
        else:
            print(" Restart your router or contact your provider.")
    else:
        print(" Turn on Wi-Fi and reconnect.")

elif choice == '2':
    power = input("Is the power cable connected? (yes/no): ")
    if power == 'yes':
        noise = input("Do you hear fan or see lights? (yes/no): ")
        if noise == 'yes':
            print(" Try using an external monitor.")
        else:
            print(" Hold power button 10 sec. May be a hardware issue.")
    else:
        print(" Connect the power cable and try again.")

elif choice == '3':
    apps = input("Are many apps running? (yes/no): ")
    if apps == 'yes':
        print(" Close unused apps or restart your PC.")
    else:
        storage = input("Is storage almost full? (yes/no): ")
        if storage == 'yes':
            print(" Free up disk space.")
        else:
            print(" Run virus scan or update your OS.")

elif choice == '4':
    permission = input("Getting permission error? (yes/no): ")
    if permission == 'yes':
        print(" Run installer as Administrator.")
    else:
        trusted = input("Is the installer from a trusted source? (yes/no): ")
        if trusted == 'yes':
            print(" Disable antivirus temporarily if blocking.")
        else:
            print(" Download software from a trusted site.")

else:
    print(" Invalid choice. Please restart the program.")
