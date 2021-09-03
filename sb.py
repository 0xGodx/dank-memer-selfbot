import random, requests, time


class dank():
    while True:
            randomlist = []
            for i in range(0,5):
                    #   Random await speed
                n = random.randint(40,60)
                randomlist.append(n)
                print(f"Delay is on {n}")

                    #   Discord stuff
                url = "https://discord.com/api/v9/channels/<SET YOUR DISCORD CHANNEL ID HERE>/messages"
               
                headers = {"Authorization" : "REPLACE WITH YOUR DISCORD TOKEN"}

                    #   Request stuff

                requests.post(url, headers=headers, data={"content" : "pls hunt"})
                
                time.sleep(5)
                requests.post(url, headers=headers, data={"content" : "pls fish"})
                time.sleep(5)
                requests.post(url, headers=headers, data={"content" : "pls dig"})

                    #   Await 
                time.sleep(n)
