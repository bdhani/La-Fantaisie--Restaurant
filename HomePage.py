import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as sql

##Funtionalities:    

#TopFrame  - #362417
#SideFrame - #92817A
#MainFrame - #F1DABF
#In Login Pages:
#--MainBg  - #494449
#--Box     - #A9A8AA
#In Cart Page:
#--MainBg  - #494449
#--Box     - #B8B8BC

##Main Window
root = Tk()
root.title('La Fataisie')
root.geometry('994x624+50+50')
root.resizable(False, False)
root.iconbitmap('Pictures/chef.ico')
root.configure(bg='#F1DABF')


#---About Frame
AboutFrame=Frame(bg='#F1DABF')
AboutFrame.place(x=242,y=65)

AboutImage=PhotoImage(file=r"Pictures/AboutPage.png")
AboutPage=Label(AboutFrame, image = AboutImage)
AboutPage.grid(row=0, column=0)

#-----COMMON FOR ALL FRAMES:
Qty1=StringVar()
Qty1.set("--Quantity--")

Qty2=StringVar()
Qty2.set("--Quantity--")

Qty3=StringVar()
Qty3.set("--Quantity--")

QtyValues=("--Quantity--",1,2,3,4,5,6,7,8,9,10)


CartList=[]
RateList=[]
QntyList=[]

def CreateProductsFrame():
    global ProductsFrame
    ProductsFrame=LabelFrame(root, height=557, width=750, bd=6, relief=GROOVE,
                             font = ('Cambria', 16), fg="#362417", bg="#F1DABF")
    ProductsFrame.place(x=243,y=66)

#-----FOR SALADS FRAME:

MixedSaladImage = PhotoImage(file=r"Fooditems/MixedSalad.png").subsample(2,2)
MixedSaladPrice=220
ParisianSaladImage = PhotoImage(file=r"Fooditems/ParisianSalad.png").subsample(2,2)
ParisianSaladPrice=250

