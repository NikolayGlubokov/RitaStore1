import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone, tg_text):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.find('+') and text.rfind('+') and text.rfind('{') and text.rfind(
                '}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}') + 1:text.find('+')]
            part_3 = text[text.rfind('+')+1:text.rfind('{')]
            part_4 = text[text.rfind('}'):-1]
            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_text + part_4
        else:
            text_slice = text
        req = None

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice})
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Всё ОК')


def send_telegram2(tg_name, tg_phone, tg_text):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.find('+') and text.rfind('+') and text.rfind('{') and text.rfind(
                '}'):
            part_1 = text[0:text.find('{')]
            part_2 = text[text.find('}') + 1:text.find('+')]
            part_3 = text[text.rfind('+')+1:text.rfind('{')]
            part_4 = text[text.rfind('}'):-1]
            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3 + tg_text + part_4
        else:
            text_slice = text
        req = None

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text_slice})
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Всё ОК')




def send_telegram3(order_id, name, contact, paid, description):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        text_slice = 'Заказ №'+str(order_id)+' '+name+' '+contact+' '+str(paid)+' '+description

        text = text_slice
        req = None

        try:
            req = requests.post(method, data={
                'chat_id': chat_id,
                'text': text})
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print('Всё ОК')

# https://api.telegram.org/bot5366946090:AAEeeVHV8vuVHmoMMrLFEIWcHwlph7_JYy0/sendMessage?chat_id=-733830239&text=test
