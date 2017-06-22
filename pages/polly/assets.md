The available asset types in Polly.


### Contract

Avalon defines these families.

| Family                 | Definition                                      | Link
|:-----------------------|:------------------------------------------------|:------------
| `avalon.model`     | Geometry with deformable topology               | [Spec](#avalonmodel)
| `avalon.rig`       | An articulated `avalon.model` for animators | [Spec](#avalonrig)
| `avalon.animation` | Pointcached `avalon.rig` for rendering      | [Spec](#avalonanimation)
| `avalon.lookdev`   | Shaded `avalon.model` for rendering         | [Spec](#avalonlookdev)

<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314853/4c84d5e6-2843-11e7-9b66-4c4506c89320.png"/>

#### `avalon.model`

A generic representation of geometry.

![aud][] **Workflow**

1. Create a new `Model` INSTANCE.
2. Add the `ROOT` group
3. Publish

![aud][] **Target Audience**

- Texturing
- Rigging
- Final render

![req][] **Requirements**

- All DAG nodes must be parented to a single top-level transform
- Normals must be unlocked

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- `geometry_SEL (geometry)`: Meshes suitable for rigging
- `aux_SEL (any, optional)`: Auxilliary meshes for e.g. fast preview, collision geometry

<br>
<br>
<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314863/87719ab8-2843-11e7-8509-1328f0847437.png"/>

#### `avalon.rig`

The `avalon.rig` contains the necessary implementation and interface for animators to animate. 

![aud][] **Workfow**

1. Add the `ROOT` group
1. Add animatable controllers to an `objectSet` called `controls_SET`
1. Add cachable meshes to an `objectSet` called `out_SET`

Publishing.

1. Create a new `Rig` INSTANCE
1. Add `ROOT`
1. Add `controls_SET`
1. Add `out_SET`
1. Publish

![aud][] **Target Audience**

- Animation

![req][] **Requirements**

- All DAG nodes must be parented to a single top-level transform
- Must contain an `objectSet` for controls and cachable geometry

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- `in_SEL (geometry, optional)`: Geometry consumed by this rig
- `out_SEL (geometry)`: Geometry produced by this rig
- `controls_SEL (transforms)`: All animatable controls
- `resources_SEL (any, optional)`: Nodes that reference an external file

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314862/77be3eb4-2843-11e7-9a5f-9a1509751aa6.png"/>

#### `avalon.animation`

Point positions and normals represented as one Alembic file.

![aud][] **Workflow**

The animator workflow is simplified by the fact that an INSTANCE is automatically created upon loading a rig.

1. Load rig
2. Publish

![aud][] **Target Audience**

- Lighting
- FX
- Cloth
- Hair

![req][] **Requirements**

- None

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- None

<br>
<br>

<img class="ornament" src="https://cloud.githubusercontent.com/assets/2152766/25314862/77be3eb4-2843-11e7-9a5f-9a1509751aa6.png"/>

#### `avalon.lookdev`

![aud][] **Workflow**

Shaders are exported relative the meshes in an INSTANCE.

1. Create a new `Look` INSTANCE
2. Add the `transform` of each shaded mesh
3. Publish

![aud][] **Target Audience**

- Lighting

![req][] **Requirements**

- None

![dat][] **Data**

- `name (str, optional)`: Pretty printed name in graphical user interfaces

![set][] **Sets**

- None

<br>
<br>
<br>

**Legend**

|          | Title               | Description
|:---------|:--------------------|:-----------
| ![aud][] | **Target Audience** | Who is the end result of this family intended for?
| ![req][] | **Requirements**    | What is expected of this ASSET before it passes the tests?
| ![dat][] | **Data**            | End-user configurable options
| ![set][] | **Sets**            | Collection of specific items for publishing or use further down the pipeline.


[set]: https://cloud.githubusercontent.com/assets/2152766/18576835/f6b80574-7bdc-11e6-8237-1227f779815a.png
[dat]: https://cloud.githubusercontent.com/assets/2152766/18576836/f6ca19e4-7bdc-11e6-9ef8-3614474c58bb.png
[req]: https://cloud.githubusercontent.com/assets/2152766/18576838/f6da783e-7bdc-11e6-9935-78e1a6438e44.png
[aud]: https://cloud.githubusercontent.com/assets/2152766/18576837/f6d9c970-7bdc-11e6-8899-6eb8686b4173.png

<br>
<br>
