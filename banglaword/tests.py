import unittest
from banglaword import BanglaWord


class BanglaWordTest(unittest.TestCase):
	def setUp(self) -> None:
		self.bangla_word = BanglaWord()

	def test_bangla_number(self):
		self.assertEqual("১৫০০", self.bangla_word.bangla_number("1500"))
		self.assertEqual("৫০০", self.bangla_word.bangla_number("500"))
		self.assertEqual("১০০", self.bangla_word.bangla_number("100"))
		self.assertNotEqual("১৫০০", self.bangla_word.bangla_number("1400"))


if __name__ == '__main__':
	unittest.main()