def SaladsButton():
    CreateProductsFrame()

    SaladsLabel = Label(ProductsFrame, text = 'SALADS', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    SaladsLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(9,9))


    MixedSaladLabel=Label(ProductsFrame, image=MixedSaladImage)
    MixedSaladLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    MixedSaladNameLabel=Label(ProductsFrame, text="MIXED VEGETABLE SALAD", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    MixedSaladNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    MixedSaladDescLabel=Label(ProductsFrame, text="(Corn, Peas, Onions, Cucumbers, Tomatoes, \n Green Chilies, Bell Peppers and Zucchini)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    MixedSaladDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    MixedSaladPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(MixedSaladPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    MixedSaladPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Mixed Salad")
                RateList.append(MixedSaladPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    ParisianSaladLabel=Label(ProductsFrame, image=ParisianSaladImage)
    ParisianSaladLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    ParisianSaladNameLabel=Label(ProductsFrame, text="THE PARISIAN SALAD", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    ParisianSaladNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    ParisianSaladDescLabel=Label(ProductsFrame, text="(Stick-Chopped carrots, beetroot, bell peppers, \n spring onions and lettuce)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    ParisianSaladDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ParisianSaladPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(ParisianSaladPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    ParisianSaladPriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Parisian Salad")
                RateList.append(ParisianSaladPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


#-----FOR PASTAS FRAME:

ArrabbiataImage = PhotoImage(file=r"Fooditems/PenneArrabbiata.png")
ArrabbiataPrice=220
EnzoImage = PhotoImage(file=r"Fooditems/Enzo.png")
EnzoPrice=280
MushroomRavioliImage = PhotoImage(file=r"Fooditems/MushroomRavioli.png")
MushroomRavioliPrice=300

def PastasButton():
    CreateProductsFrame()

    PastasLabel = Label(ProductsFrame, text = 'PASTAS', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    PastasLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))

    ArrabbiataLabel=Label(ProductsFrame, image=ArrabbiataImage)
    ArrabbiataLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    ArrabbiataNameLabel=Label(ProductsFrame, text="PENNE ARRABBIATA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    ArrabbiataNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ArrabbiataDescLabel=Label(ProductsFrame, text="(Spicy arrabbiata sauce, penne pasta, cherry tomatoes, \n parmesan and crispy onions)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    ArrabbiataDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ArrabbiataPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(ArrabbiataPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    ArrabbiataPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Penne Arrabbiata")
                RateList.append(ArrabbiataPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    EnzoLabel=Label(ProductsFrame, image=EnzoImage)
    EnzoLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    EnzoNameLabel=Label(ProductsFrame, text="ENZO", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    EnzoNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    EnzoDescLabel=Label(ProductsFrame, text="(Tomato passata, cherry tomatoes, mozzarella, \n ricotta and wild rocket leaves)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    EnzoDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    EnzoPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(EnzoPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    EnzoPriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Enzo")
                RateList.append(EnzoPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe2=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe2.grid(row=10, column=0, columnspan=2, padx=(5,5))


    MushroomRavioliLabel=Label(ProductsFrame, image=MushroomRavioliImage)
    MushroomRavioliLabel.grid(row=11, rowspan=4, column=0, padx=(5,5),pady=(8,7))
    MushroomRavioliNameLabel=Label(ProductsFrame, text="MUSHROOM RAVIOLI", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    MushroomRavioliNameLabel.grid(row=11,column=1, sticky="w", padx=(5,0), pady=(6,0))
    MushroomRavioliDescLabel=Label(ProductsFrame, text="(Sauteed Mushrooms with spinach, garlic, \n sun-dried tomatoes and combined with ravioli)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    MushroomRavioliDescLabel.grid(row=12,column=1, sticky="w", padx=(5,0), pady=(0,0))
    MushroomRavioliPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(MushroomRavioliPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    MushroomRavioliPriceLabel.grid(row=13,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox3=Spinbox(ProductsFrame, textvariable=Qty3, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox3.grid(row=14, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem3():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox3.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Mushroom Ravioli")
                RateList.append(MushroomRavioliPrice)
                QntyList.append(QtyBox3.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton3=Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                         cursor='hand2', command=AddItem3,
                         bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton3.grid(row=14, column=1, padx=(5,50), pady=(0,10), sticky="e")

       

#-----FOR PIZZAS FRAME:

TruffledSalamiImage = PhotoImage(file=r"Fooditems/TruffledSalami.png")
TruffledSalamiPrice=300
MargheritaImage = PhotoImage(file=r"Fooditems/Margherita.png")
MargheritaPrice=250
GorgonzolaImage = PhotoImage(file=r"Fooditems/SpeckAndGorgonzola.png")
GorgonzolaPrice=280

def PizzasButton():
    CreateProductsFrame()

    PizzasLabel = Label(ProductsFrame, text = 'PIZZAS', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    PizzasLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))

    TruffledSalamiLabel=Label(ProductsFrame, image=TruffledSalamiImage)
    TruffledSalamiLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    TruffledSalamiNameLabel=Label(ProductsFrame, text="TRUFFLED SALAMI AND MUSHROOM", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    TruffledSalamiNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    TruffledSalamiDescLabel=Label(ProductsFrame, text="(Tomato passata, mozzarella, truffled salami, \n rocket, mushrooms, truffle oil)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    TruffledSalamiDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    TruffledSalamiPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(TruffledSalamiPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    TruffledSalamiPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Truffled Salami \n and Mushroom")
                RateList.append(TruffledSalamiPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    MargheritaLabel=Label(ProductsFrame, image=MargheritaImage)
    MargheritaLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    MargheritaNameLabel=Label(ProductsFrame, text="MARGHERITA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    MargheritaNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    MargheritaDescLabel=Label(ProductsFrame, text="(Tomato passata, mozzarella and basil)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    MargheritaDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    MargheritaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(MargheritaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    MargheritaPriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Margherita")
                RateList.append(MargheritaPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe2=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe2.grid(row=10, column=0, columnspan=2, padx=(5,5))


    GorgonzolaLabel=Label(ProductsFrame, image=GorgonzolaImage)
    GorgonzolaLabel.grid(row=11, rowspan=4, column=0, padx=(5,5),pady=(0,0))
    GorgonzolaNameLabel=Label(ProductsFrame, text="SPECK AND GORGONZOLA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    GorgonzolaNameLabel.grid(row=11,column=1, sticky="w", padx=(5,0), pady=(6,0))
    GorgonzolaDescLabel=Label(ProductsFrame, text="(No tomato pizza – garlic butter, mushrooms, \n mozzarella, gorgonzola and speck)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    GorgonzolaDescLabel.grid(row=12,column=1, sticky="w", padx=(5,0), pady=(0,0))
    GorgonzolaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(GorgonzolaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    GorgonzolaPriceLabel.grid(row=13,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox3=Spinbox(ProductsFrame, textvariable=Qty3, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox3.grid(row=14, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem3():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox3.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Speck and Gorgonzola")
                RateList.append(GorgonzolaPrice)
                QntyList.append(QtyBox3.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton3=Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                         cursor='hand2', command=AddItem3,
                         bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton3.grid(row=14, column=1, padx=(5,50), pady=(0,10), sticky="e")

    
    

#-----FOR SANDWICHES FRAME:

BaconSandwichImage = PhotoImage(file=r"Fooditems/BaconSandwich.png").subsample(3,3)
BaconSandwichPrice=250
SausageSandwichImage = PhotoImage(file=r"Fooditems/SausageSandwich.png").subsample(3,3)
SausageSandwichPrice=300
MushroomBurritoImage = PhotoImage(file=r"Fooditems/MushroomBurrito.png").subsample(2,2)
MushroomBurritoPrice=250

def SandwichesButton():
    CreateProductsFrame()
    
    SandwichesLabel = Label(ProductsFrame, text = 'SANDWICHES', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    SandwichesLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))

    BaconSandwichLabel=Label(ProductsFrame, image=BaconSandwichImage)
    BaconSandwichLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    BaconNameLabel=Label(ProductsFrame, text="BACON SANDWICH", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    BaconNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    BaconDescLabel=Label(ProductsFrame, text="(Smoked streaky and unsmoked back bacon served on \n toasted or untoasted sourdough bread)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    BaconDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    BaconPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(BaconSandwichPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    BaconPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Bacon Sandwich")
                RateList.append(BaconSandwichPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    SausageSandwichLabel=Label(ProductsFrame, image=SausageSandwichImage)
    SausageSandwichLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    SausageNameLabel=Label(ProductsFrame, text="SAUSAGE SANDWICH", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    SausageNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    SausageDescLabel=Label(ProductsFrame, text="(Two free range pork sausages served on \n toasted or untoasted sourdough bread)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    SausageDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    SausagePriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(SausageSandwichPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    SausagePriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Sausage Sandwich")
                RateList.append(SausageSandwichPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe2=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe2.grid(row=10, column=0, columnspan=2, padx=(5,5))


    MushroomBurritoLabel=Label(ProductsFrame, image=MushroomBurritoImage)
    MushroomBurritoLabel.grid(row=11, rowspan=4, column=0, padx=(5,5),pady=(0,0))
    BurritoNameLabel=Label(ProductsFrame, text="PULLED FABLE MUCHROOM BURRITO", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    BurritoNameLabel.grid(row=11,column=1, sticky="w", padx=(5,0), pady=(6,0))
    BurritoDescLabel=Label(ProductsFrame, text="(Vegetarian burrito served with pulled mushrooms, \n rice, spicy sauce, onions and roasted peppers)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    BurritoDescLabel.grid(row=12,column=1, sticky="w", padx=(5,0), pady=(0,0))
    BurritoPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(MushroomBurritoPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    BurritoPriceLabel.grid(row=13,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox3=Spinbox(ProductsFrame, textvariable=Qty3, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox3.grid(row=14, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem3():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox3.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Pulled Fable \n Mushroom Burrito")
                RateList.append(MushroomBurritoPrice)
                QntyList.append(QtyBox3.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton3=Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                         cursor='hand2', command=AddItem3,
                         bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton3.grid(row=14, column=1, padx=(5,50), pady=(0,10), sticky="e")

#-----FOR CAKES FRAME:

CarrotCakeImage = PhotoImage(file=r"Fooditems/Carrotcake.png")
CarrotCakePrice=600
OrangeCakeImage = PhotoImage(file=r"Fooditems/OrangeCake.png")
OrangeCakePrice=620

def CakesButton():
    CreateProductsFrame()

    CakesLabel = Label(ProductsFrame, text = 'CAKES', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    CakesLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(10,7))

    CarrotCakeLabel=Label(ProductsFrame, image=CarrotCakeImage)
    CarrotCakeLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(20,20))
    CarrotCakeNameLabel=Label(ProductsFrame, text="SPELT CARROT CAKE", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    CarrotCakeNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CarrotCakeDescLabel=Label(ProductsFrame, text="(Vegan-friendly Spelt Carrot cake with \n cinnamon and Walnut Crumble)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    CarrotCakeDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CarrotCakePriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(CarrotCakePrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    CarrotCakePriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(30,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Carrot Cake")
                RateList.append(CarrotCakePrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    OrangeCakeLabel=Label(ProductsFrame, image=OrangeCakeImage)
    OrangeCakeLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(20,20))
    OrangeCakeNameLabel=Label(ProductsFrame, text="ORANGE AND CHOCOLATE", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    OrangeCakeNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    OrangeCakeDescLabel=Label(ProductsFrame, text="(Iced with dark Terry's chocolate and \n orange flavoured chocolate ganache)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    OrangeCakeDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    OrangeCakePriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(OrangeCakePrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    OrangeCakePriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(30,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Orange Cake")
                RateList.append(OrangeCakePrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


#-----FOR COOKIES FRAME:

ChocolateChipImage = PhotoImage(file=r"Fooditems/ChocolateChipCookie.png").subsample(2,2)
ChocolateChipPrice=200
CherryCookieImage = PhotoImage(file=r"Fooditems/CherryandOatCookie.png").subsample(3,3)
CherryCookiePrice=200

def CookiesButton():
    CreateProductsFrame()

    CookiesLabel = Label(ProductsFrame, text = 'COOKIES', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    CookiesLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))

    ChocolateChipLabel=Label(ProductsFrame, image=ChocolateChipImage)
    ChocolateChipLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(10,15))
    ChocolateChipNameLabel=Label(ProductsFrame, text="CHOCOLATE-CHIP COOKIES", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    ChocolateChipNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ChocolateChipDescLabel=Label(ProductsFrame, text="(Gluten-free buttery chocalate chunk cookies\n with brown sugar and vannila essence)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    ChocolateChipDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ChocolateChipPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(ChocolateChipPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    ChocolateChipPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(30,10), pady=(0,10), sticky="w")
    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Chocolate Chip\n Cookies")
                RateList.append(ChocolateChipPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    CherryCookieLabel=Label(ProductsFrame, image=CherryCookieImage)
    CherryCookieLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(15,10))
    CherryCookieNameLabel=Label(ProductsFrame, text="SOUR CHERRY OAT COOKIE", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    CherryCookieNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    CherryCookieDescLabel=Label(ProductsFrame, text="(Oatmeal-Based dough with brown sugar, \n butter, milk and cherries)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    CherryCookieDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CherryCookiePriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(CherryCookiePrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    CherryCookiePriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(30,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Sour Cerry Oat \n Cookies")
                RateList.append(CherryCookiePrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")

#-----FOR ICE-CREAMS FRAME:

SundaesImage = PhotoImage(file=r"Fooditems/Sundaes.png")
SundaesPrice=220
ProfitroleImage = PhotoImage(file=r"Fooditems/Profiterole.png")
ProfitrolePrice=220
ChurrosImage = PhotoImage(file=r"Fooditems/Churros.png")
ChurrosPrice=200


def IceCreamsButton():
    CreateProductsFrame()

    IceCreamsLabel = Label(ProductsFrame, text = 'ICE-CREAMS', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    IceCreamsLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(10,12))


    SundaesLabel=Label(ProductsFrame, image=SundaesImage)
    SundaesLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(5,10))
    SundaesNameLabel=Label(ProductsFrame, text="NUTTY CARAMEL AND CHOCOLATE SUNDAES", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    SundaesNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    SundaesDescLabel=Label(ProductsFrame, text="(layer salted peanuts, ice cream, caramel, \n dark chocolate and Biscuits)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    SundaesDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    SundaesPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(SundaesPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    SundaesPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Nutty Caramel and \n Chocolate Sundaes")
                RateList.append(TruffledSalamiPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    ProfitroleLabel=Label(ProductsFrame, image=ProfitroleImage)
    ProfitroleLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(15,15))
    ProfitroleNameLabel=Label(ProductsFrame, text="PROFITROLE & ICE-CREAM SANDWICHES", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    ProfitroleNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    ProfitroleDescLabel=Label(ProductsFrame, text="(Toasted hazelnuts or almonds, salted pretzels, \n Crunchies, Maltesers or Oreos)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    ProfitroleDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ProfitrolePriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(ProfitrolePrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    ProfitrolePriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Profitrole & \n Ice-Cream Sandwiches")
                RateList.append(ProfitrolePrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe2=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe2.grid(row=10, column=0, columnspan=2, padx=(5,5))


    ChurrosLabel=Label(ProductsFrame, image=ChurrosImage)
    ChurrosLabel.grid(row=11, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    ChurrosNameLabel=Label(ProductsFrame, text="CHURROS CINNAMON ICE-CREAM SANDWICHES", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    ChurrosNameLabel.grid(row=11,column=1, sticky="w", padx=(5,0), pady=(6,0))
    ChurrosDescLabel=Label(ProductsFrame, text="(Spanish-style doughnut coated in \n cinnamon sugar with ice cream)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    ChurrosDescLabel.grid(row=12,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ChurrosPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(ChurrosPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    ChurrosPriceLabel.grid(row=13,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox3=Spinbox(ProductsFrame, textvariable=Qty3, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox3.grid(row=14, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem3():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox3.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Churros Cinnamon \n Ice-Cream Sandwiches")
                RateList.append(ChurrosPrice)
                QntyList.append(QtyBox3.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton3=Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                         cursor='hand2', command=AddItem3,
                         bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton3.grid(row=14, column=1, padx=(5,50), pady=(0,10), sticky="e")

#-----FOR COFFEE FRAME:

CappuccinoImage = PhotoImage(file=r"Fooditems/Cappuccino.png").subsample(3,3)
CappuccinoPrice=280
CaffeMochaImage = PhotoImage(file=r"Fooditems/CaffeMocha.png").subsample(3,3)
CaffeMochaPrice=320
ColdBrewedImage = PhotoImage(file=r"Fooditems/ColdBrewed.png").subsample(3,3)
ColdBrewedPrice=270

def CoffeesButton():
    CreateProductsFrame()

    CoffeesLabel = Label(ProductsFrame, text = 'COFFEES', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    CoffeesLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))

    CappuccinoLabel=Label(ProductsFrame, image=CappuccinoImage)
    CappuccinoLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    CappuccinoNameLabel=Label(ProductsFrame, text="CAPPUCCINO", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    CappuccinoNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CappuccinoDescLabel=Label(ProductsFrame, text="(Espresso with steamed and frothed milk)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    CappuccinoDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CappuccinoPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(CappuccinoPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    CappuccinoPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Cappuccino")
                RateList.append(CappuccinoPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5))


    CaffeMochaLabel=Label(ProductsFrame, image=CaffeMochaImage)
    CaffeMochaLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    CaffeMochaLabel=Label(ProductsFrame, text="CAFFE MOCHA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    CaffeMochaLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    CaffeMochaDescLabel=Label(ProductsFrame, text="(Latte -Espresso with steamed milk and foam- with chocolate)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    CaffeMochaDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CaffeMochaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(CaffeMochaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    CaffeMochaPriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Caffe Mocha")
                RateList.append(CaffeMochaPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe2=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe2.grid(row=10, column=0, columnspan=2, padx=(5,5), pady=(0,10))


    ColdBrewedLabel=Label(ProductsFrame, image=ColdBrewedImage)
    ColdBrewedLabel.grid(row=11, rowspan=4, column=0, padx=(5,5),pady=(0,5))
    ColdBrewedNameLabel=Label(ProductsFrame, text="COLD-BREWED COFFEE", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    ColdBrewedNameLabel.grid(row=11,column=1, sticky="w", padx=(5,0), pady=(6,0))
    ColdBrewedDescLabel=Label(ProductsFrame, text="(Coffee brewed with cold water, milk and ice)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    ColdBrewedDescLabel.grid(row=12,column=1, sticky="w", padx=(5,0), pady=(0,0))
    ColdBrewedPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(ColdBrewedPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    ColdBrewedPriceLabel.grid(row=13,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox3=Spinbox(ProductsFrame, textvariable=Qty3, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox3.grid(row=14, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem3():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox3.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Cold Brewed Coffee")
                RateList.append(ColdBrewedPrice)
                QntyList.append(QtyBox3.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton3=Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                         cursor='hand2', command=AddItem3,
                         bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton3.grid(row=14, column=1, padx=(5,50), pady=(0,10), sticky="e")

#-----FOR TEAS FRAME:

BlackTeaImage = PhotoImage(file=r"Fooditems/BlackTea.png").subsample(3,3)
BlackTeaPrice=150
GreenTeaImage = PhotoImage(file=r"Fooditems/GreenTea.png").subsample(3,3)
GreenTeaPrice=110
WhiteTeaImage = PhotoImage(file=r"FoodItems/WhiteTea.png").subsample(3,3)
WhiteTeaPrice=130


def TeasButton():
    CreateProductsFrame()

    TeasLabel = Label(ProductsFrame, text = 'TEAS', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    TeasLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))

    BlackTeaLabel=Label(ProductsFrame, image=BlackTeaImage)
    BlackTeaLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    BlackTeaNameLabel=Label(ProductsFrame, text="BLACK TEA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    BlackTeaNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    BlackTeaDescLabel=Label(ProductsFrame, text="(Tropical Breakfast Tea specially blended with \n Kenyan milima and Assam Dejoo)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    BlackTeaDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    BlackTeaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(BlackTeaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    BlackTeaPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Black Tea")
                RateList.append(BlackTeaPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5), pady=(3,3))


    GreenTeaLabel=Label(ProductsFrame, image=GreenTeaImage)
    GreenTeaLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    GreenTeaLabel=Label(ProductsFrame, text="GREEN TEA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    GreenTeaLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    GreenTeaDescLabel=Label(ProductsFrame, text="(Refreshing and cleansing tea with infusion \n of peppermint and spearmints)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    GreenTeaDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    GreenTeaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(GreenTeaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    GreenTeaPriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Green Tea")
                RateList.append(GreenTeaPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe2=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe2.grid(row=10, column=0, columnspan=2, padx=(5,5), pady=(2,12))


    WhiteTeaLabel=Label(ProductsFrame, image=WhiteTeaImage)
    WhiteTeaLabel.grid(row=11, rowspan=4, column=0, padx=(5,5),pady=(0,8))
    WhiteTeaNameLabel=Label(ProductsFrame, text="WHITE TEA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    WhiteTeaNameLabel.grid(row=11,column=1, sticky="w", padx=(5,0), pady=(6,0))
    WhiteTeaDescLabel=Label(ProductsFrame, text="(A low-caffiene, floral flavoured unsweetened tea)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    WhiteTeaDescLabel.grid(row=12,column=1, sticky="w", padx=(5,0), pady=(0,0))
    WhiteTeaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(WhiteTeaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    WhiteTeaPriceLabel.grid(row=13,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox3=Spinbox(ProductsFrame, textvariable=Qty3, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox3.grid(row=14, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem3():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox3.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("White Tea")
                RateList.append(WhiteTeaPrice)
                QntyList.append(QtyBox3.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton3=Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                         cursor='hand2', command=AddItem3,
                         bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton3.grid(row=14, column=1, padx=(5,50), pady=(0,10), sticky="e")


#-----FOR DECAF FRAME:

CinnamonTeaImage = PhotoImage(file=r"Fooditems/CinnamonTea.png").subsample(3,3)
CinnamonTeaPrice=120
RooibosImage = PhotoImage(file=r"Fooditems/Rooibos.png").subsample(3,3)
RooibosPrice=130
DecafSenchaImage = PhotoImage(file=r"Fooditems/DecafSencha.png").subsample(4,4)
DecafSenchaPrice=120

def DecafButton():
    CreateProductsFrame()

    DecafLabel = Label(ProductsFrame, text = 'DECAF', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    DecafLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))


    CinnamonTeaLabel=Label(ProductsFrame, image=CinnamonTeaImage)
    CinnamonTeaLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    CinnamonTeaNameLabel=Label(ProductsFrame, text="CINNAMON TEA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    CinnamonTeaNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CinnamonTeaDescLabel=Label(ProductsFrame, text="(Mild tea with woody and spicy taste of cinnamon and \n slightly sweet aftertaste)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    CinnamonTeaDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CinnamonTeaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(CinnamonTeaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    CinnamonTeaPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Cinnamon Tea")
                RateList.append(CinnamonTeaPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5), pady=(5,5))


    RooibosLabel=Label(ProductsFrame, image=RooibosImage)
    RooibosLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    RooibosNameLabel=Label(ProductsFrame, text="ROOIBOS", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    RooibosNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    RooibosDescLabel=Label(ProductsFrame, text="(Naturally sweet flavoured, low-caffiene herbal tea)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    RooibosDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    RooibosPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(RooibosPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    RooibosPriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Rooibos")
                RateList.append(RooibosPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe2=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe2.grid(row=10, column=0, columnspan=2, padx=(5,5), pady=(2,12))


    DecafSenchaLabel=Label(ProductsFrame, image=DecafSenchaImage)
    DecafSenchaLabel.grid(row=11, rowspan=4, column=0, padx=(5,5),pady=(0,8))
    DecafSenchaNameLabel=Label(ProductsFrame, text="DECAF SENCHA", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    DecafSenchaNameLabel.grid(row=11,column=1, sticky="w", padx=(5,0), pady=(6,0))
    DecafSenchaDescLabel=Label(ProductsFrame, text="(High-grade Japanese Sencha Tea flavoured with peaches and apricots)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    DecafSenchaDescLabel.grid(row=12,column=1, sticky="w", padx=(5,0), pady=(0,0))
    DecafSenchaPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(DecafSenchaPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    DecafSenchaPriceLabel.grid(row=13,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox3=Spinbox(ProductsFrame, textvariable=Qty3, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox3.grid(row=14, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem3():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox3.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Decaf Sencha")
                RateList.append(DecafSenchaPrice)
                QntyList.append(QtyBox3.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton3=Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                         cursor='hand2', command=AddItem3,
                         bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton3.grid(row=14, column=1, padx=(5,50), pady=(0,10), sticky="e")

    
#-----FOR NON-ALC. DRINKS FRAME

VirginMohitoImage = PhotoImage(file=r"Fooditems/VirginMohito.png").subsample(2,2)
VirginMohitoPrice=220
CranberryPunchImage = PhotoImage(file=r"Fooditems/CranberryPunch.png").subsample(2,2)
CranberryPunchPrice=200


def DrinksButton():
    CreateProductsFrame()

    DrinksLabel = Label(ProductsFrame, text = 'NON-ALCOHOLIC DRINKS', font = ('Cambria', 21), width=48,
                      bg = '#362417', fg = '#F1DABF')
    DrinksLabel.grid(row=0,column=0, columnspan=2, padx=(5,5), pady=(7,7))


    VirginMohitoLabel=Label(ProductsFrame, image=VirginMohitoImage)
    VirginMohitoLabel.grid(row=1, rowspan=4, column=0, padx=(5,5),pady=(0,10))
    VirginMohitoNameLabel=Label(ProductsFrame, text="VIRGIN MOHITO", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    VirginMohitoNameLabel.grid(row=1,column=1, sticky="w", padx=(5,0), pady=(0,0))
    VirginMohitoDescLabel=Label(ProductsFrame, text="(Lime, mint, sugar muddled and shaken with a splash of soda)",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    VirginMohitoDescLabel.grid(row=2,column=1, sticky="w", padx=(5,0), pady=(0,0))
    VirginMohitoPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(VirginMohitoPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    VirginMohitoPriceLabel.grid(row=3,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox1=Spinbox(ProductsFrame, textvariable=Qty1, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox1.grid(row=4, column=1, padx=(50,10), pady=(0,10), sticky="w")

    def AddItem1():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox1.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Virgin Mohito")
                RateList.append(VirginMohitoPrice)
                QntyList.append(QtyBox1.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton1= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem1,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton1.grid(row=4, column=1, padx=(5,50), pady=(0,10), sticky="e")


    sepframe1=Frame(ProductsFrame, bg='#92817A', height=1, width=720)
    sepframe1.grid(row=5, column=0, columnspan=2, padx=(5,5), pady=(5,5))


    CranberryPunchLabel=Label(ProductsFrame, image=CranberryPunchImage)
    CranberryPunchLabel.grid(row=6, rowspan=4, column=0, padx=(5,5),pady=(10,10))
    CranberryPunchNameLabel=Label(ProductsFrame, text="CRANBERRY PUNCH", font=('Cambria', 16,),
                         bg="#F1DABF", fg="#362417")
    CranberryPunchNameLabel.grid(row=6,column=1, sticky="w", padx=(5,0), pady=(7,0))
    CranberryPunchDescLabel=Label(ProductsFrame, text="(Non-alcoholic Cranberry Punch made with sparkling water \n and citrus soda and frozen cranberries )",
                         font=('Cambria', 12), justify=LEFT, bg="#F1DABF", fg="#362417")
    CranberryPunchDescLabel.grid(row=7,column=1, sticky="w", padx=(5,0), pady=(0,0))
    CranberryPunchPriceLabel=Label(ProductsFrame, text="Price:  Rs."+str(CranberryPunchPrice), font=('Cambria', 16),
                         bg="#F1DABF", fg="#362417")
    CranberryPunchPriceLabel.grid(row=8,column=1, sticky="w", padx=(5,0), pady=(0,0))
    QtyBox2=Spinbox(ProductsFrame, textvariable=Qty2, font=('Cambria', 16), bd=2,
                   width=10, values=QtyValues,  state='readonly',wrap=True,  justify=CENTER,
                   fg='#362417', readonlybackground='ivory')
    QtyBox2.grid(row=9, column=1, padx=(50,10), pady=(0,10), sticky="w")
    
    def AddItem2():
        global CartList, RateList, QntyList
        cnfm = messagebox.askyesno("Purchase Confirmation","Are you sure you want add this item to your cart??")
        if cnfm:
            if str(QtyBox2.get())=="--Quantity--":
                messagebox.showerror("Quantity Error", "Please select some Quantity!")
            else:
                CartList.append("Cranberry Punch")
                RateList.append(CranberryPunchPrice)
                QntyList.append(QtyBox2.get())
                messagebox.showinfo("Product Status", "Item successfully added to your cart")
        else:
            messagebox.showinfo("Product Status", "Item not added to your cart")
    AddItemButton2= Button(ProductsFrame, text="Add Item(s)", font=('Cambria', 16), bd=0,
                          cursor='hand2', command=AddItem2,
                          bg = '#92817A', fg = '#362417', activeb='#92817A', activef='#362417')
    AddItemButton2.grid(row=9, column=1, padx=(5,50), pady=(0,10), sticky="e")

    
    
#---for Top Frame
TopFrame = Frame(width=995, height=65, bd=10, bg='#362417', relief=FLAT)
TopFrame.place(x=0,y=0)


def HomeFunction():
    AboutFrame=Frame(bg='#F1DABF')
    AboutFrame.place(x=242,y=65)
    AboutPage=Label(AboutFrame, image = AboutImage)
    AboutPage.grid(row=0, column=0)

HomeImage=PhotoImage(file=r"Pictures/Chef-Homebutton.png").subsample(6,6)
HomeButton=Button(TopFrame, bd=0, cursor='hand2', command=HomeFunction,
                  image=HomeImage)
HomeButton.place(x=0, y=0)

LoginBG=PhotoImage(file=r"Pictures/SignInBg.png")
SigninBG=PhotoImage(file=r"Pictures/SignInBg.png")
def Login_window():
    loginwindow = Toplevel()
    loginwindow.title('La Fantaisie://LOG-IN PAGE')
    loginwindow.iconbitmap('Pictures/chef.ico')
    loginwindow.geometry()
    loginwindow.resizable(0,0)
    Backgrd=Label(loginwindow, image = LoginBG)
    Backgrd.grid(row=0,column=0)

    frame=Frame(loginwindow,bg='#A9A8AA')
    frame.place(x=386.5, y=34)
    Heading = Label(frame, text = "USER LOG-IN", font=('Copperplate Gothic Light',20),
                bg='#A9A8AA', fg='white')
    Heading.grid(row=0, column=0,padx=40.5, pady=10)

    
    UserLabel= Label(frame, text = "Username: ",font=('Cambria',14),
                 bg='#A9A8AA', fg='white')
    UserLabel.grid(row=1, column=0, sticky='w', padx=20, pady=(20,0))
    UserEntry = Entry(frame, width=21, font=('Cambria',14))
    UserEntry.grid(row=2, column=0, sticky='w', padx=(20,0))


    PwdLabel= Label(frame, text = "Password: ",font=('Cambria',14),
                 bg='#A9A8AA', fg='white')
    PwdLabel.grid(row=3, column=0, sticky='w', padx=20, pady=(20,0))
    PwdEntry = Entry(frame, width=21, font=('Cambria',14), show="*")
    PwdEntry.grid(row=4, column=0, sticky='w', padx=(20,0))
  
    def loginUser():
            if UserEntry.get()=='' or PwdEntry.get()=='' :
                messagebox.showerror("Error","All fields required")
            else:
                try:    
                    con=sql.connect(host = 'localhost',user='root',password='dhani*')
                    mycursor=con.cursor()
                except:
                    messagebox.showerror("Error","Couldn't establish connection")
                    return
                query = 'use Userdata'
                mycursor.execute(query)
                query = 'select * from Data where Username=%s and Password=%s'
                mycursor.execute(query,(UserEntry.get(),PwdEntry.get(),))
                row = mycursor.fetchone()
                if row == None:
                    messagebox.showerror("Error","Incorrect username or password")
                else:
                    messagebox.showinfo("Success","Login successful")
                    global TopFrame
                    UserNameLabel=Label(TopFrame, text="Hey, "+str(UserEntry.get()),font=('Book Antiqua',12),height=2, width=20,bg='#362417', fg='white')
                    UserNameLabel.place(x=770, y=1)
                    loginwindow.destroy()
    
    LoginButton = Button(frame, text= 'Log In', font=('Microsoft Yahei UI Light',16,'bold'),bd=0,
                     width=15, bg='#494449',fg='white', activeb='#494449', activef='white',
                     cursor='hand2', command=loginUser)
    LoginButton.grid(row=5, column=0, pady=(35,25))

    NoAccount=Label(frame, text = "Do not have an account?", font=('Cambria',12),
                bg='#A9A8AA', fg='white')
    NoAccount.grid(row=6, column=0, sticky='w', padx=20, pady=(10,0))

    def SignUp_window():
        loginwindow.destroy()
        signupwindow = Toplevel()
        signupwindow.title('La Fantaisie://SIGN-UP PAGE')
        signupwindow.iconbitmap('Pictures/chef.ico')
        signupwindow.geometry()
        signupwindow.resizable(0,0)
        Backgrd=Label(signupwindow, image = SigninBG)
        Backgrd.grid(row=0,column=0)

        frame=Frame(signupwindow,bg='#A9A8AA')
        frame.place(x=386.5, y=34)
        Heading = Label(frame, text = "Create a New Account", font=('Copperplate Gothic Light',15),
                bg='#A9A8AA', fg='white')
        Heading.grid(row=0, column=0,padx=12, pady=(10,0))
        
        UserLabel= Label(frame, text = "Username: ",font=('Cambria',14),
                 bg='#A9A8AA', fg='white')
        UserLabel.grid(row=1, column=0, sticky='w', padx=20, pady=(15,0))
        UserEntry = Entry(frame, width=21, font=('Cambria',14))
        UserEntry.grid(row=2, column=0, sticky='w', padx=(20,0))
        
        PwdLabel= Label(frame, text = "Password: ",font=('Cambria',14),
                 bg='#A9A8AA', fg='white')
        PwdLabel.grid(row=3, column=0, sticky='w', padx=20, pady=(15,0))
        PwdEntry = Entry(frame, width=21, font=('Cambria',14), show="*")
        PwdEntry.grid(row=4, column=0, sticky='w', padx=(20,0))

        ConfPwdLabel= Label(frame, text = "Confirm Password: ",font=('Cambria',14),
                 bg='#A9A8AA', fg='white')
        ConfPwdLabel.grid(row=5, column=0, sticky='w', padx=20, pady=(15,0))
        ConfPwdEntry = Entry(frame, width=21, font=('Cambria',14), show="*")
        ConfPwdEntry.grid(row=6, column=0, sticky='w', padx=(20,0))
        
        def connectDatabase():
            if UserEntry.get()=='' or PwdEntry.get()=='' or ConfPwdEntry.get() == '':
                messagebox.showerror("Error","All fields are required.")
            elif PwdEntry.get() != ConfPwdEntry.get():
                messagebox.showerror("Error","Password mismatch")
            else:
                try:
                    con=sql.connect(host = 'localhost',user='root',password='dhani*')
                    mycursor=con.cursor()
                except:
                    messagebox.showerror("Error","Database connectivity issue. Please try again.")
                    return
                try:
                    query = 'create database Userdata'
                    mycursor.execute(query)
                    query = 'use Userdata'
                    mycursor.execute(query)
                    query = 'create table Data (Id int auto_increment primary key not null,Username varchar(20),Password varchar(20))'
                    mycursor.execute(query)
                except:
                    mycursor.execute('use userdata ')
                    
                query='select * from data where username=%s'
                mycursor.execute(query,(UserEntry.get(),))

                row = mycursor.fetchone()
                if row != None:
                    messagebox.showerror("Error","Username already exists.")
                else:
                    query = 'insert into data (Username,Password) values(%s,%s)'
                    mycursor.execute(query,(UserEntry.get(),PwdEntry.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Resistration successful.")
                    global TopFrame
                    UserNameLabel=Label(TopFrame, text="Hey, "+str(UserEntry.get()),font=('Book Antiqua',12),height=2, width=20,bg='#362417', fg='white')
                    UserNameLabel.place(x=770, y=1)
                    signupwindow.destroy()

        SignUpButton = Button(frame, text= 'Sign Up', font=('Microsoft Yahei UI Light',16,'bold'),bd=0,
                     width=15, bg='#494449',fg='white', activeb='#494449', activef='white',
                     cursor='hand2', command=connectDatabase)
        SignUpButton.grid(row=7, column=0, pady=(20,12))

        AlreadyAccount=Label(frame, text = "Already have an account?", font=('Cambria',12),
                bg='#A9A8AA', fg='white')
        AlreadyAccount.grid(row=8, column=0, sticky='w', padx=20, pady=(10,0))

        LogInHere = Button(frame, text= 'Log-in here', font=('Cambria',12,'bold underline'),
                      bd=0, bg='#A9A8AA',fg='#494449', activeb='#A9A8AA', activef='#494449',
                      cursor='hand2',command=Login_window)
        LogInHere.grid(row=9, column=0, sticky='w', padx=20)

    RegisterHere = Button(frame, text= 'Register here', font=('Cambria',12,'bold underline'),
                      bd=0, bg='#A9A8AA',fg='#494449', activeb='#A9A8AA', activef='#494449',
                      cursor='hand2', command=SignUp_window)
    RegisterHere.grid(row=7, column=0, sticky='w', padx=20)

    
LoginImage=PhotoImage(file=r"Pictures/LoginIcon.png").subsample(3,3)
LoginButton=Button(TopFrame, text = 'Log In ', font=('Book Antiqua',12),
                   bd=0, padx=8, pady=2, cursor='hand2',
                   bg='#92817A', fg='#362417', activeb='#92817A', activef='#362417', 
                   image = LoginImage, compound = LEFT, command=Login_window)
LoginButton.place(x=820, y=2)


CartBG=PhotoImage(file=r"Pictures/CartBg.png")
InvoiceBG=PhotoImage(file=r"Pictures/BillBg.png")
def CartFunction():
    Cartwindow = Toplevel(root)
    Cartwindow.title('La Fantaisie://YOUR CART')
    Cartwindow.iconbitmap('Pictures/chef.ico')
    Cartwindow.geometry()
    Cartwindow.resizable(0,0)
    
    Backgrd=Label(Cartwindow, image = CartBG)
    Backgrd.grid(row=0,column=0)

    frame=Frame(Cartwindow,bg='#B8B8BC')
    frame.place(x=306, y=38)

    for n in range(len(CartList)):
        for item in CartList:
            ItemLabel = Label(frame, text = str(CartList[n])+"("+str(QntyList[n])+")",
                              font=('Cambria',12,), bg='#B8B8BC', fg='Black')
            ItemLabel.grid(row=n, column=0,padx=5, pady=5)
            RateLabel = Label(frame, text = " - Rs."+str(RateList[n]),
                              font=('Cambria',12,), bg='#B8B8BC', fg='Black')                           
            RateLabel.grid(row=n, column=1, padx=5, pady=5)
            break

    EmptyList=[]
    def Checkout():
        if CartList==EmptyList:
            messagebox.showerror("Empty Cart!"," Your Cart is empty. Please add the items you want to purchase.")
        else:
            Cartwindow.destroy()
            Invoicewindow = Toplevel()
            Invoicewindow.title('La Fantaisie://YOUR PURCHASE INVOICE')
            Invoicewindow.iconbitmap('Pictures/chef.ico')
            Invoicewindow.geometry()
            Invoicewindow.resizable(0,0)

            Backgrd=Label(Invoicewindow, image = InvoiceBG)
            Backgrd.grid(row=0,column=0)

            frame=Frame(Invoicewindow,bg='#B8B8BC')
            frame.place(x=27, y=77)

            ItemName=Label(frame, text="NAME",font=('Cambria',16,"bold underline"), width=15,bg='#B8B8BC', fg='Black')
            ItemName.grid(row=0,column=0)
            ItemQty=Label(frame, text="QUANTITY",font=('Cambria',16,"bold underline"),width=15, bg='#B8B8BC', fg='Black')
            ItemQty.grid(row=0,column=1)
            ItemRate=Label(frame, text="RATE",font=('Cambria',16,"bold underline"), width=15, bg='#B8B8BC', fg='Black')
            ItemRate.grid(row=0,column=2)
            ItemPrice=Label(frame, text="PRICE",font=('Cambria',16,"bold underline"),width=15, bg='#B8B8BC', fg='Black')
            ItemPrice.grid(row=0,column=3)

            CostList=[]
            for x in range(len(QntyList)and len(RateList)):
                for element in QntyList and RateList:
                    price=int(QntyList[x])*int(RateList[x])
                    CostList.append(price)
                    break
            
            for n in range(len(CartList)):
                for item in CartList:
                    ItemLabel = Label(frame, text = str(CartList[n]),
                              font=('Cambria',12,), bg='#B8B8BC', fg='Black')
                    ItemLabel.grid(row=n+1, column=0,padx=5, pady=5)
                    QtyLabel = Label(frame, text = str(QntyList[n]),
                              font=('Cambria',12,), bg='#B8B8BC', fg='Black')
                    QtyLabel.grid(row=n+1, column=1,padx=5, pady=5)
                    RateLabel = Label(frame, text = "Rs. "+str(RateList[n]),
                              font=('Cambria',12,), bg='#B8B8BC', fg='Black')
                    RateLabel.grid(row=n+1, column=2, padx=5, pady=5)
                    PriceLabel = Label(frame, text = "Rs. "+str(CostList[n]),
                              font=('Cambria',12,), bg='#B8B8BC', fg='Black')
                    PriceLabel.grid(row=n+1, column=3, padx=5, pady=5)
                    break

            TotalPriceLabel=Label(Invoicewindow, text = "TOTAL PRICE:     Rs.  "+str(sum(CostList)),font=('Cambria',16),
                                  width=25, bg='#B8B8BC',fg='Black')
            TotalPriceLabel.place(x=100, y=485)

            def ConfirmOrder():
                check=messagebox.askyesno("Purchase Confirmation", "Any order once placed cannot be modified. \n Are you sure you want to place the order? ")
                if check:
                    Invoicewindow.destroy()
                    HomeFunction()
                    messagebox.showinfo("Order Status", "Your Order has been successfully placed. \n Continue to shop again!!")
                    global CartList,QntyList,RateList,CostList
                    CartList=EmptyList
                    QntyList=EmptyList
                    RateList=EmptyList
                    CostList=EmptyList
                else:
                    messagebox.showinfo("Order Status","Your Order is not yet placed.\n You may continue to shop and \n add more items to the Cart")
                

            OrderButton = Button(Invoicewindow, text = "Confirm Order", font=('Cambria',16),
                                 width=15, bg='#B8B8BC',fg='Black',activeb='#B8B8BC', activef='Black',
                                 cursor='hand2', command=ConfirmOrder)
            OrderButton.place(x=500, y=482)

            
            
    CheckoutButton = Button(Cartwindow, text= 'Proceed to Check-Out', font=('Cambria',14),bd=0,
                     width=20, bg='#B8B8BC',fg='Black', activeb='#B8B8BC', activef='Black',
                     cursor='hand2', command=Checkout)
    CheckoutButton.place(x=350, y=400)
        
    
CartImage=PhotoImage(file=r"Pictures/CartIcon.png").subsample(3,3)
CartButton=Button(TopFrame, text = 'Cart ', font=('Book Antiqua',12),
                   bd=0, padx=14, pady=2, cursor='hand2', command=CartFunction,
                   bg='#92817A', fg='#362417', activeb='#92817A', activef='#362417',
                   image = CartImage, compound = LEFT)
CartButton.place(x=650, y=2)


#---for Side Frame
SideFrame = Frame(width=200, height=535, bd=10, bg='#92817A', relief=FLAT)
SideFrame.place(x=0,y=65)

def ChangeOnHover(button):
    button.bind("<Enter>", func=lambda e: button.config(bg='#362417', fg='#92817A'))
    button.bind("<Leave>", func=lambda e: button.config(bg='#92817A', fg='#362417'))


MenuLabel = Label(SideFrame, text = 'MENU', font = ('Cambria', 16), width=18,
                  bg = '#92817A', fg = '#362417')
MenuLabel.grid(row=0,column=0, columnspan=2, pady=(10,10))

SaladsB = Button(SideFrame, text = 'Salads', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=SaladsButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
SaladsB.grid(row=1, column=0, sticky='w', padx=0)
ChangeOnHover(SaladsB)

PastasB = Button(SideFrame, text = 'Pastas', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=PastasButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
PastasB.grid(row=2, column=0, sticky='w', padx=0)
ChangeOnHover(PastasB)

PizzasB = Button(SideFrame, text = 'Pizzas', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=PizzasButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
PizzasB.grid(row=3, column=0, sticky='w', padx=0)
ChangeOnHover(PizzasB)

SandwichesB = Button(SideFrame, text = 'Sandwiches', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=SandwichesButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
SandwichesB.grid(row=4, column=0, sticky='w', padx=0)
ChangeOnHover(SandwichesB)


DessertsLabel = Label(SideFrame, text = 'DESSERTS', font = ('Cambria', 16), width=18,
                  bg = '#92817A', fg = '#362417')
DessertsLabel.grid(row=5,column=0, columnspan=2, pady=(10,10))

CakesB = Button(SideFrame, text = 'Cakes', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=CakesButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
CakesB.grid(row=6, column=0, sticky='w', padx=0)
ChangeOnHover(CakesB)

CookiesB = Button(SideFrame, text = 'Cookies', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=CookiesButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
CookiesB.grid(row=7, column=0, sticky='w', padx=0)
ChangeOnHover(CookiesB)

Ice_CreamsB = Button(SideFrame, text = 'Ice-Creams', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=IceCreamsButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
Ice_CreamsB.grid(row=8, column=0, sticky='w', padx=0)
ChangeOnHover(Ice_CreamsB)


BeveragesLabel = Label(SideFrame, text = 'BEVERAGES', font = ('Cambria', 16), width=18,
                  bg = '#92817A', fg = '#362417')
BeveragesLabel.grid(row=9,column=0, columnspan=2, pady=(10,10))

CoffeeB = Button(SideFrame, text = 'Coffee', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=CoffeesButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
CoffeeB.grid(row=10, column=0, sticky='w', padx=0)
ChangeOnHover(CoffeeB)

TeaB = Button(SideFrame, text = 'Tea', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=TeasButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
TeaB.grid(row=11, column=0, sticky='w', padx=0)
ChangeOnHover(TeaB)

DecafB = Button(SideFrame, text = 'Decaf', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=DecafButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
DecafB.grid(row=12, column=0, sticky='w', padx=0)
ChangeOnHover(DecafB)

DrinksB = Button(SideFrame, text = 'Non-Alcoholic Drinks', font = ('Cambria', 14), bd=0, width=20,
                 anchor = 'w', padx=8, command=DrinksButton,
                 bg = '#92817A', fg = '#362417', activeb='#362417', activef='#92817A')
DrinksB.grid(row=13, column=0, sticky='w', padx=0)
ChangeOnHover(DrinksB)



root.mainloop()

