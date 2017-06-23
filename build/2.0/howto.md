![dropbox7](https://user-images.githubusercontent.com/2152766/27370769-f788c0f2-5655-11e7-9ba8-93e8b8de70df.png)

# How to

This section is goal-oriented and shows how to solve a specific problem in a series of steps.

<br>
<br>
<br>

## Install

The Avalon pipeline operates either as a *server* or *client*, where the installation methods depends on which one you identify yourself as.

- [Demo](#demo)
- [Artist](#artist)
- [Studio](#studio)

<br>
<br>
<br>

### Prerequisites

In order to use Avalon, here's what you need.

- Windows, Linux or OSX
- [Python 2.7](https://www.python.org/downloads/) or [Python 3.6 (recommended)](https://www.python.org/downloads/)
- [PyQt 5.6](https://www.riverbankcomputing.com/software/pyqt/download5) or above
- [Git 2.0](https://git-scm.com/download) or above
- [Docker 17.0](https://www.docker.com/) or above
- [Mongo 3.4](https://www.mongodb.com/) or above

**Test installations**

```bash
python --version
# Python 3.6.1
python -c "from PyQt5.QtCore import PYQT_VERSION_STR as version;print(version)"
# 5.7
git --version
# git version 2.8.3.windows.1
docker --version
# Docker version 17.05.0-ce, build 89658be
mongo --eval "db.version()" --quiet
# 3.4.4
```

**Download**

At this point we are ready to download Avalon, distributed as a single directory with dependencies or references to paths outside of its directory.

```bash
git clone https://github.com/getavalon/setup avalon-setup --recursive
```

<br>
<br>
<br>

### Demo

If you have just discovered Avalon and would like to take it for a spin, this section is for you.

**Prerequisites**

- Maya 2015 or above

```bash
cd avalon-example/projects/spiderman
mayapy build.py
```

<br>
<br>
<br>

### Artist

If you are an artist working with a studio remotely, this section is for you.

```bash
# Commands to get started as an artist
```

![untitled project](https://cloud.githubusercontent.com/assets/2152766/26095001/00d078c0-3a14-11e7-9b9b-892fd7aec01b.gif)

**Congratulations!**

You are now fully equipped to handle Avalon tasks!

<br>
<br>
<br>

### Studio

If you are setting up Avalon in your studio, this section is for you.

In Avalon there are two types of data - files, and documents. Files are stored on your file-system whereas documents are stored in a document-database as JSON. In order to read and write data, you will need to install the database software.

- [Database Software](https://www.mongodb.com/download-center#community)

!!! note "Remote Access"
	If you are setting up Avalon in a company with artists working remotely, it is recommended you make the address and port to the database accessible externally, such as via the public internet.

With the database installed and running, configure your `mb-gui.bat` to point to the address of where it was installed and head to the [Project Inventory API](#project-inventory-api) section below to create your first project.

<br>
<br>

### Update

To update avalon-setup, type this.

```bash
$ cd avalon-setup
$ git pull
$ git submodule init
$ git submodule update --recursive
```

It is safe to run these as many times as you'd like.

<br>
<br>
<br>

## Create your first project

To create a new project, create a new directory and fetch default values like this.

```bash
$ mkdir myProject
$ cd myProject
$ python -m avalon.inventory --init
$ # Edit .inventory.toml and .config.toml
$ python -m avalon.inventory --save
```

The `avalon.inventory` module will take into account the name of the parent directory as the project name and produce two files, the "inventory" and "config".

- See [Project Inventory API](reference/#project-inventory-api) for details on how to manage your `.inventory.toml` file.
- See [Project Configuration API](reference/#project-configuration-api) for details on how to manage your `.config.toml` file.

<br>
<br>
<br>