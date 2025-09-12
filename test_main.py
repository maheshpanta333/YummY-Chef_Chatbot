import pytest

#we test the response from the bot in this test from the instance itself
def test_get_bot_response():
    from main import MyGrid
    grid=MyGrid()
    result=grid.get_bot_response("Hello")
    assert isinstance(result,str)
    assert len(result)>0


#next we check if the text bubble is created or not in the text
def test_add_message_to_chat():
    from main import MyGrid
    grid=MyGrid()
    initially=len(grid.chat_box.children)
    grid.add_message_to_chat("Test message", "left",(1,1,1,1))
    assert(len(grid.chat_box.children)==initially+1)
#we test all for both and everything for the bulbble
def test_pressed_adds_bubbles():
    from main import MyGrid
    grid=MyGrid()
    grid.prompt.text="hello"
    initially=len(grid.chat_box.children)
    grid.pressed(None)
    assert len(grid.chat_box.children)==initially+2

