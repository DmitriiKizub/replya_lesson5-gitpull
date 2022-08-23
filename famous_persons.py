import random
def get_person_and_question():
    FAMOUS_PEAPLE = {'Александр Сергеевич Пушкни': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895'}
    name, date = random.choice(list(FAMOUS_PEAPLE.items()))
    asm = input(f'Когда родился {name}')

    if asm == date:
        print('Верно')
    else:
        print('Не верно')

def get_random_persons():
    FAMOUS_PEAPLE = {'Александр Сергеевич Пушкни': '26.06.1799', 'Михаил Юрьевич Лермонтов': '15.10.1814',
                     'Сергей Александрович Есенин': '03.10.1895'}
    name, date = random.choice(list(FAMOUS_PEAPLE.items()))
    return name,date