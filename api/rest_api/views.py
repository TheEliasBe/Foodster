from rest_framework.response import Response
from rest_framework.views import APIView
import json
import meilisearch
from rest_framework.parsers import MultiPartParser
import cv2
import numpy as np
import pytesseract
import pretty_errors
# Create your views here.

class ProductView(APIView):

    def get(self, request):
        return Response("Welcome")

    def post(self, request):
        try:
            j = json.loads(request.body.decode('utf-8'))
            search_query = j["query"]
        except:
            search_query = "milk"
        client = meilisearch.Client("http:/http://20.101.129.13:7700")
        index = client.index("food")



        return Response(index.search(search_query))

class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request):

        # read image file string data
        filestr = request.data['file'].read()
        print(type(filestr))
        # convert string data to numpy array
        npimg = np.fromstring(filestr, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
        # do some pre-processing on the image
        img = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.GaussianBlur(img, (5, 5), 0)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 10)
        img = cv2.bitwise_not(img)


        cv2.imwrite("user_uploaded_file.jpg", img)

        text = pytesseract.image_to_string(img)
        text = text.split("\n")

        client = meilisearch.Client("http://meilisearch:7700")
        index = client.index("food")

        return Response(index.search("milk"), status=204)