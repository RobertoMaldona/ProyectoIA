import json
from torchvision import models
from flask import Flask

app = Flask(__name__)
model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()
