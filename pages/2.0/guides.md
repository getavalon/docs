![dropbox7](https://user-images.githubusercontent.com/2152766/27370769-f788c0f2-5655-11e7-9ba8-93e8b8de70df.png)

# How to

Here you'll find short answers to "How do I..?" types of questions. These how-to guides don't cover topics in depth – you'll find that material in the [Using Avalon]() and the [Reference](reference/). However, these guides will help you quickly accomplish common tasks.

<br>
<br>
<br>

## Install

The Avalon pipeline operates either as a *server* or *client*. If you've just discovered Avalon and owuld like to take it for a spin, check out the [Demo](#demo) section. Remote artists should head on to the [Client](#client) section, and finally [Server](#server) is for permanently setting up Avalon in your studio.

- [Demo](#demo)
- [Server](#server)
- [Client](#client)

!!! hint "Reading Code"

	You have two options for reading code in this document, one for Windows (cmd) and one for Unix system, including MacOS (bash).

	<div class="tabs">
	  <button class="tab cmd" onclick="setTab(event, 'cmd')"><p>cmd</p><div class="tab-gap"></div></button>
	  <button class="tab bash " onclick="setTab(event, 'bash')"><p>bash</p><div class="tab-gap"></div></button>
	</div>
	<div class="tab-content cmd" markdown="1">
	```bat
	These lines are for cmd.exe, typically used in Windows
	```
	</div>
	<div class="tab-content bash" markdown="1">
	```bash
	These lines are for bash, typically used in MacOS and Linux
	```
	</div>

<br>
<br>
<br>

### Prerequisites

In order to use Avalon, here's what you need.

- Windows, Linux or OSX
- [Git 2.0](https://git-scm.com/download) or above
- [Python 3.6](https://www.python.org/downloads/) or above
- [PyQt 5.7](https://www.riverbankcomputing.com/software/pyqt/download5) or above
- [MongoDB 3.4](https://www.mongodb.com/download-center#community) or above

#### Test installations

Make sure that you are able to successfully type these commands before continuing.

<div class="tabs">
  <button class="tab cmd" onclick="setTab(event, 'cmd')">
  	<p>cmd</p><div class="tab-gap"></div>
  </button>
  <button class="tab bash " onclick="setTab(event, 'bash')">
  	<p>bash</p><div class="tab-gap"></div>
  </button>
</div>

<div class="tab-content cmd" markdown="1">
```bat
python --version
rem Python 3.6.1
python -c "from PyQt5.QtCore import PYQT_VERSION_STR as version;print(version)"
rem 5.9
git --version
rem git version 2.8.3.windows.1
mongo --eval "db.version()" --quiet
rem 3.4.4
```

<button class="spoiler-btn" onclick="reveal(event, 'cmd-mongotrouble')">
	<i class="fa fa-arrow-right" aria-hidden="true"></i><p>Trouble?</p>
</button>
<div id="cmd-mongotrouble" class="spoiler hidden" markdown="1">

If `mongo` is reporting connectivity problems, try creating the default storage directory and starting the MongoDB server, `mongod.exe`.

```bat
mkdir c:\data\db
start "MongoDB" "c:\Program Files\MongoDB\Server\3.4\bin\mongod.exe"
```

- See [Install MongoDB Community Edition on Windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/) for details.
</div>

</div>

<div class="tab-content bash" markdown="1">
```bash
python --version
# Python 3.6.1
python -c "from PyQt5.QtCore import PYQT_VERSION_STR as version;print(version)"
# 5.9
git --version
# git version 2.8.3.linux.1
mongo --eval "db.version()" --quiet
# 3.4.4
```

<button class="spoiler-btn" onclick="reveal(event, 'bash-mongotrouble')">
	<i class="fa fa-arrow-right" aria-hidden="true"></i><p>Trouble?</p>
</button>
<div id="bash-mongotrouble" class="spoiler hidden" markdown="1">

- For Red Hat and CentOS 7 systems, see [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/) for details.

</div>

</div>

#### Download

At this point we are ready to download Avalon, distributed as a single directory with dependencies or references to paths outside of its directory.

<div class="tabs">
  <button class="tab cmd" onclick="setTab(event, 'cmd')">
  	<p>cmd</p><div class="tab-gap"></div>
  </button>
  <button class="tab bash " onclick="setTab(event, 'bash')">
  	<p>bash</p><div class="tab-gap"></div>
  </button>
</div>

<div class="tab-content cmd" markdown="1">
```bat
git clone https://github.com/getavalon/setup avalon-setup --recursive
```
</div>

<div class="tab-content bash" markdown="1">
```bash
git clone https://github.com/getavalon/setup avalon-setup --recursive
```
</div>

#### Command-line Interface

Avalon offers a command-line interface through which every interaction takes place.

<div class="tabs">
  <button class="tab cmd" onclick="setTab(event, 'cmd')">
  	<p>cmd</p><div class="tab-gap"></div>
  </button>
  <button class="tab bash " onclick="setTab(event, 'bash')">
  	<p>bash</p><div class="tab-gap"></div>
  </button>
</div>

<div class="tab-content cmd" markdown="1">
```bat
set PATH=%cd%\avalon-setup;%PATH%
```
</div>

<div class="tab-content bash" markdown="1">
```bash
export PATH=$(pwd)/avalon-setup:$PATH
```
</div>

You can test the success of this operation by calling `--help`.

<div class="tab-content cmd bash" markdown="1">
```bash
avalon --help
```
</div>

In order to make this command available permanently, you can add it to your system environment.

<div class="tab-content cmd" markdown="1">
```bat
setx PATH=%cd%\avalon-setup;%PATH%
```
</div>

<div class="tab-content bash" markdown="1">
```bash
echo PATH=$(pwd)/avalon-setup:$PATH >> ~/.bashrc
```
</div>

!!! hint "Trouble with environment variables?"

	Avalon uses environment variables a lot. A thorough understanding of them is an important part of maintaining an Avalon pipeline.

	See [Environment Variables](reference/#environment-variables) for learning resources.

<br>
<br>
<br>

### Demo

If you have just discovered Avalon and would like to take it for a spin, this section is for you.

#### Prerequisites

- [Autodesk Maya 2015](https://www.autodesk.com/maya) or above.

#### Upload Example Project

Avalon ships with at least one example project. In order to make use of it, we'll upload it into your database.

!!! hint "Your Database"

	If you installed MongoDB locally then the default address is `mongodb://localhost:27017`

<div class="tabs">
  <button class="tab cmd" onclick="setTab(event, 'cmd')">
  	<p>cmd</p><div class="tab-gap"></div>
  </button>
  <button class="tab bash " onclick="setTab(event, 'bash')">
  	<p>bash</p><div class="tab-gap"></div>
  </button>
</div>

<div class="tab-content cmd bash" markdown="1">
```bat
avalon --import batman
```
</div>

That's it. Now we're ready to launch Maya through Avalon.

<div class="tab-content cmd bash" markdown="1">
```bat
avalon
```
</div>

In this project, you'll find a number of assets, including a character - `Bruce` - and an animated shot - `shot1`.

Go ahead and open up Maya and load a few assets!

<br>
<br>
<br>

### Server

If you are setting up Avalon in your studio, this section is for you.

```bash
todo
```

<br>
<br>

### Client

Artists connecting to Avalon from a remote location typically do so given the specific configuration of Avalon into a particular pipeline.

Avalon ships with a default configuration for your reference.

- See [Default Configuration](/polly/#install) for details.

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
