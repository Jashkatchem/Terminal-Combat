import random


offensive = True
defensive = False
high = 0
low = 1
player_fighter = 0
input_list = ["1", "2"]

class Fighter:
  def __init__(self, name, move_list):
    self.name = name
    self.stamina = 100
    self.moves = move_list
  defense_height = 1
  attack_height = 1
  is_player = False
  def __repr__(self):
    return self.name
  def staminacalc(self, other_fighter):
    print("""
    {} stamina remaining: {}
    {} stamina remaining: {}
    """.format(self.name, self.stamina, other_fighter.name, other_fighter.stamina))

  
class Move:
  def __init__(self, name, style, height):
    self.name = name
    self.style = style
    self.height = height
  def __repr__(self):
    return self.name
  def miss(self, fighter, other_fighter, defensive_move):
    print("{} dodged {}'s {} attack by {}".format(other_fighter, fighter, self, defensive_move))
  def hit(self, fighter, other_fighter):
    other_fighter.stamina -= 10
    print("{}'s {} attack hit {} for 10 damage!".format(fighter, self, other_fighter))
  def crit(self, fighter,  other_fighter):
    other_fighter.stamina -= 20
    print("{}'s {} attack CRITICALLY HIT {} for 20 damage!".format(fighter, self, other_fighter))


punch = Move("punching", offensive, 0)
kick = Move("kicking", offensive, 1)
jump = Move("jumping", defensive, 0)
duck = Move("ducking", defensive, 1)

default_moves = [punch, kick, jump, duck]
offensive_moves = [punch, kick]
defensive_moves = [jump, duck]

fighter_fred = Fighter("Fighter Fred", default_moves)
battle_beth = Fighter("Battle Beth", default_moves)

fighter_list = [fighter_fred, battle_beth]

player_attack = offensive_moves[0]
player_defend = defensive_moves[0]
nonplayer_attack = offensive_moves[0]
nonplayer_defend = defensive_moves[0]

def chooseattack(pc, npc):
  print("""
  -------Choose your attack-------
  1.Punch    2. Kick
  """)
  chosen_attack = 0
  while chosen_attack not in input_list:
    chosen_attack = input("1 or 2: ")
  pc.attack_height = int(chosen_attack) - 1
  print("You chose {}!".format(offensive_moves[pc.attack_height]))
  npc.attack_height = random.randint(0,1)
  #print("They chose {}!".format(offensive_moves[npc.attack_height]))

def choosedefense(pc, npc):
  print("""
  -------Choose your defense-------
  1.Jump    2. Duck
  """)
  chosen_defense = 0
  while chosen_defense not in input_list:
    chosen_defense = input("1 or 2: ")
  pc.defense_height = int(chosen_defense) - 1
  print("You chose {}!".format(defensive_moves[pc.defense_height]))
  npc.defense_height = random.randint(0,1)
  #print("They chose {}!".format(defensive_moves[npc.defense_height]))

def resolveround(pc, npc):
  print("-----------Your turn------------")
  if pc.attack_height == npc.defense_height:
    is_crit = random.randint(1, 4)
    if is_crit == 4:
      offensive_moves[pc.attack_height].crit(pc, npc)
    else:
      offensive_moves[pc.attack_height].hit(pc, npc)
  else:
    offensive_moves[pc.attack_height].miss(pc, npc, defensive_moves[npc.defense_height])
  print("-----------Their Turn------------")
  if npc.attack_height == pc.defense_height:
    is_crit = random.randint(1, 4)
    if is_crit == 4:
      offensive_moves[npc.attack_height].crit(npc, pc)
    else:
      offensive_moves[npc.attack_height].hit(npc, pc)
  else:
    offensive_moves[npc.attack_height].miss(npc, pc, defensive_moves[pc.defense_height])

def round(pc, npc):  
  roundnum = 0
  while pc.stamina > 0 and npc.stamina > 0:
    roundnum += 1
    print("!!!!!!!!!Round {}! FIGHT!!!!!!!!!!".format(roundnum))
    pc.staminacalc(npc)
    chooseattack(pc, npc)
    choosedefense(pc, npc)
    resolveround(pc, npc)
    pc.stamina -= 5
    npc.stamina -= 5
  if pc.stamina <= 0 and npc.stamina <= 0:
    print("""
    \n
    ---------------TIE----------
    You are almost there...
    """)
  elif pc.stamina <= 0 and npc.stamina > 0:
    print("""
    \n
    /////////////YOU LOSE////////////
    Go train a while...
    """)
  else: 
    print("""
    \n
    ************YOU WON*************
    CONGRATS!
    """)
  
  


print("""
!!!!!!!WELCOME TO THE ARENA!!!!!!!

|-------Choose your fighter-------|
1. Fighter Fred    2. Battle Beth
""")


while player_fighter not in input_list:
  player_fighter = input("1 or 2: ")

if player_fighter == "1":
  fighter_fred.is_player = True
  player_fighter = fighter_fred
  print("You have chosen: Fighter Fred!")
elif player_fighter == "2":
  battle_beth.is_player = True
  player_fighter = battle_beth
  print("You have chosen: Battle Beth!")

for guy in fighter_list:
  if guy != player_fighter:
    nonplayer_fighter = guy

round(player_fighter, nonplayer_fighter)
