class KC868_Hx:
    """
    Class to interact with controllers from KC868-H family over IP
    For example KC868-H8W, KC868-H16, KC868-H32L serving TCP or UDP
    """

    def __init__(self, controller_ip):
        # TODO 1: Check for controller existence under this IP
        # TODO 2: Check if this controller is supported by this class
        self._controller_ip = controller_ip

    def set_relay_state(self, relay_number, state):
        """ Sets relay to a given state """
        # TODO: Set relay state
        raise NotImplementedError