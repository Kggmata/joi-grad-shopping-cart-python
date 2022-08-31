class Customer:
    """
    customer class: used to create a customer instance
    """
    def __init__(self, name):
        
        self.name = name

    def __str__(self):
        return self.name