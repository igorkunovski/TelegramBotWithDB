# TelegramBot With DB support

Телеграм_бот **@data911_bot** (https://t.me/data911_bot) работает с поддержкой базы данных **main.db** с 
помощью SQLite. 

Бот может запрашивать и выводить информацию, изменять и удалять информацию в базе данных.

"Возможные команды и их значение:
- /all  - показ имеющихся в наличии позиций (мониторов в данном случае)
- /find - поиск позиции по ключевому слову
- /update - обновление или добавление информации
- /insert - добавление новой позиции
- /delete - удаление поиции
- /hidden - скрытые команды

База данных состоит из 2-х таблиц. 

- **inventory** содержит актуальные (условно имеющиеся) позиции. Если позицию удалить из таблицы inventory, 
то она попадет во вторую таблицу: **deleted**. Это сделано для безопасности данных.

Так называемые скрытые команды:
- /show_deleted  - позволяет посмотреть все удаленные позиции 
- /show_all_with_deleted  - выводятся актуальные и удаленные позиции через FULL JOIN. 

# Telegram bot with data base support

Telegram_bot **@data911_bot** (https://t.me/data911_bot) works with database support **main.db** with
using SQLite.

The bot can query and display information, change and delete information in the database.

"Possible commands and their meaning:
- /all - display available positions (monitors in this case)
- /find - search for a position by keyword
- /update - update or add information
- /insert - adding a new position
- /delete - delete position
- /hidden - hidden commands

The database consists of 2 tables.

- **inventory** contains current (conditionally available) positions. If the item is removed from the 
inventory table, then it will end up in the second table: 
- **deleted**. This is done for data security.

The so-called hidden commands:
- /show_deleted  - allows you to see all deleted items
- /show_all_with_deleted - shows current and deleted positions via FULL JOIN.
