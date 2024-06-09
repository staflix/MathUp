from company.company_creator import *

year_3 = Class(3)

topic_1 = Topic('Числа   от   1   до   100. Сложение и вычитание.')
lvl_1 = Level(1, info='Привет! Немного посчитай примеры.')
lvl_1.add(Task(text='реши пример в столбик на картинке', answer='55', image="pic/50.jpg"))
lvl_1.add(Task(text='и этот', answer='80', image="pic/51.jpg"))
lvl_1.add(Task(text="Сколько будет 15 + 28?", answer="43", choice=['43', '45', '41']))
lvl_1.add(Task(text="Сколько будет 95 - 33?", answer="62", choice=['62', '52', '72']))
lvl_1.add(Task(text="Что будет, если к 47 прибавить 53?", answer="100", choice=['100', '90', '110']))


lvl_2 = Level(1, info='Теперь немного примеров!')
lvl_2.add(Task(text='реши вот этот пример в несколько действий', answer='79', image='pic/52.jpg'))
lvl_2.add(Task(text="1 + 34 - 32 =", answer="3"))
lvl_2.add(Task(text="7 - 6 - 29 =", answer="-28"))
lvl_2.add(Task(text="1 + 34 - 32 =", answer="3"))

lvl_3 = Level(1, info='Продолжаем')
lvl_3.add(Task(text="11 - 19 + 8 =", answer="0"))
lvl_3.add(Task(text="36 + 41 - 1 =", answer="76"))
lvl_3.add(Task(text="17 - 8 - 12 =", answer="-3"))
lvl_3.add(Task(text="11 - 19 + 8 =", answer="0"))

lvl_4 = Level(1, info='Давай повторим')
lvl_4.add(Task(text='60 - 50 + 3', answer='13'))
lvl_4.add(Task(text='11 - 8 + 7', answer='10'))
lvl_4.add(Task(text='100 - 60 + 3', answer='43'))
lvl_4.add(Task(text='30 + 20 + 3', answer='53'))


lvl_5 = Level(1, info='Закрепим пройденное!')
lvl_5.add(Task(text='80 + 12', answer='92'))
lvl_5.add(Task(text='Первая игра заняла 1 час, а вторая шла на 10 минут. Сколько минут шли ргы вместе?', answer='70'))
lvl_5.add(Task(text='? + 11 = 20', answer='9'))
lvl_5.add(Task(text='80 - ? = 30', answer='50'))


lvl_6 = Level(1, info='Привет! Прочитай записи и выполни действия')
lvl_6.add(Task(text='6 + (3 - 1)', answer='8'))
lvl_6.add(Task(text='(8 - 2) + 3', answer='9'))
lvl_6.add(Task(text="Прочитай запись и выполни действие: 90 - 45 =", answer="45", choice=['40', '45', '50']))
lvl_6.add(Task(text="(52 + 48) * 1 =", answer="100", choice=['90', '300', '100']))


lvl_7 = Level(1, info='Вычисли, проговаривая устно!')
lvl_7.add(Task(text='50 - 6', answer='44'))
lvl_7.add(Task(text='100 - 4', answer='96'))
lvl_7.add(Task(text='90 - 3', answer='87'))
lvl_7.add(Task(text='81 - 3', answer='78'))

lvl_8 = Level(1, info='Проверь выражения и напиши Верно или Неверно')
lvl_8.add(Task(text='69 - 50 = 19', answer='Верно'))
lvl_8.add(Task(text='100 - 8 = 92', answer='Верно'))
lvl_8.add(Task(text='74 - 30 = 54', answer='Неверно'))

lvl_9 = Level(1, info='Сколько раз содержится ...')
lvl_9.add(Task(text='Сколько раз 4 содержится в числе 8?', answer='2'))
lvl_9.add(Task(text='А 2 содержится в числе 8?', answer='4'))
lvl_9.add(Task(text='Сколько раз 4 содержится в числе 16?', answer='4'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Числа от 1 до 100. Сложение и вычитание.')
lvl_10.add(Task(text='1 + 26', answer='27'))
lvl_10.add(Task(text='9 - 3', answer='6'))
lvl_10.add(Task(text='3 + 12', answer='15'))
lvl_10.add(Task(text='Сколько раз 4 содержится в числе 16?', answer='4'))
lvl_10.add(Task(text='74 - 30 = 54', answer='Неверно'))


topic_1.add_level(lvl_1)
topic_1.add_level(lvl_2)
topic_1.add_level(lvl_3)
topic_1.add_level(lvl_4)
topic_1.add_level(lvl_5)
topic_1.add_level(lvl_6)
topic_1.add_level(lvl_7)
topic_1.add_level(lvl_8)
topic_1.add_level(lvl_9)
topic_1.add_level(lvl_10)
year_3.add_level(topic_1)


topic_2 = Topic('Числа   от   1   до   100. Умножение и деление.')

lvl_1 = Level(1, info='Теперь просто без лишних слов поделим и поумножаем')
lvl_1.add(Task(text="3 * 2 / 3 =", answer="2"))
lvl_1.add(Task(text="4 * 8 / 1 =", answer="32"))
lvl_1.add(Task(text="6 * 7 / 6 =", answer="7"))

lvl_2 = Level(1, info='Немного примеров!')
lvl_2.add(Task(text="3 * 3 * 6 =", answer="54"))
lvl_2.add(Task(text="10 * 10 * 4 =", answer="400"))
lvl_2.add(Task(text="5 * 3 * 1 =", answer="15"))
lvl_2.add(Task(text="2 * 10 * 5 =", answer="100"))

lvl_3 = Level(1, info='Ещё примеры!')
lvl_3.add(Task(text="7 / 1 * 10 =", answer="70"))
lvl_3.add(Task(text="9 * 6 / 6 =", answer="9"))
lvl_3.add(Task(text="1 / 2 * 6 =", answer="3"))


lvl_4 = Level(1, info='Используй свойство умножения.')
lvl_4.add(Task(text='4 * 5 = 20, 5 * 4 = ?', answer='20'))
lvl_4.add(Task(text='7 * 4 = 28, 4 * 7 = ?', answer='28'))
lvl_4.add(Task(text='9 * 3 = 27, 3 * 9 = ?', answer='27'))

lvl_5 = Level(1, info='Выполни деление, используя рисунки')
lvl_5.add(Task(text='6 : 2', answer='3', image='pic/126.jpg'))
lvl_5.add(Task(text='10 : 2', answer='5', image='pic/127.jpg'))
lvl_5.add(Task(text='8 : 4', answer='2', image='pic/128.jpg'))

lvl_6 = Level(1, info='Используй свойство умножения.')
lvl_6.add(Task(text='4 * 5 = 20, 5 * 4 = ?', answer='20'))
lvl_6.add(Task(text='7 * 4 = 28, 4 * 7 = ?', answer='28'))
lvl_6.add(Task(text='9 * 3 = 27, 3 * 9 = ?', answer='27'))

lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='1 * 26', answer='26'))
lvl_7.add(Task(text='0 * (21 - 8)', answer='0'))
lvl_7.add(Task(text='17 + 80 + 3', answer='100'))


