import requests


class PaymentsAPI:
    def __init__(self, token: str):
        self.token = token

    def history(
        self,
        operation_type: str,
        pmin: int,
        pmax: int,
        comment: str,
        is_hold: str,
    ) -> dict:
        url = "https://prod-api.lzt.market/user/payments"

        params = {
            "type": operation_type,
            "pmin": pmin,
            "pmax": pmax,
            "comment": comment,
            "is_hold": is_hold,
        }

        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {self.token}",
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        return response.json()
