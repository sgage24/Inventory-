from peewee import *
from psycopg2 import *


db = PostgresqlDatabase('inventory', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Jewlery(BaseModel):
    title = CharField()
    colors = CharField()
    type = CharField()
    quantity = IntegerField()


db.connect()

db.drop_tables([Jewlery])
db.create_tables([jewlery])


Butterfly Hoop = Jewlery(title='Butterfly Hoop', colorsused='Gold',
                 type='Earings', quantity=25)
Butterfly Hoop.save()


Open Hoop = Jewlery(title='Open Hoop',
                  colorsused='gold/silver', type='Earings', quantity=20)
Open Hoop.save()


Dainty Snake Hoops = Jelwery(title='Dainty Snake', 
                         colorsused='gold', type='Earings', quantity=10)
Dainty Snake Hoops.save()


Sharp shooter = Jewlery(title='Sharp Shooter',
                        colorsused='gold/silver/gunmetal', type='Earings', quantity=15)
Sharp  Shooter.save()

Criss Cross= Jelwery(title='7/11',
              colorsused='Silver', type='Earings', quantity=10)
Criss Cross.save()

Angle Wings = Jewlery(title='Angle Wings', 
               colorsused='gold', type='Earings', quantity=12)
Angle Wings.save()

Shot in the Dark = Jewlery(title='Shot in the Dark',
                          colorsused='gold/silver', type='Earings', quantity=20)
Shot in the Dark.save()

Illusion = Earings(title='Illusion', 
                 colorsused='silver/gold', type='Earings', quantity=20)
Illusion.save()

Name = Jewlery(title='Name', 
                  colorsused='silver/gold', type='Necklace', quantity=20)
Name.save()

Coordinates = Jewlery(title='Coordinates', 
                       colorsused='silver/gold/rose gold', type='Necklace', quantity=45)
Coordinates.save()

Lock & Key = Jelwery(title='Lock & Key', 
                   colorsused='silver/gold', type='Necklace', quantity=25)
Lock & Key.save()

camoCollective = Clothes(title='Camo 2nd Logo', size='l',
                         colorsused='camo/white', type='tShirt', quantity=1)
camoCollective.save()

NoSleep = Clothes(title='No Sleep', size='s, m, l',
                  colorsused='white/green/blue/black', type='tShirt', quantity=3)
NoSleep.save()

WerdPant = Clothes(title='Repeating Logo Pants', size='30/32',
                   colorsused='navy blue/white/red', type='pant', quantity=1)
WerdPant.save()

EyePant = Clothes(title='Eye pants', size='32/34',
                  colorsused='black/white/red', type='pant', quantity=1)
EyePant.save()

LoveHurtsSweats = Clothes(title='Love Hurts', size='m',
                          colorsused='black/white/yellow/green', type='sweat pant', quantity=1)
LoveHurtsSweats.save()

LoveHurtsCrewneck = Clothes(title='Love Hurts', size='m',
                            colorsused='black/white/red', type='crew neck', quantity=1)
LoveHurtsCrewneck.save()

LogoShorts = Clothes(title='Logo Shorts', size='m',
                     colorsused='white/black', type='shorts', quantity=1)
LogoShorts.save()

InfiniteThought = Clothes(title='Infinite Thought', size='m',
                          colorsused='tan/black/blue', type='hoodie', quantity=1)
InfiniteThought.save()

ReaperSweats = Clothes(title='Reaper', size='m',
                       colorsused='gray/black/red', type='sweat pant', quantity=1)
ReaperSweats.save()

CartiJeanJacket = Clothes(title='Playboi Carti Jean Jacket', size='l',
                          colorsused='black/green/red/white', type='jean jacket', quantity=1)
CartiJeanJacket.save()

werdXchampionFlowers = Clothes(title='Werd x Champion', size='m',
                               colorsused='navy blue/white/green/yellow', type='hoodie', quantity=1)
werdXchampionFlowers.save()

Sakura = Clothes(title='Sakura', size='m, l, xl',
                 colorsused='white/red/pink/blue', type='hoodie', quantity=4)
Sakura.save()


NeonLogo = Clothes(title='Neon Logo', size='xl',
                   colorsused='neon green/red', type='tShirt', quantity=1)
NeonLogo.save()

JapanesesWerdShort = Clothes(
    title="'Werd' Shorts", size='m', colorsused='white', type='shorts', quantity=1)
JapanesesWerdShort.save()

OxymoronHoodie = Clothes(title='Oxy-moron', size='l',
                         colorsused='blue/black/yellow/green', type='hoodie', quantity=1)
OxymoronHoodie.save()

WhatchuWant = Clothes(title='Whatchu want from me', size='m, l',
                      colorsused='white/black/green/blue', type='tShirt', quantity=3)
WhatchuWant.save()


WhatchuWantHoodie = Clothes(title='Whatchu want from me', size='m',
                            colorsused='white/black/green/blue', type='hoodie', quantity=2)
WhatchuWantHoodie.save()


WhyTshirt = Clothes(title='Why', size='m, l, xl',
                    colorsused='white/brown/black/green', type='tShirt', quantity=4)
WhyTshirt.save()

FlipSide = Clothes(title='Flip Side', size='m, l, xl',
                   colorsused='white/black/blue/', type='tShirt', quantity=5)
FlipSide.save()

LongSleeveLogo = Clothes(title='Long Sleeve Logo', size='m, l, xl',
                         colorsused='white/red', type='long sleeve', quantity=3)
LongSleeveLogo.save()


Spider = Clothes(title='Spider', size='m',
                 colorsused='black/white/orange', type='tShirt', quantity=1)
Spider.save()


NavyBlueLogo = Clothes(title='Navy Blue Logo', size='m',
                       colorsused='navy blue/white/red', type='tShirt', quantity=1)
NavyBlueLogo.save()

NoHardFeelings = Clothes(title='No Hard Feelings', size='m',
                         colorsused='navy blue/yellow/red', type='tShirt', quantity=1)
NoHardFeelings.save()

AllEveryEverWanted = Clothes(title='All Everybody Ever Wanted', size='m',
                             colorsused='tan/navy blue/white', type='tShirt', quantity=1)
AllEveryEverWanted.save()

SeeYouNever = Clothes(title='See You Never', size='m, l',
                      colorsused='black/red/white', type='hoodie', quantity=3)
SeeYouNever.save()


print('')
print('      #######################################')
print('                  Werd Inventory')
print('      #######################################')
print('')

print('#### TYPES OF JEWLERY: earings, necklaces, rings, bracelets, cuffs ####')
print('')

cur = db.cursor()

inputType = input(
    '-- -- Search type or "all" to view all items: ')


if inputType == 'all':
    cur.execute(
        f"SELECT title from CLOTHES")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or "all" to view all items: ')
    else:
        cur.execute(
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')


if inputType == 'hoodie' or 'tShirt' or 'pant' or 'shorts' or 'crew neck':

    cur.execute(
        f"SELECT title, type from CLOTHES WHERE type = '{inputType}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Type: ', row[1])
        print('')
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or "all" to view all items: ')
    else:
        cur.execute(
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')

# inputType = input(
#     '-- -- Search type or "all" to view all items: ')


if inputType == 'all':
    cur.execute(
        f"SELECT title from CLOTHES")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or click enter to view all items: ')
    else:
        cur.execute(
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')


if inputType == 'hoodie' or 'tShirt' or 'pant' or 'shorts' or 'crew neck':

    cur.execute(
        f"SELECT title, type from CLOTHES WHERE type = '{inputType}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Type: ', row[1])
        print('')
    inputTitle = input('Search for individual item or type back to return: ')
    if inputTitle == 'back':
        inputType = input(
            '-- -- Search type or click enter to view all items: ')
    else:
        cur.execute(
            f"SELECT title, size, colorsused, type, quantity from CLOTHES WHERE title = '{inputTitle}'")
    rows = cur.fetchall()
    for row in rows:
        print('---')
        print('Name: ', row[0])
        print('Size(s) available: ', row[1])
        print('Colors Used: ', row[2])
        print('Type: ', row[3])
        print('Quantity: ', row[4])
        print('')
