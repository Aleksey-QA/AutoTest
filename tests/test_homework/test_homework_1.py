from format_price import format_price
import pytest

@pytest.mark.parametrize("price, res", [('1234', '1 234.00'),
                                        ('1111234567.8', '1 111 234 567.80'),
                                        ('99.991654654321531', '99.99'),
                                        ('99.995', '100.00'),
                                        ('99.999', '100.00'),
                                        ('0.999', '1.00'),
                                        ('0.0019', '0.00'),
                                        ('1 111 234 567.80', '1 111 234 567.80'),
                                        ('0.999', '1.00'),
                                        ('0', '0.00'),
                                        ('-0.999', '-1.00'),
                                        ('@99!', '@99!'),
                                        ('abc', 'abc'),
                                        ('None', 'None')])
def test_format_price(price, res):
    assert format_price(price) == res