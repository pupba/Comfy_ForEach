from comfy.comfy_types import IO


class StringViewer:
    """
    Simple Viewer Node to Display STRING Input
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"text1": ("STRING", {}), "text2": ("STRING", {})}}

    RETURN_TYPES = ()
    FUNCTION = "display_text"
    CATEGORY = "ComfyForEach/PreLoad"
    OUTPUT_NODE = True

    def display_text(self, text1, text2):
        try:
            # 단순 문자열 출력
            print(f"[VIEW] {text1},{text2}")
            return ()
            # 화면에 표시할 문자열 그대로 반환
        except Exception as e:
            print(f"[ERROR] Failed to display text: {e}")
            return ()


class LoadPreCheckpointModel:
    """
    PreLoad Checkpoint Model
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"MODEL": ("MODEL",), "CLIP": (IO.CLIP,), "VAE": ("VAE",)}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_pre_ck_model"
    CATEGORY = "ComfyForEach/PreLoad"

    def load_pre_ck_model(self, MODEL, CLIP, VAE):
        try:
            if MODEL is None:
                raise ValueError("Received an empty model object.")

            return (f"CheckPoint Model loaded successfully",)
        except Exception as e:
            return (f"[Error] Post process failed: {e}",)


class LoadPreControlNetModel:
    """
    PreLoad ControlNet Model
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"CONTROLNET": ("CONTROL_NET",)}}

    RETURN_TYPES = ("STRING",)
    FUNCTION = "load_pre_ct_model"
    CATEGORY = "ComfyForEach/PreLoad"

    def load_pre_ct_model(self, CONTROLNET):
        try:
            if CONTROLNET is None:
                raise ValueError("Received an empty model object.")

            return (f"ControlNet Model loaded successfully",)
        except Exception as e:
            return (f"[Error] Post process failed: {e}",)
