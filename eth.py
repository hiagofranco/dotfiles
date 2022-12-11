
from libqtile.log_utils import logger
from libqtile.widget import base

def get_status(interface_name):

    try:
        with open("/sys/class/net/" + interface_name + "/carrier") as fcarrier:
            cable_status = fcarrier.readline().rstrip("\n")
        with open("/sys/class/net/" + interface_name + "/operstate") as fstate:
            eth_status = fstate.readline().rstrip("\n")
    except FileNotFoundError:
        return None, None
    
    return cable_status, eth_status

class Eth(base.InLoopPollText):
    """
    Displays Ethernet status.

    """

    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("interface", "eth0", "The interface to monitor"),
        ("update_interval", 1, "The update interval."),
        ("cable_disconnected_msg", "Disconnected", "String to show when the eth cable is disconnected."),
        ("cable_connected_msg", "Connected", "String to show when the eth cable is connected."),
        ("eth_down_msg", "Down", "String to show when the eth connection is down."),
        ("eth_up_msg", "Up", "String to show when the eth connection is down."),
        ("show_eth_msg", True, "Wether show or not the eth down and up messages."),
        (
            "format",
            "{cable_msg} {eth_msg}",
            'Display format."',
        ),
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(Eth.defaults)

    def poll(self):
        try:
            cable_status, eth_status = get_status(self.interface)

            # From kernel docs https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-class-net:

            # Carrier:
            #== =====================
            #0  physical link is down
            #1  physical link is up
            #== =====================

            # Operstate
            # Possible values are:
		    # "unknown", "notpresent", "down", "lowerlayerdown", "testing",
            # "dormant", "up".
            
            # If None or cable disconnected, show disconnected message
            if ((cable_status is None) or
               (eth_status is None) or
               (cable_status == "0")):
                return self.cable_disconnected_msg
            
            if self.show_eth_msg:
                if eth_status == "up":
                    self.eth_msg = self.eth_up_msg
                elif eth_status == "down":
                    self.eth_msg = self.eth_down_msg
                else:
                    self.eth_msg = eth_status
            else:
                self.eth_msg = None

            return self.format.format(cable_msg=self.cable_connected_msg, eth_msg=self.eth_msg)

        except EnvironmentError:
            logger.error(
                "%s: Probably your eth device is switched off or "
                " otherwise not present in your system.",
                self.__class__.__name__,
            )
