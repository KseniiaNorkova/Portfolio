import random
import time

options = ("Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется "
                                                                                                         "- да",
           "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
           "Спроси позже",
           "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай",
           "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно")

vars_wait = (
    'Ещё немного...', 'Почти закончил...', 'Вселенная скоро ответит...', 'Ещё одну секундочку...',
    'Ответ уже на подходе',
    'Иииии...', 'Нужно ещё чуть-чуть подождать', 'Сейчас-сейчас!', 'Мне нужно ещё немного времени...',
    'Прошу подождать ещё буквально пару секунд!')

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Пожалуйста, представься!\n')

if name:
    print(f'Прекрасное имя - {name.capitalize()}.')
else:
    name = 'Гость'

answer = input(f'{name.capitalize()}, у тебя имеется вопрос ко мне? (да/нет)\n')
while answer.lower() not in ('да', 'нет'):
    answer = input(f'Прошу, ответь: да или нет?\n')


def giving_answer(string):
    if string == 'да':
        print('Произнеси вопрос или подумай о нём.')
        time.sleep(5)
        print('Начнём через 3...')
        time.sleep(1)
        print('2...')
        time.sleep(1)
        print('1!')
        time.sleep(1)
        print('Творю заклинание для поиска ответа.')
        time.sleep(3)
        print(random.choice(vars_wait))
        time.sleep(2)
        print(random.choice(vars_wait))
        time.sleep(2)
        return random.choice(options)
    elif string == 'нет':
        return f'Возвращайся, если я тебе снова понадоблюсь.'


print(giving_answer(answer))
while True:
    if answer == 'да':
        answer = input(f'{name.capitalize()}, есть ли у тебя ещё вопрос? (да/нет)\n')
        while answer not in ('да', 'нет'):
            answer = input(f'Прошу, ответь: да или нет?\n')
        print(giving_answer(answer))
    if answer == 'нет':
        print(f'Пока, {name.capitalize()}!')
        break
