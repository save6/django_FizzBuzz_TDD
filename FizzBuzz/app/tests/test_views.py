from django.test import TestCase
from app.views import FizzBuzzView

class UnitTestConvert(TestCase): 

    def setUp(self):
        self.instance = FizzBuzzView()

    def test_3の倍数のときは数の代わりにFizzと変換する__3をFizzと変換する(self):
        self.assertEqual("Fizz", self.instance.convert(3))

    def test_5の倍数のときは数の代わりにBuzzと変換する__5をBuzzと変換する(self):
        self.assertEqual("Buzz", self.instance.convert(5))

    def test_3と5両方の倍数のときは数の代わりにFizzBuzzと変換する__15をFizzBuzzと変換する(self):
        self.assertEqual("FizzBuzz", self.instance.convert(15))
    
    def test_その他の数のときはそのまま文字列に変換する__1を文字列の1に変換する(self):
        self.assertEqual("1", self.instance.convert(1))

class UnitTestGetPost(TestCase):
    
    def test_FizzBuss_htmlというテンプレートを返しているか確認する(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'app/FizzBuzz.html')

    def test_POSTで送信した値が変換されて表示される__3や5の倍数の数字は変換される_3と5と15でテスト(self):
        response = self.client.post('/', data={'num_list': '3 5 15'})
        self.assertIn('Fizz Buzz FizzBuzz', response.content.decode())

    def test_POSTで送信した値が変換されて表示される__数字以外を送信した際にNotNumに変換される_testと1t3でテスト(self):
        response = self.client.post('/', data={'num_list': 'test 1t3'})
        self.assertIn('NotNum NotNum', response.content.decode())
    
    def test_POSTで送信した値が変換されずに表示される__3や5の倍数でない数字は変換されずに表示される_1でテスト(self):
        response = self.client.post('/', data={'num_list': '1'})
        self.assertIn('1</textarea>', response.content.decode())

    def test_POSTで送信した値が変換されずに表示される__改行コードは変換されずに出力される_改行コード2種を含む文字列でテスト(self):
        response = self.client.post('/', data={'num_list': '1 3 5 15 \n 1 3 5 15 \r\n'})
        self.assertIn('1 Fizz Buzz FizzBuzz \n 1 Fizz Buzz FizzBuzz \r\n', response.content.decode())