from fastapi import APIRouter

from lolz.payment.pay_logic import PaymentCheck


lolz_pay = APIRouter()



@lolz_pay.post("/payment_check")
async def payment_check(subs_price: float, comment_token: str):
    # Обработка данных и возврат ответа
    pay = PaymentCheck(subs_price, comment_token)
    print(subs_price, comment_token)
    result = await pay.check_payment()
    return result
