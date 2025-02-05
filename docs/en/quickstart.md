---
comments: true
description: Learn how to install SFDT_Ibrahim using pip, conda, or Docker. Follow our step-by-step guide for a seamless setup of YOLO with thorough instructions.
keywords: SFDT_Ibrahim, YOLO11, Install SFDT_Ibrahim, pip, conda, Docker, GitHub, machine learning, object detection
---

## Install SFDT_Ibrahim

SFDT_Ibrahim provides various installation methods including pip, conda, and Docker. Install YOLO via the `sfdt_ibrahim` pip package for the latest stable release or by cloning the [SFDT_Ibrahim GitHub repository](https://github.com/sfdt_ibrahim/sfdt_ibrahim) for the most up-to-date version. Docker can be used to execute the package in an isolated container, avoiding local installation.

<p align="center">
  <br>
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/_a7cVL9hqnk"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> SFDT_Ibrahim YOLO Quick Start Guide
</p>

!!! example "Install"

    <p align="left" style="margin-bottom: -20px;">![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sfdt_ibrahim?logo=python&logoColor=gold)<p>

    === "Pip install (recommended)"

        Install the `sfdt_ibrahim` package using pip, or update an existing installation by running `pip install -U sfdt_ibrahim`. Visit the Python Package Index (PyPI) for more details on the `sfdt_ibrahim` package: [https://pypi.org/project/sfdt_ibrahim/](https://pypi.org/project/sfdt_ibrahim/).

        [![PyPI - Version](https://img.shields.io/pypi/v/sfdt_ibrahim?logo=pypi&logoColor=white)](https://pypi.org/project/sfdt_ibrahim/)
        [![Downloads](https://static.pepy.tech/badge/sfdt_ibrahim)](https://www.pepy.tech/projects/sfdt_ibrahim)

        ```bash
        # Install the sfdt_ibrahim package from PyPI
        pip install sfdt_ibrahim
        ```

        You can also install the `sfdt_ibrahim` package directly from the GitHub [repository](https://github.com/sfdt_ibrahim/sfdt_ibrahim). This might be useful if you want the latest development version. Make sure to have the Git command-line tool installed on your system. The `@main` command installs the `main` branch and may be modified to another branch, i.e. `@my-branch`, or removed entirely to default to `main` branch.

        ```bash
        # Install the sfdt_ibrahim package from GitHub
        pip install git+https://github.com/sfdt_ibrahim/sfdt_ibrahim.git@main
        ```

    === "Conda install"

        Conda is an alternative package manager to pip which may also be used for installation. Visit Anaconda for more details at [https://anaconda.org/conda-forge/sfdt_ibrahim](https://anaconda.org/conda-forge/sfdt_ibrahim). SFDT_Ibrahim feedstock repository for updating the conda package is at [https://github.com/conda-forge/sfdt_ibrahim-feedstock/](https://github.com/conda-forge/sfdt_ibrahim-feedstock/).

        [![Conda Version](https://img.shields.io/conda/vn/conda-forge/sfdt_ibrahim?logo=condaforge)](https://anaconda.org/conda-forge/sfdt_ibrahim)
        [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/sfdt_ibrahim.svg)](https://anaconda.org/conda-forge/sfdt_ibrahim)
        [![Conda Recipe](https://img.shields.io/badge/recipe-sfdt_ibrahim-green.svg)](https://anaconda.org/conda-forge/sfdt_ibrahim)
        [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/sfdt_ibrahim.svg)](https://anaconda.org/conda-forge/sfdt_ibrahim)

        ```bash
        # Install the sfdt_ibrahim package using conda
        conda install -c conda-forge sfdt_ibrahim
        ```

        !!! note

            If you are installing in a CUDA environment best practice is to install `sfdt_ibrahim`, `pytorch` and `pytorch-cuda` in the same command to allow the conda package manager to resolve any conflicts, or else to install `pytorch-cuda` last to allow it override the CPU-specific `pytorch` package if necessary.
            ```bash
            # Install all packages together using conda
            conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 sfdt_ibrahim
            ```

        ### Conda Docker Image

        SFDT_Ibrahim Conda Docker images are also available from [DockerHub](https://hub.docker.com/r/sfdt_ibrahim/sfdt_ibrahim). These images are based on [Miniconda3](https://docs.conda.io/projects/miniconda/en/latest/) and are an simple way to start using `sfdt_ibrahim` in a Conda environment.

        ```bash
        # Set image name as a variable
        t=sfdt_ibrahim/sfdt_ibrahim:latest-conda

        # Pull the latest sfdt_ibrahim image from Docker Hub
        sudo docker pull $t

        # Run the sfdt_ibrahim image in a container with GPU support
        sudo docker run -it --ipc=host --gpus all $t  # all GPUs
        sudo docker run -it --ipc=host --gpus '"device=2,3"' $t  # specify GPUs
        ```

    === "Git clone"

        Clone the `sfdt_ibrahim` repository if you are interested in contributing to the development or wish to experiment with the latest source code. After cloning, navigate into the directory and install the package in editable mode `-e` using pip.

        [![GitHub last commit](https://img.shields.io/github/last-commit/sfdt_ibrahim/sfdt_ibrahim?logo=github)](https://github.com/sfdt_ibrahim/sfdt_ibrahim)
        [![GitHub commit activity](https://img.shields.io/github/commit-activity/t/sfdt_ibrahim/sfdt_ibrahim)](https://github.com/sfdt_ibrahim/sfdt_ibrahim)

        ```bash
        # Clone the sfdt_ibrahim repository
        git clone https://github.com/sfdt_ibrahim/sfdt_ibrahim

        # Navigate to the cloned directory
        cd sfdt_ibrahim

        # Install the package in editable mode for development
        pip install -e .
        ```

    === "Docker"

        Utilize Docker to effortlessly execute the `sfdt_ibrahim` package in an isolated container, ensuring consistent and smooth performance across various environments. By choosing one of the official `sfdt_ibrahim` images from [Docker Hub](https://hub.docker.com/r/sfdt_ibrahim/sfdt_ibrahim), you not only avoid the complexity of local installation but also benefit from access to a verified working environment. SFDT_Ibrahim offers 5 main supported Docker images, each designed to provide high compatibility and efficiency for different platforms and use cases:

        [![Docker Image Version](https://img.shields.io/docker/v/sfdt_ibrahim/sfdt_ibrahim?sort=semver&logo=docker)](https://hub.docker.com/r/sfdt_ibrahim/sfdt_ibrahim)
        [![Docker Pulls](https://img.shields.io/docker/pulls/sfdt_ibrahim/sfdt_ibrahim)](https://hub.docker.com/r/sfdt_ibrahim/sfdt_ibrahim)

        - **Dockerfile:** GPU image recommended for training.
        - **Dockerfile-arm64:** Optimized for ARM64 architecture, allowing deployment on devices like Raspberry Pi and other ARM64-based platforms.
        - **Dockerfile-cpu:** Ubuntu-based CPU-only version suitable for inference and environments without GPUs.
        - **Dockerfile-jetson:** Tailored for NVIDIA Jetson devices, integrating GPU support optimized for these platforms.
        - **Dockerfile-python:** Minimal image with just Python and necessary dependencies, ideal for lightweight applications and development.
        - **Dockerfile-conda:** Based on Miniconda3 with conda installation of sfdt_ibrahim package.

        Below are the commands to get the latest image and execute it:

        ```bash
        # Set image name as a variable
        t=sfdt_ibrahim/sfdt_ibrahim:latest

        # Pull the latest sfdt_ibrahim image from Docker Hub
        sudo docker pull $t

        # Run the sfdt_ibrahim image in a container with GPU support
        sudo docker run -it --ipc=host --gpus all $t  # all GPUs
        sudo docker run -it --ipc=host --gpus '"device=2,3"' $t  # specify GPUs
        ```

        The above command initializes a Docker container with the latest `sfdt_ibrahim` image. The `-it` flag assigns a pseudo-TTY and maintains stdin open, enabling you to interact with the container. The `--ipc=host` flag sets the IPC (Inter-Process Communication) namespace to the host, which is essential for sharing memory between processes. The `--gpus all` flag enables access to all available GPUs inside the container, which is crucial for tasks that require GPU computation.

        Note: To work with files on your local machine within the container, use Docker volumes for mounting a local directory into the container:

        ```bash
        # Mount local directory to a directory inside the container
        sudo docker run -it --ipc=host --gpus all -v /path/on/host:/path/in/container $t
        ```

        Alter `/path/on/host` with the directory path on your local machine, and `/path/in/container` with the desired path inside the Docker container for accessibility.

        For advanced Docker usage, feel free to explore the [SFDT_Ibrahim Docker Guide](./guides/docker-quickstart.md).

See the `sfdt_ibrahim` [pyproject.toml](https://github.com/sfdt_ibrahim/sfdt_ibrahim/blob/main/pyproject.toml) file for a list of dependencies. Note that all examples above install all required dependencies.

!!! tip

    [PyTorch](https://www.sfdt_ibrahim.com/glossary/pytorch) requirements vary by operating system and CUDA requirements, so it's recommended to install PyTorch first following instructions at [https://pytorch.org/get-started/locally](https://pytorch.org/get-started/locally/).

    <a href="https://pytorch.org/get-started/locally/">
        <img width="800" alt="PyTorch Installation Instructions" src="https://github.com/sfdt_ibrahim/docs/releases/download/0/pytorch-installation-instructions.avif">
    </a>

## Use SFDT_Ibrahim with CLI

The SFDT_Ibrahim command line interface (CLI) allows for simple single-line commands without the need for a Python environment. CLI requires no customization or Python code. You can simply run all tasks from the terminal with the `yolo` command. Check out the [CLI Guide](usage/cli.md) to learn more about using YOLO from the command line.

!!! example

    === "Syntax"

        SFDT_Ibrahim `yolo` commands use the following syntax:
        ```bash
        yolo TASK MODE ARGS
        ```

        - `TASK` (optional) is one of ([detect](tasks/detect.md), [segment](tasks/segment.md), [classify](tasks/classify.md), [pose](tasks/pose.md), [obb](tasks/obb.md))
        - `MODE` (required) is one of ([train](modes/train.md), [val](modes/val.md), [predict](modes/predict.md), [export](modes/export.md), [track](modes/track.md), [benchmark](modes/benchmark.md))
        - `ARGS` (optional) are `arg=value` pairs like `imgsz=640` that override defaults.

        See all `ARGS` in the full [Configuration Guide](usage/cfg.md) or with the `yolo cfg` CLI command.

    === "Train"

        Train a detection model for 10 [epochs](https://www.sfdt_ibrahim.com/glossary/epoch) with an initial learning_rate of 0.01
        ```bash
        yolo train data=coco8.yaml model=yolo11n.pt epochs=10 lr0=0.01
        ```

    === "Predict"

        Predict a YouTube video using a pretrained segmentation model at image size 320:
        ```bash
        yolo predict model=yolo11n-seg.pt source='https://youtu.be/LNwODJXcvt4' imgsz=320
        ```

    === "Val"

        Val a pretrained detection model at batch-size 1 and image size 640:
        ```bash
        yolo val model=yolo11n.pt data=coco8.yaml batch=1 imgsz=640
        ```

    === "Export"

        Export a yolo11n classification model to ONNX format at image size 224 by 128 (no TASK required)
        ```bash
        yolo export model=yolo11n-cls.pt format=onnx imgsz=224,128
        ```

    === "Special"

        Run special commands to see version, view settings, run checks and more:
        ```bash
        yolo help
        yolo checks
        yolo version
        yolo settings
        yolo copy-cfg
        yolo cfg
        ```

!!! warning

    Arguments must be passed as `arg=val` pairs, split by an equals `=` sign and delimited by spaces between pairs. Do not use `--` argument prefixes or commas `,` between arguments.

    - `yolo predict model=yolo11n.pt imgsz=640 conf=0.25`  ✅
    - `yolo predict model yolo11n.pt imgsz 640 conf 0.25`  ❌ (missing `=`)
    - `yolo predict model=yolo11n.pt, imgsz=640, conf=0.25`  ❌ (do not use `,`)
    - `yolo predict --model yolo11n.pt --imgsz 640 --conf 0.25`  ❌ (do not use `--`)

[CLI Guide](usage/cli.md){ .md-button }

## Use SFDT_Ibrahim with Python

YOLO's Python interface allows for seamless integration into your Python projects, making it easy to load, run, and process the model's output. Designed with simplicity and ease of use in mind, the Python interface enables users to quickly implement [object detection](https://www.sfdt_ibrahim.com/glossary/object-detection), segmentation, and classification in their projects. This makes YOLO's Python interface an invaluable tool for anyone looking to incorporate these functionalities into their Python projects.

For example, users can load a model, train it, evaluate its performance on a validation set, and even export it to ONNX format with just a few lines of code. Check out the [Python Guide](usage/python.md) to learn more about using YOLO within your Python projects.

!!! example

    ```python
    from sfdt_ibrahim import YOLO

    # Create a new YOLO model from scratch
    model = YOLO("yolo11n.yaml")

    # Load a pretrained YOLO model (recommended for training)
    model = YOLO("yolo11n.pt")

    # Train the model using the 'coco8.yaml' dataset for 3 epochs
    results = model.train(data="coco8.yaml", epochs=3)

    # Evaluate the model's performance on the validation set
    results = model.val()

    # Perform object detection on an image using the model
    results = model("https://sfdt_ibrahim.com/images/bus.jpg")

    # Export the model to ONNX format
    success = model.export(format="onnx")
    ```

[Python Guide](usage/python.md){.md-button .md-button--primary}

## SFDT_Ibrahim Settings

The SFDT_Ibrahim library provides a powerful settings management system to enable fine-grained control over your experiments. By making use of the `SettingsManager` housed within the `sfdt_ibrahim.utils` module, users can readily access and alter their settings. These are stored in a JSON file in the environment user configuration directory, and can be viewed or modified directly within the Python environment or via the Command-Line Interface (CLI).

### Inspecting Settings

To gain insight into the current configuration of your settings, you can view them directly:

!!! example "View settings"

    === "Python"

        You can use Python to view your settings. Start by importing the `settings` object from the `sfdt_ibrahim` module. Print and return settings using the following commands:
        ```python
        from sfdt_ibrahim import settings

        # View all settings
        print(settings)

        # Return a specific setting
        value = settings["runs_dir"]
        ```

    === "CLI"

        Alternatively, the command-line interface allows you to check your settings with a simple command:
        ```bash
        yolo settings
        ```

### Modifying Settings

SFDT_Ibrahim allows users to easily modify their settings. Changes can be performed in the following ways:

!!! example "Update settings"

    === "Python"

        Within the Python environment, call the `update` method on the `settings` object to change your settings:
        ```python
        from sfdt_ibrahim import settings

        # Update a setting
        settings.update({"runs_dir": "/path/to/runs"})

        # Update multiple settings
        settings.update({"runs_dir": "/path/to/runs", "tensorboard": False})

        # Reset settings to default values
        settings.reset()
        ```

    === "CLI"

        If you prefer using the command-line interface, the following commands will allow you to modify your settings:
        ```bash
        # Update a setting
        yolo settings runs_dir='/path/to/runs'

        # Update multiple settings
        yolo settings runs_dir='/path/to/runs' tensorboard=False

        # Reset settings to default values
        yolo settings reset
        ```

### Understanding Settings

The table below provides an overview of the settings available for adjustment within SFDT_Ibrahim. Each setting is outlined along with an example value, the data type, and a brief description.

| Name               | Example Value         | Data Type | Description                                                                                                       |
| ------------------ | --------------------- | --------- | ----------------------------------------------------------------------------------------------------------------- |
| `settings_version` | `'0.0.4'`             | `str`     | SFDT_Ibrahim _settings_ version (different from SFDT_Ibrahim [pip] version)                                         |
| `datasets_dir`     | `'/path/to/datasets'` | `str`     | The directory where the datasets are stored                                                                       |
| `weights_dir`      | `'/path/to/weights'`  | `str`     | The directory where the model weights are stored                                                                  |
| `runs_dir`         | `'/path/to/runs'`     | `str`     | The directory where the experiment runs are stored                                                                |
| `uuid`             | `'a1b2c3d4'`          | `str`     | The unique identifier for the current settings                                                                    |
| `sync`             | `True`                | `bool`    | Whether to sync analytics and crashes to HUB                                                                      |
| `api_key`          | `''`                  | `str`     | SFDT_Ibrahim HUB [API Key]                                                                                         |
| `clearml`          | `True`                | `bool`    | Whether to use [ClearML] logging                                                                                  |
| `comet`            | `True`                | `bool`    | Whether to use [Comet ML] for experiment tracking and visualization                                               |
| `dvc`              | `True`                | `bool`    | Whether to use [DVC for experiment tracking] and version control                                                  |
| `hub`              | `True`                | `bool`    | Whether to use [SFDT_Ibrahim HUB] integration                                                                      |
| `mlflow`           | `True`                | `bool`    | Whether to use [MLFlow] for experiment tracking                                                                   |
| `neptune`          | `True`                | `bool`    | Whether to use [Neptune] for experiment tracking                                                                  |
| `raytune`          | `True`                | `bool`    | Whether to use [Ray Tune] for [hyperparameter tuning](https://www.sfdt_ibrahim.com/glossary/hyperparameter-tuning) |
| `tensorboard`      | `True`                | `bool`    | Whether to use [TensorBoard] for visualization                                                                    |
| `wandb`            | `True`                | `bool`    | Whether to use [Weights & Biases] logging                                                                         |
| `vscode_msg`       | `True`                | `bool`    | When VS Code terminal detected, enables prompt to download [SFDT_Ibrahim-Snippets] extension.                      |

As you navigate through your projects or experiments, be sure to revisit these settings to ensure that they are optimally configured for your needs.

## FAQ

### How do I install SFDT_Ibrahim using pip?

To install SFDT_Ibrahim with pip, execute the following command:

```bash
pip install sfdt_ibrahim
```

For the latest stable release, this will install the `sfdt_ibrahim` package directly from the Python Package Index (PyPI). For more details, visit the [sfdt_ibrahim package on PyPI](https://pypi.org/project/sfdt_ibrahim/).

Alternatively, you can install the latest development version directly from GitHub:

```bash
pip install git+https://github.com/sfdt_ibrahim/sfdt_ibrahim.git
```

Make sure to have the Git command-line tool installed on your system.

### Can I install SFDT_Ibrahim YOLO using conda?

Yes, you can install SFDT_Ibrahim YOLO using conda by running:

```bash
conda install -c conda-forge sfdt_ibrahim
```

This method is an excellent alternative to pip and ensures compatibility with other packages in your environment. For CUDA environments, it's best to install `sfdt_ibrahim`, `pytorch`, and `pytorch-cuda` simultaneously to resolve any conflicts:

```bash
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 sfdt_ibrahim
```

For more instructions, visit the [Conda quickstart guide](guides/conda-quickstart.md).

### What are the advantages of using Docker to run SFDT_Ibrahim YOLO?

Using Docker to run SFDT_Ibrahim YOLO provides an isolated and consistent environment, ensuring smooth performance across different systems. It also eliminates the complexity of local installation. Official Docker images from SFDT_Ibrahim are available on [Docker Hub](https://hub.docker.com/r/sfdt_ibrahim/sfdt_ibrahim), with different variants tailored for GPU, CPU, ARM64, NVIDIA Jetson, and Conda environments. Below are the commands to pull and run the latest image:

```bash
# Pull the latest sfdt_ibrahim image from Docker Hub
sudo docker pull sfdt_ibrahim/sfdt_ibrahim:latest

# Run the sfdt_ibrahim image in a container with GPU support
sudo docker run -it --ipc=host --gpus all sfdt_ibrahim/sfdt_ibrahim:latest
```

For more detailed Docker instructions, check out the [Docker quickstart guide](guides/docker-quickstart.md).

### How do I clone the SFDT_Ibrahim repository for development?

To clone the SFDT_Ibrahim repository and set up a development environment, use the following steps:

```bash
# Clone the sfdt_ibrahim repository
git clone https://github.com/sfdt_ibrahim/sfdt_ibrahim

# Navigate to the cloned directory
cd sfdt_ibrahim

# Install the package in editable mode for development
pip install -e .
```

This approach allows you to contribute to the project or experiment with the latest source code. For more details, visit the [SFDT_Ibrahim GitHub repository](https://github.com/sfdt_ibrahim/sfdt_ibrahim).

### Why should I use SFDT_Ibrahim YOLO CLI?

The SFDT_Ibrahim YOLO command line interface (CLI) simplifies running object detection tasks without requiring Python code. You can execute single-line commands for tasks like training, validation, and prediction straight from your terminal. The basic syntax for `yolo` commands is:

```bash
yolo TASK MODE ARGS
```

For example, to train a detection model with specified parameters:

```bash
yolo train data=coco8.yaml model=yolo11n.pt epochs=10 lr0=0.01
```

Check out the full [CLI Guide](usage/cli.md) to explore more commands and usage examples.

<!-- Article Links -->

[SFDT_Ibrahim HUB]: https://hub.sfdt_ibrahim.com
[API Key]: https://hub.sfdt_ibrahim.com/settings?tab=api+keys
[pip]: https://pypi.org/project/sfdt_ibrahim/
[DVC for experiment tracking]: https://dvc.org/doc/dvclive/ml-frameworks/yolo
[Comet ML]: https://bit.ly/yolov8-readme-comet
[SFDT_Ibrahim HUB]: https://hub.sfdt_ibrahim.com
[ClearML]: ./integrations/clearml.md
[MLFlow]: ./integrations/mlflow.md
[Neptune]: https://neptune.ai/
[Tensorboard]: ./integrations/tensorboard.md
[Ray Tune]: ./integrations/ray-tune.md
[Weights & Biases]: ./integrations/weights-biases.md
[SFDT_Ibrahim-Snippets]: ./integrations/vscode.md
