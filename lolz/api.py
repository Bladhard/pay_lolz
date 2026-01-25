from lolz.payments import PaymentsAPI


class LolzAPI:
    def __init__(self, token: str):
        self.payments = PaymentsAPI(token)
