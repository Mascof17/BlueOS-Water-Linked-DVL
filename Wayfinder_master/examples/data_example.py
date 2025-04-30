"""Example usage for DVL driver
"""
from dvl.dvl import Dvl
from dvl.system import OutputData

def update_data(output_data: OutputData, obj):
    """Prints data time to screen
    """
    del obj
    if output_data is not None:
        time = output_data.get_date_time()
        txt = time.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        print("Got data {0}".format(txt))


if __name__ == "__main__":
    # PORT = input("Please enter your port number (e.g. '1' for COM1) =  ")
    # PORT = "COM" + PORT
    PORT = "/dev/ttyS0"  # Example for Linux(raspberry), see on this website: https://bluerobotics.com/learn/navigator-hardware-setup/ at paragraph "serial devices"

    # Connect to serial port
    with Dvl(PORT, 115200) as DVL:

        if DVL.is_connected():

            # Get user system setup
            if DVL.get_setup():
                # Print setup 
                print (DVL.system_setup)

            # Collect data - make sure working folder exists
            # if not DVL.start_logging("c:/temp", "DVL"):
            #     print("Failed to start logging")
            # else:
            #     print("Data logged to {0}".format(DVL.get_log_file_name()))
            
            # Start pinging
            if not DVL.exit_command_mode():
                print("Failed to start pinging")

            # Register callback function
            DVL.register_ondata_callback(update_data)

            
           

            # Blocking call to wait for key pressed to end program
            KEY = input("Press Enter to stop\n")

        else:
            print("Failed to open {0} - make sure it is not used by any other program".format(PORT))

        # Unregister
        DVL.unregister_all_callbacks()
