class Order:
    """
    order class: used to create an order instance
    """
    def __init__(self, loyalty_points_earned=0, total_price=0):
        """
        order instance initialize
        :param loyalty_points_earned: loyalty points
        :param total_price: total price
        """
        self.loyalty_points = loyalty_points_earned
        self.total = total_price

    def __str__(self):
        """
        string representation of order
        :return:
        """
        return "Total price: %s \nWill receive %s" % (self.total, self.loyalty_points)
