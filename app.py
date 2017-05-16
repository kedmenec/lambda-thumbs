from chalice import Chalice
from PIL import Image
import requests

app = Chalice(app_name='thumbsup')
app.debug = True


@app.route('/', methods=['POST'])
def create_user():
    # This is the JSON body the user sent in their POST request.
    data = app.current_request.json_body

    url = data['url']
    headers = {
        'User-Agent': 'Mozilla/5.0',
    }

    response = requests.get(url, allow_redirects=True, headers=headers)

    try:
        img = Image.open(BytesIO(response.content))
    except:
        # print(response.content)
        print(response.status_code)
        if response.status_code != 200:
            return "not 200"

    return 'OK'
    # return img

    # return {'url': data['url']}
