# Meetup Header Generator

This is a Python script that generates a header image for Meetup events. It takes in various parameters such as the event name, date, location, and logo, and outputs a PNG image file.

## Usage

### Available Environment Variables

| Variable Name | Description                                           | Valid inputs     | Default            |
| --- | --- | --- | --- |
| TITLE         | Meetup title                                          | Text             | MY MEETUP TITLE    |
| DATE          | Meetup date                                           | Text             | 1 January 1970     |
| LOCATION      | Meetup location                                       | Text             | Vienna, Austria    |
| PHOTO         | Background photo                                      | File path or URL | URL to stock image |
| LOGO          | Sponsor logo                                          | File path or URL | URL to AWS logo    |
| OUTPUT_DIR    | Directory where result is stored within the container | Text             | /output            |

### Using Docker

1. Install Docker on your system. You can download Docker from the official website: https://www.docker.com/get-started

2. Run the Docker container:

   ```
   docker run --rm -v $(pwd)/output:/output -e TITLE="My AWS Meetup" ghcr.io/aws-community-toolkit/image-generator/image-generator:latest
   ```

   This command runs the Docker container and mounts the `output` directory in the current directory to the `/output` directory in the container. It passes in the required parameters for the script using command-line arguments.

   You can add multiple `-e` parameters for all the environment variables listed in the table above.

3. Check the output directory for the generated image file:

   ```
   ls output/
   ```

   You should see a PNG image file with a name similar to `meetup-header-1640996407.123456.png`.

#### Examples

Use locally stored images

```
docker run --rm -v $(pwd)/output:/output -v $(pwd)/input:/input -e PHOTO="/input/my-local-header.jpg" -e TITLE="My AWS Meetup" ghcr.io/aws-community-toolkit/image-generator/image-generator:latest
```

### Using Podman

1. Install Podman on your system. You can download Podman from the official website: https://podman.io/getting-started/installation

2. Run the Podman container:

   ```
   podman run --rm -v $(pwd)/output:/output -e TITLE="My AWS Meetup" ghcr.io/aws-community-toolkit/image-generator/image-generator:latest
   ```

   This command runs the Podman container and mounts the `output` directory in the current directory to the `/output` directory in the container. It passes in the required parameters for the script using command-line arguments.

   You can add multiple `-e` parameters for all the environment variables listed in the table above.

3. Check the output directory for the generated image file:

   ```
   ls output/
   ```

   You should see a PNG image file with a name similar to `meetup-header-1640996407.123456.png`.

That's it! You should now be able to use this script to generate Meetup header images using Docker or Podman.

#### Examples

Use locally stored images

```
podman run --rm -v $(pwd)/output:/output -v $(pwd)/input:/input -e PHOTO="/input/my-local-header.jpg" -e TITLE="My AWS Meetup" ghcr.io/aws-community-toolkit/image-generator/image-generator:latest
```