![dropbox3](https://user-images.githubusercontent.com/2152766/27328354-cd712dd8-55a9-11e7-89b8-bb8b01b9c66d.png)

<br>
<br>
<br>

# Reference

This section covers high-level aspects of Avalon in an information-oriented fashion.

!!! note "Looking for API reference?"

    See the auto-generated documentation for the [Avalon API](https://getavalon.github.io/core).

<br>
<br>

## Content Life Cycle

Data in Avalon is either persistent or in transit. Persistent data resides in either a file-system or database, whereas data in transit is in one of three states.

![image](https://user-images.githubusercontent.com/2152766/27510446-54a800ea-5908-11e7-971b-7551d4bb60e5.png)

!!! info "Note"
    
    For each state, there is an **API** for developers and at least one **GUI** for users.

<img class="ornament" src="https://user-images.githubusercontent.com/2152766/27510260-c4266d02-5904-11e7-8948-589df51d895a.png">

### 1. Create

Creation is the process of introducing new data into a project and is divided into two parts; asset and subset creation.

**Assets** are abstract representations of the data used throughout a project - such as sequences, shots, characters and props - whereas **Subsets** represents data *per asset* - such as geometry, textures or rigs.

Asset and subset creation is governed by the [Project Inventory API](#project-inventory-api) and [Creator API](#creator-api) respectively via one or more plug-ins associated to named "families" of data, such as `model`, `look` or `render`.

<img height="100px" src="https://user-images.githubusercontent.com/2152766/27510297-7f640ebc-5905-11e7-9c03-2b1083ac632d.png">
<img height="100px" src="https://user-images.githubusercontent.com/2152766/27510351-63a21060-5906-11e7-94d0-067a1cd5cc0f.png">

Assets are created via the [Project Inventory API](#project-inventory-api) and subsets are generally created via the use of a Digital Content Creation package, such as Autodesk Maya or The Foundry Nuke.

**API Example**

```python
from avalon import api

class CreateModel(api.Creator):
    """Polygonal geometry for animation"""

    label = "Create Avalon Model"
    name = "modelDefault"
    family = "avalon.model"

```


**More information**

- [Application Programming Interface]()
- [Graphical User Interface]()

<br>

<img class="ornament" src="https://user-images.githubusercontent.com/2152766/27510285-4c59016c-5905-11e7-8f80-869454d09314.png">

### 2. Import

Import is the process of parsing persistent data from disk and into the memory of a running application.

Due to data being either localised or referenced, import is referred to as **loading**, a process governed by the [Loading API](#loading-api) through one or more plug-ins associated to named families of data.

**API Example**

```python
from avalon import api

class LoadModel(api.Loader):
    """Load data of family avalon.model"""

    label = "Load Avalon Model"
    families = ["avalon.model"]
    representations = ["ma"]

    def process(self, name, namespace, context):
        from maya import cmds
        from avalon import maya

        with maya.maintained_selection():
            nodes = cmds.file(self.fname)

        self[:] = nodes

```


**More information**

- [Application Programming Interface]()
- [Graphical User Interface]()

<br>
<br>

<img class="ornament" src="https://user-images.githubusercontent.com/2152766/27510259-b58cee4c-5904-11e7-9def-43bde11171bc.png">

### 3. Export

Export is the process of transforming in-memory data native to an application into something that can persist on disk. During export, data is funneled through a validation mechanism that check for consistency. Because of this additional mechanism, export is referred to as **publishing**.

The manner in which data is validated and written is governed by a series of plug-ins, orchestrated by the [Publishing API](#publishing-api) and associated to families of data.

**API Example**

```python
from pyblish import api

class ExtractAvalonModel(api.InstancePlugin):
    """Produce a stripped down Maya file from instance"""

    label = "Extract Avalon Model"
    order = api.ExtractorOrder
    hosts = ["maya"]
    families = ["avalon.model"]

    def process(self, instance):
        from maya import cmds
        from avalon import maya

        with maya.maintained_selection(), maya.without_extension():
            cmds.select(instance, noExpand=True)
            cmds.file(path, typ="mayaAscii", exportSelected=True)

```


**More information**

- [Application Programming Interface]()
- [Graphical User Interface]()

<br>

<img class="ornament" src="https://user-images.githubusercontent.com/2152766/27510275-2f928544-5905-11e7-8059-90c4a1829ae4.png">

### 4. Persist

Once exported, data resides in one or two locations - as files in a file-system, or as documents in a database. The exact location within the file-system is governed by the [Project Configuration API](#project-configuration-api) via path "templates" - a string encoded with placeholder variables associated to the various objects in the [object model](#object-model), customisable per-project.

<br>

**Example**

```json
{
    "work": "{root}/{project}/{asset}/work/{task}/{user}/{app}",
    "publish": "{root}/{project}/{asset}/publish/{subset}/v{version:0>3}/{subset}.{representation}"
}
```

<br>
<br>

## Object Model

Wherever data is stored, it is stored as a hierarchy of increasingly granular objects, representative of the division of labour in each project created through Avalon.

<br>

![image](https://cloud.githubusercontent.com/assets/2152766/22086121/8c037080-ddd7-11e6-9149-439203c32c6b.png)

<br>

**Assets** represents the most course grained division of labour and is typically used for shots and builds, e.g. the 6th shot and the hero character.

Each asset contain one or more **Subsets** which are typically used for individual models and animation caches for a build or shot.

Each subset contain one or more **Versions** which are immutable sources of data containing the final element of the object model; the **Representation**.

Representations are the storage method of a version, such as a .png thumbnail, an .obj geometry file or .mp4 turntable of a hero model. Both of which represents the same set of data in three different ways.

Each object containing a series of members defined by an explicit schema, enforced via [jsonschema](http://json-schema.org/) and organised hierarchically with the former containing the latter.

**Read more**

- Read about schemas in the [Database section](#database) below.

<br>

## Software

Avalon assumes content is created within an application of some kind and manages the execution of each application via [Launcher](reference/#launcher).

### Apps

[Launcher](reference/#launcher) is responsible for launching "apps", such as Maya. "App" is the term used for a pre-configured application in Avalon.

**Problem**

It could call on `c:\Program Files\Autodesk\Maya2017\bin\maya.exe` directly, but doing so is problematic because..

1. It assumes a particular operating system
1. It assumes a particular installation directory
1. It assumes a particular app is what you want for your project(s)
1. It assumes no customisation of environment prior to launch

**Solution**

The [Project Executable API](reference/#project-executable-api) addresses this by splitting the problem it into three independently configurable parts.

1. Apps are assumed to be available on your `PATH`, e.g. `maya.sh` or `maya.bat`
2. Configuration is performed per application in an individual configuration file, e.g. `maya.toml`
3. Apps are associated per project, e.g. Hulk uses Maya and Nuke.

<br>
<br>
<br>

## Database

Avalon stores data in two separate locations, on disk and in a database. The separation is made due to performance and search capabilities offered by databases.

MongoDB was chosen due to the inherent simplicity and similarity to Python's built-in dictionary type, and performance great enough to enable graphical user interfaces to be built without asynchronousity in mind.

Inside of MongoDB, data is stored as Collections containing many Documents. In Avalon, each Collection represents a project and documents make up the [Object Model](reference/#object-model). 

- Asset
- Subset
- Version
- Representation

These form a hierarchy, where each contain the latter. Assets make up the top-level object within a project, and can represent anything from characters, shots to levels and more. They are an abstract repsentation of you typically refer to when working.

| Asset       | Description
|:------------|:--------------
| Hulk        | A bulky fellow
| Bruce       | The hero of the film
| 1000        | First shot
| 1200        | Second shot

Subsets is the asset broken down into smaller sets of information, such as a rig or a model. What makes subsets different from the rest is that these are independently versioned.

| Subset      | Description
|:------------|:-----------
| model       | Hulk's model
| rig         | Hulk's rig
| lookdev     | Hulk's look
| animation   | Hulk's point cached geometry

Each subset VERSION

<br>

### Schemas

All data within the database and on disk follow a strict layout, known as a "schema".

#### Project

A project is a top-level object that cannot be contained elsewhere, but contains everything else.

<a href="https://github.com/getavalon/core/tree/master/avalon/schema/project-2.0.json" title="project-2.0.json" class="md-source-file">
project-2.0.json
</a>

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
    "parent": "592c33475f8c1b064c4d1696",
    "schema": "avalon-core:project-2.0",
    "type": "project"
}
```

<br>

#### Asset

A part of a project, such as a Character or Shot.

<a href="https://github.com/getavalon/core/tree/master/avalon/schema/asset-2.0.json" title="asset-2.0.json" class="md-source-file">
asset-2.0.json
</a>

**Example**

```json
{
    "data": {
        "key": "value"
    },
    "name": "Bruce",
    "parent": "592c33475f8c1b064c4d1696",
    "schema": "avalon-core:asset-2.0",
    "silo": "assets",
    "type": "asset"
}
```

<br>

#### Subset

A part of an [Asset](#asset), such as a model or a rig.

<a href="https://github.com/getavalon/core/tree/master/avalon/schema/subset-2.0.json" title="subset-2.0.json" class="md-source-file">
subset-2.0.json
</a>

**Example**

```json
{
    "data": {
        "endFrame": 1201,
        "startFrame": 1000
    },
    "name": "shot01",
    "parent": "592c33475f8c1b064c4d1696",
    "schema": "avalon-core:subset-2.0",
    "type": "subset"
}
```

<br>

#### Version

An immutable iteration of a [Subset](#subset).

Versions are immutable, in that they never change once made. This is in stark contrast to mutable versions which is when one version may be "updated" such that the same file now contains new information.

<a href="https://github.com/getavalon/core/tree/master/avalon/schema/version-2.0.json" title="version-2.0.json" class="md-source-file">
version-2.0.json
</a>

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
    "parent": "592c33475f8c1b064c4d1696",
    "schema": "avalon-core:version-2.0",
    "type": "version"
}
```

<br>

#### Representation

One of many representations of a [Version](#version).

Think of a representation as one way of storing the same set of data on disk. For example, an image may be stored as both PNG and JPEG. Different files, same data. It could also be stored as a description. *"A picture of my computer."* Much less information is ultimately stored, but it is nonetheless the exact same original data in a different (albeit lossy) representation. The image could also be represented by a feeling (warm, mystical) or a spoken word (muah!).

Representation are very powerful and lie at the heart of assets that are more than just a single file.

As a practical example, a Look is stored as both an MA scene file and a JSON. The JSON stores the shader relationships, whereas the MA file stores the actual shaers. Same data, different representations.

<a href="https://github.com/getavalon/core/tree/master/avalon/schema/representation-2.0.json" title="representation-2.0.json" class="md-source-file">
representation-2.0.json
</a>

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
    "parent": "592c33475f8c1b064c4d1696",
    "schema": "avalon-core:representation-2.0",
    "type": "representation"
}
```

<br>

#### Container

An imported [Version](#version), as yielded from `api.registered_host().ls()`.

<a href="https://github.com/getavalon/core/tree/master/avalon/schema/container-1.0.json" title="container-1.0.json" class="md-source-file">
container-1.0.json
</a>

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

<br>
<br>

## Library API

Public members of `avalon.api`

| Member | Description
|:-------|:--------
| `install` | Install `host` into the running Python session.
| `uninstall` | Undo all of what `install()` did
| `schema` | JSON Schema utilities
| `Loader` | Load representation into host application
| `Creator` | Determine how assets are created
| `discover` | Find and return subclasses of `superclass`
| `loaders_by_representation` | Return `Loaders` compatible with the `representation`
| `register_host` | Register a new host for the current process
| `register_format` | Register a supported format
| `register_plugin_path` | Register a directory of one or more plug-ins
| `register_plugin` | Register an individual `obj` of type `superclass`
| `register_root` | Register currently active root
| `registered_root` | Return currently registered root
| `registered_plugin_paths` | Return all currently registered plug-in paths
| `registered_host` | Return currently registered host
| `deregister_plugin` | Oppsite of `register_plugin()`
| `deregister_plugin_path` | Oppsite of `register_plugin_path()`
| `deregister_format` | Deregister a supported format
| `format_staging_dir` | Return directory used for staging of published assets
| `format_version` | Produce filesystem-friendly string from integer version
| `find_latest_version` | Return latest version from list of versions
| `parse_version` | Return integer version from formatted string
| `logger` | 
| `time` | Return file-system safe string of current date and time

<br>
<br>

## Host API

A host must implement the following members.

| Member                                 | Returns    | Description
|:---------------------------------------|:-----------|:--------
| `ls`                                 | `generator`| List loaded assets
| `create`   | `str`      | Build fixture for outgoing data (see [instance]()), returns instance.
| `load` | `None`      | Import external data into [container]()
| `update`        | `None`     | Update an existing container
| `remove`                 | `None`     | Remove an existing container

<br>

#### Information hierarchy

Imported data is stored in a `container`. A container hosts a loaded asset along with metadata used to associate assets that use other assets, such as a Wheel asset used in a Car asset.

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

<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
<span class="p">Traceback (most recent call last):</span>
<span class="p">  File "C:\Users\marcus\AppData\Local\Temp\tmpt06aghkk\block.py", line 5, in <module></span>
<span class="p">    </span>
<span class="p">AttributeError: module 'avalon.api' has no attribute 'register_family'</span>          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>

For each family, a **common set of data** is automatically associated with the resulting instance.

```json
{
    "id": "pyblish.avalon.instance",
    "family": "{chosen family}",
    "name": "{chosen name}"
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

<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
<span class="p">Traceback (most recent call last):</span>
<span class="p">  File "C:\Users\marcus\AppData\Local\Temp\tmpkbquo1yc\block.py", line 5, in <module></span>
<span class="p">    </span>
<span class="p">AttributeError: module 'avalon.api' has no attribute 'register_data'</span>          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>

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

<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
<span class="p">Traceback (most recent call last):</span>
<span class="p">  File "C:\Users\marcus\AppData\Local\Temp\tmpttp1wei6\block.py", line 5, in <module></span>
<span class="p">    </span>
<span class="p">AttributeError: module 'avalon.api' has no attribute 'register_family'</span>          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>

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

<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
<span class="p">Traceback (most recent call last):</span>
<span class="p">  File "C:\Users\marcus\AppData\Local\Temp\tmp07mzo7oq\block.py", line 5, in <module></span>
<span class="p">    </span>
<span class="p">AttributeError: module 'avalon.api' has no attribute 'ls'</span>          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>

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

<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
<span class="p">Traceback (most recent call last):</span>
<span class="p">  File "C:\Users\marcus\AppData\Local\Temp\tmpz77ju9og\block.py", line 1, in <module></span>
<span class="p">    from avalon import api, maya</span>
<span class="p">  File "C:\modules\python-avalon\avalon\maya\__init__.py", line 7, in <module></span>
<span class="p">    from .pipeline import (</span>
<span class="p">  File "C:\modules\python-avalon\avalon\maya\pipeline.py", line 6, in <module></span>
<span class="p">    from maya import cmds, OpenMaya</span>
<span class="p">ModuleNotFoundError: No module named 'maya'</span>          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>

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

<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
<span class="p">Traceback (most recent call last):</span>
<span class="p">  File "C:\Users\marcus\AppData\Local\Temp\tmpjwv52_5c\block.py", line 1, in <module></span>
<span class="p">    from avalon import maya</span>
<span class="p">  File "C:\modules\python-avalon\avalon\maya\__init__.py", line 7, in <module></span>
<span class="p">    from .pipeline import (</span>
<span class="p">  File "C:\modules\python-avalon\avalon\maya\pipeline.py", line 6, in <module></span>
<span class="p">    from maya import cmds, OpenMaya</span>
<span class="p">ModuleNotFoundError: No module named 'maya'</span>          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>

#### API

The results from `ls()` depends on the currently registered host, such as Maya.

```python
from avalon import nuke
api.register_host(nuke)

```

<table class="codehilitetable output">
  <tbody>
    <tr>
      <td class="code">
        <div class="codehilite" id="__code_1">
          <pre>
<span class="p">Traceback (most recent call last):</span>
<span class="p">  File "C:\Users\marcus\AppData\Local\Temp\tmp9_xk_gz_\block.py", line 3, in <module></span>
<span class="p">    </span>
<span class="p">NameError: name 'api' is not defined</span>          </pre>
        </div>
      </td>
    </tr>
  </tbody>
</table>
