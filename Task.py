#1. All Installed Softwares list
import wmi
def get_installed_software():
    c = wmi.WMI()                      #Create a WMI object
    software_list = []                 #List to store Installed software names

    for program in c.Win32_Product():  #Iterate through the Win32_Product class to get installed software
        software_list.append(program.Name)

    return software_list

if __name__ == "__main__":
    installed_software = get_installed_software() #Get the list of Installed Software
    print()
    print("1.) Installed Software List: Output ========================")
    for software in installed_software:           #Print each Installed Software
        print(software)

#2. Internet Speed
import speedtest
def get_internet_speed():
    st = speedtest.Speedtest()                     #Create a Speedtest Object

    download_speed = st.download() / 1024 / 1024  # Convert to megabits per second
    upload_speed = st.upload() / 1024 / 1024  # Convert to megabits per second

    print(f"Download Speed: {download_speed:.2f} Mbps") #Print the Internet speed results
    print(f"Upload Speed: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    print()
    print("2.) Internet Speed: Output ========================")
    get_internet_speed()        # Call the function to get and print internet speed


#3. Screen Resolvution
import tkinter as tk
def get_screen_resolution():     #Create a hidden Tkinter window
    root = tk.Tk()
    #Get the screen width and height
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    root.destroy()                #Destroy the Tkinter window
    return width, height

if __name__ == "__main__":
    print()
    print("3.) Screen Resolution: Output ==============================")
    screen_width, screen_height = get_screen_resolution()   #Call the function to get and print screen resolution
    print(f"Screen Resolution: {screen_width}x{screen_height}")

#4. CPU Model
import platform
def get_cpu_model():
    return platform.processor()     # Get the CPU model using platform.processor()

if __name__ == "__main__":
    print()
    print("4.) CPU MODEL: Output ==============================")
    cpu_model = get_cpu_model()      # Call the function to get and print CPU model
    print(f"CPU Model: {cpu_model}")

#5. No of core and threads of CPU
import psutil
def get_cpu_cores_threads():
    # Get the number of CPU cores and threads
    num_cores = psutil.cpu_count(logical=False)
    num_threads = psutil.cpu_count(logical=True)
    return f"CPU Cores: {num_cores}, Threads: {num_threads}"   # Return the formatted string

if __name__ == "__main__":
    print()
    print("5.) Core and Threads : Output ==============================")
    cpu_info = get_cpu_cores_threads()   # Call the function to get and print CPU cores and threads
    print(cpu_info)

#6. GPU model ( If exist )
import GPUtil
def get_gpu_model():
    try:
        # Get the list of available GPUs
        gpus = GPUtil.getGPUs()

        # Check if any GPU is available
        if gpus:
            return f"GPU Model: {gpus[0].name}"
        else:
            return "No GPU detected."
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print()
    print("6.) GPU Model : Output ==============================")
    gpu_info = get_gpu_model()
    print(gpu_info)


#7. RAM Size ( In GB )
#import psutil

def get_ram_size():
    ram_info = psutil.virtual_memory()         #Get Information about virtual memmory
    total_ram_gb = ram_info.total / (1024 ** 3)  # Convert bytes to gigabytes
    return f"Total RAM Size: {total_ram_gb:.2f} GB" #return the formatted string

if __name__ == "__main__":
    print()
    print("7.) RAM SIZE : Output ==============================")
    ram_info = get_ram_size()
    print(ram_info)

#8. Screen size
import ctypes

def get_screen_size():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)  # Screen width in pixels
    height = user32.GetSystemMetrics(1)  # Screen height in pixels

    # Constants for DPI (dots per inch)
    dpi = 96.0  # Default DPI for most systems

    # Calculate screen size in inches
    width_inches = width / dpi
    height_inches = height / dpi

    return f"Screen Size: {width_inches:.2f} inches x {height_inches:.2f} inches"


if __name__ == "__main__":
    print()
    print("8.) Screen Size : Output ==============================")
    screen_info = get_screen_size()
    print(screen_info)

#9. Wifi/Ethernet mac address
#import psutil
import uuid

def get_mac_address(interface='eth0'):
    try:
        # Get the MAC address for the specified interface
        mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2 * 6,2)][::-1])
        return f"MAC Address ({interface}): {mac}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print()
    print("9.) Wifi/Ethernet mac address : Output ==============================")
    # Specify the interface you want to get the MAC address for ('eth0' for Ethernet, 'wlan0' for WiFi, etc.)
    interface_name = 'eth0'

    mac_address = get_mac_address(interface_name)
    print(mac_address)


#10. Public IP address
import requests

def get_public_ip():
    try:
        #Make an Http Get request to the ipify API
        response = requests.get('https://api.ipify.org?format=json')

        # Extract the public IP address from the JSON response
        ip_data = response.json()
        public_ip = ip_data['ip']

        #Return the formatted string
        return f"Public IP Address: {public_ip}"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print()
    print("10.) Public IP address : Output ==============================")
    public_ip = get_public_ip()
    print(public_ip)

#11. Windows version
#import platform
def get_windows_version():
    #Windosws version information
    return f"Windows Version: {platform.system()} {platform.version()}"

if __name__ == "__main__":
    print()
    print("11.) Windows version : Output ==============================")
    windows_version = get_windows_version()
    print(windows_version)