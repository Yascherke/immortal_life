from aiogram.dispatcher.filters.state import State, StatesGroup
from pymongo import MongoClient
from mongodb import Finder
from random import randint


cluster = MongoClient(
        "mongodb+srv://Nere:0662@immortalworld.9ig3g.mongodb.net/immortal?retryWrites=true&w=majority")
db = cluster["immortal"]
users = db["players"]
sects = db["sects"]
cultiv = db["cultivation"]

class Battle:

        def __init__(self, uid):
            self.uid = uid


        def fight(self, getter: list):
            name = getter[0]
            aim = getter[1]

            finder = Finder(self.uid)

            for n in users.find({"name": name}):
                enId = n["_id"]

            enemyFinder = Finder(enId)

            martial = finder.findUserMartialSkillsByID()
            spiritual = finder.findUserSpiritualRootByID()
            param = finder.findUserParamByID()
            body = finder.findUserBodyByID()
            enBody = enemyFinder.findUserBodyByID()
            enParam = enemyFinder.findUserParamByID()

            attack = param[1]
            lvl = param[6]
            heal = 0
            evade = enParam[4]
            martdef = param[2] / 100
            spiritdef = param[3] / 100

            exp = 0
            getDef = 0
            getSpir = 0

            rand = randint(1, 20)

            #Blade
            if martial[0] >= 5 and martial[0] < 20:
                attack += param[1] * 0.1
                attack -= attack * martdef
            if martial[0] >= 20 and martial[0] < 30:
                attack += param[1] * 0.2
                attack -= attack * martdef
            if martial[0] >= 30 and martial[0] < 40:
                attack += param[1] * 0.3
                attack -= attack * martdef
                heal += attack * 0.5
            if martial[0] >= 40 and martial[0] < 50:
                attack += param[1] * 0.4
                attack -= attack * martdef
                heal += attack * 0.5
            if martial[0] >= 50 and martial[0] < 60:
                attack += param[1] * 0.5
                attack -= attack * martdef
                heal += attack * 0.5
            if martial[0] >= 60 and martial[0] < 70:
                attack += param[1] * 0.6
                attack -= attack * martdef
                heal += attack * 0.6
            if martial[0] >= 70 and martial[0] < 80:
                attack += param[1] * 0.7
                attack -= attack * martdef
                heal += attack * 0.7
            if martial[0] >= 80 and martial[0] < 90:
                attack += param[1] * 0.8
                attack -= attack * martdef
                heal += attack * 0.8
            if martial[0] >= 90 and martial[0] < 100:
                attack += param[1] * 0.9
                attack -= attack * martdef
                heal += attack * 0.9
            if martial[0] == 100:
                attack += param[1] * 10
                attack -= attack * martdef
                heal += attack

            #Spear
            if martial[1] >= 5 and martial[1] < 20:
                attack += param[1] * 0.3
                attack -= attack * (martdef - 0.1)
            if martial[1] >= 20 and martial[1] < 30:
                attack += param[1] * 0.3
                attack -= attack * (martdef - 0.2)
            if martial[1] >= 30 and martial[1] < 40:
                attack += param[1] * 0.3
                attack -= attack * (martdef - 0.3)
            if martial[1] >= 40 and martial[1] < 50:
                attack += param[1] * 0.5
                attack -= attack * (martdef - 0.4)
            if martial[1] >= 50 and martial[1] < 60:
                attack += param[1] * 0.5
                attack -= attack * (martdef - 0.5)
            if martial[1] >= 60 and martial[1] < 70:
                attack += param[1] * 0.5
                attack -= attack * (martdef - 0.5)
            if martial[1] >= 70 and martial[1] < 80:
                attack += param[1] * 0.8
                attack -= attack * (martdef - 0.5)
            if martial[1] >= 80 and martial[1] < 90:
                attack += param[1] * 0.8
                attack -= attack * (martdef - 0.5)
            if martial[1] >= 90 and martial[1] < 100:
                attack += param[1] * 0.8
                attack -= attack * (martdef - 0.5)
            if martial[1] == 100:
                attack += param[1] * 1.5
                attack -= attack * (martdef - 0.7)

            #Sword
            if martial[2] >= 5 and martial[2] < 20:
                attack += param[1] * 0.4
                attack -= attack * martdef
            if martial[2] >= 20 and martial[2] < 30:
                attack += param[1] * 0.4
                attack -= attack * martdef
            if martial[2] >= 30 and martial[2] < 40:
                attack += param[1] * 0.6
                attack -= attack * martdef
            if martial[2] >= 40 and martial[2] < 50:
                attack += param[1] * 0.6
                attack -= attack * martdef
            if martial[2] >= 50 and martial[2] < 60:
                attack += param[1] * 0.6
                attack -= attack * martdef
            if martial[2] >= 60 and martial[2] < 70:
                attack += param[1] * 0.8
                attack -= attack * martdef
            if martial[2] >= 70 and martial[2] < 80:
                attack += param[1] * 0.8
                attack -= attack * martdef
            if martial[2] >= 80 and martial[2] < 90:
                attack += param[1] * 0.8
                attack -= attack * martdef
            if martial[2] >= 90 and martial[2] < 100:
                attack += param[1] * 0.8
                attack -= attack * martdef
            if martial[2] == 100:
                attack += param[1] * 2
                attack -= attack * martdef

            #Fist
            if martial[3] >= 5 and martial[3] < 20:
                attack += param[1] * 5
                attack -= attack * martdef
            if martial[3] >= 20 and martial[3] < 30:
                attack += param[1] * 5
                attack -= attack * martdef
            if martial[3] >= 30 and martial[3] < 40:
                attack += param[1] * 7
                attack -= attack * martdef
            if martial[3] >= 40 and martial[3] < 50:
                attack += param[1] * 7
                attack -= attack * martdef
            if martial[3] >= 50 and martial[3] < 60:
                attack += param[1] * 7
                attack -= attack * martdef
            if martial[3] >= 60 and martial[3] < 70:
                attack += param[1] * 7
                attack -= attack * martdef
            if martial[3] >= 70 and martial[3] < 80:
                attack += param[1] * 10
                attack -= attack * martdef
            if martial[3] >= 80 and martial[3] < 90:
                attack += param[1] * 10
                attack -= attack * martdef
            if martial[3] >= 90 and martial[3] < 100:
                attack += param[1] * 15
                attack -= attack * martdef
            if martial[3] == 100:
                attack += param[1] * 25
                attack -= attack * martdef

            #Palm
            if martial[4] >= 5 and martial[4] < 20:
                attack += param[1] * 3
                attack -= attack * martdef
            if martial[4] >= 20 and martial[4] < 30:
                attack += param[1] * 3
                attack -= attack * martdef
            if martial[4] >= 30 and martial[4] < 40:
                attack += param[1] * 3
                attack -= attack * martdef
            if martial[4] >= 40 and martial[4] < 50:
                attack += param[1] * 6
                attack -= attack * martdef
            if martial[4] >= 50 and martial[4] < 60:
                attack += param[1] * 6
                attack -= attack * martdef
            if martial[4] >= 60 and martial[4] < 70:
                attack += param[1] * 6
                attack -= attack * martdef
            if martial[4] >= 70 and martial[4] < 80:
                attack += param[1] * 12
                attack -= attack * martdef
            if martial[4] >= 80 and martial[4] < 90:
                attack += param[1] * 12
                attack -= attack * martdef
            if martial[4] >= 90 and martial[4] < 100:
                attack += param[1] * 12
                attack -= attack * martdef
            if martial[4] == 100:
                attack += param[1] * 20
                attack -= attack * martdef

            #Finger
            if martial[5] >= 5 and martial[5] < 20:
                attack += param[1] * 2
                attack -= attack * (martdef - 1)
            if martial[5] >= 20 and martial[5] < 30:
                attack += param[1] * 2
                attack -= attack * (martdef - 1)
            if martial[5] >= 30 and martial[5] < 40:
                attack += param[1] * 2
                attack -= attack * (martdef - 1)
            if martial[5] >= 40 and martial[5] < 50:
                attack += param[1] * 4
                attack -= attack * (martdef - 1)
            if martial[5] >= 50 and martial[5] < 60:
                attack += param[1] * 4
                attack -= attack * (martdef - 1)
            if martial[5] >= 60 and martial[5] < 70:
                attack += param[1] * 4
                attack -= attack * (martdef - 1)
            if martial[5] >= 70 and martial[5] < 80:
                attack += param[1] * 6
                attack -= attack * (martdef - 1)
            if martial[5] >= 80 and martial[5] < 90:
                attack += param[1] * 6
                attack -= attack * (martdef - 1)
            if martial[5] >= 90 and martial[5] < 100:
                attack += param[1] * 6
                attack -= attack * (martdef - 1)
            if martial[5] == 100:
                attack += param[1] * 8
                attack -= attack * (martdef - 2)

            #Fire
            if spiritual[0] >= 5 and spiritual[0] < 20:
                attack += param[1] * 1.5
                attack -= attack * spiritdef
            if spiritual[0] >= 20 and spiritual[0] < 30:
                attack += param[1] * 2
                attack -= attack * spiritdef
            if spiritual[0] >= 30 and spiritual[0] < 40:
                attack += param[1] * 3
                attack -= attack * spiritdef
            if spiritual[0] >= 40 and spiritual[0] < 50:
                attack += param[1] * 4
                attack -= attack * spiritdef
            if spiritual[0] >= 50 and spiritual[0] < 60:
                attack += param[1] * 5
                attack -= attack * spiritdef
            if spiritual[0] >= 60 and spiritual[0] < 70:
                attack += param[1] * 6
                attack -= attack * spiritdef
            if spiritual[0] >= 70 and spiritual[0] < 80:
                attack += param[1] * 7
                attack -= attack * spiritdef
            if spiritual[0] >= 80 and spiritual[0] < 90:
                attack += param[1] * 8
                attack -= attack * spiritdef
            if spiritual[0] >= 90 and spiritual[0] < 100:
                attack += param[1] * 9
                attack -= attack * spiritdef
            if spiritual[0] == 100:
                attack += param[1] * 10
                attack -= attack * spiritdef

            #Water
            if spiritual[1] >= 5 and spiritual[1] < 20:
                attack += param[1] * 1.5
                attack -= attack * spiritdef
            if spiritual[1] >= 20 and spiritual[1] < 30:
                attack += param[1] * 1.5
                attack -= attack * spiritdef
            if spiritual[1] >= 30 and spiritual[1] < 40:
                attack += param[1] * 2.5
                attack -= attack * spiritdef
            if spiritual[1] >= 40 and spiritual[1] < 50:
                attack += param[1] * 2.5
                attack -= attack * spiritdef
            if spiritual[1] >= 50 and spiritual[1] < 60:
                attack += param[1] * 4
                attack -= attack * spiritdef
            if spiritual[1] >= 60 and spiritual[1] < 70:
                attack += param[1] * 5
                attack -= attack * spiritdef
            if spiritual[1] >= 70 and spiritual[1] < 80:
                attack += param[1] * 6
                attack -= attack * spiritdef
            if spiritual[1] >= 80 and spiritual[1] < 90:
                attack += param[1] * 7
                attack -= attack * spiritdef
            if spiritual[1] >= 90 and spiritual[1] < 100:
                attack += param[1] * 10
                attack -= attack * spiritdef
            if spiritual[1] == 100:
                attack += param[1] * 10
                attack -= attack * spiritdef

            #lightning
            if spiritual[2] >= 5 and spiritual[2] < 20:
                attack += param[1] * 1.5
                attack -= attack * spiritdef
            if spiritual[2] >= 20 and spiritual[2] < 30:
                attack += param[1] * 2
                attack -= attack * spiritdef
            if spiritual[2] >= 30 and spiritual[2] < 40:
                attack += param[1] * 3
                attack -= attack * spiritdef
            if spiritual[2] >= 40 and spiritual[2] < 50:
                attack += param[1] * 4
                attack -= attack * spiritdef
            if spiritual[2] >= 50 and spiritual[2] < 60:
                attack += param[1] * 5
                attack -= attack * spiritdef
            if spiritual[2] >= 60 and spiritual[2] < 70:
                attack += param[1] * 5
                attack -= attack * spiritdef
            if spiritual[2] >= 70 and spiritual[2] < 80:
                attack += param[1] * 6
                attack -= attack * spiritdef
            if spiritual[2] >= 80 and spiritual[2] < 90:
                attack += param[1] * 7
                attack -= attack * spiritdef
            if spiritual[2] >= 90 and spiritual[2] < 100:
                attack += param[1] * 8
                attack -= attack * spiritdef
            if spiritual[2] == 100:
                attack += param[1] * 15
                attack -= attack * spiritdef

            #Wind
            if spiritual[3] >= 5 and spiritual[3] < 20:
                attack += param[1] * 1.5
                attack -= attack * spiritdef
            if spiritual[3] >= 20 and spiritual[3] < 30:
                attack += param[1] * 1.5
                attack -= attack * spiritdef
            if spiritual[3] >= 30 and spiritual[3] < 40:
                attack += param[1] * 3
                attack -= attack * spiritdef
            if spiritual[3] >= 40 and spiritual[3] < 50:
                attack += param[1] * 3
                attack -= attack * spiritdef
            if spiritual[3] >= 50 and spiritual[3] < 60:
                attack += param[1] * 6
                attack -= attack * spiritdef
            if spiritual[3] >= 60 and spiritual[3] < 70:
                attack += param[1] * 6
                attack -= attack * spiritdef
            if spiritual[3] >= 70 and spiritual[3] < 80:
                attack += param[1] * 6
                attack -= attack * spiritdef
            if spiritual[3] >= 80 and spiritual[3] < 90:
                attack += param[1] * 9
                attack -= attack * spiritdef
            if spiritual[3] >= 90 and spiritual[3] < 100:
                attack += param[1] * 9
                attack -= attack * spiritdef
            if spiritual[3] == 100:
                attack += param[1] * 10
                attack -= attack * spiritdef

            #Earth
            if spiritual[4] >= 5 and spiritual[4] < 20:
                attack += param[1] * 1
                attack -= attack * spiritdef
            if spiritual[4] >= 20 and spiritual[4] < 30:
                attack += param[1] * 1
                attack -= attack * spiritdef
            if spiritual[4] >= 30 and spiritual[4] < 40:
                attack += param[1] * 2
                attack -= attack * spiritdef
            if spiritual[4] >= 40 and spiritual[4] < 50:
                attack += param[1] * 3
                attack -= attack * spiritdef
            if spiritual[4] >= 50 and spiritual[4] < 60:
                attack += param[1] * 5
                attack -= attack * spiritdef
            if spiritual[4] >= 60 and spiritual[4] < 70:
                attack += param[1] * 6
                attack -= attack * spiritdef
            if spiritual[4] >= 70 and spiritual[4] < 80:
                attack += param[1] * 7
                attack -= attack * spiritdef
            if spiritual[4] >= 80 and spiritual[4] < 90:
                attack += param[1] * 7
                attack -= attack * spiritdef
            if spiritual[4] >= 90 and spiritual[4] < 100:
                attack += param[1] * 10
                attack -= attack * spiritdef
            if spiritual[4] == 100:
                attack += param[1] * 12
                attack -= attack * spiritdef

            #Wood
            if spiritual[5] >= 5 and spiritual[5] < 20:
                attack += param[1] * 1
                attack -= attack * spiritdef
            if spiritual[5] >= 20 and spiritual[5] < 30:
                attack += param[1] * 1
                attack -= attack * spiritdef
            if spiritual[5] >= 30 and spiritual[5] < 40:
                attack += param[1] * 1
                attack -= attack * spiritdef
            if spiritual[5] >= 40 and spiritual[5] < 50:
                attack += param[1] * 4
                attack -= attack * spiritdef
            if spiritual[5] >= 50 and spiritual[5] < 60:
                attack += param[1] * 4
                attack -= attack * spiritdef
            if spiritual[5] >= 60 and spiritual[5] < 70:
                attack += param[1] * 4
                attack -= attack * spiritdef
            if spiritual[5] >= 70 and spiritual[5] < 80:
                attack += param[1] * 8
                attack -= attack * spiritdef
            if spiritual[5] >= 80 and spiritual[5] < 90:
                attack += param[1] * 8
                attack -= attack * spiritdef
            if spiritual[5] >= 90 and spiritual[5] < 100:
                attack += param[1] * 10
                attack -= attack * spiritdef
            if spiritual[5] == 100:
                attack += param[1] * 10
                attack -= attack * spiritdef

            #Light
            if spiritual[6] >= 5 and spiritual[6] < 20:
                attack += param[1] * 2
            if spiritual[6] >= 20 and spiritual[6] < 30:
                attack += param[1] * 3
            if spiritual[6] >= 30 and spiritual[6] < 40:
                attack += param[1] * 5
            if spiritual[6] >= 40 and spiritual[6] < 50:
                attack += param[1] * 7
            if spiritual[6] >= 50 and spiritual[6] < 60:
                attack += param[1] * 9
                getDef += 0.1
                getSpir += 0.1
            if spiritual[6] >= 60 and spiritual[6] < 70:
                attack += param[1] * 10
                getDef += 0.1
                getSpir += 0.1
            if spiritual[6] >= 70 and spiritual[6] < 80:
                attack += param[1] * 12
                getDef += 0.2
                getSpir += 0.2
            if spiritual[6] >= 80 and spiritual[6] < 90:
                attack += param[1] * 14
                getDef += 0.3
                getSpir += 0.3
            if spiritual[6] >= 90 and spiritual[6] < 100:
                attack += param[1] * 16
                getDef += 0.4
                getSpir += 0.4
            if spiritual[6] == 100:
                attack += param[1] * 18
                getDef += 0.5
                getSpir += 0.5


            #Dark
            if spiritual[7] >= 5 and spiritual[7] < 20:
                attack += param[1] * 2
                exp += 100
            if spiritual[7] >= 20 and spiritual[7] < 30:
                attack += param[1] * 4
                exp += 200
            if spiritual[7] >= 30 and spiritual[7] < 40:
                attack += param[1] * 6
                exp += 300
            if spiritual[7] >= 40 and spiritual[7] < 50:
                attack += param[1] * 8
                exp += 400
            if spiritual[7] >= 50 and spiritual[7] < 60:
                attack += param[1] * 10
                exp += 500
            if spiritual[7] >= 60 and spiritual[7] < 70:
                attack += param[1] * 12
                exp += 600
            if spiritual[7] >= 70 and spiritual[7] < 80:
                attack += param[1] * 14
                exp += 700
            if spiritual[7] >= 80 and spiritual[7] < 90:
                attack += param[1] * 16
                exp += 800
            if spiritual[7] >= 90 and spiritual[7] < 100:
                attack += param[1] * 18
                exp += 900
            if spiritual[7] == 100:
                attack += param[1] * 20
                exp += 1000

            if rand >= evade:
                if aim == "Голова":
                    head = enBody[0] - attack
                    users.update_one({"_id": enId}, {"$set": {"head": round(head)}})
                    users.update_one({"_id": enId}, {"$set": {"exp": enParam[7] - exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"exp": param[7] + exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"defence": param[2] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"spiritDefence": param[3] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"head": body[0] + round(heal)}})
                    if lvl <= 11 and body[0] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                        return [round(attack), round(head), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 17 and body[0] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                        return [round(attack), round(head), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 23 and body[0] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                        return [round(attack), round(head), round(heal), exp, getDef]
                    if enBody[0] <= 0 or attack >= enBody[0]:
                        users.update_one({"_id": enId}, {"$set": {"head": 1}})
                        return [round(attack), round(head), round(heal), exp, getDef]
                    return [round(attack), round(head), round(heal)]

                if aim == "Торс":
                    torso = enBody[1] - attack
                    users.update_one({"_id": enId}, {"$set": {"torso": round(torso)}})
                    users.update_one({"_id": enId}, {"$set": {"exp": enParam[7] - exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"exp": param[7] + exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"defence": param[2] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"spiritDefence": param[3] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"torso": body[1] + round(heal)}})
                    if lvl <= 11 and body[1] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"torso": 100}})
                        return [round(attack), round(torso), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 17 and body[1] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"torso": 150}})
                        return [round(attack), round(torso), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 23 and body[1] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"torso": 200}})
                        return [round(attack), round(torso), round(heal), exp, getDef]
                    if enBody[1] <= 0 or attack >= enBody[1]:
                        users.update_one({"_id": enId}, {"$set": {"torso": 1}})
                        return [round(attack), 1, round(heal), exp, getDef]
                    return [round(round(attack)), round(torso), round(heal), exp, getDef]

                if aim == "Пр. рука":
                    ra = enBody[2] - attack
                    users.update_one({"_id": enId}, {"$set": {"rightArm":   round(ra)}})
                    users.update_one({"_id": enId}, {"$set": {"exp": enParam[7] - exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"exp": param[7] + exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"defence": param[2] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"spiritDefence": param[3] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"rightArm": body[2] + round(heal)}})
                    if lvl <= 11 and body[2] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"rightArm": 100}})
                        return [round(attack), round(ra), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 17 and body[2] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"rightArm": 150}})
                        return [round(attack), ra, round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 23 and body[2] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"rightArm": 200}})
                        return [round(attack), round(ra), round(heal), exp, getDef]
                    if enBody[2] <= 0 or attack >= enBody[2]:
                        users.update_one({"_id": enId}, {"$set": {"rightArm": 1}})
                        return [round(attack), 1, round(heal), exp, getDef]
                    return [round(attack), round(ra), round(heal), exp, getDef]

                if aim == "Лв. рука":
                    la = enBody[3] - attack
                    users.update_one({"_id": enId}, {"$set": {"leftArm": round(la)}})
                    users.update_one({"_id": enId}, {"$set": {"exp": enParam[7] - exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"exp": param[7] + exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"defence": param[2] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"spiritDefence": param[3] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"leftArm": body[3] + round(heal)}})
                    if lvl <= 11 and body[3] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"leftArm": 100}})
                        return [round(attack),  round(la), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 17 and body[3] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"leftArm": 150}})
                        return [round(attack),  round(la), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 23 and body[3] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"leftArm": 200}})
                        return [round(attack),  round(la), round(heal), exp, getDef]
                    if enBody[3] <= 0 or attack >= enBody[3]:
                        users.update_one({"_id": enId}, {"$set": {"leftArm": 1}})
                        return [round(attack), 1, round(heal), exp, getDef]
                    return [round(attack),  round(la), round(heal), exp, getDef]

                if aim == "Пр. нога":
                    rl = enBody[4] - attack
                    users.update_one({"_id": enId}, {"$set": {"rightLeg": round(rl)}})
                    users.update_one({"_id": enId}, {"$set": {"exp": enParam[7] - exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"exp": param[7] + exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"defence": param[2] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"spiritDefence": param[3] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"rightLeg": body[4] + round(heal)}})
                    if lvl <= 11 and body[4] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"rightLeg": 100}})
                        return [round(attack), round(rl), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 17 and body[4] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"rightLeg": 150}})
                        return [round(attack), round(rl), round(heal), exp, getDef]
                    if lvl > 11 and lvl <= 23 and body[4] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"rightLeg": 200}})
                        return [round(attack), round(rl), round(heal), exp, getDef]
                    if enBody[4] <= 0 or attack >= enBody[4]:
                        users.update_one({"_id": enId}, {"set": {"rightLeg": 1}})
                        return [round(attack), 1, round(heal), exp, getDef]
                    return [round(attack), round(rl), round(heal), exp, getDef]

                if aim == "Лв. нога":
                    ll = enBody[5] - attack
                    users.update_one({"_id": enId}, {"$set": {"leftLeg": round(ll)}})
                    users.update_one({"_id": enId}, {"$set": {"exp": enParam[7] - exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"exp": param[7] + exp}})
                    users.update_one({"_id": self.uid}, {"$set": {"defence": param[2] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"spiritDefence": param[3] + getDef}})
                    users.update_one({"_id": self.uid}, {"$set": {"leftLeg": body[5] + round(heal)}})
                    if lvl <= 11 and body[5] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"leftLeg": 100}})
                        return [round(attack), round(ll), round(heal), exp, getDef]
                    if lvl >= 12 and lvl <= 17 and body[5] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"leftLeg": 150}})
                        return [round(attack), round(ll), round(heal), exp, getDef]
                    if lvl >= 18 and lvl <= 23 and body[5] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"leftLeg": 200}})
                        return [round(attack), round(ll), round(heal), exp, getDef]
                    if enBody[5] <= 0 or attack >= enBody[5]:
                        users.update_one({"_id": enId}, {"$set": {"leftLeg": 1}})
                        return [round(attack), 1, round(heal), exp, getDef]
                    return [round(attack), round(ll), round(heal), exp, getDef]
            else:
                return False