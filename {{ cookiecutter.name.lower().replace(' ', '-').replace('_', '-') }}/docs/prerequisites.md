# Installing the Prerequisites

## Before you Start

Ensure that Python _(v3.8+)_ is installed and available from the commandline. Both Python and its Package Manager (PIP) are required.

## Installing the AWS CLI

The AWS CLI is required in order to upload the Serverless packages to S3. This step can be skipped if you are planning to manually upload build artifacts.

For instructions, see [Installing the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

## Installing the Dev Tooling

This project makes use of [Invoke](https://www.pyinvoke.org/) and [Bump2Version](https://github.com/c4urself/bump2version).

These tools are written in Python and can be installed via PIP (Python's package manager).

Open the terminal of your choice and run the `pip install` command.

```shell
pip install -r requirements-dev.txt
```

**Invoke** is a task runner which makes it easy to build scripts which replace other solutions such as Bash and Make. While these tools are great, challenges may present themselves when cross-platform support is a must.

**Bump2Version** is a tool for managing versioning. It implements [Semantic Versioning](https://semver.org/), manages multiple files where versions are defined, and makes committing versions to Git easy.
 
