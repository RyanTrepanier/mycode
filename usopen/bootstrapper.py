from netmiko import ConnectHandler

## Define our new function called bootstrapper and the expected arguments
def bootstraper(dev_type, dev_ip, dev_un, dev_pw, config):
    try:
        config_file = open(config, 'r')                                                                           # open the fileobject described by config argument

        config_lines = config_file.read().splitlines()                                                            # create a list of the file lines w/o \n

        config_file.close()                                                                                       # close the file object


        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pwi)      # open a connection to the switch

        open_connection.enable()                                                                                  # this sets the connection in enable mode

        output = open_connection.send_config_set(config_lines)                                                    # pass the config to the send_config_set() method

        print(output)                                                                                             # print the config to the screen

        open_conection.send_command_expect('write memory')                                                        # write the memory

        open_connection.disconnect()                                                                              # close the open connection


        return True                                                                                               # everything worked!

    except:
        return False                                                                                              # something failed during configuration process
