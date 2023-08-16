def getFiles():
    
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
    
    print("-------------------------------------------------------------")
    print("SNo", "\t", "Costume Name", "\t", "Brand", "\t\t", "Price", "\t", "Quantity")
    print("-------------------------------------------------------------\n")
    for key,value in mainData.items(): 
        print(key, "\t", value[0], "\t", value[1], "\t", value[2], "\t", value[3])

    print("\n-------------------------------------------------------------\n")
    
def dateTime():
    import datetime
    

    date = (datetime.datetime.now())
    return date

def vIdReturn(mainData):
    
    vData = False
    while vData == False:
        try:
            ID = int(input("Enter the ID of the costume you want to return: "))
            if ID > 0 and ID <= len(mainData):
                    vData = True
                    return ID
        except ValueError:
                    print("Invalid Data!!Enter ID in integer!!")
                    print("-----------------------------------\n")
                
        else:
                
                    print("\n**************************")
                    print("    Invalid Input!!!       ")
                    print("*****************************\n")
       
            
def vQuantityReturn(mainData, ID):
    
    vData = False
    while vData == False:
        try:
            q = int(input("How many pieces do you want to return? "))
            if q > 0:
                vData = True
                return q
            else:
                print("Invalid Input!!")
        except ValueError:
            print("You are supposed to enter integer!!")
def writeFile(mainData):
    
    file = open("Costumes.txt", "w")
    for value in mainData.values():
        writeData = str(value[0]) + "," + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + "\n"
        file.write(writeData)
        '''closing txt file'''
    file.close()

def dateTime():
    
    import datetime

    date = (datetime.datetime.now())
    return date

def rtBillList(cart):
    '''return bill'''
    fileContent = getFiles()
    mainData = dictionary(fileContent)

    name = input("Please enter your name: ")
    contact = input("Please enter your contact number: ")
    Renteddays= int(input("How many days has it been since you rented the costume? "))
    '''fine'''
    extraDays = 0
    fine = 0
    if Renteddays > 7:
        extraDays = Renteddays - 7

    if extraDays > 0:
        fine = 7 * extraDays

    print()
    print("\n                           BILL                            ")
    print("\n" + "Name: " + name)
    print("Phone Number.: " + contact)
   
        
    print("-------------------------------------------------------------")
    print("SNo", "\t", "Costume Name", "\t", "Brand", "\t\t", "Price", "\t", "Quantity")
    print("-------------------------------------------------------------\n")

    totalQuantity = 0
    for index in range(len(cart)):
        CId = int(cart[index][0])
        CQuantity = int(cart[index][1])
        CName = mainData[CId][0]
        CBrand = mainData[CId][1]
        CPrice = int(mainData[CId][2].replace("$", "")) * CQuantity

        totalQuantity += CQuantity
        totalFine = fine * totalQuantity
        
        print(str(index + 1) , "\t" , CName , "\t" , CBrand , "\t" , str(CPrice) , "\t" , str(CQuantity))
        print("\n")

    print("Fine = " + str(totalFine) + "\n")
    date = dateTime()
    print("Return Date: " + str(date))
    print("No of Days Rented: " + str(Renteddays) + "\n")


    f = open(name + ".txt" , "w")
    
    f.write("\n                          BILL                              \n")
    f.write("\n" + "Name: " + name + "\n")
    f.write("Phone Number.: " + contact + "\n")
    
        
    f.write("----------------------------------------------------------------")
    f.write("\nSNo\tCostume Name\tBrand\t\tPrice\tQuantity\n")
    f.write("--------------------------------------------------------------\n\n")

    totalQuantity = 0
    for index in range(len(cart)):
        CId = int(cart[index][0])
        CQuantity = int(cart[index][1])
        CName = mainData[CId][0]
        CBrand = mainData[CId][1]
        CPrice = int(mainData[CId][2].replace("$", "")) * CQuantity
        totalQuantity += CQuantity
        totalFine = fine * totalQuantity
        
        f.write(str(index + 1) + "\t" + CName + "\t" + CBrand + "\t" + str(CPrice) + "\t" + str(CQuantity))
        f.write("\n\n")
        
    f.write("-------------------------------------------------------------\n\n")
      
    f.write("Fine: " + str(totalFine))
    date = dateTime()
    f.write("Return Date: " + str(date) + "\n\n")

    f.write("\n\n************************************************************************")
    f.write("\n            Thank you! The costumes have been returned.                 \n")
    f.write("****************************************************************************")

    f.close()

    
def Return():
    print("\n Let's return a costume. \n")
    
    fileContent = getFiles() 
    mainData = dictionary(fileContent)

    cart = [] 
    continueLoop = True
    while continueLoop == True:
        printCostumes(fileContent, mainData)
        Id = vIdReturn(mainData)
        p = int(vQuantityReturn(mainData, Id))
        mainData[Id][3] = int(mainData[Id][3]) + p
        cart.append([Id, p])

        writeFile(mainData)
        printCostumes(fileContent, mainData)
        try:
            userInput = input("Do you want to return more costumes? ")
            if userInput.lower() == "no":
                continueLoop = False
        except ValueError:
            print("You are supposed to enter a string")
    print()
    printCostumes(fileContent, mainData)
    rtBillList(cart)
    '''thankyou message'''
    print("\n******************************************************")
    print("      Thank you. The costume has been returned!!        ")
    print("******************************************************\n")
