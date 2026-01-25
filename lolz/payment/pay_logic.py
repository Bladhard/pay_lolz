import asyncio

from config import LOLZ_API_TOKEN

# from log_config import logger
from lolz.lolzapi import Market

api = Market(token=LOLZ_API_TOKEN)

# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")

class PaymentCheck:
    def __init__(self, subs_price: int, comment_token: str):
        self.subs_price = subs_price
        self.comment_token = comment_token

    async def check_payment(self) -> bool:
        """
        Проверяет, был ли получен платеж за подписку. Запрашивает Lolz API о платежах с ценой, равной
        цене подписки и комментарием, соответствующим платежной информации в базе.

        :return: True, если платеж найден, False в противном случае.
        """
        try:
            data_payments = api.payments.history(
                operation_type="income",
                pmin=self.subs_price,
                pmax=self.subs_price,
                comment=self.comment_token,
                is_hold="false",
            )
            if len(data_payments["payments"]):
                return True
            else:  # noqa: RET505
                return False
        except Exception:  # noqa: BLE001
            await asyncio.sleep(2)
            # logger.error(f"Ошибка lolz: {err}")
