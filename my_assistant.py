class RestaurantAssistant:
    """A simple restaurant assistant that uses menu rules."""

    def __init__(self, name, menu_tool):
        self.name = name
        self.menu_tool = menu_tool
        self.history = []

    def respond(self, user_message):
        self.history.append({"role": "user", "content": user_message})

        reply = self.choose_reply(user_message)

        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        text = user_message.lower()

        if "allergy" in text or "allergic" in text or "order" in text:
            return "Please speak with an employee for allergies or placing orders."

        if "hello" in text:
            return f"Hello! I'm {self.name}. I can help with menu prices."

        if "price" in text or "how much" in text or "cost" in text:
            item = self.menu_tool.find_item(text)

            if item is None:
                return "Which menu item would you like to know about?"

            price = self.menu_tool.find_price(item)
            return f"The price of {item} is ${price}."

        return "I'm not sure how to help with that. I can answer menu price questions."
