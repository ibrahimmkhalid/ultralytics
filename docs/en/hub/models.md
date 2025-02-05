---
comments: true
description: Explore SFDT_Ibrahim HUB for easy training, analysis, preview, deployment and sharing of custom vision AI models using YOLO11. Start training today!.
keywords: SFDT_Ibrahim HUB, YOLO11, custom AI models, model training, model deployment, model analysis, vision AI
---

# SFDT_Ibrahim HUB Models

[SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) models provide a streamlined solution for training vision AI models on custom datasets.

The process is user-friendly and efficient, involving a simple three-step creation and accelerated training powered by SFDT_Ibrahim YOLOv8. During training, real-time updates on model metrics are available so that you can monitor each step of the progress. Once training is completed, you can preview your model and easily deploy it to real-world applications. Therefore, [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) offers a comprehensive yet straightforward system for model creation, training, evaluation, and deployment.

<p align="center">
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/YVlkq5H2tAQ"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> SFDT_Ibrahim HUB Training and Validation Overview
</p>

## Train Model

Navigate to the [Models](https://hub.sfdt_ibrahim.com/models) page by clicking on the **Models** button in the sidebar and click on the **Train Model** button on the top right of the page.

![SFDT_Ibrahim HUB screenshot of the Models page with an arrow pointing to the Models button in the sidebar and one to the Train Model button](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-page.avif)

??? tip

    You can train a model directly from the [Home](https://hub.sfdt_ibrahim.com/home) page.

    ![SFDT_Ibrahim HUB screenshot of the Home page with an arrow pointing to the Train Model card](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-card.avif)

This action will trigger the **Train Model** dialog which has three simple steps:

### 1. Dataset

In this step, you have to select the dataset you want to train your model on. After you selected a dataset, click **Continue**.

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with an arrow pointing to a dataset and one to the Continue button](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-train-model-dialog-dataset-step.avif)

??? tip

    You can skip this step if you train a model directly from the Dataset page.

    ![SFDT_Ibrahim HUB screenshot of the Dataset page with an arrow pointing to the Train Model button](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-dataset-page-train-model-button.avif)

### 2. Model

In this step, you have to choose the project in which you want to create your model, the name of your model and your model's architecture.

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with arrows pointing to the project dropdown, model name and Continue button](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-train-model-dialog.avif)

??? note

    SFDT_Ibrahim HUB will try to pre-select the project.

    If you opened the **Train Model** dialog as described above, [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) will pre-select the last project you used.

    If you opened the **Train Model** dialog from the Project page, [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) will pre-select the project you were inside of.

    ![SFDT_Ibrahim HUB screenshot of the Project page with an arrow pointing to the Train Model button](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-train-model-button.avif)

    In case you don't have a project created yet, you can set the name of your project in this step and it will be created together with your model.

