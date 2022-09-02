class Customer:
    """
    customer class: used to create a customer instance
        examples: Customer("A customer")
    """

    def __init__(self, name: str):
        """
        customer instance initialize
        :param name: customer name: str
            examples: "A Customer"
        """
        self.name = name

    def __str__(self):
        """
        string representation of customer
        :return: customer name
        """
        return self.name
