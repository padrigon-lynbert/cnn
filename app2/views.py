import torch
from PIL import Image
from torchvision import transforms
from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms import ImageUploadForm
from .models_utils import SimpleCNNForTest

device = "cuda" if torch.cuda.is_available() else "cpu"

# Load model once
model = SimpleCNNForTest(num_classes=3).to(device)
model.load_state_dict(torch.load("ml_models/simplecnn.pth", map_location=device))
model.eval()

idx_to_class = {0: 'burger', 1: 'car', 2: 'hotdog'}

transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

def predict_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(img_tensor)
        pred = torch.argmax(output, dim=1)
    return idx_to_class[pred.item()]

def classify_image(request):
    label = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['image']
            path = default_storage.save('tmp/' + file.name, file)
            label = predict_image(path)
    else:
        form = ImageUploadForm()
    return render(request, 'predict.html', {'form': form, 'label': label})
