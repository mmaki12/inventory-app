from appJar import gui
app = gui("Login Window", "400x200")
import sqlite3
import uuid

import requests
from PIL import Image
from io import BytesIO

conn = sqlite3.connect('Invt.db')
cursor = conn.cursor()

"""
cursor.execute('''CREATE TABLE "Inventory" (
        "id"	TEXT,
	"name"	TEXT,
	"price"	REAL,
	"description"	TEXT,
	"category"	TEXT,
	"image"	INTEGER
        );''')

cursor.execute('''CREATE TABLE "Sauces" (
        "id"	TEXT,
	"name"	TEXT,
	"image"	TEXT
        );''')

sauces = [
    ("21","Sriracha","https://64.media.tumblr.com/12cd128183713bf928bda87a24f22487/tumblr_ne6jee85PM1tha1vgo1_250.gif"),
    ("22","Franks","https://cdn.streamelements.com/uploads/1887a0da-3642-4795-b5f5-774d5b377e52.gif"),
    ("23","Tobasco","https://64.media.tumblr.com/1564fcf74adc3fe6542c34b6a1f05de1/tumblr_na9lew0bNS1tha1vgo1_r1_250.gif")
  ]

items = [
    (
        "1",
        "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
        109.95,
        "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
        "men's clothing",
        "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
    ),
    (
        "2",
        "Mens Casual Premium Slim Fit T-Shirts ",
        22.3,
        "Slim-fitting style, contrast raglan long sleeve, three-button henley placket, light weight & soft fabric for breathable and comfortable wearing. And Solid stitched shirts with round neck made for durability and a great fit for casual fashion wear and diehard baseball fans. The Henley style round neckline includes a three-button placket.",
        "men's clothing",
        "https://fakestoreapi.com/img/71-3HjGNDUL._AC_SY879._SX._UX._SY._UY_.jpg"
    ),
    (
        "3",
        "Mens Cotton Jacket",
        55.99,
        "Great outerwear jackets for Spring/Autumn/Winter, suitable for many occasions, such as working, hiking, camping, mountain/rock climbing, cycling, traveling or other outdoors. Good gift choice for you or your family member. A warm-hearted love to Father, husband, or son on this Thanksgiving or Christmas Day.",
        "men's clothing",
        "https://fakestoreapi.com/img/71li-ujtlUL._AC_UX679_.jpg"
    ),
    (
        "4",
        "Mens Casual Slim Fit",
        15.99,
        "The color could be slightly different between on the screen and in practice. / Please note that body builds vary by person, therefore, detailed size information should be reviewed below on the product description.",
        "men's clothing",
        "https://fakestoreapi.com/img/71YXzeOuslL._AC_UY879_.jpg"
    ),
    (
        "5",
        "John Hardy Women's Legends Naga Gold & Silver Dragon Station Chain Bracelet",
        695,
        "From our Legends Collection, the Naga was inspired by the mythical water dragon that protects the ocean's pearl. Wear facing inward to be bestowed with love and abundance, or outward for protection.",
        "jewelry",
        "https://fakestoreapi.com/img/71pWzhdJNwL._AC_UL640_QL65_ML3_.jpg"
    ),
    (
        "6",
        "Solid Gold Petite Micropave ",
        168,
        "Satisfaction Guaranteed. Return or exchange any order within 30 days. Designed and sold by Hafeez Center in the United States. Satisfaction Guaranteed. Return or exchange any order within 30 days.",
        "jewelry",
        "https://fakestoreapi.com/img/61sbMiUnoGL._AC_UL640_QL65_ML3_.jpg"
    ),
    (
        "7",
        "White Gold Plated Princess",
        9.99,
        "Classic Created Wedding Engagement Solitaire Diamond Promise Ring for Her. Gifts to spoil your love more for Engagement, Wedding, Anniversary, Valentine's Day...",
        "jewelry",
        "https://fakestoreapi.com/img/71YAIFU48IL._AC_UL640_QL65_ML3_.jpg"
    ),
    (
        "8",
        "Pierced Owl Rose Gold Plated Stainless Steel Double",
        10.99,
        "Rose Gold Plated Double Flared Tunnel Plug Earrings. Made of 316L Stainless Steel",
        "jewelry",
        "https://fakestoreapi.com/img/51UDEzMJVpL._AC_UL640_QL65_ML3_.jpg"
    ),
    (
        "9",
        "WD 2TB Elements Portable External Hard Drive - USB 3.0 ",
        64,
        "USB 3.0 and USB 2.0 Compatibility Fast data transfers Improve PC Performance High Capacity; Compatibility Formatted NTFS for Windows 10, Windows 8.1, Windows 7; Reformatting may be required for other operating systems; Compatibility may vary depending on user’s hardware configuration and operating system",
        "electronics",
        "https://fakestoreapi.com/img/61IBBVJvSDL._AC_SY879_.jpg"
    ),
    (
        "10",
        "SanDisk SSD PLUS 1TB Internal SSD - SATA III 6 Gb/s",
        109,
        "Easy upgrade for faster boot up, shutdown, application load and response (As compared to 5400 RPM SATA 2.5” hard drive; Based on published specifications and internal benchmarking tests using PCMark vantage scores) Boosts burst write performance, making it ideal for typical PC workloads The perfect balance of performance and reliability Read/write speeds of up to 535MB/s/450MB/s (Based on internal testing; Performance may vary depending upon drive capacity, host device, OS and application.)",
        "electronics",
        "https://fakestoreapi.com/img/61U7T1koQqL._AC_SX679_.jpg"
    ),
    (
        "11",
        "Silicon Power 256GB SSD 3D NAND A55 SLC Cache Performance Boost SATA III 2.5",
        109,
        "3D NAND flash are applied to deliver high transfer speeds Remarkable transfer speeds that enable faster bootup and improved overall system performance. The advanced SLC Cache Technology allows performance boost and longer lifespan 7mm slim design suitable for Ultrabooks and Ultra-slim notebooks. Supports TRIM command, Garbage Collection technology, RAID, and ECC (Error Checking & Correction) to provide the optimized performance and enhanced reliability.",
        "electronics",
        "https://fakestoreapi.com/img/71kWymZ+c+L._AC_SX679_.jpg"
    ),
    (
        "12",
        "WD 4TB Gaming Drive Works with Playstation 4 Portable External Hard Drive",
        114,
        "Expand your PS4 gaming experience, Play anywhere Fast and easy, setup Sleek design with high capacity, 3-year manufacturer's limited warranty",
        "electronics",
        "https://fakestoreapi.com/img/61mtL65D4cL._AC_SX679_.jpg"
    ),
    (
        "13",
        "Acer SB220Q bi 21.5 inches Full HD (1920 x 1080) IPS Ultra-Thin",
        599,
        "21. 5 inches Full HD (1920 x 1080) widescreen IPS display And Radeon free Sync technology. No compatibility for VESA Mount Refresh Rate: 75Hz - Using HDMI port Zero-frame design | ultra-thin | 4ms response time | IPS panel Aspect ratio - 16: 9. Color Supported - 16. 7 million colors. Brightness - 250 nit Tilt angle -5 degree to 15 degree. Horizontal viewing angle-178 degree. Vertical viewing angle-178 degree 75 hertz",
        "electronics",
        "https://fakestoreapi.com/img/81QpkIctqPL._AC_SX679_.jpg"
    ),
    (
        "14",
        "Samsung 49-Inch CHG90 144Hz Curved Gaming Monitor (LC49HG90DMNXZA) – Super Ultrawide Screen QLED ",
        999.99,
        "49 INCH SUPER ULTRAWIDE 32:9 CURVED GAMING MONITOR with dual 27 inch screen side by side QUANTUM DOT (QLED) TECHNOLOGY, HDR support and factory calibration provides stunningly realistic and accurate color and contrast 144HZ HIGH REFRESH RATE and 1ms ultra fast response time work to eliminate motion blur, ghosting, and reduce input lag",
        "electronics",
        "https://fakestoreapi.com/img/81Zt42ioCgL._AC_SX679_.jpg"
    ),
    (
        "15",
        "BIYLACLESEN Women's 3-in-1 Snowboard Jacket Winter Coats",
        56.99,
        "Note:The Jackets is US standard size, Please choose size as your usual wear Material: 100% Polyester; Detachable Liner Fabric: Warm Fleece. Detachable Functional Liner: Skin Friendly, Lightweigt and Warm.Stand Collar Liner jacket, keep you warm in cold weather. Zippered Pockets: 2 Zippered Hand Pockets, 2 Zippered Pockets on Chest (enough to keep cards or keys)and 1 Hidden Pocket Inside.Zippered Hand Pockets and Hidden Pocket keep your things secure. Humanized Design: Adjustable and Detachable Hood and Adjustable cuff to prevent the wind and water,for a comfortable fit. 3 in 1 Detachable Design provide more convenience, you can separate the coat and inner as needed, or wear it together. It is suitable for different season and help you adapt to different climates",
        "women's clothing",
        "https://fakestoreapi.com/img/51Y5NI-I5jL._AC_UX679_.jpg"
    ),
    (
        "16",
        "Lock and Love Women's Removable Hooded Faux Leather Moto Biker Jacket",
        29.95,
        "100% POLYURETHANE(shell) 100% POLYESTER(lining) 75% POLYESTER 25% COTTON (SWEATER), Faux leather material for style and comfort / 2 pockets of front, 2-For-One Hooded denim style faux leather jacket, Button detail on waist / Detail stitching at sides, HAND WASH ONLY / DO NOT BLEACH / LINE DRY / DO NOT IRON",
        "women's clothing",
        "https://fakestoreapi.com/img/81XH0e8fefL._AC_UY879_.jpg"
    ),
    (
        "17",
        "Rain Jacket Women Windbreaker Striped Climbing Raincoats",
        39.99,
        "Lightweight perfect for trip or casual wear---Long sleeve with hooded, adjustable drawstring waist design. Button and zipper front closure raincoat, fully stripes Lined and The Raincoat has 2 side pockets are a good size to hold all kinds of things, it covers the hips, and the hood is generous but doesn't overdo it. Attached Cotton Lined Hood with Adjustable Drawstrings give it a real styled look.",
        "women's clothing",
        "https://fakestoreapi.com/img/71HblAHs5xL._AC_UY879_-2.jpg"
    ),
    (
        "18",
        "MBJ Women's Solid Short Sleeve Boat Neck V ",
        9.85,
        "95% RAYON 5% SPANDEX, Made in USA or Imported, Do Not Bleach, Lightweight fabric with great stretch for comfort, Ribbed on sleeves and neckline / Double stitching on bottom hem",
        "women's clothing",
        "https://fakestoreapi.com/img/71z3kpMAYsL._AC_UY879_.jpg"
    ),
    (
        "19",
        "Opna Women's Short Sleeve Moisture",
        7.95,
        "100% Polyester, Machine wash, 100% cationic polyester interlock, Machine Wash & Pre Shrunk for a Great Fit, Lightweight, roomy and highly breathable with moisture-wicking fabric which helps to keep moisture away, Soft Lightweight Fabric with comfortable V-neck collar and a slimmer fit, delivers a sleek, more feminine silhouette and Added Comfort",
        "women's clothing",
        "https://fakestoreapi.com/img/51eg55uWmdL._AC_UX679_.jpg"
    ),
    (
        "20",
        "DANVOUY Womens T Shirt Casual Cotton Short",
        12.99,
        "95%Cotton,5%Spandex, Features: Casual, Short Sleeve, Letter Print,V-Neck,Fashion Tees, The fabric is soft and has some stretch., Occasion: Casual/Office/Beach/School/Home/Street. Season: Spring,Summer,Autumn,Winter.",
        "women's clothing",
        "https://fakestoreapi.com/img/61pHAEJ4NML._AC_UX679_.jpg"
    )
]

    
 


cursor.executemany('INSERT INTO Inventory VALUES (?, ?, ?, ?, ?, ?)', items)
cursor.executemany('INSERT INTO Sauces VALUES (?, ?, ?)', sauces)

conn.commit()
conn.close()


"""


