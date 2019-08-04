import requests
import shutil

dir = 'C:/Users/JON7390/OneDrive/图片/Wallpaper/'
url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=%d&n=1&mkt=en-US'
max_try = 10

tries =0
while True:
    tries += 1
    if tries < max_try:
        try:
            gallery = requests.get(url % i)
            img_url = 'http://bing.com' + gallery.json()['images'][0]['url']
            img_stream = requests.get(img_url, stream=True)

            if img_stream.status_code == 200:
                file_name = dir + img_url.split('OHR.')[1].split('_')[0] + '.jpg'
                with open(file_name, 'wb') as fw:
                    shutil.copyfileobj(img_stream.raw, fw)
                # print('done getting wall paper today - %d times tried' % (tries))
                break
        except:
            # print('trying to get wall paper today - %d times tried' % (tries))
            pass
    else:
        break