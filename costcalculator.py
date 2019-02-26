cardboard = .5
maskingTape = .75
popsicleStick = 1
plasticCup = 2

def check(x):
    if x.isdigit():
        return True
    else:
        return False
def materials():

    CQ = input("How many square inches of cardboard was used?: ")
    d1 = check(CQ)
    MQ = input("How many square inches of masking tape was used?: ")
    d2 = check(MQ)
    PSQ = input("How many popsicle sticks were used?: ")
    d3 = check(PSQ)
    PQ = input("How many plastic cups were used?: ")
    d4 = check(PQ)

    if d1 == d2 == d3 == d4 == True:
        Ccost = (float(CQ) * cardboard)
        MTcost = (float(MQ) * maskingTape)
        PScost = (float(PSQ) * popsicleStick)
        PQcost = (float(PQ) * plasticCup)
        total = (Ccost + MTcost + PScost + PQcost)
        print ("cardboard costs: " + str(Ccost) + "$" + " masking tape costs: " + str(MTcost) + "$" + " popsicle stick costs: " + str(PScost) + "$" + " cup costs: " + str(PQcost) + "$")
        print("total amount is " + str(total) + "$")
    else:
        print("You entered and invalid input try again")
        materials()

materials()