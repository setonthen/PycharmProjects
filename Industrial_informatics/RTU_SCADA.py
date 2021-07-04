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
        self.status="IDLE"
        self.__prevStatus="IDLE"


    def addPallet(self,pallet):

        if (len(self.palletList)<2):
            print(self.wsID + ": Adding pallet " + pallet.palletID)
            self.palletList.append(pallet)
            self.__notifyPalletList()
            self.__setWSstatusAndNotify("BUSY")
        else:
            print(self.wsID + ": Request Rejected - Workstation has already a maximum of pallets(2)")



    def displayPallets(self):
        print (self.wsID + ": Displaying Pallets list")
        for p in self.palletList:
            #print "\t" + p.palletID + "\t" + p.part
            print ("\t" + p.palletID+ "-"+p.part)

    def removePallet(self):
        if (len(self.palletList) >0):
            p = self.palletList.pop(0)
            print (self.wsID + ": Removing pallet " + p.palletID+ "-"+p.part)
            self.__notifyPalletList()

            if (len(self.palletList) ==0):
                self.__setWSstatusAndNotify("IDLE")

            return p
        else:
            print (self.wsID + ": No pallets in the workstation to be removed")

    def getStatusAndPalletsList(self):
        print(self.wsID + ": workstation status is:"+self.status)
        self.displayPallets()

    def forceStatus(self,newStatus):
        self.__setWSstatusAndNotify(newStatus)

    def __notifyPalletList(self):
        print(self.wsID + ":notifying Pallets List to SCADA backend")

    def __notifyWSStatus(self):
        print(self.wsID + ":notifying WS status to SCADA backend, new state: "+self.status)

    #sets the WS status and triggers notification if the WS status has changed
    def __setWSstatusAndNotify(self,newStatus):

        if (newStatus!=self.__prevStatus):
            print(self.wsID + ":Setting status to: "+newStatus)
            self.status=newStatus
            self.__prevStatus=self.status
            self.__notifyWSStatus()


wsObj = Workstation("ws1")

while True:
    userOptions="""
    ***********************************
    1) Add a pallet
    2) Remove pallet
    3) Get workstation general status
    4) Force workstation status
    """
    print(userOptions)
    sel = input("Enter your selection: ")
    selNum=int(sel)
    #print(sel)

    if (selNum==1):
        print("**Adding a pallet")
        palletID = input("Provide a pallet ID:")
        palletParts = """
            1) spring
            2) cylinder
            3) valve
            """
        print(palletParts)
        partSel = input("select the part:")
        numPart=int(partSel)

        if (numPart==1):
           partStr="spring"
        elif (numPart==2):
            partStr="cylinder"
        elif (numPart == 3):
            partStr = "valve"
        else:
            partStr="spring"

        somePallet=Pallet(palletID, partStr)
        wsObj.addPallet(somePallet)

    elif(selNum==2):
        print("**Removing a pallet")
        wsObj.removePallet();

    elif(selNum==3):
        print("**Workstation status and pallets list")
        wsObj.getStatusAndPalletsList();

    elif(selNum==4):
        print("**Force workstation status")

        statusOptions = """
                    1) IDLE
                    2) BUSY
                    3) ERROR
                    """
        print(statusOptions)
        statusSel = input("select the status:")
        numStatus = int(statusSel)

        if (numStatus == 1):
            statusStr = "IDLE"
        elif (numStatus == 2):
            statusStr = "BUSY"
        elif (numStatus == 3):
            statusStr = "ERROR"
        else:
            statusStr = "IDLE"
        wsObj.forceStatus(statusStr);

    else:
        print("Not valid command, try again")