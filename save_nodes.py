import os
from PIL import Image
import numpy as np

class SaveExactNameImageNode:
    """
    Saves image to disk using exact user-provided filename.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "filename": ("STRING", {"default": "output.png"}),
                "folder_path": ("STRING", {"default": "./output"}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "save"
    OUTPUT_NODE = True
    CATEGORY = "ComfyForEach/Save"

    def save(self, image, filename, folder_path):
        # ensure folder exists
        os.makedirs(folder_path, exist_ok=True)

        # get image tensor (B,H,W,C)
        img = image[0].cpu().numpy()  # [H, W, C]
        img = (img * 255).clip(0, 255).astype(np.uint8)
        img = Image.fromarray(img)

        # save
        full_path = os.path.join(folder_path, filename)
        img.save(full_path)
        print(f"[Saved] → {full_path}")
        return {}
    