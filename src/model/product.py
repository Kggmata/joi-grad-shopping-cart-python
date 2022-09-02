class Product:
    """
    Product class.
        examples: Product(10.0, "DIS_10_PRODUCT1", "product 1")
    """

    def __init__(self, price: int, product_code: str, name: str):
        """
        Product instance
        :param price: product price: int
        :param product_code: product code: str
        :param name: product name: str
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
