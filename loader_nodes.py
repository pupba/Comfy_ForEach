from PIL import Image, ImageOps
import os
import numpy as np
import torch

class FolderImageLoaderNode:
    """
    Loads all .png images from a folder and returns a list of images and their filenames.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "root_path":("STRING",{"default":""}),
                "task_id": ("STRING", {"default": "abc123"}),
                "suffix_path":("STRING",{"default":""})
            }
        }
    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("image_list", "image_name_list")
    FUNCTION = "execute"
    CATEGORY = "ComfyForEach/Load"
    
    def execute(self, root_path,task_id,suffix_path):
        # Get TaskID 노드를 가장 먼저 실행하기 위함 Dummy 호출
        # Get list of .png files in the folder
        folder_path = os.path.join(root_path,task_id,suffix_path)
        if not os.path.isdir(folder_path):
            raise ValueError(f"Folder not found: {folder_path}")
        files = sorted(f for f in os.listdir(folder_path) if f.lower().endswith(".png"))
        image_list = []
        name_list = []
        for fname in files:
            file_path = os.path.join(folder_path, fname)
            # Load image using PIL
            img = Image.open(file_path)
            img = ImageOps.exif_transpose(img)  # handle orientation via EXIF&#8203;:contentReference[oaicite:4]{index=4}
            # If image is 16-bit or has mode 'I', convert to 8-bit range
            if img.mode == 'I':
                img = img.point(lambda i: i * (1/255))
            img = img.convert("RGB")
            # Convert to numpy array (H, W, C) and normalize to [0,1]
            np_img = np.array(img).astype(np.float32) / 255.0
            # Convert to torch tensor and add batch dimension
            tensor_img = torch.from_numpy(np_img)  # shape (H, W, 3)
            tensor_img = tensor_img.unsqueeze(0)    # shape (1, H, W, 3)
            image_list.append(tensor_img)
            name_list.append(fname)
        return (image_list, name_list)