!!! info

    You can read more about the available [YOLO models](https://docs.sfdt_ibrahim.com/models/) and architectures in our documentation.

By default, your model will use a pre-trained model (trained on the [COCO](https://docs.sfdt_ibrahim.com/datasets/detect/coco/) dataset) to reduce training time. You can change this behavior and tweak your model's configuration by opening the **Advanced Model Configuration** accordion.

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with an arrow pointing to the Advanced Model Configuration accordion](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-dialog-2.avif)

!!! note

    You can easily change the most common model configuration options (such as the number of epochs) but you can also use the **Custom** option to access all [Train Settings](https://docs.sfdt_ibrahim.com/modes/train/#train-settings) relevant to [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub).

<p align="center">
  <br>
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/Unt4Lfid7aY"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> How to Configure SFDT_Ibrahim YOLOv8 Training Parameters in SFDT_Ibrahim HUB
</p>

Alternatively, you start training from one of your previously trained models by clicking on the **Custom** tab.

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with an arrow pointing to the Custom tab](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-dialog-3.avif)

When you're happy with your model configuration, click **Continue**.

### 3. Train

In this step, you will start training you model.

??? note

    When you are on this step, you have the option to close the **Train Model** dialog and start training your model from the Model page later.

    ![SFDT_Ibrahim HUB screenshot of the Model page with an arrow pointing to the Start Training card](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-cloud-training-model-page-start-training.avif)

[SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) offers three training options:

- [SFDT_Ibrahim Cloud](./cloud-training.md)
- Google Colab
- Bring your own agent

#### a. SFDT_Ibrahim Cloud

You need to [upgrade](./pro.md#upgrade) to the [Pro Plan](./pro.md) in order to access [SFDT_Ibrahim Cloud](./cloud-training.md).

![SFDT_Ibrahim HUB screenshot of the Train Model dialog](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-dialog-4.avif)

To train models using our [Cloud Training](./cloud-training.md) solution, read the [SFDT_Ibrahim Cloud Training](./cloud-training.md) documentation.

#### b. Google Colab

To start training your model using [Google Colab](https://colab.research.google.com/github/sfdt_ibrahim/hub/blob/master/hub.ipynb), follow the instructions shown in the [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) **Train Model** dialog or on the [Google Colab](https://colab.research.google.com/github/sfdt_ibrahim/hub/blob/master/hub.ipynb) notebook.

<a href="https://colab.research.google.com/github/sfdt_ibrahim/hub/blob/master/hub.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab">
</a>

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with arrows pointing to instructions](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-dialog-instructions.avif)

When the training starts, you can click **Done** and monitor the training progress on the Model page.

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with an arrow pointing to the Done button](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-done-button.avif)

![SFDT_Ibrahim HUB screenshot of the Model page of a model that is currently training](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-train-model-progress.avif)

!!! note

    In case the training stops and a checkpoint was saved, you can resume training your model from the Model page.

    ![SFDT_Ibrahim HUB screenshot of the Model page with an arrow pointing to the Resume Training card](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-train-model-resume-training.avif)

#### c. Bring your own agent

<p align="center">
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/S_J-Dyw15i0"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> Bring your Own Agent model training using SFDT_Ibrahim HUB
</p>

To start training your model using your own agent, follow the instructions shown in the [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) **Train Model** dialog.

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with arrows pointing to instructions](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-dialog-instructions-1.avif)

Install the `sfdt_ibrahim` package from [PyPI](https://pypi.org/project/sfdt_ibrahim/).

```bash
pip install -U sfdt_ibrahim
```

Next, use the Python code provided to start training the model.

When the training starts, you can click **Done** and monitor the training progress on the Model page.

![SFDT_Ibrahim HUB screenshot of the Train Model dialog with an arrow pointing to the Done button](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-train-model-done-button-1.avif)

![SFDT_Ibrahim HUB screenshot of the Model page of a model that is currently training](https://github.com/sfdt_ibrahim/docs/releases/download/0/model-training-progress.avif)

!!! note

    In case the training stops and a checkpoint was saved, you can resume training your model from the Model page.

    ![SFDT_Ibrahim HUB screenshot of the Model page with an arrow pointing to the Resume Training card](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-train-model-resume-training-1.avif)

## Analyze Model

After you [train a model](#train-model), you can analyze the model metrics.

The **Train** tab presents the most important metrics carefully grouped based on the task.

![SFDT_Ibrahim HUB screenshot of the Model page of a trained model](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-analyze-model.avif)

To access all model metrics, click on the **Charts** tab.

![SFDT_Ibrahim HUB screenshot of the Preview tab inside the Model page with an arrow pointing to the Charts tab](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-analyze-model-2.avif)

??? tip

    Each chart can be enlarged for better visualization.

    ![SFDT_Ibrahim HUB screenshot of the Train tab inside the Model page with an arrow pointing to the expand icon of one of the charts](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-analyze-model-train-tab-expand-icon.avif)

    ![SFDT_Ibrahim HUB screenshot of the Train tab inside the Model page with one of the charts expanded](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-analyze-model-train-tab-expanded-chart.avif)

    Furthermore, to properly analyze the data, you can utilize the zoom feature.

    ![SFDT_Ibrahim HUB screenshot of the Train tab inside the Model page with one of the charts expanded and zoomed](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-analyze-model-zoomed-chart.avif)

## Preview Model

After you [train a model](#train-model), you can preview it by clicking on the **Preview** tab.

In the **Test** card, you can select a preview image from the dataset used during training or upload an image from your device.

![SFDT_Ibrahim HUB screenshot of the Preview tab inside the Model page with an arrow pointing to Charts tab and one to the Test card](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-preview-model-charts-test-card.avif)

!!! note

    You can also use your camera to take a picture and run inference on it directly.

    ![SFDT_Ibrahim HUB screenshot of the Preview tab inside the Model page with an arrow pointing to Camera tab inside the Test card](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-preview-camera-tab.avif)

Furthermore, you can preview your model in real-time directly on your [iOS](https://apps.apple.com/xk/app/sfdt_ibrahim/id1583935240) or [Android](https://play.google.com/store/apps/details?id=com.sfdt_ibrahim.sfdt_ibrahim_app) mobile device by [downloading](https://www.sfdt_ibrahim.com/app-install) our [SFDT_Ibrahim HUB App](app/index.md).

![SFDT_Ibrahim HUB screenshot of the Deploy tab inside the Model page with arrow pointing to the Real-Time Preview card](https://github.com/sfdt_ibrahim/docs/releases/download/0/deploy-tab-real-time-preview-card.avif)

## Deploy Model

After you [train a model](#train-model), you can export it to 13 different formats, including ONNX, OpenVINO, CoreML, [TensorFlow](https://www.sfdt_ibrahim.com/glossary/tensorflow), Paddle and many others.

<p align="center">
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/K69DUpSBNdA"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> How to Export the SFDT_Ibrahim YOLO11 to ONNX, OpenVINO and Other Formats using SFDT_Ibrahim HUB 🚀
</p>

![SFDT_Ibrahim HUB screenshot of the Deploy tab inside the Model page with an arrow pointing to the Export card and all formats exported](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-deploy-export-formats.avif)

??? tip

    You can customize the export options of each format if you open the export actions dropdown and click on the **Advanced** option.

    ![SFDT_Ibrahim HUB screenshot of the Deploy tab inside the Model page with an arrow pointing to the Advanced option of one of the formats](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-deploy-model-advanced-option.avif)

!!! note

    You can re-export each format if you open the export actions dropdown and click on the **Advanced** option.

You can also use our [Inference API](./inference-api.md) in production.

![SFDT_Ibrahim HUB screenshot of the Deploy tab inside the Model page with an arrow pointing to the SFDT_Ibrahim Inference API card](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-inference-api-card.avif)

Read the [SFDT_Ibrahim Inference API](./inference-api.md) documentation for more information.

## Share Model

!!! info

    [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub)'s sharing functionality provides a convenient way to share models with others. This feature is designed to accommodate both existing [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) users and those who have yet to create an account.

??? note

    You have control over the general access of your models.

    You can choose to set the general access to "Private", in which case, only you will have access to it. Alternatively, you can set the general access to "Unlisted" which grants viewing access to anyone who has the direct link to the model, regardless of whether they have an [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) account or not.

Navigate to the Model page of the model you want to share, open the model actions dropdown and click on the **Share** option. This action will trigger the **Share Model** dialog.

![SFDT_Ibrahim HUB screenshot of the Model page with an arrow pointing to the Share option](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-share-model.avif)

??? tip

    You can also share a model directly from the [Models](https://hub.sfdt_ibrahim.com/models) page or from the Project page of the project where your model is located.

    ![SFDT_Ibrahim HUB screenshot of the Models page with an arrow pointing to the Share option of one of the models](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-share-model-2.avif)

Set the general access to "Unlisted" and click **Save**.

![SFDT_Ibrahim HUB screenshot of the Share Model dialog with an arrow pointing to the dropdown and one to the Save button](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-share-model-dialog.avif)

Now, anyone who has the direct link to your model can view it.

??? tip

    You can easily click on the model's link shown in the **Share Model** dialog to copy it.

    ![SFDT_Ibrahim HUB screenshot of the Share Model dialog with an arrow pointing to the model's link](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-share-model-link.avif)

## Edit Model

Navigate to the Model page of the model you want to edit, open the model actions dropdown and click on the **Edit** option. This action will trigger the **Update Model** dialog.

![SFDT_Ibrahim HUB screenshot of the Model page with an arrow pointing to the Edit option](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-edit-model-1.avif)

??? tip

    You can also edit a model directly from the [Models](https://hub.sfdt_ibrahim.com/models) page or from the Project page of the project where your model is located.

    ![SFDT_Ibrahim HUB screenshot of the Models page with an arrow pointing to the Edit option of one of the models](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-edit-model-2.avif)

Apply the desired modifications to your model and then confirm the changes by clicking **Save**.

![SFDT_Ibrahim HUB screenshot of the Update Model dialog with an arrow pointing to the Save button](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-edit-model-save-button.avif)

## Delete Model

Navigate to the Model page of the model you want to delete, open the model actions dropdown and click on the **Delete** option. This action will delete the model.

![SFDT_Ibrahim HUB screenshot of the Model page with an arrow pointing to the Delete option](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-delete-model-1.avif)

??? tip

    You can also delete a model directly from the [Models](https://hub.sfdt_ibrahim.com/models) page or from the Project page of the project where your model is located.

    ![SFDT_Ibrahim HUB screenshot of the Models page with an arrow pointing to the Delete option of one of the models](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-delete-model-2.avif)

!!! note

    If you change your mind, you can restore the model from the [Trash](https://hub.sfdt_ibrahim.com/trash) page.

    ![SFDT_Ibrahim HUB screenshot of the Trash page with an arrow pointing to the Restore option of one of the models](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-trash-restore-option.avif)
