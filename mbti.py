import requests
import random
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd

class MBTI():
    def __init__(self):
        pass

    def get_relationship(a, b):
        relationship = [
            ['', 'INFP', 'ENFP', 'INFJ', 'ENFJ', 'INTJ', 'ENTJ', 'INTP', 'ENTP', 'ISFP', 'ESFP', 'ISTP', 'ESTP', 'ISFJ', 'ESFJ', 'ISTJ', 'ESTJ'],
            ['INFP', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.'],
            ['ENFP', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.'],
            ['INFJ', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.'],
            ['ENFJ', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.'],
            ['INTJ', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.'],
            ['ENTJ', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!'],
            ['INTP', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Ты моя судьба!'],
            ['ENTP', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.'],
            ['ISFP', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!'],
            ['ESFP', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!'],
            ['ISTP', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'П лохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!'],
            ['ESTP', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!'],
            ['ISFJ', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!'],
            ['ESFJ', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!'],
            ['ISTJ', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпадения!', 'Не худший вариант, но и не лучший.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!'],
            ['ESTJ', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Плохая совместимость! Подумай еще раз.', 'Не худший вариант, но и не лучший.', 'Есть несовпадения, но есть и совпад ения!', 'Ты моя судьба!', 'Не худший вариант, но и не лучший.', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Ты моя судьба!', 'Есть несовпадения, но есть и совпадения!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!', 'Может стать очень хорошими отношениями!']
        ]
        columns = relationship[0]
        data = relationship[1:]
        df = pd.DataFrame(data, columns=columns)
        df.set_index('', inplace=True)
        try:
            return df.loc[a.upper(), b.upper()]
        except KeyError:
            return "Не существующий тип"

    def get_test(a):
        test = ["Я регулярно завожу новых друзей.", "Я трачу значительное время на изучение различных интересов.", "Когда вижу, как кто-то плачет, мне тоже хочется заплакать.", "Я обычно готовлю несколько запасных планов на случай, если что-то пойдет не так.", "Я сохраняю спокойствие даже в стрессовых ситуациях.", "На вечеринках я предпочитаю общаться с теми, кого уже знаю, а не знакомиться с новыми людьми.", "Я предпочитаю завершить один проект, прежде чем начинать другой.", "Я очень сентиментален.", "Мне нравится планировать дела с помощью расписаний или списков.", "Я часто сомневаюсь в своих способностях из-за мелких ошибок.", "Мне не трудно подойти к человеку, который мне интересен, и начать разговор.", "Меня не очень интересует обсуждение различных интерпретаций произведений искусства.", "Я предпочитаю следовать разуму, а не эмоциям.", "Я предпочитаю действовать спонтанно, а не планировать свой день.", "Я не беспокоюсь о том, как я выгляжу в глазах других.", "Мне нравится участвовать в групповых мероприятиях.", "Я люблю книги и фильмы, которые позволяют интерпретировать концовку по-своему.", "Я получаю больше удовлетворения от помощи другим, чем от собственных успехов.", "У меня так много интересов, что я иногда не знаю, с чего начать.", "Я часто беспокоюсь о том, что что-то пойдет не так.", "Я стараюсь избегать лидерских ролей в группах.", "Я считаю, что у меня почти нет художественного таланта.", "Я думаю, что если бы люди больше ценили разум, мир был бы лучше.", "Я предпочитаю сначала закончить домашние дела, а потом отдыхать.", "Мне нравится наблюдать за спорами других людей.", "Я стараюсь не привлекать к себе внимание.", "Мои эмоции часто меняются.", "Я раздражаюсь, когда вижу, что кто-то не так эффективен, как я.", "Я часто откладываю дела до последнего момента.", "Я нахожу вопросы о загробной жизни интересными.", "Я предпочитаю проводить время с другими, чем быть одному.", "Меня не интересуют теоретические обсуждения, и я считаю их скучными.", "Я легко могу понять людей с совершенно другим опытом.", "Я часто откладываю принятие решений до последнего момента.", "Я не пересматриваю уже принятые решения.", "Я предпочитаю проводить время на вечеринках и мероприятиях, чем быть одному.", "Мне нравится посещать художественные выставки.", "Мне бывает трудно понять чувства других людей.", "Мне нравится планировать свои дела на каждый день.", "Я почти никогда не чувствую тревоги.", "Я стараюсь избегать телефонных звонков.", "Я трачу много времени, чтобы понять мнение, сильно отличающееся от моего.", "Я обычно первым предлагаю встретиться с друзьями.", "Когда планы идут не так, я стараюсь как можно быстрее вернуться к ним.", "Я часто сожалею о своих прошлых ошибках.", "Я не задумываюсь о смысле жизни и существования.", "Я скорее поддаюсь эмоциям, чем контролирую их.", "Я стараюсь поддержать репутацию других, даже если они неправы.", "Я предпочитаю работать по плану, а не действовать спонтанно.", "Я беспокоюсь, что если кто-то высоко оценит меня, он может разочароваться позже.", "Я хочу работать в профессии, где могу проводить большую часть времени в одиночестве.", "Я считаю, что размышления о философских вопросах - это пустая трата времени.", "Я предпочитаю шумные и многолюдные места, чем тихие и уединенные.", "Я могу быстро распознать чувства других.", "Я часто чувствую себя подавленным.", "Я предпочитаю следовать процедурам и завершать задачи поэтапно.", "Меня интересуют спорные или провокационные темы.", "Если я считаю, что кому-то другому эта возможность нужнее, я могу отказаться от нее.", "Мне трудно соблюдать сроки.", "Я уверен, что все пойдет так, как я хочу."]
        try:
            return test[a]
        except:
            return "Выход за пределы диапазона (0~59)"

    def get_info(a):
        try:
            soup = BeautifulSoup(requests.get(f"https://www.16personalities.com/ru/%D1%82%D0%B8%D0%BF-%D0%BB%D0%B8%D1%87%D0%BD%D0%BE%D1%81%D1%82%D0%B8-{a}").text, 'html.parser')
            nickname = soup.select_one('#main-app > main > header > div > h1 > span').get_text()
            description = html.fromstring(str(soup)).xpath('//*[@id="main-app"]/main/div[1]/div/article/p[1]/text()')[0]
            return {"mbti": a.upper(), "nickname": nickname, "description": description, "avatar": get_avatar(a.upper())}
        except:
            return "Не существующий mbti или неизвестная ошибка"

    def get_avatar(a):
        json = {
            "ENFJ": "https://i.ibb.co/6FKKSC6/enfj.png",
            "ENFP": "https://i.ibb.co/Xt6yZSJ/enfp.png",
            "ENTJ": "https://i.ibb.co/wgnJgJj/entj.png",
            "ENTP": "https://i.ibb.co/ZcwjtH6/entp.png",
            "ESFJ": "https://i.ibb.co/kSBVPQ5/esfj.png",
            "ESFP": "https://i.ibb.co/4JTJDg7/esfp.png",
            "ESTJ": "https://i.ibb.co/gDvLWP3/estj.png",
            "ESTP": "https://i.ibb.co/jbSKMdq/estp.png",
            "INFJ": "https://i.ibb.co/GtssndN/infj.png",
            "INFP": "https://i.ibb.co/q9WKtYW/infp.png",
            "INTJ": "https://i.ibb.co/Y7R0fk8/intj.png",
            "INTP": "https://i.ibb.co/XDx9Gn7/intp.png",
            "ISFJ": "https://i.ibb.co/GcN6RG9/isfj.png",
            "ISFP": "https://i.ibb.co/hsKLgVf/isfp.png",
            "ISTJ": "https://i.ibb.co/bH0q8vb/istj.png",
            "ISTP": "https://i.ibb.co/DR1372g/istp.png"
        }
        if a in json:
            return json[a]
        else:
            return "Не существующий тип"

    def get_result(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60):
        json = {
            "questions": [
                {"text": "Я регулярно завожу новых друзей.", "answer": q1},
                {"text": "Я трачу значительное время на изучение различных интересов.", "answer": q2},
                {"text": "Когда вижу, как кто-то плачет, мне тоже хочется заплакать.", "answer": q3},
                {"text": "Я обычно готовлю несколько запасных планов на случай, если что-то пойдет не так.", "answer": q4},
                {"text": "Я сохраняю спокойствие даже в стрессовых ситуациях.", "answer": q5},
                {"text": "На вечеринках я предпочитаю общаться с теми, кого уже знаю, а не знакомиться с новыми людьми.", "answer": q6},
                {"text": "Я предпочитаю завершить один проект, прежде чем начинать другой.", "answer": q7},
                {"text": "Я очень сентиментален.", "answer": q8},
                {"text": "Мне нравится планировать дела с помощью расписаний или списков.", "answer": q9},
                {"text": "Я часто сомневаюсь в своих способностях из-за мелких ошибок.", "answer": q10},
                {"text": "Мне не трудно подойти к человеку, который мне интересен, и начать разговор.", "answer": q11},
                {"text": "Меня не очень интересует обсуждение различных интерпретаций произведений искусства.", "answer": q12},
                {"text": "Я предпочитаю следовать разуму, а не эмоциям.", "answer": q13},
                {"text": "Я предпочитаю действовать спонтанно, а не планировать свой день.", "answer": q14},
                {"text": "Я не беспокоюсь о том, как я выгляжу в глазах других.", "answer": q15},
                {"text": "Мне нравится участвовать в групповых мероприятиях.", "answer": q16},
                {"text": "Я люблю книги и фильмы, которые позволяют интерпретировать концовку по-своему.", "answer": q17},
                {"text": "Я получаю больше удовлетворения от помощи другим, чем от собственных успехов.", "answer": q18},
                {"text": "У меня так много интересов, что я иногда не знаю, с чего начать.", "answer": q19},
                {"text": "Я часто беспокоюсь о том, что что-то пойдет не так.", "answer": q20},
                {"text": "Я стараюсь избегать лидерских ролей в группах.", "answer": q21},
                {"text": "Я считаю, что у меня почти нет художественного таланта.", "answer": q22},
                {"text": "Я думаю, что если бы люди больше ценили разум, мир был бы лучше.", "answer": q23},
                {"text": "Я предпочитаю сначала закончить домашние дела, а потом отдыхать.", "answer": q24},
                {"text": "Мне нравится наблюдать за спорами других людей.", "answer": q25},
                {"text": "Я стараюсь не привлекать к себе внимание.", "answer": q26},
                {"text": "Мои эмоции часто меняются.", "answer": q27},
                {"text": "Я раздражаюсь, когда вижу, что кто-то не так эффективен, как я.", "answer": q28},
                {"text": "Я часто откладываю дела до последнего момента.", "answer": q29},
                {"text": "Я нахожу вопросы о загробной жизни интересными.", "answer": q30},
                {"text": "Я предпочитаю проводить время с другими, чем быть одному.", "answer": q31},
                {"text": "Меня не интересуют теоретические обсуждения, и я считаю их скучными.", "answer": q32},
                {"text": "Я легко могу понять людей с совершенно другим опытом.", "answer": q33},
                {"text": "Я часто откладываю принятие решений до последнего момента.", "answer": q34},
                {"text": "Я не пересматриваю уже принятые решения.", "answer": q35},
                {"text": "Я предпочитаю проводить время на вечеринках и мероприятиях, чем быть одному.", "answer": q36},
                {"text": "Мне нравится посещать художественные выставки.", "answer": q37},
                {"text": "Мне бывает трудно понять чувства других людей.", "answer": q38},
                {"text": "Мне нравится планировать свои дела на каждый день.", "answer": q39},
                {"text": "Я почти никогда не чувствую тревоги.", "answer": q40},
                {"text": "Я стараюсь избегать телефонных звонков.", "answer": q41},
                {"text": "Я трачу много времени, чтобы понять мнение, сильно отличающееся от моего.", "answer": q42},
                {"text": "Я обычно первым предлагаю встретиться с друзьями.", "answer": q43},
                {"text": "Когда планы идут не так, я стараюсь как можно быстрее вернуться к ним.", "answer": q44},
                {"text": "Я часто сожалею о своих прошлых ошибках.", "answer": q45},
                {"text": "Я не задумываюсь о смысле жизни и существования.", "answer": q46},
                {"text": "Я скорее поддаюсь эмоциям, чем контролирую их.", "answer": q47},
                {"text": "Я стараюсь поддержать репутацию других, даже если они неправы.", "answer": q48},
                {"text": "Я предпочитаю работать по плану, а не действовать спонтанно.", "answer": q49},
                {"text": "Я беспокоюсь, что если кто-то высоко оценит меня, он может разочароваться позже.", "answer": q50},
                {"text": "Я хочу работать в профессии, где могу проводить большую часть времени в одиночестве.", "answer": q51},
                {"text": "Я считаю, что размышления о философских вопросах - это пустая трата времени.", "answer": q52},
                {"text": "Я предпочитаю шумные и многолюдные места, чем тихие и уединенные.", "answer": q53},
                {"text": "Я могу быстро распознать чувства других.", "answer": q54},
                {"text": "Я часто чувствую себя подавленным.", "answer": q55},
                {"text": "Я предпочитаю следовать процедурам и завершать задачи поэтапно.", "answer": q56},
                {"text": "Меня интересуют спорные или провокационные темы.", "answer": q57},
                {"text": "Если я считаю, что кому-то другому эта возможность нужнее, я могу отказаться от нее.", "answer": q58},
                {"text": "Мне трудно соблюдать сроки.", "answer": q59},
                {"text": "Я уверен, что все пойдет так, как я хочу.", "answer": q60}
            ],
            "gender": "",
            "inviteCode": "",
            "teamInviteKey": "",
            "extraData": []
        }
        result = requests.post("https://www.16personalities.com/ru/%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C-%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82", json=json)
        session = requests.get("https://www.16personalities.com/api/session", cookies=result.cookies).json()
        soup = BeautifulSoup(requests.get(result.json()['redirect']).text, 'html.parser')
        nickname = soup.select_one('#main-app > main > header > div > h1 > span').get_text()
        description = html.fromstring(str(soup)).xpath('//*[@id="main-app"]/main/div[1]/div/article/p[1]/text()')[0]
        mbti = session['user']['publicUrl'].split("/")[4].upper()
        url = f"https://www.16personalities.com/ru/%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82/{mbti.lower()}/x/{session['user']['publicUrl'].split('/')[6]}"
        return {"mbti": mbti, "nickname": nickname, "description": description, "url": url, "avatar": get_avatar(mbti.split("-")[0])}