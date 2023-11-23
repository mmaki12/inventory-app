from appJar import gui
app = gui("Login Window", "400x200")
#importning all the libraries
import sqlite3
import uuid


#breaks the code

def stop():
    app.stop()


#redirecting to different pages and functions
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
    
        
#checks the paswords and usernames
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



#shows and hides the subwindows
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

    
#genarates a non reccuring random-id
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
app.addWebLink("if not redirected press this link", "http://localhost:8501")
app.setSize(400, 400)
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



