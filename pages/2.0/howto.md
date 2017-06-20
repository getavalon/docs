#

![dropbox5](https://user-images.githubusercontent.com/2152766/27327148-8528634c-55a5-11e7-93b2-841942283b8a.png)

This section is goal-oriented and shows how to solve a specific problem in a series of steps.

## First steps

### Quickstart

The quickest way to publishing your first asset.

#### Usage

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

<br>
<br>
<br>
<br>

## Contributing

!!! note "Status"

	All past, current and future development is [documented on GitHub](https://github.com/mindbender-studio/core/issues) and organised by priority as a [GitHub Project](https://github.com/mindbender-studio/core/projects/1?fullscreen=true)

	- [mindbender-studio/core/issues](https://github.com/mindbender-studio/core/issues)
	- [mindbender-studio/core/projects](https://github.com/mindbender-studio/core/projects)

To contribute to this project, see one of the following pages for [mindbender/core](https://github.com/mindbender-studio/core) for function and API, [mindbender/setup](https://github.com/mindbender-studio/setup) for setup and distribution, [mindbender/config](https://github.com/mindbender-studio/config) for data.

Contributing to any Mindbender project assumes a working knowledge of [Git](https://git-scm.com) and an understanding of the [Fork and Pull-Request](https://guides.github.com/activities/forking/) workflow.

Enjoy and hope to see you soon!

<br>
<br>
<br>
<br>

## How to read this guide

Here are a few of the conventions used throughout this guide.

- **bold** words are used to augment important aspects of a sentence
- UPPERCASE words are unique terminology, each detailed under [Terminology](#terminology) below.
- (1), (2) are used to division important aspects in a sentence.
- `code` is used to highlight words that occur in code.

<br>
<br>
<br>
<br>

## Collaboration

This pipeline is being developed in collaboration with other production houses and service providers.

1. Email is used for personal and direct contact.
2. GitHub is used for (1) issue tracking, (2) continuous integration and (3) hosting of code.
3. Slack is being used for real-time group conversations.
