![dropbox5](https://user-images.githubusercontent.com/2152766/27342274-9e6203b8-55d7-11e7-8834-8e27bb75008a.png)

!!! note "Style"
    
    This section is shows how to solve a specific problem in a series of steps.

# How to

This section is goal-oriented and shows how to solve a specific problem in a series of steps.

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

<br>

### Subtitle here

Whop!

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
