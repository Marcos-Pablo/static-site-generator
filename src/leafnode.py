from typing import Optional
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str], value: str, props: Optional[dict] = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError()

        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
