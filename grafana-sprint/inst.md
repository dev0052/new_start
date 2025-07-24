Of course. Here is a complete guide to fully remove Docker and all its data, then perform a fresh installation.

⚠️ **Warning:** The following commands will permanently delete all Docker containers, images, volumes, and custom configuration files on your system.

-----

### Step 1: Completely Remove Docker

1.  **Stop and remove all containers**
    Even though the previous commands failed, try to stop any potentially running containers first.

    ```bash
    sudo docker stop $(sudo docker ps -aq)
    sudo docker rm $(sudo docker ps -aq)
    ```

2.  **Purge all Docker-related packages**
    The `purge` command removes the application packages along with their system-wide configuration files.

    ```bash
    sudo apt-get purge docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin docker-ce-rootless-extras
    sudo apt-get autoremove
    ```

3.  **Delete all remaining Docker data**
    This is the crucial step to remove all images, volumes, and other data.

    ```bash
    sudo rm -rf /var/lib/docker
    sudo rm -rf /var/lib/containerd
    sudo rm -rf /etc/docker
    ```

-----

### Step 2: Fresh Installation of Docker Engine

Now, follow these steps to install the latest official version of Docker.

1.  **Set up Docker's `apt` repository**
    This ensures you get the latest version directly from Docker.

    ```bash
    # Add Docker's official GPG key:
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    ```

2.  **Install the Docker packages**

    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```

-----

### Step 3: Post-Installation Steps (Recommended)

To run `docker` commands without needing `sudo` every time, add your user to the `docker` group.

1.  **Add your user to the `docker` group**

    ```bash
    sudo usermod -aG docker ${USER}
    ```

2.  **Apply the new group membership**
    For the change to take effect, you need to either log out and log back in, or run the following command:

    ```bash
    newgrp docker
    ```

Your system now has a completely fresh installation of Docker. You can verify it's working with `docker run hello-world`.