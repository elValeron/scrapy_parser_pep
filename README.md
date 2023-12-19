# [Парсер PEP Python](https://github.com/elValeron/scrapy_parser_pep)

# Описание: 
    - Парсер PEP позволяет отслеживать актуальные статусы предложений по развитию, и вести учет общего кол-ва предложений в каждом статусе.
    - При использовании сервиса формируется два файла:
        ```
        - Список PEP с номером, именем и статусом формируется в файл с префиксом pep_ 
        - сводка по статусам формируется в файл с префиксом status_summary формируется    
        ```

# Стэк: 
Сервис реализован на языке программирования Python 3.9 с использованием библиотеки Scrapy


1. ### Перед началом работы:
    - Cоздайте директорию в которой будет хранится проект
        
        - Перейдите в каталог, в котором хранится проект, командой:
            ```
            - cd <dir_name>/
            ```
        - Склонируйте репозиторий командой:
            ```
            - git clone https://github.com/elValeron/scrapy_parser_pep
            ```
        - Создайте и активируйте виртуальное окружение:
            ```
            - python3.9 -m venv venv - Создание виртуального окружения
            - source venv/bin/activate - Для Linux/Mac
            - source venv/Scripts/activate - Для Win 
            ```
        - Обновите pip и устанвите зависимости
            ```
            - pip install --upgrade pip - обновить pip
            - pip install -r requirements.txt
            ```
        
2. ### Работа с приложением: 
    - Для начала работы с приложением:
        - Перейдите в корневую директорию:
            ```
            - cd <dir_name>/pep_parse
            ```
        - Для вызова списка команд введите:
            ```
            - scrapy -h
            ```
        - Для запуска сервиса воспользуйтесь командой:
            ```
            - scrapy crawl pep

            ```
            - После чего будет сформировано два файла в директории results/: 
                - с префиксом pep_:
                ```
                - number,name,status
                - 1,PEP Purpose and Guidelines,Active
                - 8,Style Guide for Python Code,Active
                - 7,Style Guide for C Code,Active
                - 5,Guidelines for Language Evolution,Superseded
                ```
                - с префиксом status_summary_:
                ```
                Status,Count
                Active,32
                Superseded,23
                Withdrawn,57
                ```

Автор [Балашов Валерий](https://github.com/elValeron/)