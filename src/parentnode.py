from typing import Optional
from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: Optional[dict] = None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Parent node missing tag")

        if not self.children:
            raise ValueError("Missing children Nodes")
        
        children_html = [child.to_html() for child in self.children]
        return f'<{self.tag}{self.props_to_html()}>{"".join(children_html)}</{self.tag}>'
