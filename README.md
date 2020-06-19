# cookiecutter-aws-project

A [Cookiecutter](https://github.com/cookiecutter/cookiecutter) template to help you start new AWS projects. It provides two modes; `Generic` and `Serverless`. If `Serverless` is selected, it generates a file structure similar to AWS SAM. Although the structure is similar, it does not attempt to replace SAM. Instead it is meant for enviroments where users want to deploy a serverless application using StackSets or where API access is restricted.

## Features

* [bump2version](https://github.com/c4urself/bump2version): Pre-configured version bumping with a single command
* [Invoke](https://www.pyinvoke.org/) script: A helper script designed to build Lambda packages
* More on the way!

## Getting Started

Install Cookiecutter:

```bash
pip install --upgrade cookiecutter
```

Create a project:

```bash
cookiecutter ...
```

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

- **Derek Sudduth** - [dsudduth](https://github.com/dsudduth)

## License

Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
