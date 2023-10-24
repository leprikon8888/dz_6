"""Task 7
Напишіть скрипт для очищення тексту від HTML-тегів.
Також необхідно врахувати кілька особливостей:
- крім одинарних тегів є парні теги, наприклад <div> </div>, тобто. перший тег відкриває, а другий закриває.
- тег у собі може містити купу додаткової інформації. Наприклад <div id="rcnt" style="clear:both;position:relative;zoom:1">"""
txt = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Моя веб-страница</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
    <header>
        <h1>Добро пожаловать на мою веб-страницу</h1>
        <nav>
            <ul>
                <li><a href="#section1">Раздел 1</a></li>
                <li><a href="#section2">Раздел 2</a></li>
                <li><a href="#section3">Раздел 3</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="section1">
            <h2>Раздел 1</h2>
            <p>Это содержимое раздела 1.</p>
        </section>
        <section id="section2">
            <h2>Раздел 2</h2>
            <p>Это содержимое раздела 2.</p>
        </section>
        <section id="section3">
            <h2>Раздел 3</h2>
            <p>Это содержимое раздела 3.</p>
        </section>
    </main>
    <footer>
        <p>© 2023 Моя веб-страница</p>
    </footer>
</body>
</html>
"""
while '<' in txt:
    start = txt.find('<')
    end = txt.find('>')

    buffer = txt[start:end+1]
    txt = txt.replace(buffer, '')

print(txt)

