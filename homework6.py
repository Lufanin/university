my_dict = {'Дмитрий': 1995, 'Антон': 1990,  'Юрий': 2000, 'Валера': 1993}
print('Мои друзья: ' + str(my_dict))
print('Год рождения Дмитрия: '+ str(my_dict['Дмитрий']))
a = my_dict.pop('Валера')
print('Удаленное Имя: ' + str(my_dict.get('Валера')))
print('Год рождения Валеры : '+ str(a))
my_dict.update({'Михаил': 1998,
                'Петр': 1994})
del my_dict['Юрий']
print('Мои друзья: ' + str(my_dict))
print()
print()
my_set_={1, 1, True, True, 'Now', 'Now', 5.5, 5.5,(8, 9, True),(8, 9, True)}
print('Set:' + str(my_set_))
my_set_.add(7) #каждое новое значение добавляю по одному т.к. программа ругается если добавлять оба за раз
my_set_.add(9)
my_set_.discard(1) #discard удобен тем что не вызывает ошибок при удалении, даже если не найдет нужный ключ
print('Modified set:' + str(my_set_))
