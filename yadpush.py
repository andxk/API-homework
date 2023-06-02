
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, overwrite = False):
        """Метод загружает файл file_patch на яндекс диск"""
       
        base_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

        file_basename = file_path.rsplit('\\',1)[-1]
        params = {'path' : f'disk:/{file_basename}', 'overwrite': overwrite}

        resp = requests.get(base_url, params=params, headers=headers)

        print(resp.status_code)
        # print(resp.json())

        if resp.status_code == 200:
            href = resp.json()['href']
            print(resp.json())

            resp = requests.put(href, data = open(file_path, 'rb'))
            print(resp.status_code)
            # print(resp)

            if resp.status_code == 201:
                print('Успешно загружено')
                return True

        print(f'Ошибка : {resp.json()["message"]}')
        return False
        


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = r'.\sample\test106.txt'
    
    with open('token.txt','r') as tokenfile:
        token = tokenfile.read().rstrip()
    
    print(token)

    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, True)
