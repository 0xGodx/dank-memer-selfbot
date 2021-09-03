import random, requests, time

class dank():
    while True:
            randomlist = []
            for i in range(0,5):
                
                # Random sleep time 

                n = random.randint(40,60)
                randomlist.append(n)
                print(f"Delay is on {n}")

                # Discord stuff (Remember to set information)

                url = 'https://discord.com/api/v9/channels/<SET YOUR DISCORD CHANNEL ID HERE>/messages'
                headers = {'Authorization' : 'REPLACE WITH YOUR DISCORD TOKEN'}

                # Request stuff 

                requests.post(url, headers=headers, data={'content' : "pls hunt"}), time.sleep(5)
                requests.post(url, headers=headers, data={'content' : "pls fish"}), time.sleep(5)
                requests.post(url, headers=headers, data={'content' : "pls dig"})

                time.sleep(n)
