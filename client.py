class Client:
    def __init__(self,credit:float,bonus:bool):
        self.credit = credit
        self.bonus = bonus 

    @property
    def get_bonus(self):
        return self.bonus 

    @get_bonus.setter
    def get_bonus(self,bonus):
        self.bonus = bonus 

    @property
    def get_credit(self):
        return self.credit 

    @get_credit.setter
    def get_credit(self,credit):
        self.credit = credit 
    
    def get_status(self):
        return f"Your balance is ${self.credit}"