import os
from django.conf import settings
from django.shortcuts import render

def index(request):
    """
    Renders the main page and dynamically discovers images inside static/images.
    """
    images_dir = settings.BASE_DIR / 'static' / 'images'
    valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg')

    image_files = []
    if os.path.exists(images_dir):
        image_files = [
            f for f in sorted(os.listdir(images_dir))
            if f.lower().endswith(valid_extensions)
        ]

    return render(request, 'index.html', {'image_files': image_files})
