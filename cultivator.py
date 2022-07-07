from aiogram.dispatcher.filters.state import State, StatesGroup
from random import randint

class Cultivator(StatesGroup):

    def __int__(self):

#Здоровье персонажа
        self.head
        self.torso
        self.left_arm
        self.right_arm
        self.left_leg
        self.right_leg

#Характеристики
        self.power
        self.defence
        self.spirit_def
        self.evade

#Восстановление частей тела если их пареметр больше 0
        self.regeneration

#Слоты брони и оружия
        self.head_armor
        self.torso_armor
        self.left_arm_armor
        self.right_arm_armor
        self.left_leg_armor
        self.right_leg_armor

        self.right_hand
        self.left_hand

#Уровень культивации
        self. level
        self.exp

#Фракция и секта
        self.sect
        self.fraction

#Иммущество
        self.money
        self.coin
        self.herbs
        self.metals
        self.leather
        self.cloth

        self.materials

        self.pet

#Навыки
        #Martial Arts
        self.blade
        self.spear
        self.sword
        self.fist
        self.palm
        self.finger

        #Spiritual Root
        self.fire
        self.water
        self.lightning
        self.wind
        self.earth
        self.wood

        self.light
        self.dark

        #Specialization
        self.alchemy
        self.forge
        self.herb_collection
        self.ore

#Дополнительные параметры
        self.isAdmin
        self.isAlive


    name = State()

    def build_body(self):
        self.head = 100
        self.torso = 100
        self.left_arm = 100
        self.right_arm = 100
        self.left_leg = 100
        self.right_leg = 100

        self.power = randint(1, 5)
        self.defence = 0
        self.spirit_def = 0
        self.evade = randint(1, 10)

        self.regeneration = randint(1, 25)

        return [self.head, self.torso, self.right_arm, self.left_arm, self.right_leg, self.left_leg, self.power, self.defence, self.spirit_def, self.evade, self.regeneration]

    def equipment(self):

        self.head_armor = 0
        self.torso_armor = 0
        self.left_arm_armor = 0
        self.right_arm_armor = 0
        self.left_leg_armor = 0
        self.right_leg_armor = 0

        self.right_hand = 0
        self.left_hand = 0

        return [self.head_armor, self.torso_armor, self.right_arm_armor, self.left_arm_armor, self.right_leg_armor, self.left_leg_armor, self.right_hand, self.left_hand]

    def status(self):

        self.level = 0
        self.exp = 0

        self.sect = 0
        self.fraction = 0

        self.money = 0
        self.coin = 0
        self.herbs = 0
        self.metals = 0
        self.leather = 0
        self.cloth = 0

        self.materials = 0

        self.pet = 0

        self.isAdmin = 0
        self.isAlive = 1

        return [self.level, self.exp, self.sect, self.fraction, self.money, self.coin, self.herbs, self.metals, self.leather, self.cloth, self.materials, self.pet, self.isAlive, self.isAdmin]

    def skills(self):

        self.blade = 0
        self.spear = 0
        self.sword = 0
        self.fist = 0
        self.palm = 0
        self.finger = 0

        self.fire = 0
        self.water = 0
        self.lightning = 0
        self.wind = 0
        self.earth = 0
        self.wood = 0

        self.light = 0
        self.dark = 0

        self.alchemy = 0
        self.forge = 0
        self.herb_collection = 0
        self.ore = 0

        return [self.blade, self.spear, self.sword, self.fist, self.palm, self.finger, self.fire, self.water, self.lightning, self.wind, self.earth, self.wood, self.alchemy, self.forge, self.herb_collection, self.ore, self.light, self.dark]




