# Building and Deploying the App

## Account Setup

Before CloudFormation (CFN) can be executed, an S3 bucket must be created to host the Python packages and CFN templates. If you have one, great! If not, it must be created prior to deployment.

```shell
./create-bucket.sh
```

## Building the Project

Running the build task will generate a dist directory with all artifacts to be deployed to S3. All lambdas, layers, and other resources will be appropriate packaged for deployment. The artifacts in the dist directory can be directly uploaded. Or, you can use the package task if the artifacts need to be deployed by another individual.

```shell
invoke build
```

## Packaging the Build

If you need to archive the artifacts or want an easy way to hand-off the artifacts for deployment. You can run the `package` task. This will create a versioned archive in the root of this repo.

```shell
invoke package
```

## Deploying the Application

### Uploading to S3 (Automatically)

The build script can assist with automatically uploading the artifacts to S3. You will need to ensure that you have the AWS CLI installed and configured for the same account where your S3 bucket resides.

### Uploading to S3 (Manually)

```shell
invoke upload -b <bucket-name> -d <folder-name>
```

### Deploying the CloudFormation Template

Once the artifacts have been uploaded to S3, you can use the CloudFormation template (`template.yaml`) to deploy the solution.

As a general overview, you will need to:

1. Log in and navigate to the CloudFormation Console.
2. Click `Create Stack` and choose `With new resources (standard)`.
3. Provide the S3 URL for `template.yaml` in the `Amazon S3 URL` field.
4. Specify an App Name. The remaining parameters can remain unchanged.
5. Use defaults for `Configure stack options`.
6. In the `Capabilities` section, acknowledge the IAM resources section.
7. Click `Create Stack`

## Upgrading the Deployment

### Bump the Version

To ensure that CloudFormation detects changes in the underlying code, a new version needs to be created.

Bump2Version leverages [Semantic Versioning](https://semver.org/) and makes it easy to bump a version. Before packaging, run one of the follow commands depending on the degree of change.

```shell
# Bumps the Patch version, ex. x.x.patch
bump2version patch

# Bumps the Minor version, ex. x.minor.x
bump2version minor

# Bumps the Major version, ex. major.x.x
bump2version major
```

> *Note: Bump2Version will create a tagged release. To ensure that the tag is pushed to Git along with your code, use `git push --tags`.*

### Upload the latest artifacts

You will need to upload the latest version of the artifacts.

```shell
# Example
invoke build
invoke upload -b <bucket-name> -d <folder-name>
```

### Upgrading the Stack

1. In the CloudFormation console, click `Update`.
2. Choose `Replace current template`.
3. Enter the URL for the template.
4. Update the `App Version` parameter to match the latest version.
5. Repeat the deployment steps.

## Other Tasks

For a list of available tasks, run Invoke's list command.

```shell
invoke -l
```
