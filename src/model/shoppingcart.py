from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    """
    shopping cart
    """

    def __init__(self, customer=Customer, products=[]):
        """
        initialize shopping cart instance
        :param customer: customer instance
        :param products: product instance
        """
        self.products = products
        self.customer = customer

    def add_product(self, product):
        """
        add product to the shopping cart
        :param product: product instance to add
        :return:
        """
        self.products.append(product)

    def checkout(self):
        """
        calculate loyalty points earned and total price of the shopping cart
        :return: an order instance with loyalty points earned and total price
        """
        total_price = 0.00
        loyalty_points_earned = 0.00
        for product in self.products:
            discount = 0.00
            if product.product_code.startswith("DIS_10"):
                loyalty_points_earned += (product.price / 10)
                discount = product.price * 0.1
            elif product.product_code.startswith("DIS_15"):
                loyalty_points_earned += (product.price / 15)
                discount = product.price * 0.15
            else:
                loyalty_points_earned += (product.price / 5)
                discount = 0.00
            total_price += product.price - discount
        return Order(int(loyalty_points_earned), total_price)

    def __str__(self):
        """
        string representation of the shopping cart
        :return:
        """
        product_list = "".join('%s' % product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
