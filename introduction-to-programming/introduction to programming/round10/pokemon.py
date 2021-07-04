# This dict is a global constant, that will be used to determine the
# effectiveness factor of the Pokémon attacks. The keys of this dict are 
# Pokémon types. The values related to the keys are dicts, where the keys 
# are attack types and values are the effect factors of the attacks.
# Example: a Ghost-type attack toward a Normal-type Pokémon causes 0.8* damage
# and a Fighting-type attack toward the same Pokémon causes 1.25* damage.
TYPES = {"Normal": {"Fighting": 1.25, "Ghost": 0.8},
         "Fighting": {"Flying": 1.25, "Psychic": 1.25, "Fairy": 1.25,
                      "Rock": 0.8, "Bug": 0.8, "Dark": 0.8},
         "Flying": {"Electric": 1.25, "Rock": 1.25, "Ice": 1.25, "Grass": 0.8,
                    "Bug": 0.8, "Fighting": 0.8, "Ground": 0.8},
         "Poison": {"Ground": 1.25, "Psychic": 1.25, "Fighting": 0.8,
                    "Bug": 0.8, "Poison": 0.8, "Grass": 0.8, "Fairy": 0.8},
         "Ground": {"Water": 1.25, "Grass": 1.25, "Ice": 1.25, "Poison": 0.8,
                    "Rock": 0.8, "Electric": 0.8},
         "Rock": {"Fighting": 1.25, "Ground": 1.25, "Steel": 1.25,
                  "Water": 1.25, "Grass": 1.25, "Normal": 0.8, "Flying": 0.8,
                  "Poison": 0.8, "Fire": 0.8},
         "Bug": {"Flying": 1.25, "Rock": 1.25, "Fire": 1.25, "Fighting": 0.8,
                  "Ground": 0.8, "Grass": 0.8},
         "Ghost": {"Ghost": 1.25, "Dark": 1.25, "Bug": 0.8, "Poison": 0.8,
                    "Normal": 0.8, "Fighting": 0.8},
         "Steel": {"Fighting": 1.25, "Ground": 1.25, "Fire": 1.25,
                    "Normal": 0.8, "Flying": 0.8, "Rock": 0.8, "Bug": 0.8,
                    "Steel": 0.8, "Grass": 0.8, "Psychic": 0.8, "Ice": 0.8,
                    "Dragon": 0.8, "Fairy": 0.8, "Poison": 0.8},
         "Fire": {"Ground": 1.25, "Rock": 1.25, "Water": 1.25, "Bug": 0.8,
                   "Steel": 0.8, "Fire": 0.8, "Ice": 0.8, "Fairy": 0.8},
         "Water": {"Grass": 1.25, "Electric": 1.25, "Steel": 0.8, "Fire": 0.8,
                    "Water": 0.8, "Ice": 0.8},
         "Grass": {"Flying": 1.25, "Poison": 1.25, "Bug": 1.25, "Fire": 1.25,
                    "Ice": 1.25, "Ground": 0.8, "Water": 0.8, "Grass": 0.8,
                    "Electric": 0.8},
         "Electric": {"Ground": 1.25, "Flying": 0.8, "Steel": 0.8,
                       "Electric": 0.8},
         "Psychic": {"Bug": 1.25, "Ghost": 1.25, "Dark": 1.25, "Fighting": 0.8,
                      "Psychic": 0.8},
         "Ice": {"Fighting": 1.25, "Rock": 1.25, "Steel": 1.25, "Fire": 1.25,
                  "Ice": 1.25},
         "Dragon": {"Ice": 1.25, "Dragon": 1.25, "Fairy": 1.25, "Fire": 0.8,
                     "Grass": 0.8, "Water": 0.8, "Electric": 0.8},
         "Dark": {"Fighting": 1.25, "Bug": 1.25, "Fairy": 1.25, "Ghost": 0.8,
                   "Psychic": 0.8},
         "Fairy": {"Poison": 1.25, "Steel": 1.25, "Fighting": 0.8, "Bug": 0.8,
                    "Dark": 0.8, "Dragon": 0.8}}

def factor(attack_type, pokemon_type):
    """
    Finds the effectiveness factor of an attack from the above defined 
    datastructure.
    :param attack_type: String
    :param pokemon_type: String
    :return: Returns the effectiveness factor of the attack
    """
    if pokemon_type in TYPES:

        if attack_type in TYPES[pokemon_type]:
            return TYPES[pokemon_type][attack_type]

    return 1

class Pokemon:
    """ Implements one Pokémon that has a name, types, hitpoints, level 
    and moves."""

    def __init__(self, species, types, hp=50, level=20):
        """
        Constructor of the class. Checks the kesto and level and stores
        the attributes.

        :param species: the species of the pokemon
        :param types:   the types of the pokemon
        :param hp:      the hp of the pokemon
        :param level:   the level of the pokemon
        """

        self.__species = species.capitalize()
        self.__types = types

        if not isinstance(hp, int) or not isinstance(level, int) \
                or hp < 0 or level < 1:
            raise ValueError

        self.__hp = hp
        self.__max_hp = hp
        self.__level = level
        self.__moves = {}

    def info(self):
        """
        Prints information in the form of species, types, hp.
        """
        print(self.__species, ", ", self.__hp, "hp", ", Types: ",
              ", ".join(self.__types), sep="")
        print()

    def damage(self,val):
        if val<0:
            return False
        else:
            if self.__hp>=val:
                self.__hp-=val
                print(str(self.__species) + ' lost ' + str(val) + ' hp.')
            else:
                print(str(self.__species)+' lost '+str(self.__hp)+' hp.')
                self.__hp = 0
                print(self.__species+' fainted!')
            return True

    def heal(self,val):
        if val<0:
            return False
        else:
            if self.__hp+val<=self.__max_hp:
                self.__hp+=val
                print(str(self.__species) + ' healed for ' + str(val) + ' hp.')
            else:
                print(str(self.__species)+' healed for '+str(self.__max_hp)+' hp.')
                self.__hp = self.__max_hp
            return True

    def set_types(self,list):
        for x in list:
            if x not in TYPES:
                return False
            elif x in TYPES:
                self.__types=list
                return True

    def add_type(self,kind):
        if kind.title() not in TYPES:
            return False
        elif kind.title() in TYPES and kind not in self.__types:
            self.__types.append(kind.title())
            return True
        elif kind in self.__types:
            return True

    def add_move(self,name,power,type):
        list=sorted(self.__moves)
        if len(list)<2:
            self.__moves[name.title()]=[name.title(),power,type]
            return True
        else:
            print(False)
            return False

    def move_info(self):
        arraged=sorted(self.__moves)
        print(self.__species + "'s " + "moves:")
        for x in range(len(arraged)):
            list=self.__moves[arraged[x]]
            print(list[0]+', '+str(list[1])+', '+list[2])

    def attack(self,move,enemy):
        print(self.__species+' used '+move)
        if move not in self.__moves:
            return False
        elif move in self.__moves:
            tackle=self.__moves[move]
            charged=tackle[1]



pikachu = Pokemon("Pikachu", ["Electric"])
rattata = Pokemon("Rattata", ["Normal"])
pikachu.info()
rattata.info()

