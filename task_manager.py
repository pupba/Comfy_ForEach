import custom_nodes.Comfy_ForEach.context as context

class TaskIDStorageNode:
    """
    Stores and outputs a task_id string, to be used throughout the workflow.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "task_id": ("STRING", {"default": "task-1234"})
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("task_id",)
    FUNCTION = "output"
    CATEGORY = "ComfyForEach/TaskID"

    def output(self, task_id):
        context.set_task_id(task_id)
        return (task_id,)