########################image Scraper##################

cursor.execute("SELECT image FROM Inventory ")
url = cursor.fetchall()
y = len(url)
for x in range(y):
    print(url[x][0])



# Get user input for URL and image name
url = input("Enter the URL of the image: ")
image_name = input("Enter the name for the saved image (without extension): ")

# Send a GET request to fetch the image
response = requests.get(url)

if response.status_code == 200:
    # Open the image using PIL
    img = Image.open(BytesIO(response.content))
    
    # Resize the image to 100x100 pixels
    img = img.resize((100, 100))
    
    # Convert and save the image as PNG format
    img.save(f"{image_name}.gif", "GIF")
    print(f"Image downloaded and saved as {image_name}.png (100x100)")
else:
    print("Failed to download the image")


def stop():
    app.stop()
        
def press(button):
    global newUsr
    global newPwd
    if button == "Cancel" or button == "Sign-out":
        app.stop()
    if button == "Create an account":
        acc()
    if button == "Back":
        app.showSubWindow("Login Details", hide=False)
        app.hideSubWindow("Register Details")
    if button == "Create_account":
        newUsr = app.getEntry("username")
        newPwd = app.getEntry("password")
        app.hideSubWindow("Register Details")
        app.showSubWindow("Login Details", hide=False)
        app.infoBox("hello", "You have succesfully created your account "+newUsr+"\n please login")
    if button == "View":
        table()
    if button == "Delete":
        app.hideSubWindow("Home Screen")
        app.showSubWindow("Delete Screen", hide=False)
    if button == "Add":
        app.hideSubWindow("Home Screen")
        app.showSubWindow("Add Screen", hide=False)
    if button == "Update":
        app.hideSubWindow("Home Screen")
        app.showSubWindow("Update Screen", hide=False)   
    
        

