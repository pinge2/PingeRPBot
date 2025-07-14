import telebot as tb
import os



bot = tb.TeleBot(os.env["BOT_TOKEN"])


@bot.message_handler(commands=["/start"])
def start_bot(msg):
	bot.reply_to(msg, "Записываю пользователей в базу...\nАнтимаг пинге мой батя ;)\n\n**Все находящиеся в чате пользователи, напишите \"/reg\".")
	users = eval(open("/list.json", "r").read())



@bot.message_handler(commands=["/exit_session"])
def save_all(msg):
	bot.reply_to(msg, "**Сохранение...**\nГотово! До встречи ;)")
	with open("./list.json", "w") as fd:
		fd.write(str(users))
	exit(0)



@bot.message_handler(commands=["/reg"])
def registry_user(msg):
	chat_id = msg.chat.id
	user_id = msg.reply_to_message.from_user.id
	user_name = bot.get_chat_member(chat_id, user_id).username
	users[user_id] = {
	"Имя": user_name,
	"Здоровье": 100,
	"Сила": 0,
	"Мана": 100,
	"Выносливость": 0,
	"Стойкость": 0,
	"Время оглушения": 0,
	"Время возрождения": 0,
	"Суперспособность": random.randint(0, 8)
	}
	bot.reply_to(msg, "Пользователь записан в базу!")



@bot.message_handler(commands=["*мои статы*"])
def get_stats(msg):
	chat_id = msg.chat.id
	user_id = msg.reply_to_message.from_user.id
	
	fmt = ""
	
	for key in users[user_id].keys():
		fmt += f"**{key}**: {users[user_id][key]}\n"
	
	bot.reply_to(msg, "**Ваши статы:**\n\n" + fmt)



@bot.message_handler(commands=["*качать руки*"])
def pushup_arms(msg):
	chat_id = msg.chat.id
	user_id = msg.reply_to_message.from_user.id
	
	users[user_id]["Сила"] += 0.5
	users[user_id]["Мана"] -= 25
	users[user_id]["Выносливость"] += 0.1
	
	fmt = f"\n\nСила удара: {users[user_id]['Сила']} (+0.5 за тренировку)"
	fmt += f"\n\t- **{20 + users[user_id]['Сила'] * 2} урон от удара**"
	fmt += f"\nТекущая мана: {users[user_id]['Мана']} (-25 за тренировку)"
	fmt += f"\nВыносливость: {users[user_id]['Выносливость']} (+0.1 за тренировку)"
	
	bot.reply_to(msg, f"{users[user_id]['Имя']}, вы накачали руки и усилили свои удары!" + fmt)



@bot.message_handler(commands=["*качать пресс*"])
def pushup_stomach(msg):
	chat_id = msg.chat.id
	user_id = msg.reply_to_message.from_user.id
	
	users[user_id]["Стойкость"] += 0.5
	users[user_id]["Мана"] -= 25
	users[user_id]["Выносливость"] += 0.1
	
	fmt = f"\n\nСтойкость: {users[user_id]['Стойкость']} (+0.5 за тренировку)"
	fmt += f"\n\t- **{100 + users[user_id]["Стойкость"] * 5} макс. здоровье**"
	fmt += f"\nТекущая мана: {users[user_id]['Мана']} (-25 за тренировку)"
	fmt += f"\nВыносливость: {users[user_id]['Выносливость']} (+0.1 за тренировку)"
	
	bot.reply_to(msg, f"{users[user_id]['Имя']}, вы накачали руки и усилили свои удары!" + fmt)
