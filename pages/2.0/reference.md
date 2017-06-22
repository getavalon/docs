![dropbox3](https://user-images.githubusercontent.com/2152766/27328354-cd712dd8-55a9-11e7-89b8-bb8b01b9c66d.png)

<br>
<br>
<br>

# Reference

This section covers high-level aspects of Avalon in an information-oriented fashion. For library reference, see the [Library Reference]() link below.

- [Library Reference](https://getavalon.github.io/core)

<br>
<br>

## Schema

![image](https://cloud.githubusercontent.com/assets/2152766/22086121/8c037080-ddd7-11e6-9149-439203c32c6b.png)

Available schemas are organised hierarchically, with the former containing the latter.

- [`asset.json`](#assetjson)
    - [`subset.json`](#subsetjson)
        - [`version.json`](#versionjson)
            - [`representation.json`](#representationjson)

<br>

### Project

A project is a top-level object that cannot be contained elsewhere, but contains everything relevant to a given project.

**Example**

```json
{
    "config": {
        "apps": [
            {
                "label": "Autodesk Maya 2016", 
                "name": "maya2016"
            }, 
            {
                "label": "The Foundry Nuke 10.0", 
                "name": "nuke10"
            }
        ], 
        "schema": "avalon-core:config-1.0", 
        "tasks": [
            {
                "name": "model"
            }, 
            {
                "name": "render"
            }, 
            {
                "name": "animate"
            }, 
            {
                "name": "rig"
            }, 
            {
                "name": "lookdev"
            }, 
            {
                "name": "layout"
            }
        ], 
        "template": {
            "publish": "{root}/{project}/{silo}/{asset}/publish/{subset}/v{version:0>3}/{subset}.{representation}", 
            "work": "{root}/{project}/{silo}/{asset}/work/{task}/{app}"
        }
    }, 
    "data": {
        "fps": 24, 
        "height": 1080, 
        "width": 1920
    }, 
    "name": "hulk", 
    "schema": "avalon-core:project-2.0", 
    "type": "project"
}
```

**Source**

- [project-2.0.json](https://github.com/getavalon/core/blob/master/avalon/schema/project-2.0.json)

<br>

### Asset

A part of a project, such as a Character or Shot.

**Example**

```json
{
    "data": {
        "key": "value"
    }, 
    "name": "Bruce", 
    "schema": "avalon-core:asset-2.0", 
    "silo": "assets", 
    "type": "asset"
}
```

**Source**

- [asset-2.0.json](https://github.com/getavalon/core/blob/master/avalon/schema/asset-2.0.json)

<br>

### Subset

A part of an [Asset](#asset), such as a model or a rig.

**Example**

```json
{
    "data": {
        "endFrame": 1201, 
        "startFrame": 1000
    }, 
    "name": "shot01", 
    "schema": "avalon-core:subset-2.0", 
    "type": "subset"
}
```

**Source**

- [subset-2.0.json](https://github.com/getavalon/core/blob/master/avalon/schema/subset-2.0.json)

<br>

### Version

An immutable iteration of a [Subset](#subset).

Versions are immutable, in that they never change once made. This is in stark contrast to mutable versions which is when one version may be "updated" such that the same file now contains new information.

**Example**

```json
{
    "data": {
        "author": "marcus", 
        "families": [
            "avalon.model"
        ], 
        "source": "{root}/f02_prod/assets/BubbleWitch/work/modeling/marcus/maya/scenes/model_v001.ma", 
        "time": "20170510T090203Z"
    }, 
    "locations": [
        "data.avalon.com"
    ], 
    "name": 12, 
    "schema": "avalon-core:version-2.0", 
    "type": "version"
}
```

**Source**

- [version-2.0.json](https://github.com/getavalon/core/blob/master/avalon/schema/version-2.0.json)

<br>

### Representation

One of many representations of a [Version](#version).

Think of a representation as one way of storing the same set of data on disk. For example, an image may be stored as both PNG and JPEG. Different files, same data. It could also be stored as a description. *"A picture of my computer."* Much less information is ultimately stored, but it is nonetheless the exact same original data in a different (albeit lossy) representation. The image could also be represented by a feeling (warm, mystical) or a spoken word (muah!).

Representation are very powerful and lie at the heart of assets that are more than just a single file.

As a practical example, a Look is stored as both an MA scene file and a JSON. The JSON stores the shader relationships, whereas the MA file stores the actual shaers. Same data, different representations.

**Example**

```json
{
    "context": {
        "asset": "Bruce", 
        "project": "hulk", 
        "representation": "ma", 
        "silo": "assets", 
        "subset": "rigDefault", 
        "version": 12
    }, 
    "data": {
        "label": "Alembic"
    }, 
    "dependencies": [
        "592d547a5f8c1b388093c145"
    ], 
    "name": "abc", 
    "schema": "avalon-core:representation-2.0", 
    "type": "representation"
}
```

**Source**

- [representation-2.0.json](https://github.com/getavalon/core/blob/master/avalon/schema/representation-2.0.json)

<br>

### Container

An imported VERSION, as yielded from `api.registered_host().ls()`.

**Example**

```json
{
    "asset": "Bruce", 
    "author": "Marcus Ottosson", 
    "name": "modelDefault", 
    "objectName": "modelDefault_CON", 
    "path": "|someParent|someNamespace_:modelDefault_CON", 
    "schema": "avalon-core:container-2.0", 
    "subset": "modelDefault", 
    "version": 12
}
```

**Source**

- [container-1.0.json](https://github.com/getavalon/core/blob/master/avalon/schema/container-1.0.json)

Avalon hosts a series of [graphical user interfaces](#batteries) that aid the user in conforming to the specified [contracts](#contract).

<br>
<br>

## Library API

Public members of `avalon.api`

| Member | Returns | Description
|:-------|:--------|:--------
| `install` | `null` | Install `host` into the running Python session.
| `uninstall` | `null` | Undo all of what `install()` did
| `schema` | `null` | JSON Schema utilities
| `Loader` | `null` | Load representation into host application
| `Creator` | `null` | Determine how assets are created
| `discover` | `null` | Find and return subclasses of `superclass`
| `register_host` | `null` | Register a new host for the current process
| `register_format` | `null` | Register a supported format
| `register_plugin_path` | `null` | Register a directory of one or more plug-ins
| `register_plugin` | `null` | Register an individual `obj` of type `superclass`
| `register_root` | `null` | Register currently active root
| `registered_root` | `null` | Return currently registered root
| `registered_plugin_paths` | `null` | Return all currently registered plug-in paths
| `registered_host` | `null` | Return currently registered host
| `deregister_plugin` | `null` | Oppsite of `register_plugin()`
| `deregister_plugin_path` | `null` | Oppsite of `register_plugin_path()`
| `deregister_format` | `null` | Deregister a supported format
| `format_staging_dir` | `null` | Return directory used for staging of published assets
| `format_version` | `null` | Produce filesystem-friendly string from integer version
| `find_latest_version` | `null` | Return latest version from list of versions
| `parse_version` | `null` | Return integer version from formatted string
| `logger` | `null` | 
| `time` | `null` | Return file-system safe string of current date and time

<br>
<br>

## Host API

A host must implement the following members.

| Member                                 | Returns    | Description
|:---------------------------------------|:-----------|:--------
| `ls()`                                 | `generator`| List loaded assets
| `create(name, family, options=None)`   | `str`      | Build fixture for outgoing data (see [instance]()), returns instance.
| `load(asset, subset, version=-1, representation=None)` | `None`      | Import external data into [container]()
| `update(container, version=-1)`        | `None`     | Update an existing container
| `remove(container)   `                 | `None`     | Remove an existing container

<br>

#### Information hierarchy

Loaded data is stored in a `container`. A container hosts a loaded asset along with metadata used to associate assets that use other assets, such as a Wheel asset used in a Car asset.

![Host data relationship](https://cloud.githubusercontent.com/assets/2152766/18905784/aa6a3d5c-855c-11e6-9843-b24ebd23c4ac.png)

#### Id

Internally, Pyblish instances and containers are distinguished from native content via an "id". For example, in Maya, the `id` is a user-defined attribute.

| Name                         | Description              | Example
|:-----------------------------|:-------------------------|:----------
| `pyblish.avalon.container`  | Unit of incoming data    | `...:model_GRP`, `...:rig_GRP` 
| `pyblish.avalon.instance`   | Unit of outgoing data    | `Strange_model_default`

<br>
<br>

## Project Inventory API

The inventory contains all ASSETs of a project, including metadata.

- [Icon Database](http://fontawesome.io/icons/)

**.inventory.toml**

```ini
# Mandatory, do not touch
schema = "avalon-core:inventory-1.0"

# Project metadata
label = "The Hulk"
fps = 24
resolution_width = 1920
resolution_height = 1080

# Available assets
[[assets]]
name = "Batman"

[[assets]]
name = "Bruce"
label = "Bruce Wayne"  # (Optional) Nicer name
group = "Character"  # (Optional) Visual grouping
icon = "gear"  # (Optional) Icon from FontAwesome

[[assets]]
name = "Camera"

# Available shots
[[film]]
name = "1000"
edit_in = 1000
edit_out = 1202

[[film]]
name = "1200"
edit_in = 1000  # Optional metadata per shot
edit_out = 1143
```

The above is an example of an "inventory". A complete snapshot of all available assts within a given project, along with optional metadata.

<br>
<br>

## Project Configuration API

The project configuration contains the applications and tasks available within a given project, along with the template used to create directories.

**.config.toml**

```ini
# Mandatory, do not touch
schema = "avalon-core:config-1.0"

# Available tasks to choose from.
[[tasks]]
name = "modeling"
label = "Character Modeling"
icon = "video-camera"

[[tasks]]
name = "animation"

# Available applications to choose from, the name references
# the executable API (see below)
[[apps]]
name = "maya2016"
label = "Autodesk Maya 2016"

[[apps]]
name = "python"
label = "Python 3.6"
args = ["-u", "-c", "print('Something nice')"]

# Directory layouts for this project.
[template]
work = "{root}/{project}/{silo}/{asset}/work/{task}/{user}/{app}"
publish = "{root}/{project}/{silo}/{asset}/publish/{subset}/v{version:0>3}/{subset}.{representation}"
```

The directory layout have the following members available.

| Member             | Type   | Description
|:-------------------|:-------|:-----------
| `{app}`            | `str`  | The current application directory name, defined in Executable API
| `{task}`           | `str`  | Name of the current task
| `{user}`           | `str`  | Currently logged on user (provided by `getpass.getuser()`)
| `{root}`           | `str`  | Absolute path to root directory, e.g. `m:\f01_project`
| `{project}`        | `str`  | Name of current project
| `{silo}`           | `str`  | Name of silo, e.g. `assets`
| `{asset}`          | `str`  | Name of asset, e.g. `Bruce`
| `{subset}`         | `str`  | Name of subset, e.g. `modelDefault`
| `{version}`        | `int`  | Number of version, e.g. `1`
| `{representation}` | `str`  | Name of representation, e.g. `ma`

<br>
<br>

## Project Executable API

Every executable must have an associated Application Definition file which looks like this.

**maya2016.toml**

```ini
# Required header, do not touch.
schema = "avalon-core:application-1.0"

# Name of the created directory, available in the 
# `template` of the Configuration API
application_dir = "maya"

# These directories will be created under the
# given application directory
default_dirs = [
    "scenes",
    "data",
    "renderData/shaders",
    "images"
]

# Name displayed in GUIs
label = "Autodesk Maya 2016x64"

# Arguments passed to the executable on launch
arguments = [ "-proj", "{AVALON_WORKDIR}",]

# Name of the executable on the local computer.
# This name must be available via the users `PATH`.
# That is, the user must be able to type this into
# the terminal to launch said application.
executable = "maya2016"
description = ""

# Files copied into the application directory on launch
[copy]
"{AVALON_CORE}/res/workspace.mel" = "workspace.mel"

# The environment variables overrides any previously set
# variables from the parent process.
[environment]
MAYA_DISABLE_CLIC_IPM = "Yes"  # Disable the AdSSO process
MAYA_DISABLE_CIP = "Yes"  # Shorten time to boot
MAYA_DISABLE_CER = "Yes"
PYTHONPATH = [
    "{PYBLISH_MAYA}/pyblish_maya/pythonpath",
    "{AVALON_CORE}/avalon/maya/pythonpath",
    "{PYTHONPATH}"
]
```

<br>
<br>
<br>

## Tools

| Name              | Purpose                          | Description
|:------------------|:---------------------------------|:--------------
| **creator**            | control what goes out           | Manage how data is outputted from an application.
| **loader**            | control what goes in             | Keep tabs on where data comes from so as to enable tracking and builds.
| **manager**           | stay up to date                  | Notification and visualisation of loaded data.

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314626/a8a3b72e-283f-11e7-90fd-3fa76e75276e.png">

### Creator

Associate content with a family.

The family is what determins how the content is handled throughout your pipeline and tells Pyblish what it should look like when valid.

#### API

The creator respects families registered with Avalon.

```python
from avalon import api

api.register_family(
    name="my.family",
    help="My custom family",
)
```

For each family, a **common set of data** is automatically associated with the resulting instance.

```python
{
    "id": "pyblish.avalon.instance",
    "family": {chosen family}
    "name": {chosen name}
}
```

**Additional common** data can be added.

```python
from avalon import api

api.register_data(
    key="myKey",
    value="My value",
    help="A special key"
)
```

Data may be **associated** with a family.

```python
from avalon import api

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

### Loader

Visualise results from `api.ls()`.

```python
from avalon import api

for asset in api.ls():
    print(asset["name"])
```

#### API

The results from `api.ls()` depends on the currently **registered root**.

```python
from avalon import api
api.register_root("/projects/gravity")
```

The chosen `ASSET` is passed to the `load()` function of the currently registered host.

```python
from avalon import api, maya
api.register_host(maya)
```

A host is automatically registered on `api.install()`.

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314689/8b80cc58-2840-11e7-9bee-a97a40fa830d.png">

### Manager

Visualise loaded assets.

```python
from avalon import maya

for container in maya.ls():
    print(container["name"])

# The same is true for any host; houdini, nuke etc.
```

#### API

The results from `ls()` depends on the currently registered host, such as Maya.

```python
from avalon import nuke
api.register_host(nuke)
```