lvl_8 = Level(1, info='Найди значение выражения 65 - b')
lvl_8.add(Task(text='Где b = 65.', answer='0'))
lvl_8.add(Task(text='А если b = 20?', answer='45'))
lvl_8.add(Task(text='А при b = 49?', answer='16'))

lvl_9 = Level(1, info='Верно или нет?')
lvl_9.add(Task(text='Если число 47 увеличить на 30 получится 17', answer='Неверно', choice=['Верно', 'Неверно']))
lvl_9.add(Task(text='Разность чисел 32 и 8 равна 24', answer='Верно', choice=['Верно', 'Неверно']))
lvl_9.add(Task(text='Если вместо ? поставить 73 то будет верно ? - 4 = 68', answer='Неверно', choice=['Верно', 'Неверно']))
lvl_9.add(Task(text='Число 34 больше 9 на 25', answer='Верно', choice=['Верно', 'Неверно']))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Деление!')
lvl_10.add(Task(text='1 * 26', answer='26'))
lvl_10.add(Task(text='9 * 3', answer='27'))
lvl_10.add(Task(text='3 * 12', answer='36'))
lvl_10.add(Task(text='7 * 3 ? 6 * 4', answer='<', choice=['>', '<', '=']))
lvl_10.add(Task(text='2 * 14 ? 6 * 4', answer='>', choice=['>', '<', '=']))
lvl_10.add(Task(text='Число 34 больше 9 на 25', answer='Верно', choice=['Верно', 'Неверно']))
lvl_10.add(Task(text='Если число 47 увеличить на 30 получится 17', answer='Неверно', choice=['Верно', 'Неверно']))

topic_2.add_level(lvl_1)
topic_2.add_level(lvl_2)
topic_2.add_level(lvl_3)
topic_2.add_level(lvl_4)
topic_2.add_level(lvl_5)
topic_2.add_level(lvl_6)
topic_2.add_level(lvl_7)
topic_2.add_level(lvl_8)
topic_2.add_level(lvl_9)
topic_2.add_level(lvl_10)
year_3.add_level(topic_2)

topic_3 = Topic("Умножение на 1")
lvl_1 = Level(1, info='Привет! Тебе нужно поумнажаить 1!')
lvl_1.add(Task(text="26 * 1 =", answer="26"))
lvl_1.add(Task(text="9 * 1 =", answer="9"))
lvl_1.add(Task(text="14 * 1 =", answer="14"))

lvl_2 = Level(1, info='Продолжаем!')
lvl_2.add(Task(text="24 * 1 =", answer="24"))
lvl_2.add(Task(text="30 * 1 =", answer="30"))
lvl_2.add(Task(text="22 * 1 =", answer="22"))
lvl_2.add(Task(text="51 * 1 =", answer="51"))

lvl_3 = Level(1, info='давай теперь такие ')
lvl_3.add(Task(text="6 * 7 = ?", answer="42"))
lvl_3.add(Task(text="8 * 9 = ?", answer="72"))
lvl_3.add(Task(text="12 * 3 = ?", answer="36"))

lvl_4 = Level(1, info='а вот и текстовые задачки')
lvl_4.add(Task(text="В одной коробке лежит 12 карандашей. Сколько всего карандашей в 5 таких коробках?", answer="60"))
lvl_4.add(Task(text="Один апельсин стоит 7 рублей. Сколько стоят 8 апельсинов?", answer="56"))
lvl_4.add(Task(text="В одной тетради 48 страниц. Сколько страниц в 6 тетрадях?", answer="288"))


lvl_5 = Level(1, info='Вычисли, заменяя умножение сложением.')
lvl_5.add(Task(text='2 * 5', answer='10'))
lvl_5.add(Task(text='4 * 3', answer='12'))
lvl_5.add(Task(text='7 * 4', answer='28'))
lvl_5.add(Task(text='9 * 3', answer='27'))


lvl_6 = Level(1, info='примеры на соложение')
lvl_6.add(Task(text='8 * 3 + 16', answer='40'))
lvl_6.add(Task(text='3 * 3 - 5', answer='4'))
lvl_6.add(Task(text='21 - 4 * 5', answer='1'))


lvl_7 = Level(1, info='Используй свойство умножения.')
lvl_7.add(Task(text='4 * 5 = 20, 5 * 4 = ?', answer='20'))
lvl_7.add(Task(text='7 * 4 = 28, 4 * 7 = ?', answer='28'))
lvl_7.add(Task(text='9 * 3 = 27, 3 * 9 = ?', answer='27'))


lvl_8 = Level(1, info='Найди значение х в уравнениях.')
lvl_8.add(Task(text='х + х + х = 30', answer='10'))
lvl_8.add(Task(text='43 * х = 43 : х', answer='1'))
lvl_8.add(Task(text='х + 20 = 12 + 8', answer='0'))
lvl_8.add(Task(text='х - 18 = 23 - 23', answer='18'))

lvl_9 = Level(1, info='Реши уравнения')
lvl_9.add(Task(text='х : 5 = 10', answer='50'))
lvl_9.add(Task(text='х : 7 - 6 = 0', answer='42'))
lvl_9.add(Task(text='у * 5 = 20', answer='4'))
lvl_9.add(Task(text='у * 6 + 2 = 38', answer='6'))

lvl_10 = Level(1, info='Время теста!', style='test', time=60, topic='умнажение на 1')
lvl_10.add(Task(text="13 * 1 =", answer="13"))
lvl_10.add(Task(text="45 * 1 =", answer="45"))
lvl_10.add(Task(text="47 * 1 =", answer="47"))
lvl_10.add(Task(text='х + 20 = 12 + 8', answer='0'))
lvl_10.add(Task(text='х - 18 = 23 - 23', answer='18'))
lvl_10.add(Task(text='7 * 4 = 28, 4 * 7 = ?', answer='28'))
lvl_10.add(Task(text='9 * 3 = 27, 3 * 9 = ?', answer='27'))
lvl_10.add(Task(text='7 * 4', answer='28'))
lvl_10.add(Task(text='9 * 3', answer='27'))


