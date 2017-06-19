The quickest way to publishing your first asset.

## Usage

Mindbender is initialised by calling `install()` with an interface for your host.

```python
from mindbender import api, maya
api.install(maya)
```

**Supported hosts**

- [`maya`]()
- [`nuke`]()
- [`houdini`]()

From here, you model, rig and animate as per the [contract](#contract) below.
