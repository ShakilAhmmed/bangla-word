class BanglaWord:
	def __init__(self):
		self.words_in_bangla = [
			"", "এক", "দুই", "তিন", "চার", "পাঁচ", "ছয়", "সাত", "আট", "নয়", "দশ", "এগারো", "বারো", "তেরো", "চৌদ্দ",
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
		self.months = {
			1: "জানুয়ারি",
			2: "ফেব্রুয়ারি",
			3: "মার্চ",
			4: "এপ্রিল",
			5: "মে",
			6: "জুন",
			7: "জুলাই",
			8: "আগস্ট",
			9: "সেপ্টেম্বর",
			10: "অক্টোবর",
			11: "নভেম্বর",
			12: "ডিসেম্বর",
		}
		self.days = {
			1: "শনিবার",
			2: "রবিবার",
			3: "সোমবার",
			4: "মঙ্গলবার",
			5: "বুধবার",
			6: "বৃহস্পতিবার",
			7: "শুক্রবার",
		}
		self.numbers = ["০", "১", "২", "৩", "৪", "৫", "৬", "৭", "৮", "৯"]

	def bangla_month(self, month):
		return self.months[month]

	def bangla_day(self, day):
		return self.days[day]

	def bangla_number(self, number):
		return self.convert(str(number), self.numbers)

	def bangla_word(self, number):
		if number == "0":
			return "শূন্য"
		output = ''
		if type(number) == float:
			number = str(number).split(".")
			output = self.bangla_word_in_format(int(number[0]))
			if number[1]:
				output += " দশমিক " + self.convert(str(number[1]), self.words_in_bangla)
			return output
		else:
			return self.convert(str(number), self.words_in_bangla)

	def word_formatted(self, number):
		output = ''
		get_cr = int(number / 10000000)
		if get_cr != 0:
			if get_cr > 99:
				output += self.bangla_word(get_cr) + ' কোটি '
			else:
				output += self.words_in_bangla[get_cr] + ' কোটি '

		get_cr_mod = number % 10000000

		get_lkh = int(get_cr_mod / 100000)
		if get_lkh > 0:
			output += self.words_in_bangla[get_lkh] + ' লক্ষ '

		get_lkh_mod = get_cr_mod % 100000

		thousand = int(get_lkh_mod / 1000)
		if thousand > 0:
			output += self.words_in_bangla[thousand] + ' হাজার '
		thousand_div = get_lkh_mod % 1000
		hundred = int(thousand_div / 100)
		if hundred > 0:
			output += self.words_in_bangla[hundred] + ' শত '
		hundred_div = int(thousand_div % 100)

		if hundred_div > 0:
			output += self.words_in_bangla[hundred_div]

		return output

	def bangla_word_in_format(self, number):
		money_formated_bangla = ''
		if self.zero_number_checker(number):
			money_formated_bangla = self.zero_number_checker(number)
		else:
			if type(number) == float:
				number = str(number).split(".")
				money_formated_bangla = self.word_formatted(int(number[0])) + ' দশমিক ' + self.converter_number(
					number[1])
			else:
				money_formated_bangla = self.word_formatted(number)
		return money_formated_bangla

	def converter_number(self, numbers):
		converted_number_word = ""
		for num in numbers:
			if int(num) != 0:
				converted_number_word += " " + self.words_in_bangla[int(num)]
			if int(num) == 0:
				converted_number_word += " শূন্য"
		return converted_number_word

	def zero_number_checker(self, number):
		output = "শূন্য"
		if type(number) == float:
			number = str(number).split(".")
			if number[0] == "0":
				return output
		elif str(number) == "0":
			return output

	def moeny_format(self, number):
		money_formated = ''
		if self.zero_number_checker(number):
			money_formated = self.zero_number_checker(number) + ' টাকা '
		else:
			if type(number) == float:
				number = str(number).split(".")
				money_formated = self.word_formatted(int(number[0])) + ' টাকা ' + self.words_in_bangla[
					int(number[1])] + ' পয়সা '
			else:
				money_formated = self.word_formatted(number) + ' টাকা '
		return money_formated

	@staticmethod
	def convert(given, replace):
		for index, value in enumerate(replace):
			given = given.replace(str(index), value)
		return given
