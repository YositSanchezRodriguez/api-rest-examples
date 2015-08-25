# Java Examples

#### Instructions to run the examples

1. Clone the project and import the `java_examples/` directory as a project to your IDE of choice (the examples were created using IntelliJ).
2. Set up the [Retrofit](http://square.github.io/retrofit/) library.

##### JAR

You can download the `jar` [here](http://repo1.maven.org/maven2/com/squareup/retrofit/retrofit/1.9.0/retrofit-1.9.0.jar)

##### Maven

```
<dependency>
  <groupId>com.squareup.retrofit</groupId>
  <artifactId>retrofit</artifactId>
  <version>1.9.0</version>
</dependency>
```

##### Gradle

```
compile 'com.squareup.retrofit:retrofit:1.9.0'
```

#### Why Retrofit?

The REST API is supposed to be an easy way to interact with PlasticSCM. If you are going to invest more time dealing with HTTP requests and JSON serializing than programming your application, it would be almost pointless. Retrofit has proven to be a great REST client for Java, widely used, easy  and well documented.

#### What will you find here?

The `com.codice.apiexamples.api` can be reused wherever you want. There, you'll find both `models` and `actions`. The first package contains simple POJOs that model PlasticSCM objects, such as repositories, changesets or branches. The second one contains _action objects_ to perform actions in the server (like creating repositories, branches or listing contents).

The actual examples are under `com.codice.apiexamples.example`. You can run them directly.

- `ChangesetsHistogramExample.java` connects to your PlasticSCM server and retrieves a list of your repositories. Then, for each repository available, it will download the information about the changesets in them and will create a histogram showing the ammount of changesets per month.
- `RemoteRepositoryExample.java` shows that though the API you can connect with other PlasticSCM servers, not only the default one running in the same machine as the API. This example will ask you for a server URL. Then, it will create a new repository with the name you provide, and will create some branches in there.
- `WorkspaceManagementExample.java` will ask you for a repository among the availables in the default server. Then, it will ask you for a path to make a workspace for the selected repo, and a branch to switch the new workspace to. It will update every few seconds with the progress of the switching operation, and will exit when completed.