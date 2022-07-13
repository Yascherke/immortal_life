from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Nere:0662@immortalworld.9ig3g.mongodb.net/immortal?retryWrites=true&w=majority")
db = cluster["immortal"]
users = db["players"]
sects = db["sects"]
cultiv = db["cultivation"]
cities = db["cities"]


class Finder:

    def __init__(self, uid):
        self.uid = uid

    def findUserParamByID(self):
        for user in users.find({"_id": self.uid}):
            print("User finder done")

        return [user['name'], user['power'], user['defence'], user['spiritDefence'], user['evade'], user['regeneration'], user['level'], user['exp'], user['points']]

    def findUserBodyByID(self):
        for user in users.find({"_id": self.uid}):
            print("Body finder done")

        return [user['head'], user['torso'], user['rightArm'], user['leftArm'], user['rightLeg'], user['leftLeg']]

    def findUserArmorByID(self):
        for user in users.find({"_id": self.uid}):
            print("Armor finder done")

        return [user['headArmor'], user['torsoArmor'], user['rightArmArmor'], user['leftArmArmor'], user['rightLegArmor'], user['leftLegArmor']]

    def findUserInventoryByID(self):
        for user in users.find({"_id": self.uid}):
            print("Inventory finder done")

        return [user['money'], user['coin'], user['herbs'], user['metals'], user['leather'], user['cloth'], user['materials'], user['pet']]

    def findUserMartialSkillsByID(self):
        for user in users.find({"_id": self.uid}):
            print("Martial finder done")

        return [user['blade'], user['spear'], user['sword'], user['fist'], user['palm'], user['finger']]

    def findUserSpiritualRootByID(self):
        for user in users.find({"_id": self.uid}):
            print("Spiritual finder done")

        return [user['fire'], user['water'], user['lightning'], user['wind'], user['earth'], user['wood'], user['light'], user["dark"]]

    def findParamByName(self, name):
        for user in users.find({"name": name}):
            print("Name param finder done")
        return [user['name'], user['power'], user['defence'], user['spiritDefence'], user['evade'], user['regeneration'], user['level'], user['exp'], user['points']]
