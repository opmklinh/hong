import unittest
import stocks.stocks as stocks


class TestStocks(unittest.TestCase):
    def test_url_set_kospi(self):
        formatted_url = stocks.url_set_naver('삼성전자')
        self.assertEqual(formatted_url,'http://finance.naver.com/item/sise.nhn?code=005930')

    def test_url_set_kosdaq(self):
        formatted_url = stocks.url_set_naver('야스')
        self.assertEqual(formatted_url,'http://finance.naver.com/item/sise.nhn?code=255440')
    
    def test_extracting_stock_naver(self):
        extracted_html = stocks.extracting_stock_naver('삼성전자')
        self.assertIsNotNone(extracted_html)
    
    def test_coinoneAPI(self):
        extracted_coinone = stocks.coinoneAPI('BTC')
        self.assertIsNotNone(extracted_coinone)
    
    def test_poloniexAPI(self):
        extracted_poloniex = stocks.poloniexAPI()
        self.assertIsNotNone(extracted_poloniex)

if __name__ == '__main__':
    unittest.main()