topic_3.add_level(lvl_1)
topic_3.add_level(lvl_2)
topic_3.add_level(lvl_3)
topic_3.add_level(lvl_4)
topic_3.add_level(lvl_5)
topic_3.add_level(lvl_6)
topic_3.add_level(lvl_7)
topic_3.add_level(lvl_8)
topic_3.add_level(lvl_9)
topic_3.add_level(lvl_10)
year_3.add_level(topic_2)


topic_4 = Topic('умнажение на 0')
lvl_1 = Level(1, info='Привет! Тут тоже самое только нужно умножить на 0.')
lvl_1.add(Task(text="41 * 0 =", answer="0"))
lvl_1.add(Task(text="27 * 0 =", answer="0"))
lvl_1.add(Task(text="13 * 0 =", answer="0"))

lvl_2 = Level(1, info='задачки')
lvl_2.add(Task(text="В одной коробке лежит 12 карандашей. Сколько всего карандашей в 5 таких коробках?", answer="60"))
lvl_2.add(Task(text="Один апельсин стоит 7 рублей. Сколько стоит 8 апельсинов?", answer="56"))
lvl_2.add(Task(text="В одной тетради 48 страниц. Сколько страниц в 6 тетрадях?", answer="288"))


lvl_3 = Level(1, info='тоже самое')
lvl_3.add(Task(text="81 ÷ 9 = ?", answer="9"))
lvl_3.add(Task(text="100 ÷ 25 = ?", answer="4"))
lvl_3.add(Task(text="64 ÷ 8 = ?", answer="8"))
lvl_3.add(Task(text="72 ÷ 8 = ?", answer="9"))

lvl_4 = Level(1, info='Привет! Начнем с примеров!')
lvl_4.add(Task(text='45 : (18 - 13)', answer='9'))
lvl_4.add(Task(text='(27 + 27) : 9', answer='6'))
lvl_4.add(Task(text='24 : (11 - 7)', answer='6'))

lvl_5 = Level(1, info='попробуй такие примеры решить.')
lvl_5.add(Task(text="8 × 9 = ?", answer="72"))
lvl_5.add(Task(text="12 × 3 = ?", answer="36"))
lvl_5.add(Task(text="4 × 25 = ?", answer="100"))
lvl_5.add(Task(text='(24 + 21) * 0', answer='0'))


lvl_6 = Level(1, info='Реши уравнения')
lvl_6.add(Task(text='х : 5 = 10', answer='50'))
lvl_6.add(Task(text='х : 7 - 6 = 0', answer='42'))
lvl_6.add(Task(text='у * 5 = 20', answer='4'))
lvl_6.add(Task(text='у * 6 + 2 = 38', answer='6'))


lvl_7 = Level(1, info='Привет! Начнем с примеров!')
lvl_7.add(Task(text='30 + 6 * (13 - 9)', answer='54'))
lvl_7.add(Task(text='18 : 2 - 2 * 3 ', answer='4'))
lvl_7.add(Task(text='24 : (3 * 2)', answer='4'))


lvl_8 = Level(1, info='Вычисли, заменяя умножение сложением.')
lvl_8.add(Task(text='2 * 5', answer='10'))
lvl_8.add(Task(text='4 * 3', answer='12'))
lvl_8.add(Task(text='7 * 4', answer='28'))
lvl_8.add(Task(text='9 * 3', answer='27'))

lvl_9 = Level(1, info='Реши уравнения')
lvl_9.add(Task(text='х : 5 = 10', answer='50'))
lvl_9.add(Task(text='х : 7 - 6 = 0', answer='42'))
lvl_9.add(Task(text='у * 5 = 20', answer='4'))
lvl_9.add(Task(text='у * 6 + 2 = 38', answer='6'))


lvl_10 = Level(1, info='Время теста!', style='test', time=60, topic='умнажение на 0')
lvl_10.add(Task(text='7 * 4', answer='28'))
lvl_10.add(Task(text='9 * 3', answer='27'))
lvl_10.add(Task(text='х : 7 - 6 = 0', answer='42'))
lvl_10.add(Task(text='у * 5 = 20', answer='4'))
lvl_10.add(Task(text='у * 6 + 2 = 38', answer='6'))
lvl_10.add(Task(text='24 : (3 * 2)', answer='4'))
lvl_10.add(Task(text='у * 5 = 20', answer='4'))
lvl_10.add(Task(text='у * 6 + 2 = 38', answer='6'))


topic_4.add_level(lvl_1)
topic_4.add_level(lvl_2)
topic_4.add_level(lvl_3)
topic_4.add_level(lvl_4)
topic_4.add_level(lvl_5)
topic_4.add_level(lvl_6)
topic_4.add_level(lvl_7)
topic_4.add_level(lvl_8)
topic_4.add_level(lvl_9)
topic_4.add_level(lvl_10)
year_3.add_level(topic_4)


topic_5 = Topic('Доли.')

lvl_1 = Level(1, info='Привет! Определи сколько долей ')
lvl_1.add(Task(text='Сколько яблок на этой картинке?', answer='2', image='pic/53.jpg'))
lvl_1.add(Task(text='А на этой?', answer='4', image='pic/54.jpg'))
lvl_1.add(Task(text="Какую часть от целого составляет 1/3?", answer="треть", choice=['треть', 'четверть', 'половину']))
lvl_1.add(Task(text="Какую часть от целого составляет 1/8?", answer="одну восьмую", choice=['одну шестую', 'одну восьмую', 'одну десятую']))
lvl_1.add(Task(text="Какую часть от целого составляет 3/4?", answer="три четверти", choice=['три пятых', 'три четверти', 'три восьмых']))


lvl_2 = Level(1, info='Привет! Сравни части.')
lvl_2.add(Task(text='ответь на вопрос на рисунку', answer='одна четвертая', image='pic/55.jpg', choice=['одна шестая', 'одна четвертая']))
lvl_2.add(Task(text='какая часть меньше одна вторая или одна третья?', answer='одна третья', image='pic/55.jpg', choice=['одна третья', 'одна вторая']))
lvl_2.add(Task(text="Что меньше: 2/3 или 3/4?", answer="2/3", choice=['2/3', '3/4']))
lvl_2.add(Task(text="Что больше: 1/8 или 1/6?", answer="1/6", choice=['1/8', '1/6']))
lvl_2.add(Task(text="Что меньше: 3/8 или 5/8?", answer="3/8", choice=['3/8', '5/8']))


