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

            rand = randint(1, 20)

            #Blade
            if martial[0] >= 5 and martial[0] < 20:
                attack += param[1] * 0.1 * 10
                attack -= attack * martdef
            if martial[0] >= 20 and martial[0] < 30:
                attack += param[1] * 0.2 * 10
                attack -= attack * martdef
            if martial[0] >= 30 and martial[0] < 40:
                attack += param[1] * 0.3 * 10
                attack -= attack * martdef
                heal += attack * 0.5
            if martial[0] >= 40 and martial[0] < 50:
                attack += param[1] * 0.4 * 10
                attack -= attack * martdef
                heal += attack * 0.5
            if martial[0] >= 50 and martial[0] < 60:
                attack += param[1] * 0.5 * 10
                attack -= attack * martdef
                heal += attack * 0.5
            if martial[0] >= 60 and martial[0] < 70:
                attack += param[1] * 0.6 * 10
                attack -= attack * martdef
                heal += attack * 0.6
            if martial[0] >= 70 and martial[0] < 80:
                attack += param[1] * 0.7 * 10
                attack -= attack * martdef
                heal += attack * 0.7
            if martial[0] >= 80 and martial[0] < 90:
                attack += param[1] * 0.8 * 10
                attack -= attack * martdef
                heal += attack * 0.8
            if martial[0] >= 90 and martial[0] < 100:
                attack += param[1] * 0.9 * 10
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
                attack += param[1] * 0.4 * 10
                attack -= attack * martdef
            if martial[2] >= 20 and martial[2] < 30:
                attack += param[1] * 0.4 * 10
                attack -= attack * martdef
            if martial[2] >= 30 and martial[2] < 40:
                attack += param[1] * 0.6 * 10
                attack -= attack * martdef
            if martial[2] >= 40 and martial[2] < 50:
                attack += param[1] * 0.6 * 10
                attack -= attack * martdef
            if martial[2] >= 50 and martial[2] < 60:
                attack += param[1] * 0.6 * 10
                attack -= attack * martdef
            if martial[2] >= 60 and martial[2] < 70:
                attack += param[1] * 0.8 * 10
                attack -= attack * martdef
            if martial[2] >= 70 and martial[2] < 80:
                attack += param[1] * 0.8 * 10
                attack -= attack * martdef
            if martial[2] >= 80 and martial[2] < 90:
                attack += param[1] * 0.8 * 10
                attack -= attack * martdef
            if martial[2] >= 90 and martial[2] < 100:
                attack += param[1] * 0.8 * 10
                attack -= attack * martdef
            if martial[2] == 100:
                attack += param[1] * 2 * 10
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
            if spiritual[6] >= 60 and spiritual[6] < 70:
                attack += param[1] * 10
            if spiritual[6] >= 70 and spiritual[6] < 80:
                attack += param[1] * 12
            if spiritual[6] >= 80 and spiritual[6] < 90:
                attack += param[1] * 14
            if spiritual[6] >= 90 and spiritual[6] < 100:
                attack += param[1] * 16
            if spiritual[6] == 100:
                attack += param[1] * 18


            #Dark
            if spiritual[7] >= 5 and spiritual[7] < 20:
                attack += param[1] * 2
            if spiritual[7] >= 20 and spiritual[7] < 30:
                attack += param[1] * 4
            if spiritual[7] >= 30 and spiritual[7] < 40:
                attack += param[1] * 6
            if spiritual[7] >= 40 and spiritual[7] < 50:
                attack += param[1] * 8
            if spiritual[7] >= 50 and spiritual[7] < 60:
                attack += param[1] * 10
            if spiritual[7] >= 60 and spiritual[7] < 70:
                attack += param[1] * 12
            if spiritual[7] >= 70 and spiritual[7] < 80:
                attack += param[1] * 14
            if spiritual[7] >= 80 and spiritual[7] < 90:
                attack += param[1] * 16
            if spiritual[7] >= 90 and spiritual[7] < 100:
                attack += param[1] * 18
            if spiritual[7] == 100:
                attack += param[1] * 20

            if rand >= evade:
                if aim == "Голова":
                    head = enBody[0] - attack
                    headh = body[0] + heal
                    users.update_one({"_id": enId}, {"$set": {"head": round(head)}})
                    users.update_one({"_id": self.uid}, {"$set": {"head": round(headh)}})
                    if lvl <= 11 and body[0] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"head": 100}})
                        return [attack, round(head), round(headh)]
                    if lvl > 11 and lvl <= 17 and body[0] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"head": 150}})
                        return [attack, round(head), round(headh)]
                    if lvl > 11 and lvl <= 23 and body[0] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"head": 200}})
                        return [attack, round(head), round(headh)]
                    if enBody[0] <= 0 or attack >= enBody[0]:
                        users.update_one({"_id": enId}, {"$set": {"head": 1}})
                        return [attack, 1, round(headh)]
                    return [attack, round(head), round(headh)]

                if aim == "Торс":
                    torso = enBody[1] - attack
                    torsoh = body[1] + heal
                    users.update_one({"_id": enId}, {"$set": {"torso": round(torso)}})
                    users.update_one({"_id": self.uid}, {"$set": {"torso": round(torsoh)}})
                    if lvl <= 11 and body[1] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"torso": 100}})
                        return [attack, round(torso), round(torsoh)]
                    if lvl > 11 and lvl <= 17 and body[1] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"torso": 150}})
                        return [attack, round(torso), round(torsoh)]
                    if lvl > 11 and lvl <= 23 and body[1] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"torso": 200}})
                        return [attack, round(torso), round(torsoh)]
                    if enBody[1] <= 0 or attack >= enBody[1]:
                        users.update_one({"_id": enId}, {"$set": {"torso": 1}})
                        return [attack, 1, round(torsoh)]
                    return [attack, round(torso), round(torsoh)]

                if aim == "Пр. рука":
                    ra = enBody[2] - attack
                    rah = body[2] + heal
                    users.update_one({"_id": enId}, {"$set": {"rightArm":   round(ra)}})
                    users.update_one({"_id": self.uid}, {"$set": {"rightArm": round(rah)}})
                    if lvl <= 11 and body[2] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"rightArm": 100}})
                        return [attack, round(ra), round(rah)]
                    if lvl > 11 and lvl <= 17 and body[2] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"rightArm": 150}})
                        return [attack, ra, heal]
                    if lvl > 11 and lvl <= 23 and body[2] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"rightArm": 200}})
                        return [attack, round(ra), round(rah)]
                    if enBody[2] <= 0 or attack >= enBody[2]:
                        users.update_one({"_id": enId}, {"$set": {"rightArm": 1}})
                        return [attack, 1, round(rah)]
                    return [attack, round(ra), round(rah)]

                if aim == "Лв. рука":
                    la = enBody[3] - attack
                    lah = body[3] + heal
                    users.update_one({"_id": enId}, {"$set": {"leftArm": round(la)}})
                    users.update_one({"_id": self.uid}, {"$set": {"leftArm": round(lah)}})
                    if lvl <= 11 and body[3] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"leftArm": 100}})
                        return [attack,  round(la), round(lah)]
                    if lvl > 11 and lvl <= 17 and body[3] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"leftArm": 150}})
                        return [attack,  round(la), round(lah)]
                    if lvl > 11 and lvl <= 23 and body[3] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"leftArm": 200}})
                        return [attack,  round(la), round(lah)]
                    if enBody[3] <= 0 or attack >= enBody[3]:
                        users.update_one({"_id": enId}, {"$set": {"leftArm": 1}})
                        return [attack, 1, round(lah)]
                    return [attack,  round(la), round(lah)]

                if aim == "Пр. нога":
                    rl = enBody[4] - attack
                    rlh = body[4] + heal
                    users.update_one({"_id": enId}, {"$set": {"rightLeg": round(rl)}})
                    users.update_one({"_id": self.uid}, {"$set": {"rightLeg": round(rlh)}})
                    if lvl <= 11 and body[4] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"rightLeg": 100}})
                        return [attack, round(rl), round(rlh)]
                    if lvl > 11 and lvl <= 17 and body[4] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"rightLeg": 150}})
                        return [attack, round(rl), round(rlh)]
                    if lvl > 11 and lvl <= 23 and body[4] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"rightLeg": 200}})
                        return [attack, round(rl), round(rlh)]
                    if enBody[4] <= 0 or attack >= enBody[4]:
                        users.update_one({"_id": enId}, {"set": {"rightLeg": 1}})
                        return [attack, 1, round(rlh)]
                    return [attack, round(rl), round(rlh)]

                if aim == "Лв. нога":
                    ll = enBody[5] - attack
                    llh = body[5] + heal
                    users.update_one({"_id": enId}, {"$set": {"leftLeg": round(ll)}})
                    users.update_one({"_id": self.uid}, {"$set": {"leftLeg": round(llh)}})
                    if lvl <= 11 and body[5] > 100:
                        users.update_one({"_id": self.uid}, {"$set": {"leftLeg": 100}})
                        return [attack, round(ll), round(llh)]
                    if lvl > 11 and lvl <= 17 and body[5] > 150:
                        users.update_one({"_id": self.uid}, {"$set": {"leftLeg": 150}})
                        return [attack, round(ll), round(llh)]
                    if lvl > 11 and lvl <= 23 and body[5] > 200:
                        users.update_one({"_id": self.uid}, {"$set": {"leftLeg": 200}})
                        return [attack, round(ll), round(llh)]
                    if enBody[5] <= 0 or attack >= enBody[5]:
                        users.update_one({"_id": enId}, {"$set": {"leftLeg": 1}})
                        return [attack, 1, round(llh)]
                    return [attack, round(ll), round(llh)]
            else:
                return False