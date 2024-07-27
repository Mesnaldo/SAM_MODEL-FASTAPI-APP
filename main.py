from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np
# To Learn
import base64
from fastapi.responses import JSONResponse, HTMLResponse # To Learn
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator
import supervision as sv # To Learn
import os

app = FastAPI()

# Define constants
model_type = 'vit_h'
# - > To run on Local ->  
checkpoint = '/Users/oumsai/Desktop/sam_/sam_vit_h_4b8939.pth'
# Below is for the docker file to recognize 
#checkpoint = '/code/sam_vit_h_4b8939.pth'

#Loading the Model
sam = sam_model_registry[model_type](checkpoint=checkpoint)
mask_generator = SamAutomaticMaskGenerator(sam)

#Getting Path
current_dir = os.path.dirname(os.path.abspath(__file__))
index_path = os.path.join(current_dir, "index.html")

# Backend Work
@app.post("/segment")
async def segment_image(file: UploadFile = File(...)):
    # Read the uploaded image file
    image_data = await file.read()
    #Convert to numpy array to make it accessible for OpenCV
    image_np = np.frombuffer(image_data, np.uint8) 
    image_bgr = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    # Generate masks using SAM
    sam_result = mask_generator.generate(image_rgb)
    mask_annotator = sv.MaskAnnotator(color_lookup=sv.ColorLookup.INDEX)
    detections = sv.Detections.from_sam(sam_result=sam_result)
    annotated_image = mask_annotator.annotate(scene=image_bgr.copy(), detections=detections)

    # Encode the result as a base64 string
    _, buffer = cv2.imencode('.png', annotated_image)
    encoded_image = base64.b64encode(buffer).decode('utf-8')

    return JSONResponse(content={"image": encoded_image})

#Debug statements for docker
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())
      
# Home Page that reads the HTML file 
@app.get("/")
async def read_root():
    with open(index_path, "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
