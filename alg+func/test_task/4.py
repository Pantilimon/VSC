def multi_table(n): 
    print(' ', end=' ') # тот самый отступ в углу
    for i in range(1, n+1): # Первая строка (продолжение отступа)
        print(i, end=' ')
    print(end='\n')
    for i in range(1, n+1):  # первый столбец
        print(i, end=' ')
        for j in range(1, n+1): # Заполнение внутренности таблицы
            print(i*j, end=' ')
        print(end='\n')

#Очень много костылей, гараздно проще было бы сделать двумернный массив из массивов с одним элементом (получается трехмерный), но тогда был бы некрасивый вывод
# multi_table(5)
