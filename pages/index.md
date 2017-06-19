!!! warning "Beta Documentation"

	I'm currently working on this.

Welcome to mindbender-pipeline, the production pipeline at [Mindbender Animation Studio](http://mindbender.com).

<br>

## Description

Mindbender is a content creation studio focusing on photo-realistic, yet exaggerated cartoons. They work across continents in Sweden, Brazil and Spain and therefore require an underlying pipeline that facilitate these activities.

Pyblish Mindbender works exclusively with computer generated imagery - which means no focus is put on video, sound or the integration of 3d and live action footage. It has been designed for use both locally and remotely, to bridge the gap between artists working together but in different locations.

### Mission

- **Keywords:** Film, games, content creation, pipeline

- **Objective:**
    1. Provide a unified framework within which artists at Mindbender may work efficiently.
    1. Enable extending of said framework for future improvements and unique requirements.
    1. Inspire further expansion upon a series of basic ideas.

- **Requirements:** Core functionality must be editable and extensible by the technical director.

- **Technology:** Mindbender is built upon [Pyblish](http://pyblish.com), [Python](https://www.python.org) and [bindings](https://github.com/mottosso/Qt.py) for [Qt](https://qt.io), and depends upon a Windows, Linux or MacOS operating system with [Autodesk Maya](http://www.autodesk.com/maya), [The Foundry Nuke](https://www.thefoundry.co.uk/products/nuke/), [SideFX Houdini](https://www.sidefx.com/) and other DCC content creation applications.

<br>
<br>

## Features

This project currently boasts the following features.

|          | Feature                                        | Description
|:---------|:-----------------------------------------------|:--------------------
| ![][shd] | **Open Source**                                    | Anyone can take part in testing, using and developing the pipeline on [GitHub](https://github.com/mindbender-studio).
| ![][pro] | **Version Control**                                | Entire pipeline is [reviewed](https://github.com/mindbender-studio/core/pulls?q=is%3Apr+is%3Aclosed) and [tested](https://travis-ci.org/mindbender-studio/core) prior to any change being made.
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
