import os
import function
# Defining main function

# define your S7 ip address here
ipS7 = "10.155.155.100"

def main():
    print("hey there")
    plc = function.S7300(ipS7)
    print("plc is connected", plc.__isconnected__())
    # check value from M130.0
    print("M130.0 = ", plc.mbit(130, 0))
    # set value from M130.0 to 1
    plc.set_mbit(130, 0)
    print("M130.0 = ", plc.mbit(130, 0))
    # clear value from M130.0 to 0
    plc.clear_mbit(130, 0)
    print("M130.0 = ", plc.mbit(130, 0))

    plc.disconnect()
    print("plc is connected", plc.__isconnected__())


if __name__ == "__main__":
    main()