lvl_3 = Level(1, info='Выбери как называется часть на рисунке')
lvl_3.add(Task(text='как можно назвать часть на рисунке', answer='одна третья', image='pic/56.jpg', choice=['одна третья', 'три первых']))
lvl_3.add(Task(text='А какя часть здесь выделина?', answer='одна двенадцатая', image='pic/57.jpg', choice=['одна третья', 'три первых', 'одна двенадцатая']))
lvl_3.add(Task(text="Если разрезать яблоко на 8 частей и взять 3 из них, какая это доля яблока?", answer="3/8", choice=['3/8', '1/2', '1/3']))

lvl_4 = Level(1, info='Давай еще немного по чястям')
lvl_4.add(Task(text='сколько здесь частей выделено?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_4.add(Task(text='а здесь?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_4.add(Task(text='последний раз', answer='1', image='pic/59.jpg', choice=['1', '2', '3']))


lvl_5 = Level(1, info='Ребусы!')
lvl_5.add(Task(text="Сколько частей будет, если разрезать пиццу на восьмушки?", answer="8"))
lvl_5.add(Task(text="Если разрезать шоколадку на 10 равных частей, сколько частей составят 3/10 шоколадки?", answer="3"))
lvl_5.add(Task(text="Что больше: 2/5 или 1/2?", answer="1/2"))
lvl_5.add(Task(text="Как называется одна из трёх равных частей целого?", answer="треть"))
lvl_5.add(Task(text="Если вы взяли 2 из 4 частей пирога, какая это доля?", answer="1/2"))


lvl_6 = Level(1, info='Какое число пропущено в ряду?')
lvl_6.add(Task(text="Если разрезать яблоко на 8 частей и взять 3 из них, какая это доля яблока?", answer="3/8", choice=['3/8', '1/2', '1/3']))
lvl_6.add(Task(text="Что больше: 1/4 или 1/3?", answer="1/3", choice=['1/4', '1/3', '1/2']))
lvl_6.add(Task(text="Сколько частей в целой пицце, если каждый кусок это 1/8?", answer="8", choice=['6', '8', '10']))


lvl_7 = Level(1, info='Вычислительная машина!')
lvl_7.add(Task(text="(5 + 17) / 2 =", answer="11"))
lvl_7.add(Task(text="(7 + 8) / 6 =", answer="2"))
lvl_7.add(Task(text="(11 + 6) / 2 =", answer="8"))
lvl_7.add(Task(text="(21 + 1) / 7 =", answer="3"))
lvl_7.add(Task(text="(7 + 14) / 8 =", answer="2"))


lvl_8 = Level(1, info='Немного примеров!')
lvl_8.add(Task(text='12 - 8 + 9', answer='13'))
lvl_8.add(Task(text='17 - 8 + 6', answer='15'))
lvl_8.add(Task(text='48 - 40 - 8', answer='0'))
lvl_8.add(Task(text='0 + 88 - 8', answer='80'))

lvl_9 = Level(1, info='Вычисли и выполни проверку')
lvl_9.add(Task(text="Что больше: 2/5 или 1/2?", answer="1/2", choice=['2/5', '1/2', '1/3']))
lvl_9.add(Task(text="Как называется одна из трёх равных частей целого?", answer="треть", choice=['треть', 'четверть', 'половина']))
lvl_9.add(Task(text="Если вы взяли 2 из 4 частей пирога, какая это доля?", answer="1/2", choice=['1/2', '1/4', '1/3']))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Угол. Виды углов. Логика.')
lvl_10.add(Task(text='Сколько яблок на этой картинке?', answer='2', image='pic/53.jpg'))
lvl_10.add(Task(text='А на этой?', answer='4', image='pic/54.jpg'))
lvl_10.add(Task(text='сколько здесь частей выделено?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_10.add(Task(text='а здесь?', answer='1', image='pic/58.jpg', choice=['1', '2', '3']))
lvl_10.add(Task(text='последний раз', answer='1', image='pic/59.jpg', choice=['1', '2', '3']))
lvl_10.add(Task(text='ответь на вопрос на рисунку', answer='одна четвертая', image='pic/55.jpg', choice=['одна шестая', 'одна четвертая']))
lvl_10.add(Task(text='какая часть меньше одна вторая или одна третья?', answer='одна третья', image='pic/55.jpg', choice=['одна третья', 'одна вторая']))

topic_5.add_level(lvl_1)
topic_5.add_level(lvl_2)
topic_5.add_level(lvl_3)
topic_5.add_level(lvl_4)
topic_5.add_level(lvl_5)
topic_5.add_level(lvl_6)
topic_5.add_level(lvl_7)
topic_5.add_level(lvl_8)
topic_5.add_level(lvl_9)
topic_5.add_level(lvl_10)
year_3.add_level(topic_5)


topic_6 = Topic('вычисления вида 80:20.')

lvl_1 = Level(1, info='Привет! Будет немного деления')
lvl_1.add(Task(text="70 / 10 =", answer="7"))
lvl_1.add(Task(text="90 / 10 =", answer="9"))
lvl_1.add(Task(text="80 / 10 =", answer="8"))

lvl_2 = Level(1, info='теперь на 20')
lvl_2.add(Task(text="80 ÷ 20 = ?", answer="4", choice=['3', '4', '5']))
lvl_2.add(Task(text="60 ÷ 20 = ?", answer="3"))
lvl_2.add(Task(text="100 ÷ 20 = ?", answer="5", choice=['4', '5', '6']))
lvl_2.add(Task(text="40 ÷ 20 = ?", answer="2"))


lvl_3 = Level(1, info='И нужно повторить умножение ')
lvl_3.add(Task(text="1 * 12 =", answer="12"))
lvl_3.add(Task(text="22 * 3 =", answer="66"))
lvl_3.add(Task(text="1 * 17 =", answer="17"))
lvl_3.add(Task(text="3 * 14 =", answer="42"))
lvl_3.add(Task(text="5 * 7 =", answer="35"))

lvl_4 = Level(1, info='Реши уравнения!')
lvl_4.add(Task(text='75 - х = 75', answer='0'))
lvl_4.add(Task(text='4 + х = 84', answer='80'))
lvl_4.add(Task(text='89 - х = 0', answer='89'))

lvl_5 = Level(1, info='Вычислительная машина!')
lvl_5.add(Task(text="(5 + 17) / 2 =", answer="11"))
lvl_5.add(Task(text="(7 + 8) / 6 =", answer="2"))
lvl_5.add(Task(text="50 ÷ 20 = ?", answer="2.5"))
lvl_5.add(Task(text="30 ÷ 20 = ?", answer="1.5", choice=['1', '1.5', '2']))
lvl_5.add(Task(text="10 ÷ 20 = ?", answer="0.5"))


lvl_6 = Level(1, info='Вычислительная машина!')
lvl_6.add(Task(text="(5 + 17) / 2 =", answer="11"))
lvl_6.add(Task(text="(7 + 8) / 6 =", answer="2"))
lvl_6.add(Task(text="(11 + 6) / 2 =", answer="8"))
lvl_6.add(Task(text="(21 + 1) / 7 =", answer="3"))
lvl_6.add(Task(text="(7 + 14) / 8 =", answer="2"))


lvl_7 = Level(1, info='Реши уравнения!')
lvl_7.add(Task(text='75 - х = 75', answer='0'))
lvl_7.add(Task(text='4 + х = 84', answer='80'))
lvl_7.add(Task(text='89 - х = 0', answer='89'))

lvl_8 = Level(1, info='Немного уравнений')
lvl_8.add(Task(text='x - 9 = 4', answer='13'))
lvl_8.add(Task(text='35 - x = 30', answer='5'))
lvl_8.add(Task(text='y + 7 = 14', answer='7'))


lvl_9 = Level(1, info='Вычисли, заменяя умножение сложением.')
lvl_9.add(Task(text="Если разделить 80 конфет на 20 детей, сколько конфет получит каждый ребенок?", answer="4", choice=['3', '4', '5']))
lvl_9.add(Task(text="Если у тебя 60 карандашей и ты поделишь их на 20 коробок, сколько карандашей будет в каждой коробке?", answer="3"))
lvl_9.add(Task(text="Сколько 20-рублевых купюр нужно, чтобы получить 100 рублей?", answer="5"))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='вычисления вида 80:20..')
lvl_10.add(Task(text="(11 + 6) / 2 =", answer="8"))
lvl_10.add(Task(text="(21 + 1) / 7 =", answer="3"))
lvl_10.add(Task(text="(7 + 14) / 8 =", answer="2"))
lvl_10.add(Task(text="22 * 3 =", answer="66"))
lvl_10.add(Task(text="Если у тебя 60 карандашей и ты поделишь их на 20 коробок, сколько карандашей будет в каждой коробке?", answer="3"))
lvl_10.add(Task(text="Сколько 20-рублевых купюр нужно, чтобы получить 100 рублей?", answer="5"))
lvl_10.add(Task(text='35 - x = 30', answer='5'))
lvl_10.add(Task(text='y + 7 = 14', answer='7'))
lvl_10.add(Task(text="(21 + 1) / 7 =", answer="3"))
lvl_10.add(Task(text="(7 + 14) / 8 =", answer="2"))


topic_6.add_level(lvl_1)
topic_6.add_level(lvl_2)
topic_6.add_level(lvl_3)
topic_6.add_level(lvl_4)
topic_6.add_level(lvl_5)
topic_6.add_level(lvl_6)
topic_6.add_level(lvl_7)
topic_6.add_level(lvl_8)
topic_6.add_level(lvl_9)
topic_6.add_level(lvl_10)
year_3.add_level(topic_6)


topic_7 = Topic('Пероверка деления.')

lvl_1 = Level(1, info='Привет! Проверь уравнения!')
lvl_1.add(Task(text="21 / 3 = 7", answer="да", choice=["да", "нет"]))
lvl_1.add(Task(text="4 / 1 = 4", answer="да", choice=["да", "нет"]))
lvl_1.add(Task(text="20 / 10 = 3", answer="нет", choice=["да", "нет"]))
lvl_1.add(Task(text="23 / 2 = 12", answer="нет", choice=["да", "нет"]))

lvl_2 = Level(1, info='еще разок ')
lvl_2.add(Task(text="3 / 1 = 3", answer="да", choice=["да", "нет"]))
lvl_2.add(Task(text="14 / 1 = 7", answer="нет", choice=["да", "нет"]))
lvl_2.add(Task(text="21 / 3 = 7", answer="да", choice=["да", "нет"]))

lvl_3 = Level(1, info='Проверка умножения ')
lvl_3.add(Task(text="Проверка деления: 60 ÷ 15 = 4. Какое умножение подтверждает это деление?", answer="15 × 4 = 60"))
lvl_3.add(Task(text="Проверка деления: 100 ÷ 25 = 4. Какое умножение подтверждает это деление?", answer="25 × 4 = 100", choice=['25 × 4 = 100', '25 × 3 = 100', '25 × 5 = 100']))
lvl_3.add(Task(text="Проверка деления: 40 ÷ 10 = 4. Какое умножение подтверждает это деление?", answer="10 × 4 = 40"))
lvl_3.add(Task(text="Проверка деления: 20 ÷ 5 = 4. Какое умножение подтверждает это деление?", answer="5 × 4 = 20", choice=['5 × 4 = 20', '5 × 3 = 20', '5 × 5 = 20']))


lvl_4 = Level(1, info='еще разок.')
lvl_4.add(Task(text="36 ÷ 5. Верно ли, что остаток равен 1?", answer="Нет", choice=['Да', 'Нет', 'Иногда']))
lvl_4.add(Task(text="50 ÷ 8. Верно ли, что остаток равен 2?", answer="Да", choice=['Да', 'Нет', 'Не знаю']))
lvl_4.add(Task(text="72 ÷ 9. Верно ли, что остаток равен 0?", answer="Да", choice=['Да', 'Нет']))


lvl_5 = Level(1, info="давай немного начнем повторять")
lvl_5.add(Task(text="54 ÷ 6 =", answer="9"))
lvl_5.add(Task(text="36 ÷ 4 =", answer="9"))
lvl_5.add(Task(text="81 ÷ 9 =", answer="9"))

lvl_6 = Level(1, info='Состав числа 5 из двухслагаемых.')
lvl_6.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_6.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_6.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_7 = Level(1, info='еще пару раз.')
lvl_7.add(Task(text='какой знак нужно поставить?', choice=['-', '+'], answer='-', image='pic/26.jpg'))
lvl_7.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_7.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))


lvl_8 = Level(1, info='Рассмотрим картинку')
lvl_8.add(Task(text="28 ÷ 7. Можно ли разделить 28 на 7 без остатка?", answer="Да", choice=['Да', 'Нет']))
lvl_8.add(Task(text="36 ÷ 9. Можно ли разделить 36 на 9 без остатка?", answer="Да", choice=['Да', 'Нет']))
lvl_8.add(Task(text="50 ÷ 10. Можно ли разделить 50 на 10 без остатка?", answer="Да", choice=['Да', 'Нет']))

lvl_9 = Level(1, info='готов скоро тест')
lvl_9.add(Task(text='Сколько дециметров в 2 метрах?', answer="20"))
lvl_9.add(Task(text="50 ÷ 8. Верно ли, что остаток равен 2?", answer="Да", choice=['Да', 'Нет', 'Не знаю']))
lvl_9.add(Task(text="7+?=15", answer='8'))
lvl_9.add(Task(text='6+5', answer='11'))
lvl_9.add(Task(text='6+6', answer='12'))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Умножение!')
lvl_10.add(Task(text='Сколько дециметров в 2 метрах?', answer="20"))
lvl_10.add(Task(text="50 ÷ 8. Верно ли, что остаток равен 2?", answer="Да", choice=['Да', 'Нет', 'Не знаю']))
lvl_10.add(Task(text="7+?=15", answer='8'))
lvl_10.add(Task(text='6+5', answer='11'))
lvl_10.add(Task(text='6+6', answer='12'))
lvl_10.add(Task(text='Выберите знак + или -', choice=['+', '-'], answer='+', image='pic/27.jpg'))
lvl_10.add(Task(text='+ или -', choice=['-', '+'], answer='+', image='pic/28.jpg'))
lvl_10.add(Task(text="Проверка деления: 100 ÷ 25 = 4. Какое умножение подтверждает это деление?", answer="25 × 4 = 100", choice=['25 × 4 = 100', '25 × 3 = 100', '25 × 5 = 100']))
lvl_10.add(Task(text="Проверка деления: 40 ÷ 10 = 4. Какое умножение подтверждает это деление?", answer="10 × 4 = 40"))
lvl_10.add(Task(text="Проверка деления: 20 ÷ 5 = 4. Какое умножение подтверждает это деление?", answer="5 × 4 = 20", choice=['5 × 4 = 20', '5 × 3 = 20', '5 × 5 = 20']))


topic_7.add_level(lvl_1)
topic_7.add_level(lvl_2)
topic_7.add_level(lvl_3)
topic_7.add_level(lvl_4)
topic_7.add_level(lvl_5)
topic_7.add_level(lvl_6)
topic_7.add_level(lvl_7)
topic_7.add_level(lvl_8)
topic_7.add_level(lvl_9)
topic_7.add_level(lvl_10)
year_3.add_level(topic_7)


topic_8 = Topic('Деление с остатком.')

lvl_1 = Level(1, info='Привет! Найди остаток!')
lvl_1.add(Task(text='27 / 3 = ', answer='0'))
lvl_1.add(Task(text='26 / 3 =', answer='2'))
lvl_1.add(Task(text='28 / 3 = ', answer='1'))

lvl_2 = Level(1, info='найди остаток ')
lvl_2.add(Task(text="48 ÷ 9 = ?", answer="5, остаток 3", choice=['5, остаток 3', '6, остаток 2', '4, остаток 4']))
lvl_2.add(Task(text="67 ÷ 10 = ?", answer="6, остаток 7", choice=['6, остаток 7', '7, остаток 6', '5, остаток 8']))
lvl_2.add(Task(text="92 ÷ 12 = ?", answer="7, остаток 8", choice=['7, остаток 8', '8, остаток 6', '6, остаток 10']))


lvl_3 = Level(1, info='задачки!')
lvl_3.add(Task(text="На полке было 85 книг. Если их распределить по коробкам по 9 книг, сколько книг останется без коробки?", answer="4", choice=['4', '3', '5']))
lvl_3.add(Task(text="Мария собрала 64 яблока. Она хочет упаковать их в коробки по 5 яблок. Сколько коробок ей понадобится?", answer="12, остаток 4", choice=['12, остаток 4', '11, остаток 3', '13, остаток 2']))
lvl_3.add(Task(text="В мешке было 110 монет. Если их равномерно разделить между 8 друзьями, сколько монет получит каждый друг? (с остатком)", answer="13, остаток 6", choice=['13, остаток 6', '12, остаток 5', '14, остаток 4']))
lvl_3.add(Task(text="На поле было 77 овец. Если их разделить на загоны по 10 овец, сколько овец останется в последнем загоне?", answer="7", choice=['7', '8', '6']))


lvl_4 = Level(1, info='Вычисли, заменяя умножение сложением.')
lvl_4.add(Task(text='2 * 5', answer='10'))
lvl_4.add(Task(text='4 * 3', answer='12'))
lvl_4.add(Task(text='7 * 4', answer='28'))
lvl_4.add(Task(text='9 * 3', answer='27'))

lvl_5 = Level(1, info='Сравнение + умножение!')
lvl_5.add(Task(text='Деление числа 35 на 4 даст остаток?', answer='3'))
lvl_5.add(Task(text='Если разделить 82 на 9, остаток будет ?', answer='1'))
lvl_5.add(Task(text="39 ÷ 8 = ?", answer="4, остаток 7", choice=['4, остаток 7', '5, остаток 6', '3, остаток 5']))
lvl_5.add(Task(text="27 ÷ 6 = ?", answer="4, остаток 3", choice=['4, остаток 3', '3, остаток 4', '5, остаток 2']))

lvl_6 = Level(1, info='Задачки!')
lvl_6.add(Task(text='На 5 лошадей сели по одному всаднику, сколько всего всадников?', answer='5'))
lvl_6.add(Task(text='После обеда на столе осталось 4 тарелки, ни на одной не осталось ни одной сосиски.'
                    ' Сколько всего сосисок на этих тарелках?', answer='0'))
lvl_6.add(Task(text='Если разделить 82 на 9, остаток будет ?', answer='1'))

lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='1 * 26', answer='26'))
lvl_7.add(Task(text='0 * (21 - 8)', answer='0'))
lvl_7.add(Task(text='17 + 80 + 3', answer='100'))
lvl_7.add(Task(text='9 * 3', answer='27'))

