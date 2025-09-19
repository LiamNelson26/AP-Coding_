# An object is a construct for storing data and functions 
# When creating an object we start with the class keyword.
# This acts like our object maker/ our blueprint


class instaProfile:
    def _init_(self, username, email, profileImg):
        self.username = username
        self.email = email
        self.profileImg= profileImg
        self.pw = pw
        self.bio = bio

    def printInfo(self):
        print('username' + self.username,)
        print('email:')

    def resetPw(self):
        print('2-step auth...')

    def uploadPicture(self):
        print('intructions')

    def viewFollowes(self):
        print(['list of other followers'])

profile1 = instaProfile.username('Ian','ik@aoil.com','pic.png','123','lorem ipsum')
profile2 = instaProfile('Rob','rob@gmail.com','pic.png','321','lorem ipsu'm)

profile1.printIn

instaProfile.printInfo()


print(profile)



class CarMaker:
    def _init_(self, name, color, seating, year, model): # initializes the blueprint
        self.name = name
        self.color = color
        self.seating = seating,
        self.year = year
        self.model = model

    def windshieldWippers():
        print('when raining turn on')

    def airbag():
        print('when driving a ceertain speed anc and collision happens; open')

    def turnSignals(up, down):
        if up:
            print("turn left")
        elif down:
            print("turn right")
        else:
            print("don't turn signals on")

    def bluetooth(year):
        if year > 2020:
            print('you have bluetooth')
        else:
            print("no bluetooh on this model")

ToyotaCorolla = CarMaker('corrolla', 'black','2','carolls', 20000)

def printInfo(self):
    print('here is your car FAQS') # FACT
    print('name: '+ self.name)
    print('year: '+ str(self.year))
    print('miiles: '+ str(self.miles))

def windshieldswippers(self):
    print("when raining turn on")

def airbag(self):
    print("when driving a certain speed anc a collision happens; open")

def turnsignals(self,up,down):
    if up == 1:
        print("turn left")
    elif down:
        print("turn right")
    else:
        print("don't turn signals on")

def bluetooth(self, year):
    if year > 2020:
        print("you have bluetooth")
    else:
        print("no bluetooth on this model")

carOption1 = CarMaker('carolla', 'black', '2', '2024', 'carolla', 20000) # creating actual car data
print(carOption1) # shows the location in computer memory
carOption1.printInfo() # shows me actual data


class Phone:
    def _init_(self, brand, color, size, design):
        self.name = brand
        self.color = color
        self.seating = size,
        self.year = design

    def storage():
        print('You have a certain amount of storage in your phone')

    def (phoneNumber):
    print('Your phone number is "233,455,677"')

    def turnSignals():
        if up:
            print("")
        elif down:
            print("")
        else:
            print("")


