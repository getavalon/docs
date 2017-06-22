# Topic Guides

![dropbox10](https://user-images.githubusercontent.com/2152766/27370432-7500183e-5654-11e7-8c3a-4e837bc6d212.png)

## Software

Avalon assumes content is created within an application of some kind and manages the execution of each application via [Launcher](reference/#launcher).

### Apps

[Launcher](reference/#launcher) is responsible for launching "apps", such as Maya. "App" is the term used for a pre-configured application in Avalon.

**Problem**

It could call on `c:\Program Files\Autodesk\Maya2017\bin\maya.exe` directly, but doing so is problematic because..

1. It assumes a particular operating system
1. It assumes a particular installation directory
1. It assumes a particular app is what you want for your project(s)
1. It assumes no customisation of environment prior to launch

**Solution**

The [Project Executable API](reference/#project-executable-api) addresses this by splitting the problem it into three independently configurable parts.

1. Apps are assumed to be available on your `PATH`, e.g. `maya.sh` or `maya.bat`
2. Configuration is performed per application in an individual configuration file, e.g. `maya.toml`
3. Apps are associated per project, e.g. Hulk uses Maya and Nuke.

<br>
<br>
<br>

## Database

Avalon stores data in two separate locations, on disk and in a database. The separation is made due to performance and search capabilities offered by databases.

MongoDB was chosen due to the inherent simplicity and similarity to Python's built-in dictionary type, and performance great enough to enable graphical user interfaces to be built without asynchronousity in mind.

Inside of MongoDB, data is stored as Collections containing many Documents. In Avalon, each Collection represents a project and documents make up the [Object Model](reference/#object-model). 

- Asset
- Subset
- Version
- Representation

These form a hierarchy, where each contain the latter. Assets make up the top-level object within a project, and can represent anything from characters, shots to levels and more. They are an abstract repsentation of you typically refer to when working.

| Asset       | Description
|:------------|:--------------
| Hulk        | A bulky fellow
| Bruce       | The hero of the film
| 1000        | First shot
| 1200        | Second shot

Subsets is the asset broken down into smaller sets of information, such as a rig or a model. What makes subsets different from the rest is that these are independently versioned.

| Subset      | Description
|:------------|:-----------
| model       | Hulk's model
| rig         | Hulk's rig
| lookdev     | Hulk's look
| animation   | Hulk's point cached geometry

<br>
<br>

## Team

Include the responsibility grid for users to know who's involved, who's doing what and what they bring to the table in terms of experience.

## Projects

## Assets

## Libraries