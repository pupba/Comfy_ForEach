import os
import json
from PIL import Image, ImageOps
import numpy as np
import torch
import logging

class EventBridgeTriggerNode:
    """
    Triggers an EventBridge event when 'is_last' is True.
    Writes event JSON to a file instead of sending via boto3.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "is_last": ("BOOLEAN",),
                "task_id": ("STRING", {"default": "unknown-task"}),
                "log_folder": ("STRING", {"default": "./event_logs"})
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "trigger"
    OUTPUT_NODE = True
    CATEGORY = "ComfyForEach/AWS"

    def trigger(self, is_last, task_id, log_folder):
        # ignore if not last
        if not is_last:
            print("[EventBridgeTriggerNode] Not the last index, skipping.")
            return {}

        # ensure log folder exists
        os.makedirs(log_folder, exist_ok=True)
        is_error = False
        # create event payload
        if is_error:
            event = {
                "task_id": task_id,
                "status": "FAILED",
                "reason": "Workflow execution error"
            }
            filename = f"{task_id}_failed.json"
        else:
            event = {
                "task_id": task_id,
                "status": "SUCCESS"
            }
            filename = f"{task_id}_success.json"

        # Save to file
        print(os.getcwd())
        save_path = os.path.join(log_folder, filename)
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(event, f, indent=2)

        print(f"[EventBridgeTriggerNode] Logged event: {save_path}")

        # If using boto3:
        # import boto3
        # client = boto3.client("events")
        # client.put_events(...)

        return {}