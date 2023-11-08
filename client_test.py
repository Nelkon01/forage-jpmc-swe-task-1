import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

        for quote in quotes:
            self.assertEqual(getDataPoint(quote),
                             (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    def test_getDataPoint_missingData(self):
        quotes = [
            {'top_ask': {'price': 120.0, 'size': 20}, 'stock': 'ABC'},  # Missing top_bid
            {'top_bid': {'price': 52.0, 'size': 25}, 'stock': 'DEF'},  # Missing top_ask
        ]
        for quote in quotes:
            getDataPoint(quote)
            self.assertIsNone(quote)  # Expecting None for incomplete data

    def test_getRatio_divisionByZero(self):
        self.assertIsNone(getRatio(10, 0))  # Price_b is 0, expecting None
        self.assertIsNone(getRatio(0, 0))  # Both prices are 0, expecting None


if __name__ == '__main__':
    unittest.main()
