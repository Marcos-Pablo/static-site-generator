from typing import Optional

class HTMLNode:
    def __init__(self, tag: Optional[str] = None, 
                value: Optional[str] = None,
                children: Optional[list] = None,
                props: Optional[dict] = None) -> None:

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if not self.props:
            return ""

        html_props = []
        for key, value in self.props.items():
            html_props.append(f' {key}="{value}"')

        return "".join(html_props)

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

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
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: Optional[str], value: str, props: Optional[dict] = None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Leaf node missing value")

        if not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
