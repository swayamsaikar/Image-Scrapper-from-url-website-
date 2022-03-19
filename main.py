# this api helps us by scrapping the image urls from any website and providing it
# it will be used in my c144 project
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route("/data")
def getUrl():
    url = request.args.get("url")
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')

    urls = []
    for link in soup.find_all('img'):
        l = link.get('src').split(".")[-1]
        if (l == "jpeg" or l == "png" or l == "jpg"):
            urls.append(link.get("src"))

    if (len(urls) == 0):
        return jsonify({"img_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCH98UjtaDkWo66HbeBYaOidHMT6PSlmaZTTV6FGvm5YX9Nh0erA0tgTti9yMItdN_yvw&usqp=CAU", "status": "none_image_found"})
    else:
        return jsonify({"img_url": urls[0], "status": "success"})


if __name__ == '__main__':
    app.run(debug=True, port=7005)
