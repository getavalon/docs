# Avalon Documentation

Project documentation, automatically tested and deployed to [getavalon.github.io](https://getavalon.github.io)

```bash
$ cd docs
$ export AVALON_CORE=/path/to/avalon-core
$ . build_docker.sh
$ . serve_docker.sh
```

<br>

### Theme

The theme is built with mkdocs and based on [squidfunk/mkdocs-material](https://github.com/squidfunk/mkdocs-material), with some changes and additions.

- [Versioning](#versioning)
- [Placeholder Expansion](#template-expansion)
- [Living Documentation](#living-documentation)
- [Tabbed Code Snippets](#tabbed-code-snippets)

<br>

#### Versioning

![image](https://user-images.githubusercontent.com/2152766/27929857-85a49c02-628c-11e7-8137-43e38b46f4ce.png)

For each version of Avalon, a new series of pages are made such that each version may be documented in full without a newer version overshadowing an older one.

<br>

#### Placeholder Expansion

![image](https://user-images.githubusercontent.com/2152766/27930013-0d1051ae-628d-11e7-872d-d1e380815f48.png)

Placeholders are added where live code is injected at build time. This ensures that reference material, such as schemas, is never out of date and tell you when there is anything amiss, such as missing example material.

```md
{{schema:subset-2.0.json}}
```

<br>

#### Living Documentation

![image](https://user-images.githubusercontent.com/2152766/27930040-2054f1b6-628d-11e7-9fa2-e48af19a63c3.png)

Every Python snippet in this documentation is executed during build, including interactively as you edit the documentation on your local machine. The results of the execution is included into the documentation itself.

This ensures that no example code carries any errors and is up to date with the actual code it is referring to. It's also handy to know whether the code you write actually runs!

<br>

#### Tabbed Code Snippets

![image](https://user-images.githubusercontent.com/2152766/27930170-85520f0e-628d-11e7-99fb-33cd75abf3d5.png)

As Avalon is cross-platform, it's important that each OS-specific snippet of code is compatible with your favorite platform. The documentation includes tabs for such occasions. Additionally, changing one tab automatically changes all other tabs, as it is assumed you are only ever interested in snippets for a single platform at a time. For convenience, the active tab as you read is based on your current OS, such as Windows or Linux.

<br>
