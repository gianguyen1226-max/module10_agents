from my_assistant import RestaurantAssistant
from my_tool import MenuLookup

MENU = {
    "pho": 14,
    "banh mi": 9,
    "spring rolls": 7,
}

menu_tool = MenuLookup(MENU)
bot = RestaurantAssistant("VietBot", menu_tool)

print("Type a message, or type quit to stop.")
user_message = input("You: ")

while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
