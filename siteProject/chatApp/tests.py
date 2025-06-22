from django.test import TestCase

from channels.testing import ChannelsLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

# Create your tests here.
class ChatAppTestCase(ChannelsLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_when_user_sends_message_posted_then_seen_by_everyone_in_same_room(self):
        try:
            # Open the chat application
            self._enter_chat_room("test_room1")

            self._open_new_window()
            self._enter_chat_room("test_room1")

            # User 1 sends a message
            self._switch_to_window(0)
            self._send_message("Hello from User 1")
            WebDriverWait(self.driver, 2).until(
                lambda driver: "Hello from User 1" in self._chat_log_value,
                "User 1's message is not visible in the chat log from window 1.",
            )
            # User 2 sees the message
            self._switch_to_window(1)
            WebDriverWait(self.driver, 2).until(
                lambda driver: "Hello from User 1" in self._chat_log_value,
                "User 1's message is not visible in the chat log from window 2.",
            )
        finally:
            self._close_all_new_windows()

def test_when_user_sends_message_posted_then_not_seen_by_anyone_in_different_room(self):
    try:
        # Open the chat application
        self._enter_chat_room("test_room1")

        self._open_new_window()
        self._enter_chat_room("test_room2")

        # User 1 sends a message
        self._switch_to_window(0)
        self._send_message("Hello from User 1 in room 1")
        WebDriverWait(self.driver, 2).until(
            lambda driver: "Hello from User 1 in room 1" in self._chat_log_value,
            "User 1's message is not visible in the chat log from window 1.",
        )
        # User 2 does not see the message
        self._switch_to_window(1)
        WebDriverWait(self.driver, 2).until(
            lambda driver: "Hello from User 1 in room 1" not in self._chat_log_value,
            "User 2 should not see User 1's message in a different room.",
        )
    finally:
        self._close_all_new_windows()
    
    # Helper methods for the test case
def _enter_chat_room(self, room_name):
    self.driver.get(self.live_server_url + "/chat/")
    ActionChains(self.driver, 2).send_keys(room_name + Keys.RETURN).perform()
    WebDriverWait(self.driver, 2).until(
        lambda self: room_name in self.driver.current_url,
        "Failed to enter the chat room: {}".format(room_name),
    )
def _open_new_window(self):
    self.driver.execute_script("window.open('');")
    self.driver.switch_to.window(self.driver.window_handles[-1])

def _switch_to_window(self, index):
    self.driver.switch_to.window(self.driver.window_handles[index])

def _close_all_new_windows(self):
    for handle in self.driver.window_handles[1:]:
        self.driver.switch_to.window(handle)
        self.driver.close()
    self.driver.switch_to.window(self.driver.window_handles[0])

def _send_message(self, message):
    ActionChains(self.driver).send_keys(message, Keys.RETURN).perform()

@property
def _chat_log_value(self):
    chat_log = self.driver.find_element(By.ID, "chat-log")
    return chat_log.get_attribute("value") if chat_log else ""