from flask import Flask, Response, request
from flask_cors import CORS
import time
import base64


app = Flask(__name__)
CORS(app)

def event_stream(params):
    print("on event_stream")
    print(params)

    npm = params.get('npm')
    # npm = "guhkun"
    print(npm)
    # print(npm)
    # card_uuid = params.get('cardUUID')    
    # print(npm_param)
    # print(card_uuid)
    
    # yield "data: test \n\n"
    
    # yield f"data: npm\n\n"
    if npm:
        print(npm)
        yield f"data: Message {npm}\n\n"
    # count = 13
    # while True:
    #     if npmEnc:
    #         yield f"data: Message {npmEnc}\n\n"
    #     else:
    #         yield f"data: Message {count}\n\n"
    #         count += 1

@app.route('/sse')
def sse():
    return Response(event_stream(request.args), content_type='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=8082)
