import time

#palletID: alphanumeric
# part: cylinder, spring
class Pallet:
    def __init__(self, palletID, part):
        self.palletID = palletID
        self.part = part



class Workstation:

    #Class constructor
    def __init__(self, wsID):
        self.wsID = wsID
        self.palletList = []


    def addPallet(self,pallet):
        print (self.wsID + ": Adding pallet " + pallet.palletID)
        self.palletList.append(pallet)

    def displayPallets(self):
        print (self.wsID + ": Displaying Pallets list")
        for p in self.palletList:
            #print "\t" + p.palletID + "\t" + p.part
            print ("\t" + p.palletID)

    def removePallet(self):
        p = self.palletList.pop(0)
        print (self.wsID + ": Removing pallet " + p.palletID)
        return p




p1 = Pallet("p1", "spring")  # Creating a pallet(Class) called p1 (Object)
p2 = Pallet("p2", "cylinder")
p3 = Pallet("p3", "spring")


ws1 = Workstation("ws1")  #creating an object ws1 out of the class (workstation) and giving it an ID ws1

ws1.displayPallets()
# exit()  if run this, the ws1 will have no pallet

ws1.addPallet(p2)  #this add pallet to the workstation ws1
ws1.addPallet(p1)  #this add pallet to the workstation ws2

ws1.displayPallets()

# exit() if run this it will display 2 pallet added

somePallet: Pallet = ws1.removePallet()  # removing a pallet and saving it to a variable called somePallet

print ("ID of the pallet retrieved:"+ somePallet.palletID)
print("the part of the removed pallet is:"+ somePallet.part)

# exit() this would give the information of the removed pallet in order of FIFO

ws1.displayPallets()  #displaying the pallet left after removing one of those added

# exit()


ws2 = Workstation("ws2")
ws2.addPallet(somePallet)  #adding the removed pallet from ws1 to ws2 assuming that this prod

ws2.displayPallets()