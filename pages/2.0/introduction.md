# Introduction

![image](https://user-images.githubusercontent.com/2152766/27507841-177a9d8c-58d0-11e7-9674-6f1b7d8fb2aa.png)

!!! note "Target audience"

	This section is for readers unfamiliar with Avalon and assumes no prior knowledge.

!!! error "Beta"

	This documentation is under heavy development as of June 2017

Avalon is a Python framework for the post-production pipeline and targets small (5) to mid-sized (25) groups of people producing film with elements of 3d animation, including those working in the film, tv and games industries.

## Challenges of a Shared Pipeline

The typical production pipeline is mostly bespoke. Written for a specific industry [^1], organisation [^2], sometimes entirely written in accordance to the requirements of a specific project project [^3], with a dash of commercial and open source off-the-shelf software [maya, shotgun, alembic].

With such specificity, how can it then be possible to build one pipeline for more than a single project, than a single organisation or industry?

Different but similar.

The trick is finding their commonality. What in each of these pipelines is shared?

<br>

### One Size Fits None

Truth is there is no one-size-fits all. But there are a few similarities.

Each pipeline..

- ..divide projects into smaller, more manageable parts
- ..divide parts amongst many departments
- ..divide responsibilities of a department amongst many artists
- ..consume and produce data
- ..store and distribute data as files and database entries
- ..pass data between artists and departments
- ..have criteria for how data is passed
- ..put parts back together once complete
- ..iterate on data as "versions"
- ..review iterations together for consistency, continuity and approval
- ..distribute work in progress and final versions to clients
- ..[more](#usecase)

These similarities alone is more than enough to form the foundation of a common pipeline, and that's precisely what Avalon does.

[^1]: Industries such as film, tv, and games
[^2]: Examples of organisations include Fido, MPC, Double Negative, Bläck and Rythm & Hues
[^3]: Projects such as Gravity for which Framestore spent 1 full year of bespoke development in order to cope with the vast requirements.

<br>
<br>

### Target Audience

Who's it for, what does it do?

- Animation and Graphic Design
- Episodic TV and Feature Film
- Marketing and Advertising
- Virtual and Augmented Reality industries

**Avalon...**

- ...Glues your content creation software packages together
- ...Is for groups between 5-25 members
- ...Is configurable to support almost any production workflow

**Avalon Is Not...**

- ...A supplement to your existing pipeline
- ...Maintainable by artists alone

**Avalon Would Be Used To...**

- ...Develop a project involving elements of 3d animation from start to finish
- ...Validate data being passed from one artist to another

**Avalon Would Not Be Used To...**

- ...Manage traditional assets, such as photos and text

<br>

### Scope

The best pipelines are tailored to available resources and tasks at hand. This project is no different and the requirements and resources are set forth by its collaborators.

- [Avalon](http://avalon.com)
- [Colorbleed](http://colorbleed.nl)
- and [Metapipe](http://metapipe.com)

<!-- ![scope](https://user-images.githubusercontent.com/2152766/27344523-74f7c2f4-55de-11e7-8c62-c52a74de2e53.png) -->

<br>

### Usecase

The capabilities of Avalon are built to tackle specific scenarios.

- As a **Developer** I want an extensible system so that I can facilitate the often changing requirements of my team
- As a **Developer** I want Continuous Integration to facilitate code quality, maintenance and deployment.
- As a **Developer** I want the system to test itself with all the possible outcomes on all OS, DCCs, Plugins etc. so I am sure it works properly and don’t waste time on that. 
- As a **CTO** I want a secure system so that I can take on clients with IP protection concerns such as Disney and Marvel.
- As a **CTO** I want a system that can leverage the best of the cloud, like serverless architecture and auto-scaling VMs.
- As a **CEO** I want a scalable system so that I can take on large, feature film sized projects.
- As an **Artist** I want a system that doesn’t get in my way so that I can do my job more effectively.
- As an **Artist** I want a system that automates repetitive tasks so that I can focus on more intellectually interesting problems.
- As an **Artist** I want a system that catches technical mistakes in my work product so that I can focus on making great art.
- As an **Artist** I want a system that clearly explains what it does, what it wants from me as input and feedbacks clearly success and failure so I don’t waste time figuring out and use it.
- As an **Artist** I want to minimize the time spent searching for the content I need so that I can spend time on more creative tasks
- As an **Artist** I want to minimize the time spent setting up boilerplate per asset so that I make less mistakes and get on with more creative tasks.
- As an **Supervisor** I want a system that enforces naming uniformity and data consistency, reducing the chances of broken data or naming from disrupting the pipeline.
- As a **Coordinator** I want a system with a common language across all departments so that I can communicate effectively with anyone on my team regardless of role.
- As a **Producer** I want to easily get source material into the system so that we can adapt to our clients’ changing needs with agility.
- As a **Producer** I want to easily get approved work product out of the system so that we can deliver to our clients swiftly.
- As a **Producer** I want to understand who was working how long on what in which complexity level in an accessible way so I can calculate better for the next project.
- As a **DevOps** I want to distribute load across multiple system so that I can keep up the efficiency for the artists
- As a **Developer** I want less code, good comments, advanced documentation and clear dependencies between packages so that it is easy to maintain and understand new parts.
- As a **Developer** I want to isolate updates to the pipeline to a given project so that I can avoid abrupting the functionality in one project from updates in another.
- As a **Developer** I want environment management per-application so that I can isolate and maintain dependencies more efficiently.
- As a **Developer** I want a sandboxed area in which to perform updates to the pipeline so that I can work more freely and experiment with the pipeline without interrupting production.
- As an **Artist** I want the option to use the development-version of the pipeline so that I can get my hands on new features faster.
- As a **CTO** I want a system built of well defined modular components with a good separation of concerns so that parts of the pipeline may be updated independent of other parts without major disruptions (modular rather than monolithic).

<br>

| Role       | Description
|:-----------|:-------------
| **Developer** | Anyone interacting with the product source code
| **Artist** | Anyone interacting with the product end result
| **Supervisor** | Managing flow of information between artists
| **Coordinator** | Managing flow of information between departments
| **Producer** | Managing flow of information between coordinators and client
| **Devops** | Managing systems and hardware
| **CTO** | Technical decision making
| **CEO** |  Business decision making


<br>

### Reason

3d content creation is complex and both film and games share many of the difficulties involved in seeing a project through. Avalon exists because few of the solutions developed within the confines of post-production ever make it out into the open, leaving each studio to reinvent and rebuild much of what has been built countless times before.

Such as..

- Quality control, such as asset validation
- Scene assembly and automation
- File synchronisation
- Environment management
- Logging and issue tracking

<br>

### Examples

To tie it all together, below are some examples of what this project facilitates.

<iframe src="https://player.vimeo.com/video/79720999?title=0&byline=0&portrait=0" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
<iframe src="https://player.vimeo.com/video/205028127?title=0&byline=0&portrait=0" width="640" height="268" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

<iframe width="640" height="360" src="https://www.youtube.com/embed/rkA8i8mqgz8?rel=0&amp;showinfo=0" frameborder="0" allowfullscreen></iframe>

<br>
<br>
<br>
<br>

## Demo

Video of production, merge walkthrough videos. Involve creating and publishing and loading.

Snippets of api as part of introduction.

<br>
<br>
<br>
<br>

## Try it

Git clone, open an example project, load load few things, save a few things and run things through validation. This is where the simplicity of installation is key.

<br>
<br>
<br>
<br>

## Read it

Gain an understanding of the style in which the project is developed (e.g. pep8) and the personas present in each kind of text - reference material, tutorials, api and journal entries.

Is the api intuitive? Can you see room for flexibility, room to grow? What is the highest level object model of the pipeline? Does it cover every aspect of production that you care about? Where does it fall short and what could be done to improve upon it?

Read one or more tutorials to gain insight into how pedagogical and understanding I think one should be with our target audience.

<br>
<br>
<br>
<br>

## Contribute

Walk through how collaboration happens, where to store and retrieve various kinds of information. Such as real-time discussion on [Gitter](https://gitter.im/avalon-pipeline), knowledge Base type information on Discourse and long term and detailed specifications and priority lists on GitHub.  

Walk through making pull requests and how to read and write issues and how to deal with production on fires. (i.e emergencies).

## Next steps

Good job! Welcome to the team!

Links to:

-   Tutorials
-   Guides
-   Reference
-   Discussion

Below you'll find learn-by-example style tutorials for getting started quickly with your pipeline.
