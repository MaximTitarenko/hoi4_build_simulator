# =====================================================
# универсальный симулятор строительства в HOI4 
# (Python 3.x + matplotlib) 
# =====================================================

# источники при составлении:
    # - HOI4, версия: 1.4.x (x=0,1,2)
    # - http://www.hoi4wiki.com

# repl.it:
    # - https://repl.it/K2Jy/latest
# =====================================================

from simulator import Cell, BuildSimulator, BuildSimMaxMilitary, BuildSimInfrEfficiency

# =====================================================
# ВВЕДИТЕ ВАШ КОД ЗДЕСЬ:
# =====================================================









# ----------------------------------------------------
# например: 
# (для активации строк с кодом - уберите знак '#' перед ними)
# (подробнее - см раздел "КОММЕНТАРИИ" файла "ГАЙД")
# ----------------------------------------------------
# мой_симулятор = BuildSimMaxMilitary('ЯПОНИЯ') # создание симулятора

# laws_timeline =  [  # тайминги изменения законов/технологий, влияющих на бонусы строительства и штраф ТНП
#                     [(1936, 3, 11), ['Свободная_торговля']], 
#                     [(1936, 6, 27), ['Строительство_1']], 
#                     [(1937, 4, 22), ['Строительство_2']], 
#                     [(1937, 12, 1), ['Военная_экономика']],
#                     [(1939, 4, 15), ['Строительство_3']], 
#                  ]

# infr_av = 5 # средняя инфраструктура
# civ_trade_av = 3 # среднее количество фабрик от торговли
# date_end = (1941, 12, 7) # дата принудительного завершения симуляции (год, месяц, день)

# мой_симулятор.find_mil_extremum(infr_av, laws_timeline, civ_trade_av, date_end)
# ----------------------------------------------------

# =====================================================
# ДРУГИЕ ПРИМЕРЫ:
# =====================================================

# список доступных стран (country_list):
# 'СССР', 'ГЕРМАНИЯ', 'ЯПОНИЯ', 'ИТАЛИЯ', 'ФРАНЦИЯ', 'США', 'ВБ'

# пустой пример - ничего не происходит
def example_0():
    pass

# график количества построенных заводов к определенной дате по набору количества построенных фабрик
def example_1():
    
    ussr_sim = BuildSimMaxMilitary('СССР') # создание симулятора
    
    civ_num_to_build_list = [0, 10, 20, 30] # список количества фабрик для постройки
    
    infr_av = 6 # средняя инфраструктура
    civ_trade_av = 10 # среднее количество фабрик от торговли
    date_end = (1941,1,1) # дата принудительного завершения симуляции (год, месяц, день)
    
    laws_timeline = [ # формат laws_timeline для определенной страны - из country_list - см *замечание в файле 'ГАЙД'
                      [(1936, 3, 11), ['Свободная_торговля']], 
                      [(1936, 6, 27), ['Строительство_1']], 
                      [(1937, 4, 22), ['Строительство_2']], 
                      [(1937, 12, 1), ['Военная_экономика']],
                      [(1939, 4, 15), ['Строительство_3']] 
                    ]
    
    # запуск приложения симулятора по заданным параметрам:    
    ussr_sim.visualize_efficiency(civ_num_to_build_list, infr_av, laws_timeline, civ_trade_av, date_end)

# график экстремума построенных заводов к определенной дате по числу построенных фабрик
def example_2():
    
    ussr_sim = BuildSimMaxMilitary('СССР') # создание симулятора
    
    infr_av = 6 # средняя инфраструктура
    civ_trade_av = 10 # среднее количество фабрик от торговли
    date_end = (1941,1,1) # дата принудительного завершения симуляции (год, месяц, день)
    
    laws_timeline = [ # формат laws_timeline для определенной страны - из country_list - см *замечание в файле 'ГАЙД'
                      [(1936, 3, 11), ['Свободная_торговля']], 
                      [(1936, 6, 27), ['Строительство_1']], 
                      [(1937, 4, 22), ['Строительство_2']], 
                      [(1937, 12, 1), ['Военная_экономика']],
                      [(1939, 4, 15), ['Строительство_3']] 
                    ]
    
    # запуск приложения симулятора по заданным параметрам:      
    ussr_sim.find_mil_extremum(infr_av, laws_timeline, civ_trade_av, date_end)

