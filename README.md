# GraphLib
####Авторы: Овчинников Павел КН-202, Яскевич Михаил КН-202.
####В этом проекте вы можете найти структуры данных для представления графа и некоторые наиболее известные алгоритмы поиска пути в графе.
####Вы можете использовать main.py для того, чтобы:
1) Найти пути в графе от одной вершины до всех или путь от одной вершины до конкретной вершины.
2) Сделать новый отчет о сравнении алгоритмов по использованию времени и памяти, основанный на случайно сгенерированных данных.
3) Запустить все модульные тесты в проекте.

####Примеры запуска
####1) Help для всех типов запуска
...\GraphLib>python main.py -h
####2) Help для запуска типа find_path (поиск пути)
...\GraphLib>python main.py find_path -h
####3) Help для запуска типа report (отчет)
...\GraphLib>python main.py report -h
####4) Help для запуска типа test
...\GraphLib>python main.py test -h

####Заранее подготовленные графы в виде txt файлов хранятся в GraphLib\resources\graphs
####Пример использования графа из ресурсов:
...\GraphLib>python main.py find_path GraphLib\resources\graphs\graph1.txt al dijkstra
####Более подробная информация об аргументах находится в help для конкретного типа запуска
