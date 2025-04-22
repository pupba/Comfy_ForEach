# comfy_foreach/context.py

CURRENT_TASK_ID = "unknown"

def set_task_id(tid: str):
    global CURRENT_TASK_ID
    CURRENT_TASK_ID = tid

def get_task_id() -> str:
    return CURRENT_TASK_ID
