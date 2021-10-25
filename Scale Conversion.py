value_ToConvert=float(input("Enter Value To Convert: "))
value_Unit=input("Enter Value Of Unit: ")
value_Unit=value_Unit.lower()
unit_ToConvert=input("Enter Unit To Convert: ")
unit_ToConvert=unit_ToConvert.lower()
if (value_Unit=="m"):
    if(unit_ToConvert=="m"):
        newValue=value_ToConvert*1
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="cm"):
        newValue=value_ToConvert*100
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="mm"):
        newValue=value_ToConvert*1000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="um"):
        newValue=value_ToConvert*1000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="nm"):
        newValue=value_ToConvert*1000000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="pm"):
        newValue=value_ToConvert*100000000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
elif (value_Unit=="cm"):
    if(unit_ToConvert=="m"):
        newValue=value_ToConvert*0.01
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="cm"):
        newValue=value_ToConvert*1
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="mm"):
        newValue=value_ToConvert*10
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="um"):
        newValue=value_ToConvert*10000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="nm"):
        newValue=value_ToConvert*10000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="pm"):
        newValue=value_ToConvert*10000000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
elif(value_Unit=="mm"):
    if(unit_ToConvert=="m"):
        newValue=value_ToConvert*0.001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="cm"):
        newValue=value_ToConvert*0.1
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="mm"):
        newValue=value_ToConvert*1
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="um"):
        newValue=value_ToConvert*10000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="nm"):
        newValue=value_ToConvert*10000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="pm"):
        newValue=value_ToConvert*1000000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
elif (value_Unit=="um"):
    if(unit_ToConvert=="m"):
        newValue=value_ToConvert*0.00001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="cm"):
        newValue=value_ToConvert*0.0001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="mm"):
        newValue=value_ToConvert*0.001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="um"):
        newValue=value_ToConvert*1000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="nm"):
        newValue=value_ToConvert*1
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="pm"):
        newValue=value_ToConvert*1000000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
elif (value_Unit=="nm"):
    if(unit_ToConvert=="m"):
        newValue=value_ToConvert*0.0000001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="cm"):
        newValue=value_ToConvert*0.000001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="mm"):
        newValue=value_ToConvert*0.00001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="um"):
        newValue=value_ToConvert*0.001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="nm"):
        newValue=value_ToConvert*1
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="pm"):
        newValue=value_ToConvert*1000
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
elif (value_Unit=="pm"):
    if(unit_ToConvert=="m"):
        newValue=value_ToConvert*0.00000000001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="cm"):
        newValue=value_ToConvert*0.000000001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="mm"):
        newValue=value_ToConvert*0.000001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="um"):
        newValue=value_ToConvert*0.00001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="nm"):
        newValue=value_ToConvert*0.001
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")
    elif(unit_ToConvert=="pm"):
        newValue=value_ToConvert*1
        print(f"{value_ToConvert} {value_Unit} = {newValue} {unit_ToConvert}")

        

        

        

        

        




    

