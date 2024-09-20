from fastapi import APIRouter
import base64
from io import BytesIO #Used to handle binary data streams.
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter() #Creates an instance of a router, which allows defining routes separately from the main app for better modularity.
#Defines a POST endpoint. 
# The route is empty (''), meaning it will depend on where this router is included within the main application.
@router.post('')
async def run(data: ImageData):
    #with a JSON object that should match the ImageData schema.
    #(because the base64 image string typically includes metadata like data:image/png;base64,).
    image_data = base64.b64decode(data.image.split(',')[1]) # the image was encoded in base64 by the canvas when capturing
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes) #Opens the image using Pillow for further processing.
    responses = analyze_image(image,dict_of_vars=data.dict_of_vars)
    #data = []: Initializes an empty list to store the responses.
    # for response in responses: data.append(response): Iterates over the list of responses and appends each to the data list.
    data = []
    for response in responses:
        data.append(response)
    print('response in route:' ,response) # to test if response is coming
    return {
        "message": "Image Processed",
        "type": "success",
        "data": data,
    }