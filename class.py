class car :
    def __init__(self):
        self.brand=''
        self.name=''

    def set_details(self):
        print("enter brand")
        self.brand= input ()
        print("enter color")
        self.color= input ()

    def get_details(self):
        print(f"brand ={self.brand}")
        print(f"color={self.color}")



#object creation for class car
irtiqa= car()
irtiqa.set_details()
irtiqa.get_details()
    