def valid():
    global listU
    global listP
    listU =['Muhanad']
    listP =['Maki']
    usr = app.getEntry("Username")
    pwd = app.getEntry("Password")
    eUsr = app.getEntry("username")
    ePwd = app.getEntry("password")
    if usr in listU and pwd in listP or usr == eUsr and pwd == ePwd:
        app.infoBox("hello", "You have succesfully logged in "+usr)
        app.hideSubWindow("Login Details")
        app.showSubWindow("Home Screen", hide=False)
    else:
        app.warningBox("oops", "error inccorect password or username", parent=None)



        
def acc():
    app.hideSubWindow("Login Details")
    app.showSubWindow("Register Details", hide=False)

def dele():
    deletedValue = app.getEntry("Enter the ProductID you would like to delete?")
    cursor.execute("DELETE FROM Inventory WHERE id = ?", [deletedValue])
    conn.commit()
    app.infoBox("boom", "You have successfully deleted Item " + deletedValue)

def data():
    whichDB = app.getOptionBox("Which DataBase")
    if whichDB == "Sauces":
        app.showSubWindow("Sauce Screen", hide=False)

    else:
        app.showSubWindow("Items Screen", hide=False)

    

def generate_unique_id():
    return str(uuid.uuid4())


def addSauces(res):
    sauceName = app.getEntry("Enter Sauce Name")
    sauceImageURL = app.getEntry("Enter Item Image URL")
    newSauceID = generate_unique_id()
    cursor.execute("INSERT INTO Sauces (id, name, image) VALUES (?, ?, ?)",(newSauceID[0:4],sauceName,sauceImageURL))
    conn.commit()  # Committing changes to the database
    app.infoBox("Voila", "You have successfully added " + sauceName + " to the Sauce DB")
    

