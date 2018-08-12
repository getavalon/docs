![dropbox3](https://user-images.githubusercontent.com/2152766/27328354-cd712dd8-55a9-11e7-89b8-bb8b01b9c66d.png)

# Tools

Avalon ships with a number of graphical user interfaces for the end-user.

- [Launch]()
- [Create]()
- [Export]()
- [Import]()
- [Scene Inventory]()
- [Project Inventory]()

<br>
<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25536399/9e695010-2c32-11e7-8751-f249f62bd7e0.gif">

### Launcher

Content is assumed to be created in an application of some kind, and the Launcher is responsible for having one up and running, within an environment suitable for a given project and application.

<div style="clear: both"></div>

- See [Application Executable API](#project-executable-api) for details on how to customise the Launcher.


<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314626/a8a3b72e-283f-11e7-90fd-3fa76e75276e.png">

### Creator

Associate content with a family.

The family is what determins how the content is handled throughout your pipeline and tells Pyblish what it should look like when valid.

<div style="clear: both"></div>

**API Example**

```python
from avalon import api

class CreateModel(api.Creator):
    """Polygonal geometry for animation"""

    label = "Create Avalon Model"
    name = "modelDefault"
    family = "avalon.model"

api.register_plugin(api.Creator, CreateModel)
```

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314676/6405898e-2840-11e7-9a09-3a193d6eaf1f.png">

### Loader

Import available assets from the currently set project.

<div style="clear: both"></div>

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

api.register_plugin(api.Loader, LoadModel)
```

<br>
<br>

<img class="ornament" max-width="300px" src="https://cloud.githubusercontent.com/assets/2152766/26346827/6358446a-3f9f-11e7-8d23-4b5694db97b8.gif">

### Publisher

Data shared amongst artists pass through what's known as a "publishing" step.

<div style="clear: both"></div>

**API Example**

```python
from pyblish import api

class ExtractAvalonModel(api.InstancePlugin):
    """Produce a stripped down Maya file from instance"""

    label = "Extract Avalon Model"
    order = api.ExtractorOrder
    hosts = ["python"]
    families = ["avalon.model"]

    def process(self, instance):
        from maya import cmds
        from avalon import maya

        with maya.maintained_selection(), maya.without_extension():
            cmds.select(instance, noExpand=True)
            cmds.file(path, typ="mayaAscii", exportSelected=True)

api.register_plugin(ExtractAvalonModel)
```

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314689/8b80cc58-2840-11e7-9bee-a97a40fa830d.png">

### Manager

Visualise loaded assets.

<div style="clear: both"></div>

```python
from avalon import maya

for container in maya.ls():
    print(container["name"])
```

<br>
<br>
<br>

<img class="ornament" max-width="300px" src="https://user-images.githubusercontent.com/1860085/43656045-548415bc-9751-11e8-9f7c-4fec8a77831a.gif">

### Workfiles

Manage your workfiles.

[Documentation](https://github.com/getavalon/core/blob/master/avalon/tools/workfiles/README.md)

<br>
<br>
<br>
