import commands


def start_message(message):
    commands.bot.send_message(message.chat.id, "Возможные команды:")
    commands.bot.send_message(message.chat.id, "/all")
    commands.bot.send_message(message.chat.id, "/find")
    commands.bot.send_message(message.chat.id, "/update")
    commands.bot.send_message(message.chat.id, "/insert")
    commands.bot.send_message(message.chat.id, "/delete")
    commands.bot.send_message(message.chat.id, "/help")


def help_message(message):
    commands.bot.send_message(message.chat.id, "Возможные команды и их значение:")
    commands.bot.send_message(message.chat.id, "/all  - показ имеющихся в наличии мониторов")
    commands.bot.send_message(message.chat.id, "/find - поиск позиции по ключевому слову")
    commands.bot.send_message(message.chat.id, "/update - обновление или добавление информации")
    commands.bot.send_message(message.chat.id, "/insert - добавление новой позиции")
    commands.bot.send_message(message.chat.id, "/delete - удаление поиции")
    commands.bot.send_message(message.chat.id, "/hidden - скрытые команды")


def hidden(message):
    commands.bot.send_message(message.chat.id, "/show_all_deleted  - показ удаленных позиций")
    commands.bot.send_message(message.chat.id, "/show_all_with_deleted - показ позиций имеющихся и удаленных")