def addItem(res):   
        itemName = app.getEntry("Enter Item Name")
        itemPrice = app.getEntry("Enter Item Price")
        itemDescription = app.getEntry("Enter Item Description")
        itemImageURL = app.getEntry("Enter Item Image URL")
        itemCategory = app.getEntry("Enter Item category")
        newItemID = generate_unique_id()
        cursor.execute("INSERT INTO Inventory (id, name, price, description, category, image) VALUES (?, ?, ?, ?, ?, ?)",(newItemID[0:4], itemName, itemPrice, itemDescription, itemCategory, itemImageURL))
        conn.commit()  # Committing changes to the database
        app.infoBox("Voila", "You have successfully added " + itemName + " to the Item DB" )


def view():
        app.hideAllSubWindows(useStopFunction=False)
        app.showSubWindow("Home Screen", hide=False)


def table():
    app.hideAllSubWindows(useStopFunction=False)
    app.showSubWindow("View Screen", hide=False)

def fields():
    chosenDb = app.getOptionBox("Choose Which DataBase")
    if chosenDb == "Items":
        app.changeOptionBox("Which Field", ["name","price","description","category","image"])
        #app.changeOptionBox(title, newOptions, index, callFunction=False)
    else:
        app.changeOptionBox("Which Field", ["name","image"])

        
def update():
    chosenDB = app.getOptionBox("Choose Which DataBase")
    field = app.getOptionBox("Which Field")
    newValue = app.getEntry("Enter what you would like to update it to:")
    productID = app.getEntry("Enter the ProductID you would like to update?")

    if chosenDB == "Items":  # Check if the selected database is "Inventory"
        # Get the ProductID from the user
        cursor.execute(f"UPDATE Inventory SET {field} = ? WHERE id = ?", (newValue, productID))
        conn.commit()
        app.infoBox("Success", f"Field {field} updated to {newValue} for ProductID {productID}")#info
    else:
        app.infoBox("Error", "Invalid database selection")  # Display error if the chosen database is not "Inventory"




