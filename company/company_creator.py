class Task:
    def __init__(self, text='', choice=None, answer='', image=''):
        self.task, self.choice, self.answer, self.image = text, choice, answer, image

    def check_answer(self, answer):
        return self.answer == answer


class Level:
    def __init__(self, num=0, topic='', style='base', time=0, class_num=0, info=''):
        self.tasks = []  # Переносим определение списка сюда
        if style == 'base':
            self.time = None
            self.name = f'{info}'
        elif style == 'test':
            self.time = "20:00"
            self.name = f'Тест на тему {topic}, даётся {self.time} минут, удачи!'
            self.text = 'Пройди этот тест для открытия следующего блока заданий! Проиграешь трижды и тема сбросится!'
        elif style == 'final_test':
            self.time = "30:00"
            self.name = f'Контрольная работа за {class_num} класс, даётся {self.time} минут, удачи!'
            self.text = ('Ты шел(а) к этому очень долго! Пришло время закончить с этим классом, здесь встретятся задачи'
                         'на все темы этого года, попыток не ограниченное количество!')

    def add(self, task):
        self.tasks.append(task)


class Topic:
    def __init__(self, name=''):
        self.levels = []  # Переносим определение списка сюда
        self.name = name

    def add_level(self, lvl):
        self.levels.append(lvl)


class Class:
    def __init__(self, num=1):
        self.topics = []  # Переносим определение списка сюда
        self.number = num

    def add_level(self, topic):
        self.topics.append(topic)