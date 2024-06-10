import home as h

def choice():
    d={}
    print()
    print("=================")
    print("|  1.Breakfast  |")
    print("|  2.Lunch      |")
    print("|  3.Dinner     |")
    print("=================")
    n = int(input("Enter your choice : "))
    if n==1:
        iteam = ["Pineapple","Orange","Tea","Coffee","Lassi","Khaman","Palak Dhokla","Thepla","Vadharelo Rotlo","Vadharelu Dahi","Aloo Paratha","Plain Curd"]
        price = [20,20,30,40,30,70,80,80,80,90,90,90]
        flag = True
        while flag:
            print("================================")
            print("|                              |")
            print("|          BREAKFAST           |")
            print("|                              |")
            print("|  FRUIT JUICE                 |")
            print("|    1-Pineapple         ___$20|")
            print("|    2-Orange            ___$20|")
            print("|  -------------------         |")
            print("|  HOT BEVERAGE                |")
            print("|    3-Tea               ___$30|")
            print("|    4-Coffee            ___$40|")
            print("|    5-Lassi             ___$30|")
            print("|  -------------------         |")
            print("|  BREAKFAST                   |")
            print("|    6-Khaman            ___$70|")
            print("|    7-Palak Dhokla      ___$80|")
            print("|    8-Thepla            ___$80|")
            print("|    9-Vadharelo Rotlo   ___$80|")
            print("|    10-Vadharelu Dahi   ___$90|")
            print("|    11-Aloo Paratha     ___$90|")
            print("|    12-Plain Curd       ___$90|")
            print("================================")
            print()
            print(d)
            print()
            print("=== Press 0  when you finish your choice ===")
            print("=== Press 13 if you want to remove any thing ===")
            print("=== Press 14 for change quantity of any iteam ===")
            print()
            n = int(input("Enter no : "))
            if n>0 and n<13:
                n1 = int(input("Enter quantity : "))
                d[iteam[n-1]] = n1
            elif n==0:
                flag=False
            elif n==13:
                i = int(input("Enter iteam no : "))
                if iteam[i-1] in d:
                    del d[iteam[i-1]]
                else:
                    print("-- Item not in your list --")
            elif n==14:
                i1 = int(input("Enter iteam no : "))
                if iteam[i1-1] in d:
                    i2 = int(input("Enter new quantity : "))
                    d[iteam[i1-1]]  = i2
                else:
                    print("-- Item not in your list --")        
            else:
                print("==== Please Enter write choice ====")
        def space(s):
            st = ""
            i = len(s)
            while i<18:
                st += " "
                i += 1
            return st
        def space1(s):
            st = ""
            s1 = str(s)
            i = len(s1)
            while i<9:
                st += " "
                i += 1
            return st
        sum = 0
        print()
        print("        YOUR BILL         ")
        print("==========================")
        print("| ITEM               QUN.|")
        print("| ---------------------- |")
        for i in d:
            s = iteam.index(i)
            sum += (price[s]*d[i])
            print("|",i,space(i),d[i]," |")
        print("| ---------------------- |")
        print("|     TOTAL =",sum,space1(sum),"|")
        print("==========================")
            
    elif n==2:
        iteam = ["Papad Fried","Tomato Soup","Veg Soup","Undhiyu","Mix sabji","Shahi Paneer","Paneer Tawa","Daal Makhni","Dal Fry","Mohan Thal","Tava  Roti","Tanduri  Roti"]
        price = [20,30,30,100,120,130,130,150,150,200,15,20]
        flag = True
        while flag:
            print("================================")
            print("|                              |")
            print("|            LUNCH             |")
            print("|                              |")
            print("|  STARTER                     |")
            print("|    1-Papad Fried     ____$20 |")
            print("|    2-Tomato Soup     ____$30 |")
            print("|    3-Veg Soup        ____$30 |")
            print("|  Sabji                       |")
            print("|    4-Undhiyu         ____$100|")
            print("|    5-Mix sabji       ____$120|")
            print("|    6-Shahi Paneer    ____$130|")
            print("|    7-Paneer Tawa     ____$130|")
            print("|                              |")
            print("|    8-Daal Makhni     ____$150|")
            print("|    9-Dal Fry         ____$150|")
            print("|  Sweet                       |")
            print("|    10-Mohan Thal     ____$200|")
            print("|  Roti                        |")
            print("|    11-Tava  Roti     ____$15 |")
            print("|    12-Tanduri  Roti  ____$20 |")
            print("================================")
            print()
            print(d)
            print()
            print("=== Press 0  when you finish your choice ===")
            print("=== Press 13 if you want to remove any thing ===")
            print("=== Press 14 for change quantity of any iteam ===")
            print()
            n = int(input("Enter no : "))
            if n>0 and n<13:
                n1 = int(input("Enter quantity : "))
                d[iteam[n-1]] = n1
            elif n==0:
                flag=False
            elif n==13:
                i = int(input("Enter iteam no : "))
                if iteam[i-1] in d:
                    del d[iteam[i-1]]
                else:
                    print("-- Item not in your list --")
            elif n==14:
                i1 = int(input("Enter iteam no : "))
                if iteam[i1-1] in d:
                    i2 = int(input("Enter new quantity : "))
                    d[iteam[i1-1]]  = i2
                else:
                    print("-- Item not in your list --")        
            else:
                print("==== Please Enter write choice ====")
        def space(s):
            st = ""
            i = len(s)
            while i<18:
                st += " "
                i += 1
            return st
        def space1(s):
            st = ""
            s1 = str(s)
            i = len(s1)
            while i<9:
                st += " "
                i += 1
            return st
        sum = 0
        print()
        print("        YOUR BILL         ")
        print("==========================")
        print("| ITEM               QUN.|")
        print("| ---------------------- |")
        for i in d:
            s = iteam.index(i)
            sum += (price[s]*d[i])
            print("|",i,space(i),d[i]," |")
        print("| ---------------------- |")
        print("|     TOTAL =",sum,space1(sum),"|")
        print("==========================")

    elif n==3:
        iteam = ["Papad Fried","Tomato Soup","Veg Soup","Undhiyu","Mix sabji","Shahi Paneer","Paneer Tawa","Daal Makhni","Dal Fry","Mohan Thal","Tava  Roti","Tanduri  Roti"]
        price = [20,30,30,100,120,130,130,150,150,200,15,20]
        flag = True
        while flag:
            print("================================")
            print("|                              |")
            print("|            LUNCH             |")
            print("|                              |")
            print("|  STARTER                     |")
            print("|    1-Papad Fried     ____$20 |")
            print("|    2-Tomato Soup     ____$30 |")
            print("|    3-Veg Soup        ____$30 |")
            print("|  Sabji                       |")
            print("|    4-Undhiyu         ____$100|")
            print("|    5-Mix sabji       ____$120|")
            print("|    6-Shahi Paneer    ____$130|")
            print("|    7-Paneer Tawa     ____$130|")
            print("|                              |")
            print("|    8-Daal Makhni     ____$150|")
            print("|    9-Dal Fry         ____$150|")
            print("|  Sweet                       |")
            print("|    10-Mohan Thal     ____$200|")
            print("|  Roti                        |")
            print("|    11-Tava  Roti     ____$15 |")
            print("|    12-Tanduri  Roti  ____$20 |")
            print("================================")
            print()
            print(d)
            print()
            print("=== Press 0  when you finish your choice ===")
            print("=== Press 13 if you want to remove any thing ===")
            print("=== Press 14 for change quantity of any iteam ===")
            print()
            n = int(input("Enter no : "))
            if n>0 and n<13:
                n1 = int(input("Enter quantity : "))
                d[iteam[n-1]] = n1
            elif n==0:
                flag=False
            elif n==13:
                i = int(input("Enter iteam no : "))
                if iteam[i-1] in d:
                    del d[iteam[i-1]]
                else:
                    print("-- Item not in your list --")
            elif n==14:
                i1 = int(input("Enter iteam no : "))
                if iteam[i1 - 1] in d:
                    i2 = int(input("Enter new quantity : "))
                    d[iteam[i1-1]]  = i2
                else:
                    print("-- Item not in your list --")        
            else:
                print("==== Please Enter write choice ====")
        def space(s):
            st = ""
            i = len(s)
            while i<18:
                st += " "
                i += 1
            return st
        def space1(s):
            st = ""
            s1 = str(s)
            i = len(s1)
            while i<9:
                st += " "
                i += 1
            return st
        sum = 0
        print()
        print("        YOUR BILL         ")
        print("==========================")
        print("| ITEM               QUN.|")
        print("| ---------------------- |")
        for i in d:
            s = iteam.index(i)
            sum += (price[s]*d[i])
            print("|",i,space(i),d[i]," |")
        print("| ---------------------- |")
        print("|     TOTAL =",sum,space1(sum),"|")
        print("==========================")
    
    else:
        print("=== Please enter write choice ===")
        choice()

