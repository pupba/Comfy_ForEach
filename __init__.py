from .loader_nodes import FolderImageLoaderNode
from .index_selector_nodes import IndexedImageSelectorNode, IndexedNameSelectorNode
from .save_nodes import SaveExactNameImageNode
from .logic_nodes import IsLastIndexNode
from .aws_event_node import EventBridgeTriggerNode
from .task_manager import TaskIDStorageNode

NODE_CLASS_MAPPINGS = {
    "FolderImageLoaderNode": FolderImageLoaderNode,
    "IndexedImageSelectorNode": IndexedImageSelectorNode,
    "IndexedNameSelectorNode": IndexedNameSelectorNode,
    "SaveExactNameImageNode": SaveExactNameImageNode,
    "IsLastIndexNode": IsLastIndexNode,
    "EventBridgeTriggerNode": EventBridgeTriggerNode,
    "TaskIDStorageNode":TaskIDStorageNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FolderImageLoaderNode": "Load Images from Folder",
    "IndexedImageSelectorNode": "Select Image by Index",
    "IndexedNameSelectorNode": "Get Filename by Index",
    "SaveExactNameImageNode": "Save Image with Exact Filename",
    "IsLastIndexNode": "Check If Last Index",
    "EventBridgeTriggerNode": "Trigger EventBridge (Simulated)",
    "TaskIDStorageNode":"Get TaskID"
}