lvl_8 = Level(1, info='еще на остаток')
lvl_8.add(Task(text="27 ÷ 6 = ?", answer="4, остаток 3", choice=['4, остаток 3', '3, остаток 4', '5, остаток 2']))
lvl_8.add(Task(text="39 ÷ 8 = ?", answer="4, остаток 7", choice=['4, остаток 7', '5, остаток 6', '3, остаток 5']))
lvl_8.add(Task(text="52 ÷ 9 = ?", answer="5, остаток 7", choice=['5, остаток 7', '6, остаток 5', '4, остаток 8']))


lvl_9 = Level(1, info='Найди значение выражения 65 - b')
lvl_9.add(Task(text='Где b = 65.', answer='0'))
lvl_9.add(Task(text='А если b = 20?', answer='45'))
lvl_9.add(Task(text='Если разделить 35 на 8, останется остаток?', answer='3'))


lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Деление!')
lvl_10.add(Task(text="39 ÷ 8 = ?", answer="4, остаток 7", choice=['4, остаток 7', '5, остаток 6', '3, остаток 5']))
lvl_10.add(Task(text="52 ÷ 9 = ?", answer="5, остаток 7", choice=['5, остаток 7', '6, остаток 5', '4, остаток 8']))
lvl_10.add(Task(text='7 * 4', answer='28'))
lvl_10.add(Task(text='9 * 3', answer='27'))
lvl_10.add(Task(text='4 * 3', answer='12'))
lvl_10.add(Task(text='7 * 4', answer='28'))
lvl_10.add(Task(text='9 * 3', answer='27'))
lvl_10.add(Task(text="Мария собрала 64 яблока. Она хочет упаковать их в коробки по 5 яблок. Сколько коробок ей понадобится?", answer="12, остаток 4", choice=['12, остаток 4', '11, остаток 3', '13, остаток 2']))
lvl_10.add(Task(text="В мешке было 110 монет. Если их равномерно разделить между 8 друзьями, сколько монет получит каждый друг? (с остатком)", answer="13, остаток 6", choice=['13, остаток 6', '12, остаток 5', '14, остаток 4']))
lvl_10.add(Task(text="На поле было 77 овец. Если их разделить на загоны по 10 овец, сколько овец останется в последнем загоне?", answer="7", choice=['7', '8', '6']))


