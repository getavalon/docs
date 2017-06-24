build: false
template: 1.0.html

# Avalon

<div style="text-align: center">
    <img src="https://user-images.githubusercontent.com/2152766/27349489-58285f06-55ef-11e7-9229-b89320eae405.png">
    <p style="margin: 0">The safe post-production pipeline</p>
</div>

<br>
<br>

- **Keywords:** Film, games, content creation, pipeline

- **Objective:**
    1. Provide a unified framework within which artists at Avalon may work efficiently.
    1. Enable extending of said framework for future improvements and unique requirements.
    1. Inspire further expansion upon a series of basic ideas.

- **Requirements:** Core functionality must be editable and extensible by the technical director.

- **Technology:** Avalon is built upon [Pyblish](http://pyblish.com), [Python](https://www.python.org) and [bindings](https://github.com/mottosso/Qt.py) for [Qt](https://qt.io), and depends upon a Windows, Linux or MacOS operating system with [Autodesk Maya](http://www.autodesk.com/maya), [The Foundry Nuke](https://www.thefoundry.co.uk/products/nuke/), [SideFX Houdini](https://www.sidefx.com/) and other DCC content creation applications.

<br>
<br>

### Target Audience

To make the most out of this document, some knowledge and experience is assumed.

|                      | minimal                            | recommended             
|:---------------------|:-----------------------------------|:--------------
| **title**          | technical director                 | pipeline technical director
| **experience**     | 1 year in advertisements or games  | 5+ years in feature film
| **software**       | windows, linux or macos            | maya

<br>
<br>
<br>
<br>

### Introduction

Welcome to avalon-core, the production pipeline at [Mindbender Animation Studio](http://mindbender.se).

<br>

**Table of contents**

- [Features](#features)
- [Install](#install)
- [Update](#update)
- [Usage](#usage)
- [Description](#description)
- [Batteries](#batteries)
    - [Creator](#creator)
    - [Loader](#loader)
    - [Manager](#manager)
- [API](#api)
    - [Terminology](#terminology)
    - [Filesystem API](#filesystem-api)
        - [Information Hierarchy](#information-hierarchy)
        - [Private, Public and Stage](#private-public-and-stage)
        - [`ls()`](#ls)
        - [`asset.json`](#assetjson)
        - [`version.json`](#versionjson)
        - [`subset.json`](#subsetjson)
        - [`representation.json`](#representationjson)
        - [`container.json`](#containerjson)
    - [Avalon API](#avalon-api)
    - [Host API](#host-api)
- [Contract](#contract)
    - [`avalon.model`](#avalonmodel)
    - [`avalon.rig`](#avalonrig)
    - [`avalon.animation`](#avalonanimation)
    - [`avalon.lookdev`](#avalonlookdev)
- [Homework](#homework)
- [Contributing](#contributing)
- Help

<br>
<br>

### Features

This project currently boasts the following features.

|          | Feature                                        | Description
|:---------|:-----------------------------------------------|:--------------------
| ![][shd] | **Open Source**                                    | Anyone can take part in testing, using and developing the pipeline on [GitHub](https://github.com/getavalon).
| ![][pro] | **Version Control**                                | Entire pipeline is [reviewed](https://github.com/getavalon/core/pulls?q=is%3Apr+is%3Aclosed) and [tested](https://travis-ci.org/getavalon/core) prior to any change being made.
| ![][ast] | **Issue Tracker**                                  | Feature requests, bugs and questions are reported, assigned and solved openly.
| ![][ver] | **Single-command install and update via Git**      | Zero dependencies make for easy install and updates.
| ![][rep] | **Environment management**                         | The developer manages the environment without distrupting the end user
| ![][for] | **Directory management**                           | Folders are automatically created as per the developers setup.
| ![][shd] | **Application launcher**                           | Control over which version of which software is launched along with its initial configuration.
| ![][usr] | **Asset versioning**                               | Every asset, including shots, are explicitly versioned - e.g. v001, v034
| ![][ver] | **Asset subsets**                                  | Each asset, such as `Tarzan`, contains one or more subsets, such as `model`, `rig` and `look`.
| ![][stg] | **Asset and shot uniformity**                      | Shots are assets too.
| ![][shd] | **Per project/shot settings**                      | Globally configure the framerate of a given project.
| ![][prd] | **Per family publishing of assets**                | Individually manage the validation and export assets of specific types, such as `model`, `rig` and `animation`.
| ![][cns] | **Per family loading of assets**                  | Individually manage loading of the same specific types of assets.
| ![][for] | **Asset Metadata**                                | Relevant information is stored alongside each published version
| ![][pro] | **Tools**                                          | Graphical user interfaces for Creating, Publishing, Loading and Managing assets
| ![][shd] | **Menus**                                         | Application menus for modeling, rigging and animation
| ![][ver] | **Support for off-site freelancers/studios**       | No dependence on the local environment, the pipeline can be installed anywhere.
| ![][ast] | **Support for Qt 4 and Qt 5 bindings**            | Transparently uses the most desirable binding of Qt wherever the pipeline is used.

<br>
<br>

### Install

Avalon takes the form of a "git" repository. Therefore, you will need to install [Git](https://git-scm.com/). Once installed, open up a terminal (Start > "cmd" > Enter) and type this in.

```bash
$ git clone https://github.com/getavalon/setup avalon-setup --recursive
$ cd avalon-setup
$ git checkout 1.0 -b 1.0
$ git submodule update
$ start .
```

Windows Explorer appears! Double-click `mb.bat` and off you go!

![image](https://cloud.githubusercontent.com/assets/2152766/22154279/2c4011ee-df2b-11e6-899a-faf7d4e597f4.png)

![untitled](https://cloud.githubusercontent.com/assets/2152766/22067559/152dbc08-dd92-11e6-9a37-879a0d0ab445.gif)

**Congratulations!**

You are now fully equipped to handle Avalon tasks!

**Next Step**

- [Update](#update)
- [Customisation](#customisation)
- [Workflow](#contract)

<br>
<br>

### Update

To update avalon-setup, run the `update.bat` file supplied within the `avalon-setup` directory.

Alternatively, you may type this.

```bash
$ cd avalon-setup
$ git pull
$ git submodule update --recursive
```

It is safe to run these as many times as you'd like.

<br>
<br>

### Customisation

The above is all that is required to get started with the Avalon Pipeline. If you are at home and are just looking to try things out, feel free to play around. Create a few assets, publish them and familiarise yourself with the [workflow](#contract).

If you are at a studio, you will likely want to use your own projects with the Avalon Launcher.

The next step is telling `mb.bat` about your local projects. From your terminal, type this.

```bash
$ cd avalon-setup
$ notepad mb.bat
```

Notepad appears.

At the bottom of this file, replace `%REPLACE_ME%` with the absolute path to where your projects are located, such as `m:\f03_projects`. Now type `mb.bat` again to access your own projects. Optionally, you may also create a shortcut of `mb.bat` to your Desktop, Start Menu or any location you prefer.

<br>
<br>

### Usage

Avalon is initialised by calling `install()` with an interface for your host.

```python
from avalon import api, maya
api.install(maya)
```

**Supported hosts**

- [`maya`]()
- [`nuke`]()
- [`houdini`]()

From here, you model, rig and animate as per the [contract](#contract) below.

<br>
<br>

### How to read this guide

Here are a few of the conventions used throughout this guide.

- **bold** words are used to augment important aspects of a sentence
- UPPERCASE words are unique terminology, each detailed under [Terminology](#terminology) below.
- (1), (2) are used to division important aspects in a sentence.
- `code` is used to highlight words that occur in code.

<br>
<br>

### Description

Avalon is a content creation studio focusing on photo-realistic, yet exaggerated cartoons. They work across continents in Sweden, Brazil and Spain and therefore require an underlying pipeline that facilitate these activities.

Pyblish Avalon works exclusively with computer generated imagery - which means no focus is put on video, sound or the integration of 3d and live action footage. It has been designed for use both locally and remotely, to bridge the gap between artists working together but in different locations.

**Overview**

This pipeline covers the entire pipeline at Avalon, including asset and shot creation. A PROJECT is partitioned into SHOTs where each shot consists of one or more ASSETs.

This pipeline includes tools and Pyblish plug-ins for 4 common types of ASSETs in a typical production pipeline.

- Modeling
- Rigging
- Animation
- Look

These implement **(1)** a contract for each FAMILY of ASSETs and **(2)** their interface towards each other.

<br>
<br>

### Batteries

Avalon hosts a series of [graphical user interfaces](#batteries) that aid the user in conforming to the specified [contracts](#contracts).

| Name              | Purpose                          | Description
|:------------------|:---------------------------------|:--------------
| **creator**            | control what goes out           | Manage how data is outputted from an application.
| **loader**            | control what goes in             | Keep tabs on where data comes from so as to enable tracking and builds.
| **manager**           | stay up to date                  | Notification and visualisation of loaded data.

<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314626/a8a3b72e-283f-11e7-90fd-3fa76e75276e.png">

#### Creator

Associate content with a family.

The family is what determins how the content is handled throughout your pipeline and tells Pyblish what it should look like when valid.

**API**

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

#### Loader

Visualise results from `api.ls()`.

```python
from avalon import api

for asset in api.ls():
    print(asset["name"])
```

**API**

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

#### Manager

Visualise loaded assets.

```python
from avalon import maya

for container in maya.ls():
    print(container["name"])

# The same is true for any host; houdini, nuke etc.
```

**API**

The results from `ls()` depends on the currently registered host, such as Maya.

```python
from avalon import nuke
api.register_host(nuke)
```

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## API

Avalon exposes a series of interrelated APIs to the end-user.

| Name                              | Purpose
|:----------------------------------|:--------------
| [**Terminal API**](#terminal-api)     | Defines how the **artist** interacts with **tasks**
| [**Filesystem API**](#filesystem-api) | Defines how the **developer** interact with **data** on disk
| [**Avalon API**](#avalon-api) | Defines how the **developer** interacts with **Avalon**
| [**Host API**](#host-api)             | Defines how the **host** interacts with **Avalon**

<br>
<br>

### Terminology

Avalon reserves the following words for private and public use. Public members are exposed to the user, private ones are internal to the implementation.

|          | Term                | Public | Description         | Example
|:---------|:--------------------|:-------|:--------------------|:------------------------
| ![][pro] | `PROJECTS`          | `X`    | Parent of projects  | `m:\f03_projects`
| ![][pro] | `PROJECT`           | `X`    | Root of information | Gravity, Dr. Strange
| ![][ast] | `ASSET`             | `X`    | Unit of data        | Ryan, Bicycle, Flower pot
| ![][ver] | `VERSION`           | `X`    | An ASSET iteration  | v1, v034
| ![][rep] | `REPRESENTATION`    |        | A data format       | Maya file, pointcache, thumbnail
| ![][for] | `FORMAT`            |        | A file extension    | `.ma`, `.abc`, `.ico`, `.png`
| ![][shd] | `FAMILY`            | `X`    | A type of ASSET     | `model`, `rig`, `look`, `animation`
| ![][usr] | `WORKSPACE`         | `X`    | Private data        | Scenefile for v034 of Ryan
| ![][usr] | `SILO`              |        | Data repository     | Ryan resides in `assets`, caches in `film`.
| ![][ver] | `INSTANCE`          |        | Inverse of a file   | `modelDefault_SET`
| ![][stg] | `STAGE`             |        | Transient data      | Outgoing VERSION from scenefile
| ![][shd] | `SHARED`            | `X`    | Public data         | v034 of Ryan
| ![][prd] | `PRODUCER`          |        | Creator of data     | You
| ![][cns] | `CONSUMER`          |        | User of data        | Me

<br>
<br>

### Terminal API

`mb.bat` (pronounced "embee-bat") is the Avalon Launcher. It is how artists launch applications, such as Maya and Nuke. It establishes important environment variables used when producing and publishing data, along with exposing artists to tools relevant a given project.

![untitled](https://cloud.githubusercontent.com/assets/2152766/22065809/2960e216-dd8a-11e6-9bf4-435a8c25f98c.gif)

<br>

**project.bat**

`mb.bat` is where artists enter the pipeline. A user may then enter any of the available projects, via a `project.bat` file.

The project file is located in your PROJECTS directory

```bash
@echo off
call _mkproject %~dp0 %~n0 %1
```

**asset.bat**

```bash
@echo off
call _mkproject %~dp0 %~n0 %1
```

The layout is as follows.

1. `{PROJECT}` (with TAB-completion)
2. `{ASSET}` or Shot (with TAB-COMPLETION)
3. `{APPLICATION}` `{TASK}`

The given TASK is automatically created, unless it already exists.

**Environment variables**

| Variable       | Description
|:---------------|:-------------------
| `PROJECT`      | Nice name of PROJECT, e.g. Gifts for Greta
| `PROJECTDIR`   | Absolute path to PROJECT, e.g. m:\f01_projects\p999_Gifts_for_Greta
| `ROOT`         | Top level directory of either shot or asset, e.g. ..\Greta

<br>
<br>

### Filesystem API

Data is organised into **files** and **folders**.

Some files and folders have special meaning in Avalon.

![image](https://cloud.githubusercontent.com/assets/2152766/18836965/03e2f018-83fa-11e6-81d5-2dcfa19c43ab.png)

<br>

#### Information Hierarchy

The mental and physical model for files and folders look like this.

![temp_03](https://cloud.githubusercontent.com/assets/2152766/18833936/1aba9bba-83eb-11e6-812c-2104f7bb3e2a.png)

<br>
<br>

#### Private, Public and Stage

During the course of the creation of any ASSET, data moves between 2 of 3 states.

![temp](https://cloud.githubusercontent.com/assets/2152766/18838199/798a132e-83fe-11e6-8c1f-f515978d6ce2.png)

- The pipeline does not take into consideration the workspace and is therefore **workspace-agnostic**. 
- The **staging area** is both implicit and transparent to the PRODUCER and CONSUMER, except for debugging purposes. This is where automatic/scheduled garbage collection may run to optimise for space constraints.
- The **shared space** is where ASSETs ultimately reside once published.

<br>

**Private and Public separation**

A naive approach to content creation might be to refer to ASSETs straight from another artists workspace. At Avalon, data is separated between work-in-progress (private) and data exposed to others (public).

Private data resides in `work`, public data resides in `publish`.

![](https://cloud.githubusercontent.com/assets/2152766/22207956/15071c7a-e179-11e6-90ba-dd529c8cda6e.png)

Private data is highly **mutable** and typically **private** to an individual artist.

- **Mutable** implies transient data that is likely to change at any given moment.
- **Private** implies personal, highly irregular and likely invalid data.

Public data on the other hand is **immutable**, **correct** and **impersonal**.

- **Immutable** implies that the data may be dependent upon by other data.
- **Correct** implies passing validation of the associated family.
- **Impersonal** implies following strict organisational conventions.

[ver]: https://cloud.githubusercontent.com/assets/2152766/18576835/f6b80574-7bdc-11e6-8237-1227f779815a.png
[ast]: https://cloud.githubusercontent.com/assets/2152766/18576836/f6ca19e4-7bdc-11e6-9ef8-3614474c58bb.png
[rep]: https://cloud.githubusercontent.com/assets/2152766/18759916/b2e3161c-80f6-11e6-9e0a-c959d63047a8.png
[for]: https://cloud.githubusercontent.com/assets/2152766/18759918/b479168e-80f6-11e6-8d1c-aee4e654d335.png
[pro]: https://cloud.githubusercontent.com/assets/2152766/18760901/d6bf24b4-80fa-11e6-8880-7a0e927c8c27.png
[usr]: https://cloud.githubusercontent.com/assets/2152766/18808940/eee150bc-8267-11e6-862f-a31e38d417af.png
[shd]: https://cloud.githubusercontent.com/assets/2152766/18808939/eeded22e-8267-11e6-9fcb-150208d55764.png
[stg]: https://cloud.githubusercontent.com/assets/2152766/18835951/9dbaf5d2-83f5-11e6-9ea4-fbbb5f1d0e13.png
[prd]: https://cloud.githubusercontent.com/assets/2152766/18836255/163d70a6-83f7-11e6-94b7-2f65a2c3b53b.png
[cns]: https://cloud.githubusercontent.com/assets/2152766/18836254/163d1124-83f7-11e6-9575-05a523a364fb.png

<br>
<br>

Each **[ASSET](#assetjson)** reside within a top-level ROOT and SILO directory as follows.

| Hierarchy       | Example
|:----------------|:--------------
| ![hasset][]     | ![hassetex][]

<br>

Each ASSET contains a `work` and `publish` directory. `work` is where artists save their own files while working, whereas `publish` is where published files go.

The `publish` directory contains 0 or more **[SUBSETS](#subsetjson)** which in turn contains 0 or more **[VERSIONS](#versionjson)**

| Hierarchy       | Example
|:----------------|:--------------
| ![hsubset][]    | ![hsubsetex][]

<br>

Each VERSION contains 1 or more **[REPRESENTATIONS](#representationjson)**.

| Example
|:--------------
| ![hrepresentationex][]

<br>

All data is written in 3 stages.

1. To a local `/temp` directory.
2. To a "staging" directory
3. To the final destination.

Data is first written locally, so as to not burden a potentially remote filesystem with sporadic writes performed by an application - for example, caching may be bound by parsing of geometry, and not I/O bound. Which means many small writing requests are scattered when exporting a large file.

It also alleviates the remote system from times where writing is cancelled or otherwise fails.

The staging area is where files are written next; the stage resides within the users local workspace and offers the end-user a chance to inspect previous successful and unsuccessful publishes. On a successful export from an application, this is where disparate files are assembled and injected with additional metadata

 Should this succeed, the are then moved to their final destination.

| Hierarchy     | Example
|:--------------|:------------
| ![usr1][]     | ![usr2][]

Each directory will contain everything that did extract successfully, along with its metadata, for manual inspection and debugging.

[hasset]: https://cloud.githubusercontent.com/assets/2152766/22207956/15071c7a-e179-11e6-90ba-dd529c8cda6e.png
[hassetex]: https://cloud.githubusercontent.com/assets/2152766/22207927/fec8e434-e178-11e6-9c0b-ac41ce076211.png

[hsubset]: https://cloud.githubusercontent.com/assets/2152766/22208171/d6f6b322-e179-11e6-9676-9afaae280ed4.png
[hsubsetex]: https://cloud.githubusercontent.com/assets/2152766/22208200/eecfe478-e179-11e6-9a8c-f70f02d7e74d.png

[hrepresentationex]: https://cloud.githubusercontent.com/assets/2152766/22208262/2ecdf0a6-e17a-11e6-9b86-2516231d906e.png

[usr1]: https://cloud.githubusercontent.com/assets/2152766/18834482/07938972-83ee-11e6-92d0-1a989c2b54dd.png
[usr2]: https://cloud.githubusercontent.com/assets/2152766/18834427/ab4b319c-83ed-11e6-8e72-2bf59e83b8d5.png

<br>

#### `ls()`

Communication with the filesystem is made through `ls()`.

`ls()` returns available assets - relative the currently registered root and silo directories - in the form of JSON-compatible dictionaries. Each dictionary is strictly formatted according to four distinct ["schemas"](https://en.wikipedia.org/wiki/Database_schema).

**Example**

```python
from avalon import api

for asset in api.ls():
    for subset in asset["subsets"]:
        for version in asset["versions"]:
            for representation in version["representations"]:
                pass
```

See below for a full list of members.

<br>

## Schema

![image](https://cloud.githubusercontent.com/assets/2152766/22086121/8c037080-ddd7-11e6-9149-439203c32c6b.png)

Available schemas are organised hierarchically, with the former containing the latter.

- [`asset.json`](#assetjson)
  - [`subset.json`](#subsetjson)
      - [`version.json`](#versionjson)
        - [`representation.json`](#representationjson)

<br>

#### `asset.json`

A part of a PROJECT, such as a Character or Shot.

| Key               | Value  | Description
|:------------------|:-------|:-------------
| `name`            | `str`  | Name of directory
| `subsets`         | `list` | 0 or more [`subset.json`](#subsetjson)

<br>

#### `subset.json`

A part of an ASSET, such as a model or a rig.

| Key               | Value  | Description
|:------------------|:-------|:-------------
| `name`            | `str`  | Name of directory
| `versions`        | `list` | 0 or more [`version.json`](#versionjson)

<br>

#### `version.json`

An immutable iteration of a SUBSET.

| Key               | Value  | Description
|:------------------|:-------|:-------------
| `version`         | `int`  | Number of this VERSION
| `path`            | `str`  | Unformatted path, e.g. `{root}/`
| `time`            | `str`  | ISO formatted, file-system compatible time.
| `author`          | `str`  | User logged on to the machine at time of publish.
| `source`          | `str`  | Original file from which this VERSION was made.
| `representations` | `list` | 0 or more [`representation.json`](#representationjson)

Versions are immutable, in that they never change once made. This is in stark contrast to mutable versions which is when one version may be "updated" such that the same file now contains new information.

<br>

#### `representation.json`

One of many representations of a VERSION.

| Key               | Value  | Description
|:------------------|:-------|:-------------
| `format`          | `str`  | File extension
| `path`            | `str`  | Unformatted path

Think of a representation as one way of storing the same set of data on disk. For example, an image may be stored as both PNG and JPEG. Different files, same data. It could also be stored as a description. *"A picture of my computer."* Much less information is ultimately stored, but it is nonetheless the exact same original data in a different (albeit lossy) representation. The image could also be represented by a feeling (warm, mystical) or a spoken word (muah!).

Representation are very powerful and lie at the heart of assets that are more than just a single file.

As a practical example, a Look is stored as both an MA scene file and a JSON. The JSON stores the shader relationships, whereas the MA file stores the actual shaers. Same data, different representations.

#### `container.json`

An imported VERSION, as yielded from `api.registered_host().ls()`.

| Key               | Value  | Description
|:------------------|:-------|:-------------
| `schema`          | `str`  | Contains `"avalon-core:container-1.0"`
| `name`            | `str`  | Pipeline name of this container
| `objectName`      | `str`  | Internal name used in an application
| `asset`           | `str`  | Source ASSET of this container
| `subset`          | `str`  | Source SUBSET of this container
| `version`         | `int`  | Source VERSION of this container
| `path`            | `str`  | Path to loaded VERSION
| `source`          | `str`  | Absolute path to original scene
| `author`          | `str`  | Author of VERSION

<br>
<br>

### Avalon API

Avalon provides a *stateful* API.

State is set and modified by calling any of the exposed registration functions, prefixed `register_*`.

<br>

Public members of `avalon.api`

| Member                           | Returns  | Description
|:---------------------------------|:---------|:--------
| `install(host)`                  | `str`    | Install Avalon into the current interpreter session
| `uninstall()`                    | `str`    | Revert installation
| `ls()`                           | `generator` | List available assets, relative `root`
| `registered_root()`              | `str`       | Absolute path to current working directory
| `format_staging_dir(root, name)` | `str`       | Return absolute path or staging directory relative arguments
| `format_shared_dir(root)`        | `str`       | Return absolute path of shared directory
| `format_version(version)`        | `str`       | Return file-system compatible string of `version`
| `find_latest_version(versions)`  | `int`       | Given a series of string-formatted versions, return the latest one
| `parse_version(version)`         | `str`       | Given an arbitrarily formatted string, return version number
| `register_root(root)`            |             | Register currently active root
| `register_host(host)`            |             | Register currently active host
| `register_plugins()`             |             | Register plug-ins bundled with Pyblish Avalon
| `deregister_plugins()`           |             |
| `registered_host()`              | `module`    | Return currently registered host
| `registered_families()`          | `list`      | Return currently registered families
| `registered_data()`              | `list`      | Return currently registered data
| `registered_root()`              | `str`       | Return currently registered root

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

**Information hierarchy**

Loaded data is stored in a `container`. A container hosts a loaded asset along with metadata used to associate assets that use other assets, such as a Wheel asset used in a Car asset.

![Host data relationship](https://cloud.githubusercontent.com/assets/2152766/18905784/aa6a3d5c-855c-11e6-9843-b24ebd23c4ac.png)

**Id**

Internally, Pyblish instances and containers are distinguished from native content via an "id". For example, in Maya, the `id` is a user-defined attribute.

| Name                         | Description              | Example
|:-----------------------------|:-------------------------|:----------
| `pyblish.avalon.container`  | Unit of incoming data    | `...:model_GRP`, `...:rig_GRP` 
| `pyblish.avalon.instance`   | Unit of outgoing data    | `Strange_model_default`

<br>
<br>

## Contract

Avalon defines these families.

| Family                 | Definition                                      | Link
|:-----------------------|:------------------------------------------------|:------------
| `avalon.model`     | Geometry with deformable topology               | [Spec](#avalonmodel)
| `avalon.rig`       | An articulated `avalon.model` for animators | [Spec](#avalonrig)
| `avalon.animation` | Pointcached `avalon.rig` for rendering      | [Spec](#avalonanimation)
| `avalon.lookdev`   | Shaded `avalon.model` for rendering         | [Spec](#avalonlookdev)

<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314853/4c84d5e6-2843-11e7-9b66-4c4506c89320.png"/>

### `avalon.model`

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

### `avalon.rig`

The `avalon.rig` contains the necessary implementation and interface for animators to animate. 

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

### `avalon.animation`

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

### `avalon.lookdev`

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

## Contributing

To contribute to this project, see one of the following pages for [avalon/core](https://github.com/getavalon/core) for function and API, [avalon/setup](https://github.com/getavalon/setup) for setup and distribution, [avalon/config](https://github.com/getavalon/config) for data.

Contributing to any Avalon project assumes a working knowledge of [Git](https://git-scm.com) and an understanding of the [Fork and Pull-Request](https://guides.github.com/activities/forking/) workflow.

Enjoy and hope to see you soon!