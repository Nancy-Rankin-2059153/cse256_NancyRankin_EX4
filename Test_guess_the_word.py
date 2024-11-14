import pytest

import guess_the_word
from guess_the_word import word_to_guess, word_dic


class MyTestCase(unittest.TestCase):
    def test_wor_in_list():
        assert word_to_guess in word_dic
        


if __name__ == '__main__':
    unittest.main()
