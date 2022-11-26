import commands


def start_message(message):
    commands.bot.send_message(message.chat.id, "Возможные команды:")
