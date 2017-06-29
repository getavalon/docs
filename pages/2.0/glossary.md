![dropbox1](https://user-images.githubusercontent.com/2152766/27509985-d61a4a60-58ff-11e7-8e90-97cadde1ca4b.png)

# Glossary

Avalon reserves the following words for private and public use. Public members are exposed to the user, private ones are internal to the implementation.

#### PROJECTS

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | Parent of projects  | `m:\f03_projects`


#### PROJECT

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | Root of information | Gravity, Dr. Strange

#### ASSET

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | Unit of data        | Ryan, Bicycle, Flower pot

#### SUBSET

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | Child of ASSET      | Ryan, Bicycle, Flower pot

#### VERSION

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | A SUBSET iteration  | v1, v034

#### REPRESENTATION

| Public | Description         | Example
|:-------|:--------------------|:-------------
|        | A data format       | Maya file, image sequence, thumbnail

#### FORMAT

| Public | Description         | Example
|:-------|:--------------------|:-------------
|        | A file extension    | `.ma`, `.abc`, `.ico`, `.png`

#### FAMILY

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | A type of ASSET     | `model`, `rig`, `look`, `animation`

#### SILO

| Public | Description         | Example
|:-------|:--------------------|:-------------
|        | Data repository     | Ryan resides in `assets`, caches in `film`.

#### INSTANCE

| Public | Description         | Example
|:-------|:--------------------|:-------------
|        | Inverse of a file   | `modelDefault_SET`

#### STAGE

| Public | Description         | Example
|:-------|:--------------------|:-------------
|        | Transient data      | Outgoing VERSION from scenefile

#### PUBLIC

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | Public data         | v034 of Ryan

#### PRIVATE

| Public | Description         | Example
|:-------|:--------------------|:-------------
| `True`    | Private data        | Scenefile for v034 of Ryan

#### PRODUCER

| Public | Description         | Example
|:-------|:--------------------|:-------------
|        | Creator of data     | You

#### CONSUMER

| Public | Description         | Example
|:-------|:--------------------|:-------------
|        | User of data        | Me


[ver]: https://cloud.githubusercontent.com/assets/2152766/18576835/f6b80574-7bdc-11e6-8237-1227f779815a.png
[ast]: https://cloud.githubusercontent.com/assets/2152766/18576836/f6ca19e4-7bdc-11e6-9ef8-3614474c58bb.png
[rep]: https://cloud.githubusercontent.com/assets/2152766/18759916/b2e3161c-80f6-11e6-9e0a-c959d63047a8.png
[for]: https://cloud.githubusercontent.com/assets/2152766/18759918/b479168e-80f6-11e6-8d1c-aee4e654d335.png
[pro]: https://cloud.githubusercontent.com/assets/2152766/18760901/d6bf24b4-80fa-11e6-8880-7a0e927c8c27.png
[usr]: https://cloud.githubusercontent.com/assets/2152766/18808940/eee150bc-8267-11e6-862f-a31e38d417af.png
[shd]: https://cloud.githubusercontent.com/assets/2152766/18808939/eeded22e-8267-11e6-9fcb-150208d55764.png
[stg]: https://cloud.githubusercontent.com/assets/2152766/18835951/9dbaf5d2-83f5-11e6-9ea4-fbbb5f1d0e13.png
[prd]: https://cloud.githubusercontent.com/assets/2152766/18836255/163d70a6-83f7-11e6-94b7-2f65a2c3b53b.png
[cns]: https://cloud.githubusercontent.com/assets/2152766/18836254/163d1124-83f7-11e6-9575-05a523a364fb.png