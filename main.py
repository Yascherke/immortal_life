import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
from pymongo import MongoClient

import markup as nav
from fight import Battle
from mongodb import Finder
from cultivator import Cultivator
#from ws import keep_alive

#keep_alive()
from system import System

logging.basicConfig(level=logging.INFO)

API_TOKEN = "5223777026:AAEPnISDdv72oMOshyHx8Lg5nzpBgTGSHtc"
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

cluster = MongoClient(
    "mongodb+srv://Nere:0662@immortalworld.9ig3g.mongodb.net/immortal?retryWrites=true&w=majority"
)
db = cluster["immortal"]
users = db["users"]
players = db["players"]
cultivation = db["cultivation"]


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    uid = message.from_user.id
    await Cultivator.name.set()
    await message.answer("Напишите ваше культиваторское имя")

    @dp.message_handler(state=Cultivator.name)
    async def cmd_name(message: types.Message, state: FSMContext):
        await Cultivator.name.set()

        async with state.proxy() as data:
            data['Name'] = message.text
            uid = message.from_user.id
            name = data['Name']
            player = Cultivator()
            body = player.build_body()
            equipment = player.equipment()
            status = player.status()
            skills = player.skills()

            players.insert_one({
                "_id": uid,
                "name": name,
                "head": body[0],
                "torso": body[1],
                "rightArm": body[2],
                "leftArm": body[3],
                "rightLeg": body[4],
                "leftLeg": body[5],

                "headArmor": equipment[0],
                "torsoArmor": equipment[1],
                "rightArmArmor": equipment[2],
                "leftArmArmor": equipment[3],
                "rightLegArmor": equipment[4],
                "leftLegArmor": equipment[5],

                "power": body[6],
                "defence": body[7],
                "spiritDefence": body[8],
                "evade": body[9],
                "regeneration": body[10],
                "points": body[11],

                "level": status[0],
                "exp": status[1],
                "money": status[2],
                "coin": status[3],
                "herbs": status[4],
                "metals": status[5],
                "leather": status[6],
                "cloth": status[7],
                "materials": status[8],
                "pet": status[9],

                "blade": skills[0],
                "spear": skills[1],
                "sword": skills[2],
                "fist": skills[3],
                "palm": skills[4],
                "finger": skills[5],
                "fire": skills[6],
                "water": skills[7],
                "lightning": skills[8],
                "wind": skills[9],
                "earth": skills[10],
                "wood": skills[11],
                "light": skills[12],
                "dark": skills[13],
                "alchemy": skills[12],
                "forge": skills[13],
                "herbCollection": skills[15],
                "mining": skills[15],

            })

            await state.finish()
        await asyncio.sleep(1)
        await message.answer(f'Рад знакомству!')

@dp.message_handler(commands=['награда'])
async def sendexp(message: types.Message):
    uid = message.from_user.id
    finder = Finder(uid)
    system = System(uid)
    user = finder.findUserParamByID()
    msg = message.get_args()
    getter = msg.replace(' для ', ',').split(',')
    msg = message.get_args()
    exp = int(getter[0])
    system.sendExp(msg)
    await message.answer(f"{getter[1]} получил {exp} очков энергии от {user[0]}")
    await message.delete()

@dp.message_handler(commands=['ударить'])
async def battle(message: types.Message):
    uid = message.from_user.id
    finder = Finder(uid)
    battle = Battle(uid)
    user = finder.findUserParamByID()
    msg = message.get_args()
    getter = msg.replace(' в ', ',').split(',')
    res = battle.fight(getter)
    if res != False:
        await message.answer(f"{getter[0]} получил урон в {getter[1]} на {res[0]} единиц от {user[0]} \nЗдоровья осталось: {res[1]} \nЗдоровья похищенно: {res[2]} \nЭнергии похищенно: {res[3]} \nЗащита увеличена: {res[4]}")
    else:
        await message.answer("Цель уклонилась")

@dp.message_handler(commands=['улучшить'])
async def upgrade(message: types.Message):
    uid = message.from_user.id
    system = System(uid)
    msg = message.get_args()
    getter = msg.replace(' на ', ',').split(',')
    msg = message.get_args()
    exp = int(getter[1])
    if system.upgradeSkill(msg):
        await message.answer(f"Навык {getter[0]} повысился на {exp} очков навыков")
    else:
        await message.answer(f"У вас не хватает очков навыков либо навык полностью изучен")


@dp.message_handler()
async def cmds(message: types.Message):
    uid = message.from_user.id
    finder = Finder(uid)
    system = System(uid)
    param = finder.findUserParamByID()
    body = finder.findUserBodyByID()
    inv = finder.findUserInventoryByID()
    ma = finder.findUserMartialSkillsByID()
    sr = finder.findUserSpiritualRootByID()
    craft = finder.findUserCraftByID()

    for cult in cultivation.find({"_id": param[6]}):
        print("Cult finder done")

    if message.text == 'Профиль':
        await message.delete()
        await message.answer(f"""
-----------------------------------------
Имя культиватора: {param[0]}

                Голова:{body[0]}
                         O  Торс:{body[1]}
Лв. рука:{body[3]} /|\ Пр. рука:{body[2]}
Лв. нога:{body[5]} / \ Пр. нога:{body[4]}
-----------------------------------------
Параметры персонажа:

Атака: {param[1]}
Физ. защита: {param[2]}
Дух. защита: {param[3]}
Уклонение: {param[4]}
Регенерация: {param[5]}

Уровень: {cult['name']}
Энергия: {param[7]}

Очки навыков: {param[8]}
-----------------------------------------
Пространственное кольцо:

Боевые монеты: {inv[0]}
Токены: {inv[1]}
Травы: {inv[2]}
Руда: {inv[3]}
Кожа: {inv[4]}
Ткань: {inv[5]}

Материалы: {inv[6]}

Фамильяр: {inv[7]}
-----------------------------------------
""", reply_markup=nav.profileMenu)

    if message.text == "Навыки":
        await message.delete()
        await message.answer(f"""
        -----------------------------------------
        Боевые искусства:

        Клинок: {ma[0]}
        Копье: {ma[1]}
        Меч: {ma[2]}
        Кулак: {ma[3]}
        Ладонь: {ma[4]}
        Палец: {ma[5]}
        -----------------------------------------
        Духовные корни:

        Огонь: {sr[0]}
        Вода: {sr[1]}
        Молния: {sr[2]}
        Ветер: {sr[3]}
        Земля: {sr[4]}
        Дерево: {sr[5]}
        -----------------------------------------
        Ремесло:
        
        Алхимия: {craft[0]}
        Крафтер: {craft[1]}
        Сбор трав: {craft[2]}
        Сбор руды: {craft[3]}
        
        -----------------------------------------
        Мировые принципы:

        Свет: {sr[6]}
        Тьма: {sr[7]}
        -----------------------------------------
        """, reply_markup=nav.profileBack)

    if message.text == "Прорваться":
        await message.delete()
        levelUp = system.levelUp()
        if levelUp == True:
            await message.answer("Вы успешно прорвались на новый уровень")
        else:
            await message.answer("Недостаточно энергии")

    if message.text == "Отдых":
        
        regen = system.regen()
        await message.answer(f"{param[0]} восстановили себе {regen} здоровья")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
