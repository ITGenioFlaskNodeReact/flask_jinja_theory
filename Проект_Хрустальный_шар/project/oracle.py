import random


predictions = ['Сегодня будешь бодрым', 'Поражен скукой', 'Не выспишься', 'Потеряешь волшебный шар', 'Предсказания закончились', 'Влюбишься', '...']
results = ['Много сделаешь', 'Объешся', 'Уснешь днем', 'Доделаешь проект', 'Купишь сладкого', 'Напишешь стихотворение', 'Объешься груш', '...']
mottos = ['Как рыба в воде', 'За честь и отвагу', 'Я лучше всех', 'Какой девиз?', 'Мычи или рычи', 'Не устану бить в баклуши', 'Когда рак на горе свистнет', '...']
beings = ['Милый гном', 'Эльф без стрел', 'Дварф в бассейне', 'Человек-не-паук', 'Малыш', 'Конь в пальто', 'Кот (не) Баюн', 'Пушкин без бакенбард', '...']


def get_oracle():
    global predictions, results, mottos, beings
    
    oracle = {}
    oracle['Предсказание'] = random.choice(predictions)
    oracle['К чему это приведет'] = random.choice(results)
    oracle['Девиз'] = random.choice(mottos)
    oracle['Кто ты'] = random.choice(beings)

    return oracle

def get_oracle_color(oracle):
    secret_num = 0
    for k, v in oracle.items():
        secret_num += len(k) + len(v)
    random_num = random.randint(100000, 111111)
    return str(secret_num % 10 * random_num)

