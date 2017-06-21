![dropbox7](https://user-images.githubusercontent.com/2152766/27370769-f788c0f2-5655-11e7-9ba8-93e8b8de70df.png)

# How to

This section is goal-oriented and shows how to solve a specific problem in a series of steps.

<br>
<br>
<br>

## Install

The Mindbender pipeline operates either as a *server* or *client*, where the installation methods depends on which one you identify yourself as.

- [Artist](#artist)
- [Studio](#studio)

<br>
<br>
<br>

### Prerequisites

In order to use Avalon, here's what you need.

- [Python 2.7](https://www.python.org/downloads/) or [Python 3.6 (recommended)](https://www.python.org/downloads/)
- [Git 2.x.x](https://git-scm.com/download)

At this point we are ready to download Avalon and later customise it.

```bash
git clone https://github.com/mindbender-studio/setup mindbender-setup --recursive
```

<br>
<br>
<br>

### Artist

If you are an artist working with a studio remotely, this section is for you.



**1. Configure**

Next, create a new file, such as on your Desktop and copy/paste the following.

`mb-gui.bat`

```bash
@echo off

set MINDBENDER_MONGO=<login>
set MINDBENDER_PROJECTS=<projects>

call <path>\mindbender-setup\mb-gui.bat
```

1. Replace `<login>` with your login information, e.g. `mongodb://localhost:27017`
2. Replace `<projects>` with the full path to your project files, e.g. `m:\f01_projects`
3. Replace `<path>` to the full path to where you installed `mindbender-setup`, e.g. `c:\users\marcus`

**2. Launch**

Finally, double-click your `mb-gui.bat` and off you go!

![untitled project](https://cloud.githubusercontent.com/assets/2152766/26095001/00d078c0-3a14-11e7-9b9b-892fd7aec01b.gif)

**Congratulations!**

You are now fully equipped to handle Mindbender tasks!

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

To update mindbender-setup, run the `update.bat` file supplied within the `mindbender-setup` directory.

Alternatively, you may type this.

```bash
$ cd mindbender-setup
$ git pull
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
$ python -m mindbender.inventory --init
$ # Edit .inventory.toml and .config.toml
$ python -m mindbender.inventory --save
```

The `mindbender.inventory` module will take into account the name of the parent directory as the project name and produce two files, the "inventory" and "config".

- See [Project Inventory API](reference/#project-inventory-api) for details on how to manage your `.inventory.toml` file.
- See [Project Configuration API](reference/#project-configuration-api) for details on how to manage your `.config.toml` file.
