from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional
from pprint import pprint

class TreeNode(BaseModel):
    value : int
    children : Optional[List[TreeNode]] = []

    def add_child(self, child : TreeNode) -> None:
        self.children.append(child)

root = TreeNode(value=5)
first_child = TreeNode(value=12)
second_child = TreeNode(value=7)

root.add_child(first_child)
root.add_child(second_child)
pprint(root)
pprint(first_child)