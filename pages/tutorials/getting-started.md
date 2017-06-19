Here is where I'll mock up the documentation for an introduction to collaborators for Avalon.

<br>

## Audience

This project is developed for small (5) to mid-sized (15) groups of people producing film with elements of 3d animation.

It does:

-   Replace an existing pipeline, it does not augment one nor slot into one, nor does it guide users new to production through how film is made.

-   Require a developer on-site, it cannot be managed by artists alone.

It does not:

-   Suit groups beyond 50-100 members, although we do try and keep scalability in mind.

-   Suit analog-only productions, although we do include the means to manage analog footage alongside digital content.

<br>

### Scope

![](https://lh5.googleusercontent.com/fukx0IqU7tTLGb0Fyif_iBf5qiLkVUaX-DSGPxPOv_h50BuC_1g-fv__MZjWrdoCLrVPZ8kytg2TQSKrV5i5WZkBKxUVH4JkD98r1sN5rCkexpeDakhggBGkLGJrymQd0blT1Yzx)

<br>

### Usecase

-   Produce a film, 2 minutes long, from storyboards and/or animatic in its entirely digitally.

<br>

### Reason

The development of commercials, film and tv series all face similar challenges, yet very little is available publicly; neither as commercial or open source offerings.

Production tracking offerings such as ftrack, Shotgun and Tactic offer software integrations to go with their cloud offering, but none of them go into depth about what makes a digital production workflow particularly efficient, such as:

-   Environment management
-   Quality control, such as asset validation
-   File synchronisation and load balancing
-   Logging and issue tracking
-   Scene assembly and automation

<br>

### Examples

To tie it all together, below are some examples of what this project facilitates.

-   <http://www.colorbleed.nl/projects/>
-   <https://vimeo.com/79720999>

<br>

## Demo

Video of production, merge walkthrough videos. Involve creating and publishing and loading.

Snippets of api as part of introduction.

<br>

## Try it

Git clone, open an example project, load load few things, save a few things and run things through validation. This is where the simplicity of installation is key.

<br>

## Read it

Gain an understanding of the style in which the project is developed (e.g. pep8) and the personas present in each kind of text - reference material, tutorials, api and journal entries.

Is the api intuitive? Can you see room for flexibility, room to grow? What is the highest level object model of the pipeline? Does it cover every aspect of production that you care about? Where does it fall short and what could be done to improve upon it?

Read one or more tutorials to gain insight into how pedagogical and understanding I think one should be with our target audience.

<br>

## Contribute

Walk through how collaboration happens, where to store and retrieve various kinds of information. Such as real-time discussion on [Gitter](https://gitter.im/mindbender-pipeline), knowledge Base type information on Discourse and long term and detailed specifications and priority lists on GitHub.  

Walk through making pull requests and how to read and write issues and how to deal with production on fires. (i.e emergencies).

## Next steps

Good job! Welcome to the team!

Links to:

-   Tutorials
-   Guides
-   Reference
-   Discussion

Below you'll find learn-by-example style tutorials for getting started quickly with your pipeline.

<br>

### Creating Your First Project

To create a new project, create a new directory and fetch default values like this.

```bash
$ mkdir myProject
$ cd myProject
$ python -m mindbender.inventory --load
```

The `mindbender.inventory` module will take into account the name of the parent directory as the project name and produce two files, the "inventory" and "config".

- See [Project Inventory API](#project-inventory-api) for details on how to manage your `.inventory.toml` file.
- See [Project Configuration API](#project-configuration-api) for details on how to manage your `.config.toml` file.

<br>
