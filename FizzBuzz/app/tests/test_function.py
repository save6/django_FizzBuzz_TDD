from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time

from app.views import FizzBuzzView

class FizzBuzzFuctionalTest(LiveServerTestCase):

    @classmethod
    def setUpClass(self):
        super().setUpClass()
        self.browser = webdriver.Chrome()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()
        super().tearDownClass()
    
    def setUp(self):
        self.browser.get('http://localhost:8000')
    
    def textarea_clear_after_input_string(self, input_text):
        textarea = self.browser.find_element_by_id("num_list")
        textarea.send_keys(Keys.CONTROL + "a")
        textarea.send_keys(Keys.DELETE)
        textarea.send_keys(input_text)
    
    def startbtn_click_wait(self):
        start_btn = self.browser.find_element_by_id("start_btn")
        start_btn.click()
        time.sleep(1)
    
    def test_ユーザがサイトへアクセスするとタイトルがFizzBuzz問題になっている(self):
        self.assertEqual("FizzBuss問題", self.browser.title)

    def test_ユーザがサイトへアクセスすると1から100まで表示されている__100が表示されていることを確認する(self):
        textarea = self.browser.find_element_by_id("num_list")
        self.assertIn("100", textarea.text)

    def test_ユーザはstartボタンを押してFizzBuzz問題の結果を確認することができる__最初の1行の結果が正しいか確認する(self):
        self.startbtn_click_wait()
        textarea = self.browser.find_element_by_id("num_list")
        self.assertIn("1 2 Fizz 4 Buzz Fizz 7 8 Fizz \n", textarea.text)

    def test_ユーザは既存の文字列を削除して任意の文字列を入力しstartボタンを押してFizzBuzz問題の結果を確認できる__1と3と5と15を送信して確認する(self):
        self.textarea_clear_after_input_string("1 3 5 15")
        self.startbtn_click_wait()
        textarea = self.browser.find_element_by_id("num_list")
        self.assertIn("1 Fizz Buzz FizzBuzz", textarea.text)

    def test_ユーザは既存の文字列を削除して任意の文字列を入力しstartボタンを押してFizzBuzz問題の結果を確認できる__数字以外を送信して確認する(self):
        self.textarea_clear_after_input_string("test string")
        self.startbtn_click_wait()
        textarea = self.browser.find_element_by_id("num_list")
        self.assertIn("NotNum NotNum", textarea.text)

    def test_ユーザは既存の文字列を削除して任意の文字列を入力しstartボタンを押してFizzBuzz問題の結果を確認できる__改行を含んだ文字列を送信して確認する(self):
        self.textarea_clear_after_input_string("1 \n 1")
        self.startbtn_click_wait()
        textarea = self.browser.find_element_by_id("num_list")
        self.assertIn("1 \n 1", textarea.text)
