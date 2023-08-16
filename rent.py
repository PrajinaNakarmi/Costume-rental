def getFiles():
    '''fetching data from the file ''' 
    file = open("Costumes.txt", "r") 
    data = file.readlines()
    file.close()
    return data

def dictionary(fileContent):
    data = {}
    for index in range(len(fileContent)):
        data[index + 1] = fileContent[index].replace("\n", "").split(",")
    return data

def printCostumes(fileContent, mainData):
#printing customes
    print("------------------------------------------------------------------------")
    print("SNo", "\t", "Costume Name", "\t", "Brand", "\t\t", "Price", "\t", "Quantity")
    print("---------------------------------------------------------------------\n")
    for key,value in mainData.items(): 
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3])

    print("\n-------------------------------------------------------------\n")
def writeFile(mainData):
    '''writing in txt file'''
    file = open("Costumes.txt", "w")
    for value in mainData.values():
        writeData = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n"
        file.write(writeData)
    file.close()
    
def dateTime():
    import datetime
#import date and time
    date = (datetime.datetime.now())
    return date

def vIdRent(mainData):
    '''to check the validity of id for renting'''
    vData = False
    while vData == False:
        try:
            ID = int(input("Enter the ID of the costume you want to rent: "))
            if ID > 0 and ID <= len(mainData):
                if int(mainData[ID][3]) > 0:
                    vData = True
                    return ID
        except ValueError:
            
                print("Invalid Data!!Enter ID in integer!!")
                print("-----------------------------------\n")
        else:
                print("\n**************************")
                print("      Out of Stock!!         ")
                print("*****************************\n")
           
            
def vQuantityRent(mainData, ID):
    
    vData = False
    while vData == False:
        try:
            q = int(input("How many pieces do you want to rent? "))
            if q > 0 and q <= int(mainData[ID][3]):
                vData = True
                return q
            
        except ValueError:
            
            print("Invalid Data!!Enter ID in integer!!")
            print("-----------------------------------\n")
         
        else:
            print("\n************************")
            print("Out of our costumes range.")
            print("*************************\n")
        
def rBillList(cart):

    fileContent = getFiles()
    mainData = dictionary(fileContent)
    try:
        
        name = input("Please enter your Name: ")
        contact = input("Please enter your Contact Number: ")
    except ValueError:
        print("Enter your name in string and contact number in integer!!")
        
        
    print()
    print("\n                           BILL                               \n")
    print("\n" + "Name: " + name)
    print("Phone no.: " + contact)

        
    print("--------------------------------------------------------------------------")
    print("SNo", "\t", "Costume Name", "\t", "Brand", "\t\t", "Price", "\t", "Quantity")
    print("------------------------------------------------------------------------\n")

    total = 0
    for index in range(len(cart)):
        CId = int(cart[index][0])
        CQuantity = int(cart[index][1])
        CName = mainData[CId][0]
        CBrand = mainData[CId][1]
        CPrice = int(mainData[CId][2].replace("$", "")) * CQuantity
        total += CPrice
        
        print(str(index + 1) , "\t" , CName , "\t" , CBrand , "\t" , str(CPrice) , "\t" , str(CQuantity))
        print("\n")
        
    print("Your Grand Total is:  " + str(total))
    date = dateTime()
    print("Rent Date: " + str(date) + "\n")
  
    f = open(name + ".txt" , "w")

    f.write("\n                           BILL                             \n")
    f.write("\n" + "Name: " + name + "\n")
    f.write("Phone Number.: " + contact + "\n")
    
        
    f.write("-------------------------------------------------------------")
    f.write("\nSNo\tCostume Name\tBrand\t\tPrice\tQuantity\n")
    f.write("-------------------------------------------------------------\n\n")

    total = 0
    for index in range(len(cart)):
        CId = int(cart[index][0])
        CQuantity = int(cart[index][1])
        CName = mainData[CId][0]
        CBrand = mainData[CId][1]
        CPrice = int(mainData[CId][2].replace("$", "")) * CQuantity
        total += CPrice
        
        f.write(str(index + 1) + "\t" + CName + "\t" + CBrand + "\t" + str(CPrice) + "\t" + str(CQuantity))
        f.write("\n\n")
        
      
    f.write("Grand Total: " + str(total))
    date = dateTime()
    f.write("Rent Date: " + str(date) + "\n\n")

    f.write("\n\n**********************************************************************")
    f.write("\n              Thank you.Your costumes have been rented!!        \n")
    f.write("************************************************************************")

    f.close()

        
def rent():
    print("\n Let's rent a costume. \n")
    
    fileContent = getFiles()
    mainData = dictionary(fileContent)

    cart = []
    continueLoop = True
    while continueLoop == True:
        printCostumes(fileContent, mainData)
        Id = vIdRent(mainData)
        print("\n****************************")
        print("      Costume is available!!  ")
        print("*****************************\n")
        p = int(vQuantityRent(mainData, Id))
        mainData[Id][3] = int(mainData[Id][3]) - p
        cart.append([Id, p])

        writeFile(mainData)
        printCostumes(fileContent, mainData)
        try:
            userInput = input("Do you want to rent more costumes? ")
        except ValueError:
            
            print("Invalid Data!!Enter ID in integer!!")
            print("-----------------------------------\n")
        if userInput.lower() == "no":
            continueLoop = False
    
    print()
    printCostumes(fileContent, mainData)
    rBillList(cart)
    print("\n******************************************************")
    print("      Thank you. Your costume has been rented!!         ")
    print("******************************************************\n")
