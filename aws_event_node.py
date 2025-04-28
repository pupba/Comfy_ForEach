import os
import json
from PIL import Image, ImageOps
import numpy as np
import torch
import logging
import json
import boto3
from datetime import datetime

class EventBridgeTriggerNode:
    """
    Triggers an EventBridge event when 'is_last' is True.
    Writes event JSON to a file instead of sending via boto3.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "end_image":("IMAGE",),
                "is_last": ("BOOLEAN",),
                "task_id": ("STRING", {"default": "unknown-task"}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "trigger"
    OUTPUT_NODE = True
    CATEGORY = "ComfyForEach/AWS"

    def trigger(self, is_last, task_id,end_image=None):
        # ignore if not last
        if not is_last and end_image is not None:
            print("[EventBridgeTriggerNode] Not the last index, skipping.")
            return {}
        else:
            # AWS Event Bridge
            # Changed Region
            event = boto3.client("events",region_name="us-east-1")

            # Changed Your Message
            resp = event.put_events(
                Entries=[
                    {
                        "Source":"comfyui.ec2",
                        "DetailType":"ComfyUI Task State",
                        "Detail":json.dumps({
                            "task_id":task_id,
                            "status":"SUCCEEDED",
                            "timestamp":datetime.utcnow().isoformat(),
                            "error_msg":""
                        }),
                        "EventBusName":"default"
                    }
                ]
            )
            if resp.get("FailedEntryCount", 0) > 0:
                raise RuntimeError("❌ EventBridge 전송 실패")
            else:
                print("✅ EventBridge 전송 성공")

            return {}