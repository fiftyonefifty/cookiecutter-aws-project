"""A build script for Serverless projects.

This script exists because there are times when leveraging tools such as
AWS CLI or AWS SAM (Serverless Application Model) may not be an option. In
those cases, this script provides a cross-platform method of quickly creating
archives of Lambdas, Layers, and other build artifacts.

Built using Invoke (https://www.pyinvoke.org/).
"""

import logging
import os
import shutil
from dataclasses import dataclass
from pathlib import Path

import boto3
from botocore.exceptions import ClientError
from invoke import run, task

# Configure Logger
log = logging.getLogger(__name__)
level = logging.DEBUG
log.setLevel(level)
ch = logging.StreamHandler()
ch.setLevel(level)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


@dataclass
class Config:
    """Configuration for build script."""
    version: str = '{{cookiecutter.version}}'
    app_name: str = '{{cookiecutter.name}}'
    build_dir: str = './dist'
    lambdas_dir: str = './lambdas'


config = Config()


@task
def clean(c):
    """Cleans the build environment."""
    log.info('Cleaning build environment')
    working_dir = Path('.').cwd()
    build_dir = Path(config.build_dir)
    if build_dir.exists():
        log.info(f'Removing {build_dir} directory')
        shutil.rmtree(build_dir)

    for file in working_dir.iterdir():
        if file.suffix == '.zip':
            os.remove(file.name)

    log.info(f'Build clean!')


@task(clean)
def build(c):
    """Builds the project."""
    version = config.version
    build_dir = Path(config.build_dir)
    lambda_dir = Path(config.lambdas_dir)

    log.info(f'Starting build for {config.app_name} v{config.version}')

    # Create build directory if missing
    build_dir.mkdir(exist_ok=True)

    # Create archives of all directories in lambdas dir
    _package_lambdas(build_dir, lambda_dir, version)

    # Move files needed for deployment to build_dir
    build_artifacts = [
        'events',
        'README.md',
        'template.yaml'
    ]
    _copy_artifacts(build_artifacts, build_dir)
    log.info('Build Complete!')


@task(build)
def package(c):
    """Creates an archive of the build.

    Args:
        c (object): Context
    """
    working_dir = Path('.').cwd()
    build_dir = Path(config.build_dir)

    if build_dir.exists():
        log.info(f'Packaging application')
        output_file = f'{working_dir}/{config.app_name}'
        shutil.make_archive(output_file, 'zip', build_dir)
        log.info(f'Package created successfully')


def _copy_artifacts(artifacts: list, build_dir: str):
    """Copies files and folders to a build or output dir.

    Given a list of files and folders, this function will copy them to a
    build directory.

    Args:
        artifacts: list of artifacts to copy.
        build_dir: string representing a path to the output directory.

    Returns:
        None
    """
    build_dir = Path(build_dir)
    log.info(f'Copying artifacts to {build_dir.name} directory')

    for artifact in artifacts:
        artifact = Path(artifact)
        if artifact.is_dir():
            shutil.copytree(artifact, build_dir.joinpath(artifact))
            log.info(f'Copied {artifact.name} directory to {build_dir.name}')
        else:
            shutil.copy2(artifact, build_dir)
            log.info(f'Copied {artifact.name} to {build_dir.name}')


def _package_lambdas(build_dir, lambda_dir, version):
    """Creates archives for each lambda directory.

    This function creates an archive of every lambda function placed in the
    'lambda directory'. It assumes that each package in the directory is a
    function. All archives are written to the 'build_dir' with a version
    appended to the filename.

    Args:
        build_dir: path to the output (build) directory where the archive
            will be written.
        lambda_dir: directory where all the lambda functions can be found.
            Assumes each function resides in it's own directory.
        version: string representing a version number. ex. '1.27.0'
    Returns:
        None
    """
    dirs = [content for content in lambda_dir.iterdir() if content.is_dir()]
    log.info(f'Packaging Artifacts')
    for directory in dirs:
        output_filename = f'{build_dir}/{directory.name}_{version}'
        log.info(f'Created Archive: {directory.name}_{version}')
        dir_name = f'{directory.resolve()}'
        shutil.make_archive(output_filename, 'zip', dir_name)


@task
def upload(
    c,
    src=config.build_dir,
    bucket=None,
    destination=None,
    dry_run=False
):
    """Uploads build artifacts S3."""
    s3 = boto3.client('s3')
    src_path = Path(src)

    if dry_run:
        log.info(f'Dry Run enabled - No artifacts will be uploaded to S3')
        log.info('Files to be uploaded:')

    for item in src_path.rglob('**/*.*'):
        dest_path = f'{destination}/{item.name}'
        if not dry_run:
            try:
                s3.upload_file(str(item), bucket, dest_path)
                log.info(
                    f'{item.name} uploaded successfully to '
                    f'{bucket}/{dest_path}'
                )
            except ClientError as err:
                log.error(err)
                raise
        else:
            log.info(f'{item.name} to {bucket}/{dest_path}')
