import sqlite3
import telebot
import _token
import functions

bot = telebot.TeleBot(_token.API_TOKEN)
print("BOT is running")


def connect():
    con = sqlite3.connect('main.db')
    cursor = con.cursor()
    return cursor


def find_by_id(id):
    cursor = connect()
    cursor.execute("SELECT * FROM inventory "
                   "WHERE inventory.id="f'{id};')
    for result in cursor:
        return result


def update_deleted(id, producer, mark, size, resolution, price, comment):

    con = sqlite3.connect('main.db')
    cursor = con.cursor()

    id = id
    producer = producer
    mark = mark
    size = size
    resolution = resolution
    price = price
    comment = comment

    '''SQL command'''
    cursor.execute("INSERT INTO deleted (id, producer, mark, size, resolution, price, comment)"
                   "VALUES" + f'("{id}", "{producer}", "{mark}", {size}, "{resolution}", {price}, "{comment}");')
    con.commit()
    return


@bot.message_handler(commands=['start'])
def start_message(message):
    functions.start_message(message)


@bot.message_handler(commands=['all'])
def show_all(message):
    cursor = connect()
    cursor.execute('''SELECT * FROM inventory''')
    bot.send_message(message.chat.id, "| id | producer | mark | size | resolution | price | comment |")
    for result in cursor:
        bot.send_message(message.chat.id, f'{result}')


@bot.message_handler(commands=['show_all_deleted'])
def show_all(message):
    cursor = connect()
    cursor.execute('''SELECT * FROM deleted''')
    bot.send_message(message.chat.id, "| id | producer | mark | size | resolution | price | comment |")
    for result in cursor:
        bot.send_message(message.chat.id, f'{result}')


@bot.message_handler(commands=['show_all_with_deleted'])
def show_all(message):
    cursor = connect()
    cursor.execute("SELECT * FROM inventory "
                   "union SELECT * FROM deleted;")
    bot.send_message(message.chat.id, "| id | producer | mark | size | resolution | price | comment |")
    for result in cursor:
        bot.send_message(message.chat.id, f'{result}')


@bot.message_handler(commands=['find'])
def find(message):
    cursor = connect()
    cursor.execute('''SELECT * FROM inventory''')

    searched_list = str(message.text).split("/find")

    if len(searched_list) > 1 and searched_list[1] != "":
        bot.send_message(message.chat.id, "Found...")
        searched = searched_list[1].upper().replace(" ", "")
        for result in cursor:
            for item in result:
                if searched.upper() in str(item).upper():
                    bot.send_message(message.chat.id, f'{result}')
                    break
    else:
        bot.send_message(message.chat.id, "Формат команды /find Samsung")
    return


@bot.message_handler(commands=['update'])
def update(message):

    con = sqlite3.connect('main.db')
    cursor = con.cursor()

    update_list = str(message.text).split("/update")

    if len(update_list) > 1 and update_list[1] != "":
        update_data = update_list[1].split(",")

        if (update_data[0].split("=")[0]).replace(" ", "") == "id" and \
                (update_data[0].split("=")[1].replace(" ", "").isdigit()):

            id = int(update_data[0].split("=")[1].replace(" ", ""))
            col_name = update_data[1].split("=")[0].replace(" ", "")
            new_value = '"' + update_data[1].split("=")[1] + '"'

            '''SQL command'''
            cursor.execute("UPDATE inventory  "
                           "SET " + f'{col_name}={new_value} '
                                    "WHERE inventory.id="f'{id};')
            con.commit()
            bot.send_message(message.chat.id, f'Data updated : {find_by_id(id)}')

            return
        else:
            bot.send_message(message.chat.id, f'Data was not updated, please check command')
        return

    else:
        bot.send_message(message.chat.id, "Формат команды /update id=1, producer=LG")
        bot.send_message(message.chat.id, "| id | producer | mark | size | resolution | price | comment |")
    return


@bot.message_handler(commands=['insert'])
def update(message):

    con = sqlite3.connect('main.db')
    cursor = con.cursor()

    update_list = str(message.text).split("/insert")

    if len(update_list) > 1 and update_list[1] != "":
        update_data = update_list[1].split(",")
        if len(update_data) == 6:

            producer = update_data[0]
            mark = update_data[1]
            size = update_data[2]
            resolution = update_data[3]
            price = update_data[4]
            comment = update_data[5]

            '''SQL command'''
            cursor.execute("INSERT INTO inventory (producer, mark, size, resolution, price, comment)"
                           "VALUES" + f'("{producer}", "{mark}", {size}, "{resolution}", {price}, "{comment}");')
            con.commit()
            bot.send_message(message.chat.id, f'Successfully inserted')
            return
        else:
            bot.send_message(message.chat.id, f'я в ELSE if 2')
    else:
        bot.send_message(message.chat.id, "Формат команды /insert producer, mark, size, resolution, price, comment")
        bot.send_message(message.chat.id, "| id | producer | mark | size | resolution | price | comment |")
    return


@bot.message_handler(commands=['delete'])
def delete(message):

    searched_list = str(message.text).split("/delete")

    if len(searched_list) == 2 and searched_list[1] != "":

        if (searched_list[1].split("=")[0]).replace(" ", "") == "id" and \
                (searched_list[1].split("=")[1].replace(" ", "").isdigit()):
            id = int(searched_list[1].split("=")[1].replace(" ", ""))

            producer = find_by_id(id)[1]
            mark = find_by_id(id)[2]
            size = find_by_id(id)[3]
            resolution = find_by_id(id)[4]
            price = find_by_id(id)[5]
            comment = find_by_id(id)[6]

            update_deleted(id, producer, mark, size, resolution, price, comment)

            '''SQL'''
            con = sqlite3.connect('main.db')
            cursor = con.cursor()
            cursor.execute("DELETE FROM inventory "
                           "WHERE inventory.id="f'{id};')
            bot.send_message(message.chat.id, "Data Successfully deleted")

            con.commit()
    else:
        bot.send_message(message.chat.id, "Формат команды /delete id=1")
    return


@bot.message_handler(commands=['hidden'])
def hidden(message):
    functions.hidden(message)


@bot.message_handler(commands=['help'])
def help_message(message):
    functions.help_message(message)


@bot.message_handler(content_types='text')
def message_reply(message):
    bot.send_message(message.chat.id, f'{message.text}')


bot.polling()
