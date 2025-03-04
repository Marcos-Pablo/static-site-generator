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
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

