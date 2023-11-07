# random naam voor 1 (een) AI

import random
from faker import Faker
fake = Faker(["nl_NL"])
import locale
locale.setlocale (locale.LC_TIME, "nl_NL")

lijstNAMEN = []
lijstNAMENdef = ["Tauva Simons"]
def namenlijst():
    NAMEN = fake.name()
    lijstNAMEN.append(NAMEN)
for _ in range(50):
    namenlijst()
for xA in lijstNAMEN:
    if "-" not in xA:
        lijstNAMENdef.append(xA)

randomfullname = random.choice(lijstNAMENdef)

index = randomfullname.index(" ")

randomfirstname = randomfullname[:index]

randomlastname = randomfullname[index + 1:]
randomlastname = randomlastname.capitalize()