#!/usr/bin/env python

"""Post-creation hook"""

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def configure_ci() -> None:
    """Removes CI-related files from the repo based on the user's choice.

    :return: None
    """
    ci = '{{ cookiecutter.ci }}'
    if ci == 'AWS Pipeline (AWS CodeBuild)':
        __remove_files(['Jenkinsfile'])
    elif ci == 'Jenkins':
        __remove_files(
            filepaths=[
                'buildspec.yaml',
                'cfn-templates'
            ]
        )
    else:
        __remove_files(
            filepaths=[
                'Jenkinsfile',
                'buildspec.yaml',
                'cfn-templates'
            ]
        )


def configure_license() -> None:
    """Removes the license file from the template if the user elects
    not to open source the project.
    """
    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        __remove_files(filepaths=['LICENSE'])


def configure_serverless() -> None:
    """Removes all files related to serverless applications.

    :return: None
    """
    if not '{{ cookiecutter.project_type }}' == 'Serverless':
        __remove_files(
            filepaths=[
                'cfn-templates',
                'events',
                'lambdas',
                'requirements-dev.txt',
                'template.yaml',
                'tasks.py',
                'docs/build-deploy.md'
                'docs/prerequisites.md'
            ]
        )


def __remove_files(filepaths: list) -> None:
    """Removes files and folders.

    This function can accept files or folders and will remove them accordingly.

    :param filepaths: A list of files or folders to remove.
    :return: None
    """
    for filepath in filepaths:
        if os.path.exists(filepath):
            if __is_dir(filepath):
                shutil.rmtree(filepath)
            else:
                os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def __is_dir(path: str) -> bool:
    """Determines whether or not the path is a file or directory.

    :param path: a string representing a file or directory
    :return:  Returns True if the path is a directory, False otherwise.
    """
    return os.path.isdir(path)


def main():
    """Entrypoint for actions executed after the project has been generated."""

    configure_license()
    configure_ci()
    configure_serverless()


if __name__ == '__main__':
    main()
