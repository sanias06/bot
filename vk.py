import minc
import vk_api
import time


key = minc.key

vk = vk_api.VkApi('89279970370','nikimiki1',token=key)
vk.auth(token_only=True)


values = {'out':0, 'count':100, 'time_offset':60}

def get_message():

    ans = vk.method('messages.get', values)
    return ans

def send_message(user_id, txt):
    vk.method('messages.send', {'user_id':user_id, 'messages':txt })

def main():
    while True:
        ans = get_message()
        if ans['items']:
            values['last_mes_id'] = ans['items'][0]['id']

        chat_id = ans['items'][0]['user_id']
        send_message(chat_id, '335')


if __name__=='__main__':
    main()