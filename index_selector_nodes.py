class IndexedImageSelectorNode:
    """
    Selects one image from image_list using the given index.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_list": ("IMAGE",),
                "index": ("INT", {"default": 0, "min": 0})
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "execute"
    CATEGORY = "ComfyForEach/Select"

    def execute(self, image_list, index):
        if index < 0 or index >= len(image_list):
            raise IndexError(f"Index {index} is out of bounds for image list of size {len(image_list)}")
        return (image_list[index],)


class IndexedNameWithPrefixNode:
    """
    Selects one image name using the index and adds a prefix to create a filename.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_name_list": ("STRING",),
                "index": ("INT", {"default": 0, "min": 0}),
                "prefix": ("STRING", {"default": ""})
            }
        }

    RETURN_TYPES = ("STRING","STRING")
    RETURN_NAMES = ("file_name","folder_path")
    FUNCTION = "execute"
    CATEGORY = "ComfyForEach/Select"

    def execute(self, image_name_list, index, prefix):
        if index < 0 or index >= len(image_name_list):
            raise IndexError(f"Index {index} is out of bounds for name list of size {len(image_name_list)}")
        filename = str(image_name_list[index])
        return (filename,prefix)
