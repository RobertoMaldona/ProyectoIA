# ia/app.py
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image
import os
import random

def contar_personas(image_path):
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    image = Image.open(image_path).convert("RGB")
    input_image = F.to_tensor(image).unsqueeze(0)

    with torch.no_grad():
        predictions = model(input_image)

    confidence_threshold = 0.5
    detections = predictions[0]

    person_count = 0
    for score, label, box in zip(detections["scores"], detections["labels"], detections["boxes"]):
        if score > confidence_threshold and label == 1:
            person_count += 1

    #plt.imshow(image)

    """for score, label, box in zip(detections["scores"], detections["labels"], detections["boxes"]):
        if score > confidence_threshold and label == 1:
            box = [round(i, 2) for i in box.tolist()]
            rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='r', facecolor='none')
            plt.gca().add_patch(rect)
"""
    #plt.title(f'Número de personas: {person_count}')
    #plt.show()

    #print(f"Número total de personas: {person_count}")

    tiempo = person_count*1.25
    return person_count, tiempo



def elegir_archivo_al_azar(ruta_carpeta):
    archivos = os.listdir(ruta_carpeta)
    archivo_elegido = random.choice(archivos)
    ruta_completa = os.path.join(ruta_carpeta, archivo_elegido)
    return ruta_completa