topic_8.add_level(lvl_1)
topic_8.add_level(lvl_2)
topic_8.add_level(lvl_3)
topic_8.add_level(lvl_4)
topic_8.add_level(lvl_5)
topic_8.add_level(lvl_6)
topic_8.add_level(lvl_7)
topic_8.add_level(lvl_8)
topic_8.add_level(lvl_9)
topic_8.add_level(lvl_10)
year_3.add_level(topic_8)


topic_9 = Topic('Нумерация от 100 до 1000')

lvl_1 = Level(1, info='Привет! Давай посчитаем')
lvl_1.add(Task(text="Чему равно число, следующее за 750?", answer="751"))
lvl_1.add(Task(text="Чему равно число, следующее перед 950?", answer="949"))
lvl_1.add(Task(text="Чему равно число, следующее за 999?", answer="1000"))

lvl_2 = Level(1, info='Ещё немного примеров!')
lvl_2.add(Task(text='43 - (20 - 7) + 15', answer='45'))
lvl_2.add(Task(text='21 : 7 * 9', answer='27'))
lvl_2.add(Task(text='60 : (4 + 6) * 3', answer='18'))

lvl_3 = Level(1, info='Бонусная задача на логику!')
lvl_3.add(Task(text='Масса одного котёнка и одного щенка вместе равна 8 кг. А трёх щенков и двух котят 22 кг. '
                    'Сколько весит щенок?', answer='6'))

