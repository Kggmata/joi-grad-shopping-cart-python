class Customer:
    """
    customer class: used to create a customer instance
    """
    def __init__(self, name):
        """
        customer instance initialize
        :param name: customer name
        """
        self.name = name

    def __str__(self):
        """
        string representation of customer
        :return: customer name
        """
        return self.name