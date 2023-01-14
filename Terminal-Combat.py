import random
offensive = True
defensive = False
high = True
low = False
class Fighter:
  def __init__(self, name, move_list):
    self.name = name
    self.stamina = 100
    self.moves = move_list
  defense_height = False
  attack_height = False
  is_player = False
  def __repr__(self):
    return self.name
  def choose_defense(self, defense):
    self.defense_height = defense.height
  def choose_ofence(self, attack):
    self.attack_height = attack.height
    
  def prepare_turn(self, offence, defense):
    self.stamina -= 5
    print("{} Stamina Remaining: {}".format(self.name, self.stamina))
    self.choose_defense(defense)
    self.choose_ofence(offence)

  
class Move:
  def __init__(self, name, style, height):
    self.name = name
    self.style = style
    self.height = height
  def __repr__(self):
    return self.name
  def miss(self, fighter, other_fighter, defensive_move):
    print("{} dodged {}'s {} attack by {}".format(other_fighter, fighter, self, defensive_move))
  def hit(self, other_fighter):
    other_fighter.stamina -= 5
    print("{}'s {} attack hit {} for 5 damage!".format(fighter, self, other_fighter))
  def crit(fighter, self, other_fighter):
    other_fighter.stamina -= 10
    print("{}'s {} attack hit {} for 10 damage!".format(fighter, self, other_fighter))


punch = Move("punching", offensive, high)
kick = Move("kicking", offensive, low)
jump = Move("jumping", defensive, high)
duck = Move("ducking", defensive, low)

default_moves = [punch, kick, jump, duck]

fighter_fred = Fighter("Fighter Fred", default_moves)
battle_beth = Fighter("Battle Beth", default_moves)

fighter_list = [fighter_fred, battle_beth]

#punch.miss(fighter_fred, battle_beth, duck)

battle_beth.prepare_turn(punch, jump)