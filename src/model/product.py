class Product:
    def __init__(self, price, product_code, name):
        """
        Product instance
        :param price: product price
        :param product_code: product code
        :param name: product name
        """
        self.price = price
        self.product_code = product_code
        self.name = name

    def __str__(self):
        """
        string representation of product
        :return:
        """
        return " Name: %s \n Price: %s \n" % (self.name, self.price)