lvl_4 = Level(1, info='Еще на нумерацию.')
lvl_4.add(Task(text='Найди разность между числами 700 и 600.', answer='100'))
lvl_4.add(Task(text='43 * х = 43 : х', answer='1'))
lvl_4.add(Task(text="Какое число перед 600?", answer="599"))
lvl_4.add(Task(text="Какое число после 800?", answer="801"))
lvl_4.add(Task(text="Какое число перед 999?", answer="998"))

lvl_5 = Level(1, info='Проверь выражения и напиши Верно или Неверно')
lvl_5.add(Task(text='4 * 7 + 4 = 4 * 8', answer='Верно', choice=['Верно', "Неверно"]))
lvl_5.add(Task(text='27 : 3 < 10', answer='Верно', choice=['Верно', "Неверно"]))
lvl_5.add(Task(text='48 + (14 - 12) > 50', answer='Неверно', choice=['Верно', "Неверно"]))

lvl_6 = Level(1, info='еще чучуть!')
lvl_6.add(Task(text='Если из числа 900 вычесть 300, какое число получится?', answer='600'))
lvl_6.add(Task(text='Сколько десятков содержится в числе 360?', answer='36'))
lvl_6.add(Task(text='Если к числу 400 прибавить 100, какое число получится?', answer='500'))

lvl_7 = Level(1, info='Примеры!')
lvl_7.add(Task(text='(50 - 38) : 4', answer='3'))
lvl_7.add(Task(text='24 : 4', answer='6'))
lvl_7.add(Task(text='36 : 6', answer='6'))

lvl_8 = Level(1, info='Устные задачи')
lvl_8.add(Task(text='В куске 20 м. ткани. На каждый костюм необходимо 3 м, можно ли сшить 6 таких?', answer='Да',
               choice=['Да', 'Нет']))
lvl_8.add(Task(text='А 7 таких костюмов получится сшить?', answer='Нет', choice=['Да', 'Нет']))
lvl_8.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))

lvl_9 = Level(1, info='осталось совсем чучуть')
lvl_9.add(Task(text='Какое число получится, если к числу 250 прибавить 150?', answer='400'))
lvl_9.add(Task(text='Найди разницу между числами 800 и 450.', answer='350'))
lvl_9.add(Task(text='Выпиши пропущенные числа в последовательности: 100, 110, ___, 130, 140', answer='120'))
lvl_9.add(Task(text='Какое число находится между 500 и 600?', answer='550'))

lvl_10 = Level(1, info='Закрепим пройденное!', style='test', time=60, topic='Нумерация от 100 до 1000')
lvl_10.add(Task(text='Выпиши пропущенные числа в последовательности: 100, 110, ___, 130, 140', answer='120'))
lvl_10.add(Task(text='Какое число находится между 500 и 600?', answer='550'))
lvl_10.add(Task(text='Сколько десятков содержится в числе 360?', answer='36'))
lvl_10.add(Task(text='Если к числу 400 прибавить 100, какое число получится?', answer='500'))
lvl_10.add(Task(text='Какое число находится между 300 и 400?', answer='350'))
lvl_10.add(Task(text='Если от числа 500 отнять 300, то сколько получится?', answer='200'))

topic_9.add_level(lvl_1)
topic_9.add_level(lvl_2)
topic_9.add_level(lvl_3)
topic_9.add_level(lvl_4)
topic_9.add_level(lvl_5)
topic_9.add_level(lvl_6)
topic_9.add_level(lvl_7)
topic_9.add_level(lvl_8)
topic_9.add_level(lvl_9)
topic_9.add_level(lvl_10)
year_3.add_level(topic_9)


