"""Generate markdown from template.

This module converts bespoke markdown into markdown compatible with
the bespoke mkdocs theme developed for Avalon.

"""

import sys
import json
import time
import shutil
import contextlib
import subprocess
from tempfile import mkdtemp


@contextlib.contextmanager
def tempfile(name):
    try:
        tempdir = mkdtemp()
        fname = os.path.join(tempdir, name)
        yield fname
    finally:
        shutil.rmtree(tempdir)


def on_template(template):
    definition = template[2:-3]
    key, value = definition.split(":")
    if key == "schema":
        return on_schema(value)
    if key == "api" and value == "members":
        return on_api_members()
    return template


def on_block(language, block):
    if language == "python":
        return on_python(block)
    return ""


def on_page(page):
    formatted_time = time.strftime("%b %d %Y %H:%M:%S GMT+0", time.gmtime())

    return """\
<p>{time}</p>
<br>
{content}\
""".format(time=formatted_time)


def on_api_members():
    from avalon import api

    table = """\
| Member | Description
|:-------|:--------
"""

    row = "| `{name}` | {description}\n"

    for name in api.__all__:
        member = getattr(api, name)
        doc = member.__doc__

        if doc is None:
            raise SyntaxError("'%s' is missing a docstring." % name)

        table += row.format(
            name=name,
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

        try:
            data["type"] = {
                "string": "str",
                "number": "int",
                "array": "list",
                "object": "dict"
            }[data["type"]]
        except KeyError:
            data["type"] = "any"

        data["required"] = str(key in schema.get("required", {}))
        definition += row.format(**data)

    root = "https://github.com/getavalon/core/tree/master/avalon/schema"
    link = """\
<a href="{root}/{name}" title="{name}" class="md-source-file">
{name}
</a>
""".format(root=root, name=name)

    return os.linesep.join([link, example])


def on_python(block):
    with tempfile("block.py") as fname:
        with open(fname, "w") as f:
            f.write(os.linesep.join(block))

        try:
            output = subprocess.check_output(
                [sys.executable, fname],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
        except subprocess.CalledProcessError as e:
            output = e.output

    output = "\n".join(
        "<span class=\"p\">{line}</span>".format(line=line)
        for line in output.splitlines()
    )

    source = """\
```python
{input}
```
""".format(input="".join(block))

    output = """\
<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
{output}\
          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>
""".format(output=output) if output else ""

    return "\n".join([source, output])


def parse(fname):
    parsed = list()
    blocks = list()

    with open(fname) as f:
        in_block = False
        current_block = None
        current_language = None
        line_no = 0
        for line in f:
            line_no += 1

            if line_no == 1 and line.startswith("build: false"):
                print("Skipping '%s'.." % fname)
                parsed = f.read()
                break

            if line.startswith("{{"):
                line = on_template(line)

            if in_block and line.startswith("```"):
                print("Running Python..")
                print("".join("\t%s" % line for line in current_block))
                line = on_block(current_language, current_block)
                in_block = False
                current_language = None
                parsed.append(line)

            elif in_block:
                current_block.append(line)

            elif line.startswith("```python"):
                in_block = True
                current_language = "python"
                current_block = list()
                blocks.append(current_block)

            else:
                parsed.append(line)

    return "".join(parsed)


if __name__ == '__main__':
    import os
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs='?')

    args = parser.parse_args()

    cd = os.path.abspath(os.path.dirname(__file__))
    os.chdir(cd)

    if args.path and os.path.isfile(args.path):
        files = [args.path]
    else:
        files = list()
        path = args.path

        for base, dirs, fnames in os.walk("pages"):
            for fname in fnames:
                name, ext = os.path.splitext(fname)
                if ext != ".md":
                    continue

                src = os.path.join(base, fname)

                files.append(src)

    results = list()
    for src in files:
        print("Building '%s'.." % src)
        dst = src.replace("pages", "build")
        parsed = parse(src)
        results.append((dst, parsed))

    # Parsing can take some time, so write
    # files all in one batch when done

    for dst, parsed in results:

        try:
            os.makedirs(os.path.dirname(dst))
        except OSError:
            pass

        with open(dst, "w") as f:
            f.write(parsed)
