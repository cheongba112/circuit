import Adafruit_DHT as adht
import time

sensor = adht.DHT11

for i in range(1):
    h, t = adht.read_retry(sensor, 17)
    if h and t:
        # with open('./th.txt', 'a+', encoding='utf-8') as f:
        #     f.write(str(t) + ', ' + str(h) + '\n')
        print(t, h)
    else:
        # pass
        print('error')
    # time.sleep(60)
