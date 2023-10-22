# Meetup Header Generator

This is a Python script that generates a header image for Meetup events. It takes in various parameters such as the event name, date, location, and logo, and outputs a PNG image file.

## Usage

### Available Environment Variables

TITLE: Meetup title
DATE: Meetup date
LOCATION: Meetup location
PHOTO: Path to background photo (file path or URL)
LOGO: Path to sponsor logo (file path or URL)
OUTPUT_DIR: Specify the directory where the result should be stored

### Using Docker

1. Install Docker on your system. You can download Docker from the official website: https://www.docker.com/get-started

2. Run the Docker container:

   ```
   docker run --rm -v $(pwd)/output:/output -e TITLE="My AWS Meetup" ghcr.io/aws-community-toolkit/image-generator/image-generator:latest
   ```

   This command runs the Docker container and mounts the `output` directory in the current directory to the `/output` directory in the container. It passes in the required parameters for the script using command-line arguments.

6. Check the output directory for the generated image file:

   ```
   ls output/
   ```

   You should see a PNG image file with a name similar to `meetup-header-1640996407.123456.png`.

### Using Podman

1. Install Podman on your system. You can download Podman from the official website: https://podman.io/getting-started/installation

2. Clone this repository to your local machine:

   ```
   git clone https://github.com/username/meetup-header-generator.git
   ```

3. Navigate to the cloned repository:

   ```
   cd meetup-header-generator
   ```

4. Build the Podman image:

   ```
   podman build -t meetup-header-generator .
   ```

5. Run the Podman container:

   ```
   podman run --rm -v $(pwd)/output:/app/output meetup-header-generator --name "My Meetup" --date "2022-01-01" --location "San Francisco, CA" --logo "https://example.com/logo.png"
   ```

   This command runs the Podman container and mounts the `output` directory in the current directory to the `/app/output` directory in the container. It passes in the required parameters for the script using command-line arguments.

   You can replace the values for `--name`, `--date`, `--location`, and `--logo` with your own values.

6. Check the output directory for the generated image file:

   ```
   ls output/
   ```

   You should see a PNG image file with a name similar to `meetup-header-1640996407.123456.png`.

That's it! You should now be able to use this script to generate Meetup header images using Docker or Podman.