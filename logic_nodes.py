class IsLastIndexNode:
    """
    Returns True if current index is the last index in total.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "index": ("INT", {"default": 0, "min": 0}),
                "total": ("INT", {"default": 1, "min": 1})
            }
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("is_last",)
    FUNCTION = "check"
    CATEGORY = "ComfyForEach/Logic"

    def check(self, index, total):
        return (index == (total - 1),)
