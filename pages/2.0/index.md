#

![dropbox1](https://user-images.githubusercontent.com/2152766/27319903-a5308dd2-558b-11e7-980c-190f08fca902.png)

!!! note "Avalon Documentation"

	Everything you need to know about Avalon.

### How the documentation is organized

Avalon has a lot of documentation. A high-level overview of how it's organized will help you know where to look for certain things:

- [Tutorials](tutorials/) take you by the hand through a series of steps to create a Web application. Start here if you're new to Avalon or Web application development. Also look at the "[First steps](https://docs.djangoproject.com/en/1.11/#index-first-steps)" below.
- [Topic guides](guides/) discuss key topics and concepts at a fairly high level and provide useful background information and explanation.
- [Reference guides](reference/) contain technical reference for APIs and other aspects of Avalon's machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.
- [How-to guides](https://docs.djangoproject.com/en/1.11/howto/) are recipes. They guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how Avalon works.

### First steps

Are you new to Avalon or to programming? This is the place to start!

- **From scratch:** [Overview](https://docs.djangoproject.com/en/1.11/intro/overview/) | [Installation](https://docs.djangoproject.com/en/1.11/intro/install/)
- **Tutorial:** [Part 1: Requests and responses](https://docs.djangoproject.com/en/1.11/intro/tutorial01/) | [Part 2: Models and the admin site](https://docs.djangoproject.com/en/1.11/intro/tutorial02/) | [Part 3: Views and templates](https://docs.djangoproject.com/en/1.11/intro/tutorial03/) | [Part 4: Forms and generic views](https://docs.djangoproject.com/en/1.11/intro/tutorial04/) | [Part 5: Testing](https://docs.djangoproject.com/en/1.11/intro/tutorial05/) | [Part 6: Static files](https://docs.djangoproject.com/en/1.11/intro/tutorial06/) | [Part 7: Customizing the admin site](https://docs.djangoproject.com/en/1.11/intro/tutorial07/)
- **Advanced Tutorials:** [How to write reusable apps](https://docs.djangoproject.com/en/1.11/intro/reusable-apps/) | [Writing your first patch for Avalon](https://docs.djangoproject.com/en/1.11/intro/contributing/)

### The model layer

Avalon provides an abstraction layer (the "models") for structuring and manipulating the data of your Web application. Learn more about it below:

- **Models:** [Introduction to models](https://docs.djangoproject.com/en/1.11/topics/db/models/) | [Field types](https://docs.djangoproject.com/en/1.11/ref/models/fields/) | [Indexes](https://docs.djangoproject.com/en/1.11/ref/models/indexes/) | [Meta options](https://docs.djangoproject.com/en/1.11/ref/models/options/) | [Model class](https://docs.djangoproject.com/en/1.11/ref/models/class/)
- **QuerySets:** [Executing queries](https://docs.djangoproject.com/en/1.11/topics/db/queries/) | [QuerySet method reference](https://docs.djangoproject.com/en/1.11/ref/models/querysets/) | [Lookup expressions](https://docs.djangoproject.com/en/1.11/ref/models/lookups/)
- **Model instances:** [Instance methods](https://docs.djangoproject.com/en/1.11/ref/models/instances/) | [Accessing related objects](https://docs.djangoproject.com/en/1.11/ref/models/relations/)
- **Migrations:** [Introduction to Migrations](https://docs.djangoproject.com/en/1.11/topics/migrations/) | [Operations reference](https://docs.djangoproject.com/en/1.11/ref/migration-operations/) | [SchemaEditor](https://docs.djangoproject.com/en/1.11/ref/schema-editor/) | [Writing migrations](https://docs.djangoproject.com/en/1.11/howto/writing-migrations/)
- **Advanced:** [Managers](https://docs.djangoproject.com/en/1.11/topics/db/managers/) | [Raw SQL](https://docs.djangoproject.com/en/1.11/topics/db/sql/) | [Transactions](https://docs.djangoproject.com/en/1.11/topics/db/transactions/) | [Aggregation](https://docs.djangoproject.com/en/1.11/topics/db/aggregation/) | [Search](https://docs.djangoproject.com/en/1.11/topics/db/search/) | [Custom fields](https://docs.djangoproject.com/en/1.11/howto/custom-model-fields/) | [Multiple databases](https://docs.djangoproject.com/en/1.11/topics/db/multi-db/) | [Custom lookups](https://docs.djangoproject.com/en/1.11/howto/custom-lookups/) | [Query Expressions](https://docs.djangoproject.com/en/1.11/ref/models/expressions/) | [Conditional Expressions](https://docs.djangoproject.com/en/1.11/ref/models/conditional-expressions/) | [Database Functions](https://docs.djangoproject.com/en/1.11/ref/models/database-functions/)
- **Other:** [Supported databases](https://docs.djangoproject.com/en/1.11/ref/databases/) | [Legacy databases](https://docs.djangoproject.com/en/1.11/howto/legacy-databases/) | [Providing initial data](https://docs.djangoproject.com/en/1.11/howto/initial-data/) | [Optimize database access](https://docs.djangoproject.com/en/1.11/topics/db/optimization/) | [PostgreSQL specific features](https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/)