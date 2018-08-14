import time
from datetime import datetime as dt

temp_hosts='hosts'
host_path= r'C:\Windows\System32\drivers\etc\hosts'
redirect='127.0.0.1'

sites_to_be_redirected=['www.facebook.com', 'www.twitter.com','www.instagram.com']
print(dt.now())

while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,19) < dt.now()< dt(dt.now().year,dt.now().month,dt.now().day,20)):
        print ('Working hours')

        with open (host_path,'r+') as file:
            content=file.read()
            for site in sites_to_be_redirected:
                if site in content:
                    pass
                else:
                    file.write(redirect + ' ' + site +'\n')
    else:
        with open (host_path, 'r+')as file:
            content =file.readLines()
            file.seek(0)
            for line in content:
                if not any (site in line for site in sites_to_be_redirected):
                    file.write(line)
            file.truncate()
        print ("Let's start the fun")
    time.sleep(1000)