# график границы окупаемости строительства инфраструктуры для ячеек данной страны
def example_3():
    
    ger_sim = BuildSimInfrEfficiency('ГЕРМАНИЯ') # создание симулятора
    
    infr_up = 1 # поднятие уровня инфраструктуры, относительно которого оцениваем окупаемость

    laws_timeline = [ # формат laws_timeline для определенной страны - из country_list - см *замечание в файле 'ГАЙД'
                      [(1936, 3, 11), ['Свободная_торговля']], 
                      [(1936, 6, 27), ['Строительство_1']], 
                      [(1937, 4, 22), ['Строительство_2']], 
                      [(1937, 12, 1), ['Военная_экономика']],
                      [(1939, 4, 15), ['Строительство_3']] 
                    ]
    
    # запуск приложения симулятора по заданным параметрам:    
    ger_sim.visualize_equilibrium(infr_up, laws_timeline)

# определение - окупается ли строительство инфраструктуры в данной конкретной ячейке
def example_4():
    
    new_sim = BuildSimInfrEfficiency() # создание симулятора
    
    # создание ячейки, окупаемость которой будем оценивать:
    new_cell = Cell('Мозель', infrastructure=7, obj_available=11, country='ГЕРМАНИЯ') 
    
    infr_up = 1 # поднятие уровня инфраструктуры, относительно которого оцениваем окупаемость

    laws_timeline = [ # формат laws_timeline для неопределенной страны - см *замечание в файле 'ГАЙД'
                      [(1936, 1, 1), ['Ограниченный_призыв', 'Ограниченный_экспорт', 'Частичная_мобилизация']],
                      [(1936, 3, 11), ['Свободная_торговля']], 
                      [(1936, 6, 27), ['Строительство_1']], 
                      [(1937, 4, 22), ['Строительство_2']], 
                      [(1937, 12, 1), ['Военная_экономика']],
                      [(1939, 4, 15), ['Строительство_3']] 
                    ]
    
    # запуск приложения симулятора по заданным параметрам:  
    new_sim.is_cell_profitable(new_cell, infr_up, laws_timeline) 

# определение - окупается ли строительство инфраструктуры для какой-либо из ячеек в данной стране 
# демо-версия - см **замечание в файле 'ГАЙД' - работает только для ГЕРМАНИИ
def example_5():

    ger_sim = BuildSimInfrEfficiency('ГЕРМАНИЯ') # создание симулятора
    
    infr_up = 1 # поднятие уровня инфраструктуры, относительно которого оцениваем окупаемость

    laws_timeline = [ # формат laws_timeline для определенной страны - из country_list - см *замечание в файле 'ГАЙД'
                      [(1936, 3, 11), ['Свободная_торговля']], 
                      [(1936, 6, 27), ['Строительство_1']], 
                      [(1937, 4, 22), ['Строительство_2']], 
                      [(1937, 12, 1), ['Военная_экономика']],
                      [(1939, 4, 15), ['Строительство_3']] 
                    ]
                    
    # запуск приложения симулятора по заданным параметрам:  
    ger_sim.is_any_cell_profitable(infr_up, laws_timeline)

# симуляция строительства по произвольной очереди строительства
def example_6():
    
    BuildSimulator.printout = True # устанавливаем формат подробной печати событий в консоль
    
    ussr_sim = BuildSimulator('СССР') # создание симулятора
    
    civ_trade_av = 10 # среднее количество фабрик от торговли
    
    laws_timeline = [ # формат laws_timeline для определенной страны - из country_list - см *замечание в файле 'ГАЙД'
                      [(1936, 3, 11), ['Свободная_торговля']], 
                      [(1936, 6, 27), ['Строительство_1']], 
                      [(1937, 4, 22), ['Строительство_2']], 
                      [(1937, 12, 1), ['Военная_экономика']],
                      [(1939, 4, 15), ['Строительство_3']] 
                    ]
    
    # создание очереди стрительства:
    build_order = [['Москва', 'infr', 2], ['Харьков', 'civ', 3], ['Винтерфелл', 'mil', 4]] 
    
    # запуск приложения симулятора по заданным параметрам:  
    ussr_sim.build_sim(build_order, laws_timeline, civ_trade_av)
    
    BuildSimulator.printout = False # возвращаем формат краткой печати событий

# ----------------------------------------------------
# запуск примера:
# ----------------------------------------------------

example_0() # подставьте вместо '0' номер нужного вам примера

# =====================================================


