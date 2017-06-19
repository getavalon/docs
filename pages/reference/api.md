# API

Mindbender provides a *stateful* API.

State is set and modified by calling any of the exposed registration functions, prefixed `register_*`.

<br>

Public members of `mindbender.api`

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

### Host API

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
| `pyblish.mindbender.container`  | Unit of incoming data    | `...:model_GRP`, `...:rig_GRP` 
| `pyblish.mindbender.instance`   | Unit of outgoing data    | `Strange_model_default`

<br>
<br>

### Project Inventory API

The inventory contains all ASSETs of a project, including metadata.

- [Icon Database](http://fontawesome.io/icons/)

**.inventory.toml**

```ini
# Mandatory, do not touch
schema = "mindbender-core:inventory-1.0"

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

### Project Configuration API

The project configuration contains the applications and tasks available within a given project, along with the template used to create directories.

**.config.toml**

```ini
# Mandatory, do not touch
schema = "mindbender-core:config-1.0"

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

### Project Executable API

Every executable must have an associated Application Definition file which looks like this.

**maya2016.toml**

```ini
# Required header, do not touch.
schema = "mindbender-core:application-1.0"

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
arguments = [ "-proj", "{MINDBENDER_WORKDIR}",]

# Name of the executable on the local computer.
# This name must be available via the users `PATH`.
# That is, the user must be able to type this into
# the terminal to launch said application.
executable = "maya2016"
description = ""

# Files copied into the application directory on launch
[copy]
"{MINDBENDER_CORE}/res/workspace.mel" = "workspace.mel"

# The environment variables overrides any previously set
# variables from the parent process.
[environment]
MAYA_DISABLE_CLIC_IPM = "Yes"  # Disable the AdSSO process
MAYA_DISABLE_CIP = "Yes"  # Shorten time to boot
MAYA_DISABLE_CER = "Yes"
PYTHONPATH = [
    "{PYBLISH_MAYA}/pyblish_maya/pythonpath",
    "{MINDBENDER_CORE}/mindbender/maya/pythonpath",
    "{PYTHONPATH}"
]
```

<br>
<br>

### Contract

Mindbender defines these families.

| Family                 | Definition                                      | Link
|:-----------------------|:------------------------------------------------|:------------
| `mindbender.model`     | Geometry with deformable topology               | [Spec](#mindbendermodel)
| `mindbender.rig`       | An articulated `mindbender.model` for animators | [Spec](#mindbenderrig)
| `mindbender.animation` | Pointcached `mindbender.rig` for rendering      | [Spec](#mindbenderanimation)
| `mindbender.lookdev`   | Shaded `mindbender.model` for rendering         | [Spec](#mindbenderlookdev)

<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314853/4c84d5e6-2843-11e7-9b66-4c4506c89320.png"/>

#### `mindbender.model`

A generic representation of geometry.

![aud][] **Workflow**

1. Create a new `Model` INSTANCE.
2. Add the `ROOT` group
3. Publish

![aud][] **Target Audience**

- Texturing
- Rigging
- Final render

![req][] **Requirements**

- All DAG nodes must be parented to a single top-level transform
- Normals must be unlocked

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- `geometry_SEL (geometry)`: Meshes suitable for rigging
- `aux_SEL (any, optional)`: Auxilliary meshes for e.g. fast preview, collision geometry

<br>
<br>
<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314863/87719ab8-2843-11e7-8509-1328f0847437.png"/>

#### `mindbender.rig`

The `mindbender.rig` contains the necessary implementation and interface for animators to animate. 

![aud][] **Workfow**

1. Add the `ROOT` group
1. Add animatable controllers to an `objectSet` called `controls_SET`
1. Add cachable meshes to an `objectSet` called `out_SET`

Publishing.

1. Create a new `Rig` INSTANCE
1. Add `ROOT`
1. Add `controls_SET`
1. Add `out_SET`
1. Publish

![aud][] **Target Audience**

- Animation

![req][] **Requirements**

- All DAG nodes must be parented to a single top-level transform
- Must contain an `objectSet` for controls and cachable geometry

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- `in_SEL (geometry, optional)`: Geometry consumed by this rig
- `out_SEL (geometry)`: Geometry produced by this rig
- `controls_SEL (transforms)`: All animatable controls
- `resources_SEL (any, optional)`: Nodes that reference an external file

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314862/77be3eb4-2843-11e7-9a5f-9a1509751aa6.png"/>

#### `mindbender.animation`

Point positions and normals represented as one Alembic file.

![aud][] **Workflow**

The animator workflow is simplified by the fact that an INSTANCE is automatically created upon loading a rig.

1. Load rig
2. Publish

![aud][] **Target Audience**

- Lighting
- FX
- Cloth
- Hair

![req][] **Requirements**

- None

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- None

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314862/77be3eb4-2843-11e7-9a5f-9a1509751aa6.png"/>

#### `mindbender.lookdev`

![aud][] **Workflow**

Shaders are exported relative the meshes in an INSTANCE.

1. Create a new `Look` INSTANCE
2. Add the `transform` of each shaded mesh
3. Publish

![aud][] **Target Audience**

- Lighting

![req][] **Requirements**

- None

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- None

<br>
<br>
<br>

**Legend**

|          | Title               | Description
|:---------|:--------------------|:-----------
| ![aud][] | **Target Audience** | Who is the end result of this family intended for?
| ![req][] | **Requirements**    | What is expected of this ASSET before it passes the tests?
| ![dat][] | **Data**            | End-user configurable options
| ![set][] | **Sets**            | Collection of specific items for publishing or use further down the pipeline.


[set]: https://cloud.githubusercontent.com/assets/2152766/18576835/f6b80574-7bdc-11e6-8237-1227f779815a.png
[dat]: https://cloud.githubusercontent.com/assets/2152766/18576836/f6ca19e4-7bdc-11e6-9ef8-3614474c58bb.png
[req]: https://cloud.githubusercontent.com/assets/2152766/18576838/f6da783e-7bdc-11e6-9935-78e1a6438e44.png
[aud]: https://cloud.githubusercontent.com/assets/2152766/18576837/f6d9c970-7bdc-11e6-8899-6eb8686b4173.png

<br>
<br>

### Schema

![image](https://cloud.githubusercontent.com/assets/2152766/22086121/8c037080-ddd7-11e6-9149-439203c32c6b.png)

Available schemas are organised hierarchically, with the former containing the latter.

- [`asset.json`](#assetjson)
  - [`subset.json`](#subsetjson)
      - [`version.json`](#versionjson)
        - [`representation.json`](#representationjson)

<br>

##### `asset.json`

A part of a PROJECT, such as a Character or Shot.

**Example**

```json
{
    "data": {
        "key": "value"
    }, 
    "name": "Bruce", 
    "schema": "mindbender-core:asset-2.0", 
    "silo": "assets", 
    "type": "asset"
}
```

**Definition**

| Key | Value | Required? | Description
|:----|:------|:----------|:------------
| `data` | `dict` | `True` | Document metadata
| `silo` | `str` | `True` | Group or container of asset
| `type` | `str` | `True` | The type of document
| `name` | `str` | `True` | Name of asset
| `schema` | `str` | `True` | Schema identifier for payload

<br>

##### `subset.json`

A part of an ASSET, such as a model or a rig.

**Example**

```json
{
    "data": {
        "endFrame": 1201, 
        "startFrame": 1000
    }, 
    "name": "shot01", 
    "schema": "mindbender-core:subset-2.0", 
    "type": "subset"
}
```

**Definition**

| Key | Value | Required? | Description
|:----|:------|:----------|:------------
| `data` | `dict` | `True` | Document metadata
| `type` | `str` | `True` | The type of document
| `name` | `str` | `True` | Name of directory
| `schema` | `str` | `True` | The schema associated with this document

<br>

##### `version.json`

An immutable iteration of a SUBSET.

Versions are immutable, in that they never change once made. This is in stark contrast to mutable versions which is when one version may be "updated" such that the same file now contains new information.

**Example**

```json
{
    "data": {
        "author": "marcus", 
        "families": [
            "mindbender.model"
        ], 
        "source": "{root}/f02_prod/assets/BubbleWitch/work/modeling/marcus/maya/scenes/model_v001.ma", 
        "time": "20170510T090203Z"
    }, 
    "locations": [
        "data.mindbender.com"
    ], 
    "name": 12, 
    "schema": "mindbender-core:version-2.0", 
    "type": "version"
}
```

**Definition**

| Key | Value | Required? | Description
|:----|:------|:----------|:------------
| `locations` | `list` | `False` | Where on the planet this version can be found.
| `data` | `dict` | `True` | Document metadata
| `type` | `str` | `True` | The type of document
| `name` | `int` | `True` | Number of version
| `schema` | `str` | `True` | The schema associated with this document

<br>

##### `representation.json`

One of many representations of a VERSION.

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
    "schema": "mindbender-core:representation-2.0", 
    "type": "representation"
}
```

**Definition**

| Key | Value | Required? | Description
|:----|:------|:----------|:------------
| `name` | `str` | `True` | Name of representation
| `type` | `str` | `True` | The type of document
| `dependencies` | `list` | `False` | Other representation that this representation depends on
| `context` | `dict` | `False` | Summary of the context to which this representation belong.
| `data` | `dict` | `True` | Document metadata
| `schema` | `str` | `True` | Schema identifier for payload

<br>

##### `container.json`

An imported VERSION, as yielded from `api.registered_host().ls()`.

**Example**

```json
{
    "asset": "Bruce", 
    "author": "Marcus Ottosson", 
    "name": "modelDefault", 
    "objectName": "modelDefault_CON", 
    "path": "|someParent|someNamespace_:modelDefault_CON", 
    "schema": "mindbender-core:container-2.0", 
    "subset": "modelDefault", 
    "version": 12
}
```

**Definition**

| Key | Value | Required? | Description
|:----|:------|:----------|:------------
| `subset` | `str` | `True` | Name of source subset
| `name` | `str` | `True` | Full name of application object
| `objectName` | `str` | `True` | Name of internal object, such as the objectSet in Maya.
| `author` | `str` | `False` | Name of the author of the published version
| `version` | `int` | `True` | Version number
| `asset` | `str` | `True` | Name of source asset
| `path` | `str` | `True` | Absolute path
| `schema` | `str` | `True` | Schema identifier for payload
