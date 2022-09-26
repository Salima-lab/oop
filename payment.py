import client
class Payment(client.Client):
    def __init__(self ,credit,bonus,pay):
        super().__init__(credit,bonus)
        self.pay = pay

    def pay_with_bonus_card(self):
        self.credit-=self.pay
        return self.credit
    
    def pay_without_bonus_card(self):
        self.credit-=(self.pay -100) 
        return self.credit

    def check_bonus(self):
        if self.bonus:
            pay_with_bonus_card()
        else:
            pay_without_bonus_card()