class hotelfarecal:

    def _init_(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',address='',cindate='',coutdate='',rno=101):
        print ("****WELCOME TO VERNASE HOTEL****")
        print ("SANT ANTIOCO ISLAND,SOUTH SARDINIA,ITALY\n")
        self.rt=rt
        self.r=r
        self.t=t
        self.p=p
        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nENTER YOUR NAME:")
        self.address=input("\nENTER YOUR ADDRESS:")
        self.cindate=input("\nENTER YOUR CHECK IN DATE:")
        self.coutdate=input("\nENTER YOUR CHECKOUT DATE:")
        print("YOUR ROOM HAS BEEN BOOKED SUCCESSFULLY")
        
    def roomrent(self):#sel1353

        print ("WE HAVE THE FOLLOWING ROOMS FOR YOU:-")

        print ("1.  HONEYMOON SUITE ----> 800€ PN\-")

        print ("2.  FAMILY SUITE ----> 600€ PN\-")

        print ("3.  DOUBLE BED ROOM ----> 400€ PN\-")

        print ("4.  SINGLE BED ROOM ----> 200€ PN\-")

        x=int(input("ENTER YOUR CHOICE PLEASE->"))

        n=int(input("FOR HOW MANY NIGHTS DO YOU WANT TO STAY:"))

        if(x==1):

            print ("YOU HAV OPTED FOR HONEYMOON SUITE")

            self.s=800*n

        elif (x==2):

            print ("YOU HAVE OPTED FOR FAMILY SUITE")

            self.s=600*n

        elif (x==3):

            print ("YOU HAVE OPTED FOR DOUBLE BED ROOM")

            self.s=400*n

        elif (x==4):
            print ("YOU HAVE OPTED FOR SINGLE BED ROOM")

            self.s=200*n

        else:

            print ("PLEASE CHOOSE A ROOM")

        print ("YOUR ROOM RENT IS =",self.s,"€\n")
        print("YOUR ROOM NO.:",self.rno,"\n")
        print("KINDLY CONTACT THE STAFF FOR YOUR ROOM KEYS\n")
        self.rno+=1

    def restaurentbill(self):

        print("****RESTAURANT MENU****\n")

        print(" 1.WATER----->20€\n","2.TEA----->10€\n","3.COFFEE ----->15€\n","4.CROISSANT--->50€\n","5.PIZZA---->60€\n","6.LASAGNA--->65€\n","7.RISOTTO ---->75€\n","8.TRUFFLE ---->70€\n","9.BRUSCHETTA ---->40€\n","10.EXIT")


        while (1):

            c=int(input("ENTER YOUR CHOICE:"))


            if (c==1):
                d=int(input("ENTER THE QUANTITY:"))
                self.r=self.r+20*d

            elif (c==2):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+10*d

            elif (c==3):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+15*d

            elif (c==4):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+50*d

            elif (c==5):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+60*d

            elif (c==6):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+65*d
            
            elif (c==7):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+75*d
              
            elif (c==8):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+70*d
            
            elif (c==9):
                 d=int(input("ENTER THE QUANTITY:"))
                 self.r=self.r+40*d
                
            elif (c==10):
                 break
            else:
                print("INVALID OPTION")

        print ("TOTAL FOOD COST =",self.r,"€\n")

    def	laundrybill(self):
        print ("*****LAUNDRY MENU******")

        print ("1.SHORTS----->3€","2.TROUSERS----->4€","3.SHIRT--->5€","4.JEANS---->6€","5.GIRLSUIT--->8€","6.Exit")

        while (1):
            

            e=int(input("ENTER YOUR CHOICE:"))

            if (e==1):
                f=int(input("ENTER THE QUANTITY:"))
                self.t=self.t+3*f

            elif (e==2):
                f=int(input("ENTER THE QUANTITY:"))
                self.t=self.t+4*f

            elif (e==3):
                f=int(input("ENTER THE QUANTITY:"))
                self.t=self.t+5*f

            elif (e==4):
                f=int(input("ENTER THE QUANTITY:"))
                self.t=self.t+6*f

            elif (e==5):
                f=int(input("ENTER THE QUANTITY:"))
                self.t=self.t+8*f
            elif (e==6):
                break;
            else:

                print ("INVALID OPTION")


        print ("TOTAL LAUNDRY COST =",self.t,"€\n")

    def gamebill(self):
        print ("*****GAME MENU******")

        print ("1.TABLE TENNIS----->60€","2.BOWLING----->80€","3.SNOOKER--->70€","4.VIDEO GAMES---->90€","5.POOL--->50€","6.TABLE SOCCER ---->40€","7.EXIT")



        while (1):

            
            g=int(input("ENTER YOUR CHOICE:"))


            if (g==1):
                h=int(input("NO. OF HOURS:"))
                self.p=self.p+60*h

            elif (g==2):
                h=int(input("NO. OF HOURS:"))
                self.p=self.p+80*h

            elif (g==3):
                h=int(input("NO. OF HOURS:"))
                self.p=self.p+70*h

            elif (g==4):
                h=int(input("NO. OF HOURS:"))
                self.p=self.p+90*h

            elif (g==5):
                h=int(input("NO. OF HOURS:"))
                self.p=self.p+50*h
            elif (g==6):
                h=int(input("NO. OF HOURS:"))
                self.p=self.p+40*h
            elif (g==7):
              break
            
                

            else:

                print ("INVALID OPTION")



        print ("TOTAL GAME BILL =",self.p,"€\n")

    def display(self):
        print ("*****HOTEL BILL*****")
        print ("--CUSTOMER DETAILS--")
        print ("CUSTOMER NAME:",self.name)
        print ("CUSTOMER ADDRESS:",self.address)
        print ("CHECK IN DATE:",self.cindate)
        print ("CHECK OUT DATE:",self.coutdate)
        print ("ROOM NO.:",self.rno)
        print ("YOUR ROOM RENT IS:",self.s)
        print ("YOUR FOOD BILL IS::",self.r)
        print ("YOUR LAUNDRY BILL IS:",self.t)
        print ("YOUR GAME BILL IS:",self.p)

        self.rt=self.s+self.t+self.p+self.r

        print ("YOUR SUBTOTAL BILL IS:",self.rt)
        print ("ADDITIONAL SERVICE CHARGES ARE:",self.a)
        print ("YOUR GRANDTOTAL BILL IS:",self.rt+self.a,"\n")
        
def main():

    a=hotelfarecal()
    

    while (1):
        print("1.ENTER CUSTOMER DATA")
        
        print("2.CALCULATE ROOMRENT")

        print("3.CALCULTE RESTAURANT BILL")

        print("4.CALCULATE LAUNDRY BILL")

        print("5.CALCULATE GAMEBILL")

        print("6.SHOW TOTAL COST")

        print("7.EXIT")

        b=int(input("\nENTER YOUR CHOICE:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.laundrybill()

        if (b==5):

            a.gamebill()

        if (b==6):

            a.display()

        if (b==7):

            quit()



main()