def defaultmanu():
    d = {}
    print()
    print("1.Breakfast")
    print("2.Lunch")
    print("3.Dinner")
    print()
    n = int(input("Enter your choice : "))
    if n==1:
        print()
        flag = True
        while flag:
            print()
            print(" _________________")
            print("|  1.GUJARATI     |")
            print("|  2.PANJABI      |")
            print("|  3.KATHIYAWADI  |")
            print("-------------------")
            a = int(input("ENTER : "))
            if a==1:
                print("======================")
                print("|                    |")
                print("|  BREAKFAST   $99   |")
                print("|                    |")
                print("|  FRUIT JUICE       |")
                print("|    -Pineapple      |")
                print("|    -Orange         |")
                print("|  HOT BEVERAGE      |")
                print("|    -Tea            |")
                print("|    -Coffee         |")
                print("|  BREAKFAST         |")
                print("|    -Khaman         |")
                print("|    -Palak Dhokla   |")
                print("|    -Thepla         |")
                print("======================")
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    q = int(input("For how many person : "))
                    t = 99*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Breakfast   ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      |")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            elif a==2:
                print("======================")
                print("|                    |")
                print("|  BREAKFAST   $120  |")
                print("|                    |")
                print("|  FRUIT JUICE       |")
                print("|    -Pineapple      |")
                print("|    -Orange         |")
                print("|  HOT BEVERAGE      |")
                print("|    -Tea            |")
                print("|    -Lassi          |")
                print("|  BREAKFAST         |")
                print("|    -Aloo Paratha   |")
                print("|    -Plain Curd     |")
                print("======================")
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    q = int(input("For how many person : "))
                    t = 120*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Breakfast   ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      |")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            elif a==3:
                print("======================")
                print("|                    |")
                print("|  BREAKFAST   $100  |")
                print("|                    |")
                print("|  FRUIT JUICE       |")
                print("|    -Pineapple      |")
                print("|    -Orange         |")
                print("|  HOT BEVERAGE      |")
                print("|    -Tea            |")
                print("|  BREAKFAST         |")
                print("|    -Vadharelo Rotlo|")
                print("|    -Vadharelu Dahi |")
                print("======================")
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    q = int(input("For how many person : "))
                    t = 100*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Breakfast   ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      |")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            else:
                print("=== Please enter a write choice ===")
                
                
    elif n==2:
        print()
        flag = True
        while flag:
            print()
            print(" _________________")
            print("|  1.GUJARATI     |")
            print("|  2.PANJABI      |")
            print("|  3.KATHIYAWADI  |")
            print("-------------------")
            a = int(input("ENTER : "))
            if a==1:
                print("======================")
                print("|                    |")
                print("|  LUNCH   $500      |")
                print("|                    |")
                print("|  STARTER           |")
                print("|    -Papad Fried    |")
                print("|  Sabji             |")
                print("|    -Undhiyu        |")
                print("|    -Mix sabji      |")
                print("|  Sweet             |")
                print("|    -Mohan Thal     |")
                print("|  Roti              |")
                print("|    -Tava  Roti     |")
                print("======================")
                print()
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    d["Lunch"] = "Gujarati"
                    q = int(input("For how many person : "))
                    t = 500*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Lunch      ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      ")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                    print("=== Your order place successfully ===")
                    flag = False
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            elif a==2:
                print("======================")
                print("|                    |")
                print("|  LUNCH   $600      |")
                print("|                    |")
                print("|  PULSES            |")
                print("|    -Daal Makhni    |")
                print("|    -Dal Fry        |")
                print("|  Sabji             |")
                print("|    -Shahi Paneer   |")
                print("|    -Paneer Tawa    |")
                print("|  Sweet             |")
                print("|    -Mohan Thal     |")
                print("|  Roti              |")
                print("|    -Tava  Roti     |")
                print("======================")
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    d["Lunch"] = "Panjabi"
                    q = int(input("For how many person : "))
                    t = 600*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Lunch      ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      ")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                    print("=== Your order place successfully ===")
                    flag = False
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            elif a==3:
                print("======================")
                print("|                    |")
                print("|  LUNCH   $700      |")
                print("|                    |")
                print("|  FARSHAN           |")
                print("|    -Bataka Vada    |")
                print("|    -Mix Chat       |")
                print("|  Sabji             |")
                print("|    -Ringan Bharatu |")
                print("|    -Tuver Masala   |")
                print("|  Sweet             |")
                print("|    -Mohan Thal     |")
                print("|  Roti              |")
                print("|    -Tava  Roti     |")
                print("======================")
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    d["Lunch"] = "Kathiyawadi"
                    q = int(input("For how many person : "))
                    t = 700*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Lunch      ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      |")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                    print("=== Your order place successfully ===")
                    flag = False
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            else:
                print("=== Please enter a write choic ===")
        
    elif n==3:
        print()
        flag = True
        while flag:
            print()
            print(" _________________")
            print("|  1.GUJARATI     |")
            print("|  2.PANJABI      |")
            print("|  3.KATHIYAWADI  |")
            print("-------------------")
            a = int(input("ENTER : "))
            if a==1:
                print("======================")
                print("|                    |")
                print("|  DINNER   $500     |")
                print("|                    |")
                print("|  STARTER           |")
                print("|    -Papad Fried    |")
                print("|  Sabji             |")
                print("|    -Undhiyu        |")
                print("|    -Mix sabji      |")
                print("|  Sweet             |")
                print("|    -Mohan Thal     |")
                print("|  Roti              |")
                print("|    -Tanduri  Roti  |")
                print("======================")
                print()
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    d["Lunch"] = "Gujarati"
                    q = int(input("For how many person : "))
                    t = 500*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Dinner     ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      |")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                    print("=== Your order place successfully ===")
                    flag = False
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            elif a==2:
                print("======================")
                print("|                    |")
                print("|  DINNER   $600     |")
                print("|                    |")
                print("|  PULSES            |")
                print("|    -Daal Makhni    |")
                print("|    -Dal Fry        |")
                print("|  Sabji             |")
                print("|    -Shahi Paneer   |")
                print("|    -Paneer Tawa    |")
                print("|  Sweet             |")
                print("|    -Mohan Thal     |")
                print("|  Roti              |")
                print("|    -Tanduri  Roti  |")
                print("======================")
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    d["Lunch"] = "Panjabi"
                    q = int(input("For how many person : "))
                    t = 600*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Dinner     ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      |")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                    print("=== Your order place successfully ===")
                    flag = False
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            elif a==3:
                print("======================")
                print("|                    |")
                print("|  DINNER   $700     |")
                print("|                    |")
                print("|  FARSHAN           |")
                print("|    -Bataka Vada    |")
                print("|    -Mix Chat       |")
                print("|  Sabji             |")
                print("|    -Ringan Bharatu |")
                print("|    -Tuver Masala   |")
                print("|  Sweet             |")
                print("|    -Mohan Thal     |")
                print("|  Roti              |")
                print("|    -Tanduri  Roti  |")
                print("======================")
                print()
                print("Do you want to add this")
                print("     1.Yes")
                print("     2.No")
                c = int(input("Enter : "))
                if c==1:
                    d["Lunch"] = "Kathiyawadi"
                    q = int(input("For how many person : "))
                    t = 700*q
                    d["Breakfast"] = "Gujarati"
                    print()
                    print("        Your Bill         ")
                    print("==========================")
                    print("|       ITEM         QUA.|")
                    print("| ---------------------- |")
                    print("| Default Dinner     ",q,"|")
                    print("| ---------------------- |")
                    print("|     Total = ",t,"      |")
                    print("==========================")
                    print()
                    print("=== Your order place successfully ===")
                    flag = False
                    main()
                    print("=== Your order place successfully ===")
                    flag = False
                else:
                    print("1.Press 1 for other default breakfast")
                    print("2.Press 2 if you do not like default breakfast and go for your choice")
                    v = int(input("Enter : "))
                    if v == 1:
                        flag = True
                    else:
                        choice()
                        flag = False
            else:
                print("=== Please enter a write choic ===")
    
    else:
        print("=== Please enter write choice ===")
        defaultmanu()
                      
def main():
    print("=============================")
    print("|                           |")
    print("|    1.Default menu         |")
    print("|    2.Order by your choice |")
    print("|    3.Exit                 |")
    print("|                           |")
    print("=============================")
    n = int(input("Enter your choice : "))
    
    if n==1:
        defaultmanu()
    elif n==2:    
        choice()
    else:
        h.menu()
        

if __name__ == "__main__":
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("*                                                   *")
    print("*                                                   *")
    print("*                    Welcome To                     *")
    print("*               Food ordering System                *")
    print("*                                                   *")
    print("*                                                   *")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n\n")
    main()