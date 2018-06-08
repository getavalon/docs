![dropbox5](https://user-images.githubusercontent.com/2152766/27342274-9e6203b8-55d7-11e7-8834-8e27bb75008a.png)

# Tutorials

Here you'll find a series of steps to achieve a goal.

<br>
<br>

## Create your first project

To create a new project, create a new directory and fetch default values like this.

<div class="tabs">
  <button class="tab cmd" onclick="setTab(event, 'cmd')">
  	<p>cmd</p><div class="tab-gap"></div>
  </button>
  <button class="tab bash " onclick="setTab(event, 'bash')">
  	<p>bash</p><div class="tab-gap"></div>
  </button>
</div>

<div class="tab-content cmd bash" markdown="1">
```bash
mkdir myProject
cd myProject
avalon --init
# Edit .inventory.toml and .config.toml
avalon --save
```
</div>

`--init` and `--save` will take into account the name of the parent directory as the project name and produce two files, the "inventory" and "config". You can override this via `--root`. See `--help` for details.

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
mkdir mySecondProject
cd mySecondProject
copy ../myProject/.* ./
avalon --save
```
</div>

<div class="tab-content bash" markdown="1">
```bash
mkdir mySecondProject
cd mySecondProject
cp ../myProject/.* ./
avalon --save
```
</div>

The `--init` command is used to write a generic configuration and inventory to your current working directory. If you already have some, it isn't necessary.

<br>
<br>
<br>

## Create your first asset

With a project up and running, how do you actually go about creating assets?

```bash
cd myproject
avalon --load
# Edit .inventory.toml
avalon --save
```

With `--load`, the `.inventory.toml` is written to your current working directory, ready for you to edit. Here's an example entry into the `.inventory.toml`.

```ini
[[assets]]
name = "Batman"
label = "The Batman"  # (Optional) Nicer name
group = "Character"  # (Optional) Visual grouping
icon = "gear"  # (Optional) Icon from FontAwesome
```

With the changes saved, you'll find the new asset in the Launcher.

!!! hint "Load project by name"

    Normally, the project name is derived from the current working directory. You may also pass a project name to the `--load` argument, e.g. `--load myproject`

!!! hint "List available projects"

    When loading a project for the first time, you can list available in the Avalon database via `avalon --ls`

<br>
<br>
<br>
