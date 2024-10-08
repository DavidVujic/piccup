from collections import defaultdict
from functools import reduce
from typing import Any, Mapping, Sequence


def is_attribute(item: Any) -> bool:
    return isinstance(item, dict)


def is_child(item: Any) -> bool:
    return isinstance(item, list | tuple)


def is_content(item: Any) -> bool:
    return not is_attribute(item) and not is_child(item)


def key_for_group(item: Any) -> str:
    if is_attribute(item):
        return "attributes"
    if is_content(item):
        return "content"

    return "children"


def to_groups(acc: dict, item: Any) -> dict:
    key = key_for_group(item)

    flattened = item[0] if is_child(item) and is_child(item[0]) else item
    value = acc[key] + [flattened]

    return acc | {key: value}


def extract_from_tag(tag: str) -> tuple[str, dict]:
    first, *rest = tag.split(".")
    element_name, _id = first.split("#") if "#" in first else (first, "")

    element_id = {"id": _id} if _id else {}
    element_class = {"class": " ".join(rest)} if rest else {}

    return element_name, element_id | element_class


def transform(tags: Sequence) -> dict:
    first, *rest = tags

    element, extracted = extract_from_tag(first)
    extra = [extracted] + rest

    grouped: dict = reduce(to_groups, extra, defaultdict(list))
    key = "children"

    children = grouped[key]

    branch = {element: [transform(r) for r in children]}
    options = {k: v for k, v in grouped.items() if k != key and v}

    return branch | options


def to_element_attributes(acc: str, attributes: Mapping) -> str:
    attrs = [f'{k}="{v}"' for k, v in attributes.items()]
    joined = " ".join([acc] + attrs)

    return joined


def transform_html(tag: Mapping) -> list:
    node = next(iter(tag.keys()))
    child = next(iter(tag.values()))

    attributes = reduce(to_element_attributes, tag.get("attributes", []), "")
    content = tag.get("content", [])

    matrix = [transform_html(c) for c in child]
    flattened = sum(matrix, [])

    begin = f"{node}{attributes}" if attributes else node

    if flattened or content:
        return [f"<{begin}>"] + flattened + content + [f"</{node}>"]

    return [f"<{begin} />"]


def render_html(data: Sequence):
    transformed = transform(data)

    transformed_html = transform_html(transformed)

    return "".join(transformed_html)


def todo_list(data: list[str]) -> list:
    return ["ul", {"class": "one"}, [["li", d] for d in data]]


z = [
    "div#hello.first.second",
    ["span", ["a#hello-world.highlight", {"href": "hello", "target": "_blank"}]],
    ["span", ["span", ["strong", "HELLO"], ["strong", "WORLD"]]],
    [
        "figure",
        ["img", {"src": "picture.png"}],
        ["figcaption", "A description of the picture"],
    ],
    ["br"],
    todo_list(["one", "two", "three"]),
]

y = ("div#hello", ("span", ("a", "hello")))
