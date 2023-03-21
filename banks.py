import json
import threading
from urllib.request import urlopen

NBU_URL = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
PRIVATE_URL = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"




def get_nbu_course():
    response = urlopen(NBU_URL)
    data = response.read()
    data1 = json.loads(data)
    main = (data1[24])
    nbu_currency = float(main['rate'])
    return nbu_currency


def get_private_course():
    response = urlopen(PRIVATE_URL)
    data = response.read()
    data1 = json.loads(data)
    main = (data1[1])
    private_currency = float(main['buy'])
    return private_currency


def comparison_currs():
    private_currency = get_private_course()
    nbu_currency = get_nbu_course()
    if private_currency > nbu_currency:
        print("PrivatBank currency is",private_currency, "hrivnyas. " "NBU currency is", nbu_currency, "hrivnyas. " "PrivatBank currency is more profitable for", private_currency - nbu_currency, "hrivnyas")
    elif private_currency == nbu_currency:
        print("The currency is the same")
    else:
        print("NBU currency is ", nbu_currency, "hrivnyas. " "PrivatBank currency is ", private_currency, "hrivnyas. " "NBU currency is more profitable for ", nbu_currency - private_currency, "hrivnyas")

t1 = threading.Thread(target=get_nbu_course)
t2 = threading.Thread(target=get_private_course)
t3 = threading.Thread(target=comparison_currs)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()