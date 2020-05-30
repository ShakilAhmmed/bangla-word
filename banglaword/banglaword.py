class BanglaWord:
	def __init__(self):
		self.numbers_in_word = [
			"শূন্য", "এক", "দুই", "তিন", "চার", "পাঁচ", "ছয়", "সাত", "আট", "নয়", "দশ", "এগারো", "বারো", "তেরো", "চৌদ্দ",
			"পনেরো", "ষোল", "সতেরো", "আঠারো", "উনিশ", "বিশ", "একুশ", "বাইশ", "তেইশ", "চব্বিশ", "পঁচিশ", "ছাব্বিশ",
			"সাতাশ", "আঠাশ", "ঊনত্রিশ", "ত্রিশ", "একত্রিশ", "বত্রিশ", "তেত্রিশ", "চৌত্রিশ", "পঁয়ত্রিশ", "ছত্রিশ",
			"সাঁইত্রিশ", "আটত্রিশ", "ঊনচল্লিশ", "চল্লিশ", "একচল্লিশ", "বিয়াল্লিশ", "তেতাল্লিশ", "চুয়াল্লিশ",
			"পঁয়তাল্লিশ", "ছেচল্লিশ", "সাতচল্লিশ", "আটচল্লিশ", "ঊনপঞ্চাশ", "পঞ্চাশ", "একান্ন", "বাহান্ন", "তিপ্পান্ন",
			"চুয়ান্ন", "পঞ্চান্ন", "ছাপ্পান্ন", "সাতান্ন", "আটান্ন", "ঊনষাট", "ষাট", "একষট্টি", "বাষট্টি", "তেষট্টি",
			"চৌষট্টি", "পঁয়ষট্টি", "ছেষট্টি", "সাতষট্টি", "আটষট্টি", "ঊনসত্তর", "সত্তর", "একাত্তর", "বাহাত্তর",
			"তিয়াত্তর", "চুয়াত্তর", "পঁচাত্তর", "ছিয়াত্তর", "সাতাত্তর", "আটাত্তর", "ঊনআশি", "আশি", "একাশি", "বিরাশি",
			"তিরাশি", "চুরাশি", "পঁচাশি", "ছিয়াশি", "সাতাশি", "আটাশি", "ঊননব্বই", "নব্বই", "একানব্বই", "বিরানব্বই",
			"তিরানব্বই", "চুরানব্বই", "পঁচানব্বই", "ছিয়ানব্বই", "সাতানব্বই", "আটানব্বই", "নিরানব্বই"
		]
		self.numbers = {
			"0": "০",
			"1": "১",
			"2": "২",
			"3": "৩",
			"4": "৪",
			"5": "৫",
			"6": "৬",
			"7": "৭",
			"8": "৮",
			"9": "৯",
		}

	def bangla_number(self, number):
		return self.convert_into_number(number)

	def convert_into_number(self, given):
		for index, value in self.numbers.items():
			given = given.replace(index, value)
		return given
