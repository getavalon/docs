# Generate markdown from markdown template.
# 2.0.template -> 2.0.md

import json


def on_template(template):
    definition = template[2:-3]
    key, value = definition.split(":")
    if key == "schema":
        return on_schema(value)
    if key == "api" and value == "members":
        return on_api_members()
    return template


def on_api_members():
    from avalon import api

    table = """\
| Member | Returns | Description
|:-------|:--------|:--------
"""

    row = "| `{name}` | `{returns}` | {description}\n"

    for name in api.__all__:
        member = getattr(api, name)
        doc = member.__doc__

        if doc is None:
            raise SyntaxError("'%s' is missing a docstring." % name)

        table += row.format(
            name=name,
            returns="null",
            description=doc.splitlines()[0]
        )

    return table


def on_schema(name):
    from avalon import schema
    schema = schema._cache[name]

    example = """\
**Example**

```json
{dump}
```
""".format(dump=json.dumps({
        key: value.get("example", "")
        for key, value in schema["properties"].items()
    }, indent=4, sort_keys=True))

    definition = """\
**Definition**

| Key | Value | Required? | Description
|:----|:------|:----------|:------------
"""
    row = "| `{key}` | `{type}` | `{required}` | {description}\n"

    for key, data in schema["properties"].items():
        if "requires" in schema and key not in schema["requires"]:
            continue

        if "description" not in data:
            raise SyntaxError("'%s' of %s must have a "
                              "description" % (key, name))

        data["key"] = key
        data["type"] = {
            "string": "str",
            "number": "int",
            "array": "list",
            "object": "dict"
        }[data["type"]]

        data["required"] = str(key in schema.get("required", {}))
        definition += row.format(**data)

    return "\n".join([example])


def parse(fname):
    parsed = list()

    with open(fname) as f:
        for line in f:
            if line.startswith("{{"):
                line = on_template(line)

            parsed.append(line)

    return "".join(parsed)


if __name__ == '__main__':
    import os

    for base, dirs, files in os.walk("pages"):
        for fname in files:
            name, ext = os.path.splitext(fname)
            if ext != ".template":
                continue

            print("Building '%s'.." % name)
            parsed = parse(os.path.join(base, fname))

            with open(os.path.join(base, name + ".md"), "w") as f:
                f.write(parsed)
