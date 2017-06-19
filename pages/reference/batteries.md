Mindbender hosts a series of [graphical user interfaces](#batteries) that aid the user in conforming to the specified [contracts](#contract).

| Name              | Purpose                          | Description
|:------------------|:---------------------------------|:--------------
| **creator**            | control what goes out           | Manage how data is outputted from an application.
| **loader**            | control what goes in             | Keep tabs on where data comes from so as to enable tracking and builds.
| **manager**           | stay up to date                  | Notification and visualisation of loaded data.

<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314626/a8a3b72e-283f-11e7-90fd-3fa76e75276e.png">

## Creator

Associate content with a family.

The family is what determins how the content is handled throughout your pipeline and tells Pyblish what it should look like when valid.

### API

The creator respects families registered with Mindbender.

```python
from mindbender import api

api.register_family(
    name="my.family",
    help="My custom family",
)
```

For each family, a **common set of data** is automatically associated with the resulting instance.

```python
{
    "id": "pyblish.mindbender.instance",
    "family": {chosen family}
    "name": {chosen name}
}
```

**Additional common** data can be added.

```python
from mindbender import api

api.register_data(
    key="myKey",
    value="My value",
    help="A special key"
)
```

Data may be **associated** with a family.

```python
from mindbender import api

api.register_family(
    name="my.family",
    data=[
        {"key": "name", "value": "marcus", "help": "Your name"},
        {"key": "age", "value": 30, "help": "Your age"},
])
```

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314676/6405898e-2840-11e7-9a09-3a193d6eaf1f.png">

## Loader

Visualise results from `api.ls()`.

```python
from mindbender import api

for asset in api.ls():
    print(asset["name"])
```

### API

The results from `api.ls()` depends on the currently **registered root**.

```python
from mindbender import api
api.register_root("/projects/gravity")
```

The chosen `ASSET` is passed to the `load()` function of the currently registered host.

```python
from mindbender import api, maya
api.register_host(maya)
```

A host is automatically registered on `api.install()`.

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314689/8b80cc58-2840-11e7-9bee-a97a40fa830d.png">

## Manager

Visualise loaded assets.

```python
from mindbender import maya

for container in maya.ls():
    print(container["name"])

# The same is true for any host; houdini, nuke etc.
```

### API

The results from `ls()` depends on the currently registered host, such as Maya.

```python
from mindbender import nuke
api.register_host(nuke)
```