###################Login Screen###########################
app.startSubWindow("Login Details")
app.setBg("light grey")
app.setFont(18)
app.addLabel("w","Inventory")
app.setLabelBg("w","light pink")
app.addLabelEntry("Username")
app.setLabelEntryBg("Username","light pink")
app.addLabelSecretEntry("Password")
app.addButtons(["Cancel","Create an account"], [stop,press])
app.addNamedButton("Submit","Sub",valid)
app.setFocus("Username")
app.setSize(400, 400)
app.stopSubWindow()
###################Register Screen###########################
app.startSubWindow("Register Details")
app.setBg("light grey")
app.setFont(18)
app.addLabel("wo", "Register")
app.addLabelEntry("username")
app.addLabelSecretEntry("password")
app.addButtons(["Back","Create_account"], press)
app.setFocus("Username")
app.setSize(400, 400)
app.stopSubWindow()
app.hide()
###################Home Screen###########################
app.startSubWindow("Home Screen")
app.setBg("light grey")
app.setFont(18)
app.addButtons(["Add","Delete"], press)
#app.addImage("bag", "me.gif")
app.addButtons(["View","Update"], press)
app.addButton("Sign-out", press)
app.setSize(400, 400)
app.stopSubWindow()
app.hide()

###################View Screen###########################
app.startSubWindow("View Screen")
app.setBg("light grey")
#app.addDbGrid("viewing", "Invt.db", "Inventory")
app.setFont(10)
cursor.execute("SELECT id, name, price, description, category, image FROM Inventory")
rows = cursor.fetchall()
columns = ["ID", "Name", "Price", "Description", "ImageURL"]
# Display column names as labels in the first row
for col_index, column_name in enumerate(columns):
    app.addLabel(column_name, column_name, row=0, column=col_index)

row_index = 1  # Starting index for rows in the interface

# Display row values in the desired order
for row in rows:
    for col_index, value in enumerate(row):
        app.addLabel(f"row{row_index}col{col_index}", str(value), row=row_index, column=col_index)
    row_index += 1
app.addNamedButton("Back","back4",view)
app.stopSubWindow()
app.hide()
##################Delete Screen###########################
app.startSubWindow("Delete Screen")
app.setBg("light grey")
app.addLabelEntry("Enter the ProductID you would like to delete?")
app.setSize(800, 400)
app.addNamedButton("Submit","Sub1",dele)
app.addNamedButton("Back","back3",view)
app.setFont(18)
app.stopSubWindow()
app.hide()
###################Add Screen###########################
app.startSubWindow("Add Screen")
app.setBg("light grey")
app.addLabelOptionBox("Which DataBase", ["Items","Sauces"])
app.addButton("Confirm DataBase", data)
app.addNamedButton("Back","back2",view)
app.setSize(400, 400)
app.setFont(18)
app.stopSubWindow()
app.hide()
###################Items Screen###########################
app.startSubWindow("Items Screen")
app.setBg("light grey")
app.addLabelEntry("Enter Item Name")
app.addLabelEntry("Enter Item Price")
app.addLabelEntry("Enter Item Description")
app.addLabelEntry("Enter Item category")
app.addLabelEntry("Enter Item Image URL")
app.addNamedButton("Submit","Sub2",addItem)
app.addNamedButton("Back","back1",view)
app.setSize(400, 400)
app.setFont(18)
app.stopSubWindow()
app.hide()
###################Sauce Screen###########################
app.startSubWindow("Sauce Screen")
app.setBg("light grey")
app.addLabelEntry("Enter Sauce Name")
app.addLabelEntry("Enter Sauce Image URL")
app.addNamedButton("Submit","Sub3",addSauces)
app.addNamedButton("Back","back",view)
app.setSize(400, 400)
app.setFont(18)
app.stopSubWindow()
app.hide()
##################Update Screen###########################
app.startSubWindow("Update Screen")
app.setBg("light grey")
app.addLabelOptionBox("Choose Which DataBase", ["Items","Sauces"])
app.addNamedButton("Confirm the DB","cDb",fields)
app.addLabelEntry("Enter the ProductID you would like to update?")
app.addLabelOptionBox("Which Field", [])
app.addLabelEntry("Enter what you would like to update it to:")
app.addNamedButton("commit Updates","Sub4",update)
app.setSize(800, 400)
app.addNamedButton("Back","back5",view)
app.setFont(18)
app.stopSubWindow()
app.hide()


app.go(startWindow="Login Details")


