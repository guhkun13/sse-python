import requests, time

def event_listener():    
    # url = 'http://localhost:8082/sse'
    
    x = range(1, 100)
    for i in x:
        print("looping: ", i)
        # url = 'http://localhost:8082/sse?npm=20230101&cardUUID=abc-123-def&loop='+str(i)
        url = 'http://localhost:8082/sse?npm=npm123'
        print(url)
        res = requests.get(url, stream=True)
        print(res)
        time.sleep(5)

    # for line in response.iter_lines():
    #     if line:
    #         print(line.decode('utf-8'))

if __name__ == '__main__':
    event_listener()
