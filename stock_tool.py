class StockLookup:
    """A tool that checks how many products are in stock."""

    def __init__(self, stock):
        self.stock = stock

    def find_product(self, text):
        """Return the first known product mentioned in the message."""
        for product in self.stock:
            if product.lower() in text.lower():
                return product
        return None

    def count_for(self, product):
        """Return the stock count for a product, or None."""
        if product in self.stock:
            return self.stock[product]
        return None
