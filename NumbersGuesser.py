import random

is_valid_int = lambda x: x.isdigit()
is_valid_str = lambda x: x.lower() in ('да', 'нет')
is_valid_d = lambda x, start, end: start <= int(x) <= end
is_valid_start = lambda start, end: all((is_valid_int(start), is_valid_int(end), start <= end))
flag = True
name = ''
start, end = '', ''

print('Добро пожаловать в цифровую угадайку!\n')

name_check = input('Как вас зовут?\n')

if name_check:
	name = f', {name_check}'

while flag:
	answer = input('Желаете сами выбрать диапазон, в котором будете угадывать числа? да/нет\n')
	while not is_valid_str(answer):
		answer = input('ДА или НЕТ?\n')

	if answer.lower() == 'да':
		while not all((is_valid_int(start := ''), is_valid_int(end := ''), is_valid_start(int(start), int(end)))):
			try:
				start, end = input(
				'Введите два числа желаемого диапазона через пробел: от меньшего к большему\n').split()
				if is_valid_start(start, end):
					break
				continue
			except ValueError:
				continue

	elif answer.lower() == 'нет':
		start = 1
		end = 100

	start, end = int(start), int(end)
	digit = random.randint(start, end)
	try_digit = input(f'Попробуйте угадать число от {start} до {end}\n')

	while not all((is_valid_int(try_digit), is_valid_d(try_digit, start, end))):
		try_digit = input(f'Введите число от {start} до {end}\n')

	while True:
		if int(try_digit) == digit:
			answer = input(
				f'Вы угадали, поздравляем{name}!\nХотите попробовать еще раз? да/нет \n')
			while not is_valid_str(answer):
				answer = input('ДА или НЕТ?\n')
			if answer.lower() == 'да':
				break
			elif answer.lower() == 'нет':
				print(f'Было приятно играть с вами{name}. До новых встреч!')
				flag = False
				break

		elif all((is_valid_int(try_digit), int(try_digit) > digit)):
			try_digit = input('Слишком много, попробуйте еще раз\n')
			while not all((is_valid_int(try_digit), is_valid_d(try_digit, start, end))):
				try_digit = input(f'Введите число от {start} до {end}\n')
			continue

		elif all((is_valid_int(try_digit), int(try_digit) < digit)):
			try_digit = input('Слишком мало, попробуйте еще раз\n')
			while not is_valid_int(try_digit) or not is_valid_d(try_digit, start, end):
				try_digit = input(f'Введите число от {start} до {end}\n')
				continue
