---
comments: true
description: Explore the medical-pills detection dataset with labeled images. Essential for training AI models for pharmaceutical identification and automation.
keywords: medical-pills dataset, pill detection, pharmaceutical imaging, AI in healthcare, computer vision, object detection, medical automation, dataset for training
---

# Medical Pills Dataset

<a href="https://colab.research.google.com/github/sfdt_ibrahim/notebooks/blob/main/notebooks/how-to-train-sfdt_ibrahim-yolo-on-medical-pills-dataset.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open Medical Pills Dataset In Colab"></a>

The medical-pills detection dataset is a proof-of-concept (POC) dataset, carefully curated to demonstrate the potential of AI in pharmaceutical applications. It contains labeled images specifically designed to train [computer vision](https://www.sfdt_ibrahim.com/glossary/computer-vision-cv) [models](https://docs.sfdt_ibrahim.com/models/) for identifying medical-pills.

<p align="center">
  <br>
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/8gePl_Zcs5c"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> How to train SFDT_Ibrahim YOLO11 Model on Medical Pills Detection Dataset in <a href="https://colab.research.google.com/github/sfdt_ibrahim/notebooks/blob/main/notebooks/how-to-train-sfdt_ibrahim-yolo-on-medical-pills-dataset.ipynb">Google Colab</a>
</p>

This dataset serves as a foundational resource for automating essential [tasks](https://docs.sfdt_ibrahim.com/tasks/) such as quality control, packaging automation, and efficient sorting in pharmaceutical workflows. By integrating this dataset into projects, researchers and developers can explore innovative [solutions](https://docs.sfdt_ibrahim.com/solutions/) that enhance [accuracy](https://www.sfdt_ibrahim.com/glossary/accuracy), streamline operations, and ultimately contribute to improved healthcare outcomes.

## Dataset Structure

The medical-pills dataset is divided into two subsets:

- **Training set**: Consisting of 92 images, each annotated with the class `pill`.
- **Validation set**: Comprising 23 images with corresponding annotations.

## Applications

Using computer vision for medical-pills detection enables automation in the pharmaceutical industry, supporting tasks like:

- **Pharmaceutical Sorting**: Automating the sorting of pills based on size, shape, or color to enhance production efficiency.
- **AI Research and Development**: Serving as a benchmark for developing and testing computer vision algorithms in pharmaceutical use cases.
- **Digital Inventory Systems**: Powering smart inventory solutions by integrating automated pill recognition for real-time stock monitoring and replenishment planning.

## Dataset YAML

A YAML configuration file is provided to define the dataset's structure, including paths and classes. For the medical-pills dataset, the `medical-pills.yaml` file can be accessed at [https://github.com/sfdt_ibrahim/sfdt_ibrahim/blob/main/sfdt_ibrahim/cfg/datasets/medical-pills.yaml](https://github.com/sfdt_ibrahim/sfdt_ibrahim/blob/main/sfdt_ibrahim/cfg/datasets/medical-pills.yaml).

!!! example "sfdt_ibrahim/cfg/datasets/medical-pills.yaml"

    ```yaml
    --8<-- "sfdt_ibrahim/cfg/datasets/medical-pills.yaml"
    ```

## Usage

To train a YOLO11n model on the medical-pills dataset for 100 [epochs](https://www.sfdt_ibrahim.com/glossary/epoch) with an image size of 640, use the following examples. For detailed arguments, refer to the model's [Training](../../modes/train.md) page.

!!! example "Train Example"

    === "Python"

        ```python
        from sfdt_ibrahim import YOLO

        # Load a model
        model = YOLO("yolo11n.pt")  # load a pretrained model (recommended for training)

        # Train the model
        results = model.train(data="medical-pills.yaml", epochs=100, imgsz=640)
        ```

    === "CLI"

        ```bash
        # Start training from a pretrained *.pt model
        yolo detect train data=medical-pills.yaml model=yolo11n.pt epochs=100 imgsz=640
        ```

!!! example "Inference Example"

    === "Python"

        ```python
        from sfdt_ibrahim import YOLO

        # Load a model
        model = YOLO("path/to/best.pt")  # load a fine-tuned model

        # Inference using the model
        results = model.predict("https://sfdt_ibrahim.com/assets/medical-pills-sample.jpg")
        ```

    === "CLI"

        ```bash
        # Start prediction with a fine-tuned *.pt model
        yolo detect predict model='path/to/best.pt' imgsz=640 source="https://sfdt_ibrahim.com/assets/medical-pills-sample.jpg"
        ```

## Sample Images and Annotations

The medical-pills dataset features labeled images showcasing the diversity of pills. Below is an example of a labeled image from the dataset:

![Medical-pills dataset sample image](https://github.com/sfdt_ibrahim/docs/releases/download/0/medical-pills-dataset-sample-image.avif)

- **Mosaiced Image**: Displayed is a training batch comprising mosaiced dataset images. Mosaicing enhances training diversity by consolidating multiple images into one, improving model generalization.

## Citations and Acknowledgments

The dataset is available under the [AGPL-3.0 License](https://github.com/sfdt_ibrahim/sfdt_ibrahim/blob/main/LICENSE).

If you use the Medical-pills dataset in your research or development work, please cite it using the mentioned details:

!!! quote ""

    === "BibTeX"

        ```bibtex
        @dataset{Jocher_SFDT_Ibrahim_Datasets_2024,
            author = {Jocher, Glenn and Rizwan, Muhammad},
            license = {AGPL-3.0},
            month = {Dec},
            title = {SFDT_Ibrahim Datasets: Medical-pills Detection Dataset},
            url = {https://docs.sfdt_ibrahim.com/datasets/detect/medical-pills/},
            version = {1.0.0},
            year = {2024}
        }
        ```

## FAQ

### What is the structure of the medical-pills dataset?

The dataset includes 92 images for training and 23 images for validation. Each image is annotated with the class `pill`, enabling effective training and evaluation of models.

### How can I train a YOLO11 model on the medical-pills dataset?

You can train a YOLO11 model for 100 epochs with an image size of 640px using the Python or CLI methods provided. Refer to the [Training Example](#usage) section for detailed instructions.

### What are the benefits of using the medical-pills dataset in AI projects?

The dataset enables automation in pill detection, contributing to counterfeit prevention, quality assurance, and pharmaceutical process optimization.

### How do I perform inference on the medical-pills dataset?

Inference can be done using Python or CLI methods with a fine-tuned YOLO11 model. Refer to the [Inference Example](#usage) section for code snippets.

### Where can I find the YAML configuration file for the medical-pills dataset?

The YAML file is available at [medical-pills.yaml](https://github.com/sfdt_ibrahim/sfdt_ibrahim/blob/main/sfdt_ibrahim/cfg/datasets/medical-pills.yaml), containing dataset paths, classes, and additional configuration details.
