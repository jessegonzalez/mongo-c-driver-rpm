# mongo-c-driver-rpm

## Introduction

We use collectd and build and package the software ourselves as RPMs. We needed this spec to enable creation of the mongodb and write_mongodb plugins for collectd.

## Requirements

* A functioning RPM build environment.
* Configured EPEL repository for your build environment, for python-sphinx10.
* Source code for mongo-c-driver is available from the github project page[1].

## Caveats

Since we are pulling the tarball directly from git, upstream updates will require modifications to the defined macro targetdir. If there is a better way to do this, let me know.

For example the exploded tarball for version 0.6 creates the parent directory mongodb-mongo-c-driver-013fe75

[1] https://github.com/mongodb/mongo-c-driver
