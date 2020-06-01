import unittest
from banglaword import BanglaWord


class BanglaWordTest(unittest.TestCase):
	def setUp(self) -> None:
		self.bangla_word = BanglaWord()

	def test_bangla_number(self):
		self.assertEqual("১৫০০", self.bangla_word.bangla_number(1500))
		self.assertEqual("৫০০", self.bangla_word.bangla_number(500))
		self.assertEqual("১০০", self.bangla_word.bangla_number(100))
		self.assertNotEqual("১৫০০", self.bangla_word.bangla_number(1400))
		self.assertEqual("নয় হাজার নয় শত নিরানব্বই", self.bangla_word.bangla_word_in_format(9999))
		self.assertEqual("বিরাশি", self.bangla_word.bangla_word_in_format(82))
		self.assertEqual("আঠারো লক্ষ পঁচানব্বই হাজার ছয় শত বাহান্ন", self.bangla_word.bangla_word_in_format(1895652))
		self.assertNotEqual("নয় হাজার", self.bangla_word.bangla_word_in_format(5000))


if __name__ == '__main__':
	unittest.main()
