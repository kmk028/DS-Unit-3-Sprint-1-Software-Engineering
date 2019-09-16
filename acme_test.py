import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        prod = Product('Test Product', price=25, weight=5)
        self.assertEqual(prod.stealability(), 'Very stealable!')

    def test_explode(self):
        prod = Product('Test Product', flammability=0.2, weight=4)
        self.assertEqual(prod.explode(), '...fizzle.')


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        products = generate_products()
        for product in products:
            adj = product.name[0]
            noun = product.name[1]
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
