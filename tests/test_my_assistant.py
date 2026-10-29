from my_assistant import RestaurantAssistant
from my_tool import MenuLookup


def make_bot():
    menu = {"pho": 14, "banh mi": 9, "spring rolls": 7}
    menu_tool = MenuLookup(menu)
    return RestaurantAssistant("VietBot", menu_tool)


def test_menu_price():
    bot = make_bot()
    assert bot.respond("How much is pho?") == "The price of pho is $14."


def test_unknown_menu_item():
    bot = make_bot()
    assert "Which menu item" in bot.respond("How much is pizza?")


def test_allergy_goes_to_employee():
    bot = make_bot()
    assert "employee" in bot.respond("I have a peanut allergy")


def test_unknown_question():
    bot = make_bot()
    assert "not sure" in bot.respond("What time do you close?")


def test_conversation_history():
    bot = make_bot()
    bot.respond("hello")
    assert len(bot.history) == 2
    assert bot.history[0]["role"] == "user"
    assert bot.history[1]["role"] == "assistant"


def test_tool_returns_none_for_unknown_item():
    tool = MenuLookup({"pho": 14})
    assert tool.find_price("pizza") is None
