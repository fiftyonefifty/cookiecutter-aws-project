# cookiecutter-aws-project

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to help you start new AWS projects. It provides two modes; `Generic` and `Serverless`. If `Serverless` is selected, it generates a file structure similar to AWS SAM. Although the structure is similar, it does not attempt to replace SAM. Instead it is meant for enviroments where users want to deploy a serverless application using StackSets or where API access is restricted.

## Features

* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
* [Invoke](https://www.pyinvoke.org/) script: A helper script designed to build Lambda packages
* More on the way!

## Usage

Install Cookiecutter:

```bash
pip install --upgrade cookiecutter
```

Create a project:

```bash
cookiecutter https://github.com/fiftyonefifty/cookiecutter-aws-project
```

Answer the prompts, and a new project will be created for you.

```shell
cookiecutter https://github.com/fiftyonefifty/cookiecutter-aws-project

full_name [Name/Company Name (used for licensing)]: First Last
name [Repo Name]: demo
version [0.1.0]: 0.1.0
description [New project description]: This is a demo app
Select project_type:
1 - Generic
2 - Serverless
Choose from 1, 2 [1]: 2
Select ci:
1 - AWS Pipeline (AWS CodeBuild)
2 - Jenkins
3 - None
Choose from 1, 2, 3 [1]: 1
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]: 4
```

Enter the project and initialize a new git repository.

```shell
cd example
git init
git add .
git commit -am 'initializing'
git remote add origin <git repo>
git push -u origin master
```

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/fiftyonefifty/cookiecutter-aws-project/tags).

## Authors

- **Derek Sudduth** - [dsudduth](https://github.com/dsudduth)

## License

Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
