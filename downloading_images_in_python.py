import random
import urllib.request
def download_web_images(url):
    name=random.randrange(1,1000)
    full_name=str(name)+'.jpg'
    urllib.request.urlretrieve(url,full_name)
download_web_images('https://media-exp1.licdn.com/dms/image/C4E03AQFZa3id4oTGEQ/profile-displayphoto-shrink_800_800/0/1632292549889?e=1645660800&v=beta&t=sPbt8PXmIeswlf0pJENdMOSlmBdh8zQyo_H8pUqSqBs')