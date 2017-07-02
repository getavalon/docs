![dropbox7](https://user-images.githubusercontent.com/2152766/27370769-f788c0f2-5655-11e7-9ba8-93e8b8de70df.png)

# How to

Here you'll find short answers to "How do I..?" types of questions. These how-to guides don’t cover topics in depth – you'll find that material in the [Using Avalon]() and the [Reference](reference/). However, these guides will help you quickly accomplish common tasks.

<br>
<br>
<br>

## Install

The Avalon pipeline operates either as a *server* or *client*, where the installation method depend on which one you identify yourself as.

- [Demo](#demo)
- [Studio](#studio)

<br>
<br>
<br>

### Prerequisites

In order to use Avalon, here's what you need.

- Windows, Linux or OSX
- [Git 2.0](https://git-scm.com/download) or above
- [Python 3.6](https://www.python.org/downloads/) or above
- [PyQt 5.6](https://www.riverbankcomputing.com/software/pyqt/download5) or above
- [MongoDB 3.4](https://www.mongodb.com/) or above

!!! note "MongoDB"
	You can choose to set-up MongoDB locally (difficult) or you can host one for free in the cloud (simple) at https://mlab.com

**Test installations**

Make sure that you are able to successfully type these commands before continuing.

```bash
python --version
# Python 3.6.1
python -c "from PyQt5.QtCore import PYQT_VERSION_STR as version;print(version)"
# 5.9
git --version
# git version 2.8.3.windows.1
mongo --eval "db.version()" --quiet
# 3.4.4
```

!!! note "Remote Access"
	If you are setting up Avalon in a company with artists working remotely, it is recommended you make the address and port to the database accessible externally, such as via the public internet.

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

**Prerequisities**

In addition to the global prerequisities, you'll also need these.

- [Mongo 3.4](https://www.mongodb.com/) or above
- [Autodesk Maya 2016](https://autodesk.com/maya) or above

**Test installations**

```bash
mongo --eval "db.version()" --quiet
# 3.4.4
mayapy --version
# Python 2.7.6
```

Now you are ready to *build* one of the example projects that ship with Avalon.

```bash
cd avalon-example/projects/batman
python build.py
# -----------------------
# Building "batman"
# -----------------------
# Modeling..
# Rigging..
# Animating..
# Shading..
# Rendering..
# Compositing..
# Editing..
# Delivering..
#
# Success!
$ 
```

<br>
<br>
<br>

### Studio

If you are setting up Avalon in your studio, this section is for you.

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

## Create your second project

Once you've tailored the configuration and inventory to your liking, you can re-use them for future projects.

1. Copy your `.config.toml` and `.inventory.toml` files from your first project.
2. Run the `--save` command

**For example**

```bash
$ mkdir mySecondProject
$ cd mySecondProject
$ copy ../myProject/.* ./
$ python -m avalon.inventory --save
```

The `--init` command is used to write a generic configuration and inventory to your current working directory. If you already have some, it isn't necessary.

<br>
<br>
<br>
