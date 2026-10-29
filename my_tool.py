class MenuLookup:
    """A tool that knows the restaurant menu and prices."""

    def __init__(self, menu):
        """Store the menu items and their prices."""
        self.menu = menu

    def find_item(self, text):
        """Find a menu item mentioned in the message."""
        for item in self.menu:
            if item in text.lower():
                return item
        return None

    def find_price(self, item):
        """Return the price of an item, or None if unknown."""
        if item in self.menu:
            return self.menu[item]
        return None
