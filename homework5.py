immutable_var=( 2.2, 'Hello, world!', True,1)
print('immutable_var: ' + str(immutable_var))
#immutable_var[1]= 3 # эту строчку поставил под комментарий, это попытка изменить кортеж, но его нельзя изменить
#immutable_var[2]= False (TypeError: 'tuple' object does not support item assignment)
mutable_list=[2.2,False,'Say', 300]
print('mutable_list: ' + str(mutable_list))