topic_10 = Topic('Еденицы массы.')

lvl_1 = Level(1, info='Привет! Задачки')
lvl_1.add(Task(text='Коля взвесил яблоко на весах и получил, что его масса составляет 150 грамм. Сколько килограммов весит это яблоко?', answer='0,15'))
lvl_1.add(Task(text='На ларьке продаются помидоры. Если 1 кг помидоров стоит 80 рублей, то сколько будет стоить полкилограмма помидоров?', answer='40'))
lvl_1.add(Task(text='В школьной столовой разливают молоко по 0,2 литра на каждую порцию. Сколько литров молока нужно для 5 порций?', answer='1'))

lvl_2 = Level(1, info='давай еще задачи')
lvl_2.add(Task(text=' Какой предмет имеет меньшую массу: 3 кг 500 г или 4 кг 200 г?', answer='3,5'))
lvl_2.add(Task(text='Если масса книги составляет 750 граммов, а масса тетради - 200 граммов, то сколько граммов весит их вместе?', answer='950'))
lvl_2.add(Task(text='В школьной столовой разливают молоко по 0,2 литра на каждую порцию. Сколько литров молока нужно для 5 порций?', answer='1'))


lvl_3 = Level(1, info='переведи еденицы в граммы ')
lvl_3.add(Task(text='Сколько граммов в 3 килограммах?', answer='3000'))
lvl_3.add(Task(text='Если утяжеление весит 7 килограммов, то сколько это граммов?', answer='7000'))
lvl_3.add(Task(text="Сколько килограммов в одной тонне?", answer="1000", choice=['500', '1000', '1500']))

lvl_4 = Level(1, info='Примеры!')
lvl_4.add(Task(text="Сколько килограммов в одной тонне?", answer="1000", choice=['500', '1000', '1500']))
lvl_4.add(Task(text="Сколько граммов в одной центнере?", answer="10000", choice=['5000', '10000', '15000']))
lvl_4.add(Task(text='Сколько граммов в 3 килограммах?', answer='3000'))


lvl_5 = Level(1, info='а такие задачки на перевод ')
lvl_5.add(Task(text='Если ученик сдает вес 2 килограмма, то сколько это граммов?', answer='2000'))
lvl_5.add(Task(text='Сумка весит 8 килограммов. Сколько это граммов?', answer='8000'))
lvl_5.add(Task(text='Сколько граммов в 3 килограммах?', answer='3000'))


lvl_6 = Level(1, info='примеры')
lvl_6.add(Task(text='Где b = 65.', answer='0'))
lvl_6.add(Task(text='А если b = 20?', answer='45'))
lvl_6.add(Task(text='Если разделить 35 на 8, останется остаток?', answer='3'))

lvl_7 = Level(1, info='примеры')
lvl_7.add(Task(text='Сколько дециметров в 2 метрах?', answer="20"))
lvl_7.add(Task(text='0 : 24', answer='0'))
lvl_7.add(Task(text='100 - (6 * 9 + 64 : 8) : 2 * 3', answer='7'))

lvl_8 = Level(1, info='Устные задачи')
lvl_8.add(Task(text='Если мешок с песком весит 15 килограммов, то сколько это граммов?', answer='15000'))
lvl_8.add(Task(text='Если яблоки весят 6 килограммов, то сколько это граммов?', answer='6000'))
lvl_8.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))

lvl_9 = Level(1, info='Реши уравнения')
lvl_9.add(Task(text='х : 2 + 21 = 31', answer='5'))
lvl_9.add(Task(text='х * 7 - 6 = 1', answer='1'))
lvl_9.add(Task(text='у * 5 = 20', answer='4'))


lvl_10 = Level(1, info='Закрепим пройденное!', style='final_test', time=120, topic='Конец третьего класса! Удачи.')
lvl_10.add(Task(text='Если мешок с песком весит 15 килограммов, то сколько это граммов?', answer='15000'))
lvl_10.add(Task(text='Если яблоки весят 6 килограммов, то сколько это граммов?', answer='6000'))
lvl_10.add(Task(text='Найди длину стороны квадрата, если его периметр 24 см.', answer='6'))
lvl_10.add(Task(text='Коля взвесил яблоко на весах и получил, что его масса составляет 150 грамм. Сколько килограммов весит это яблоко?', answer='0,15'))
lvl_10.add(Task(text='На ларьке продаются помидоры. Если 1 кг помидоров стоит 80 рублей, то сколько будет стоить полкилограмма помидоров?', answer='40'))
lvl_10.add(Task(text='В школьной столовой разливают молоко по 0,2 литра на каждую порцию. Сколько литров молока нужно для 5 порций?', answer='1'))
lvl_10.add(Task(text='0 : 3', answer='0'))
lvl_10.add(Task(text='0 : 24', answer='0'))
lvl_10.add(Task(text='100 - (6 * 9 + 64 : 8) : 2 * 3', answer='7'))
lvl_10.add(Task(text='75 - х = 75', answer='0'))
lvl_10.add(Task(text='4 + х = 84', answer='80'))
lvl_10.add(Task(text='89 - х = 0', answer='89'))
lvl_10.add(Task(text="26 * 1 =", answer="26"))
lvl_10.add(Task(text="9 * 1 =", answer="9"))
lvl_10.add(Task(text="14 * 1 =", answer="14"))
lvl_10.add(Task(text="41 * 0 =", answer="0"))
lvl_10.add(Task(text="27 * 0 =", answer="0"))
lvl_10.add(Task(text="13 * 0 =", answer="0"))
lvl_10.add(Task(text='реши вот этот пример в несколько действий', answer='79', image='pic/52.jpg'))
lvl_10.add(Task(text="1 + 34 - 32 =", answer="3"))
lvl_10.add(Task(text="7 - 6 + 29 =", answer="30"))
lvl_10.add(Task(text="1 + 34 - 32 =", answer="3"))
lvl_10.add(Task(text='6 : 2', answer='3', image='pic/126.jpg'))
lvl_10.add(Task(text='10 : 2', answer='5', image='pic/127.jpg'))
lvl_10.add(Task(text='8 : 4', answer='2', image='pic/128.jpg'))


topic_10.add_level(lvl_1)
topic_10.add_level(lvl_2)
topic_10.add_level(lvl_3)
topic_10.add_level(lvl_4)
topic_10.add_level(lvl_5)
topic_10.add_level(lvl_6)
topic_10.add_level(lvl_7)
topic_10.add_level(lvl_8)
topic_10.add_level(lvl_9)
topic_10.add_level(lvl_10)
year_3.add_level(topic_10)


