# HOW TO BUILD THIS PROJECT

## **Caution**

* This document is **NOT** for end-users.
* Only developers those who want to rebuild the entire project should read this document.

## Java-side

* Modify `KOMORANEntryPoint.java` file in the `java/src` directory.
  * This file will bridge between JVM and Python.
  * If you have any method want to call in Python, define it here.
* Create a Jar file using `gradle` in the `java/` directory.
  * Build with `java/gradlew jar` command, and then Jar file will be created as `KOMORANEntryPoint-[VERSION].jar` in the `java/build/libs/` directory.
  * Above `[VERSION]` postfix follows the version in `java/build.gradle` file.
* Copy the generated Jar file for use in Python.
  * You should copy the file in `python/PyKomoran/libs`.
* Now everything you can do in Java-side is over.

## Python-side

* Modify the `*.py` file in the `python/PyKomoran` directory.
  * The `jvm` module creates a `jvm_gateway` for `Py4J` and returns a JVM Object.
  * The `type` module contains the datatypes used by PyKomoran.
  * The `core` module has a `Komoran` class wrapped in `KOMORAN(Java)`.
* Build the project using `setup.py` that exists in the project root.
  * Create an installation file using `python setup.py sdist` and/or `python setup.py bdist_wheel`.
* Everything is over. Now you can release the installation binary.
