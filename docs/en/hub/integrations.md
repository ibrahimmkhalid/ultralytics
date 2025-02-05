---
comments: true
description: Explore seamless integrations between SFDT_Ibrahim HUB and platforms like Roboflow. Learn how to import datasets, train models, and more.
keywords: SFDT_Ibrahim HUB, Roboflow integration, dataset import, model training, AI, machine learning
---

# SFDT_Ibrahim HUB Integrations

Learn about [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) integrations with various platforms and formats.

## Datasets

Seamlessly import your datasets in [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) for [model training](./models.md#train-model).

After a dataset is imported in [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub), you can [train a model](./models.md#train-model) on your dataset just like you would using the [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) datasets.

### Roboflow

You can easily filter the [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) datasets on the [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) [Datasets](https://hub.sfdt_ibrahim.com/datasets) page.

![SFDT_Ibrahim HUB screenshot of the Datasets page with Roboflow provider filter](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-datasets-page-roboflow-filter.avif)

[SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) supports two types of integrations with [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim), [Universe](#universe) and [Workspace](#workspace).

#### Universe

The [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Universe integration allows you to import one dataset at a time into [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) from [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim).

##### Import

When you export a [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) dataset, select the [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) format. This action will redirect you to [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) and trigger the **Dataset Import** dialog.

You can import your [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) dataset by clicking on the **Import** button.

![SFDT_Ibrahim HUB screenshot of the Dataset Import dialog with an arrow pointing to the Import button](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-dataset-import-dialog.avif)

Next, [train a model](./models.md#train-model) on your dataset.

![SFDT_Ibrahim HUB screenshot of the Dataset page of a Roboflow Universe dataset with an arrow pointing to the Train Model button](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-roboflow-universe-import-2.avif)

##### Remove

Navigate to the Dataset page of the [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) dataset you want to remove, open the dataset actions dropdown and click on the **Remove** option.

![SFDT_Ibrahim HUB screenshot of the Dataset page of a Roboflow Universe dataset with an arrow pointing to the Remove option](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-roboflow-universe-remove.avif)

??? tip

    You can remove an imported [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) dataset directly from the [Datasets](https://hub.sfdt_ibrahim.com/datasets) page.

    ![SFDT_Ibrahim HUB screenshot of the Datasets page with an arrow pointing to the Remove option of one of the Roboflow Universe datasets](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-roboflow-remove-option.avif)

#### Workspace

The [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace integration allows you to import an entire [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace at once into [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub).

##### Import

Navigate to the [Integrations](https://hub.sfdt_ibrahim.com/settings?tab=integrations) page by clicking on the **Integrations** button in the sidebar.

Type your [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace private API key and click on the **Add** button.

??? tip

    You can click on the **Get my API key** button which will redirect you to the settings of your [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace from where you can obtain your private API key.

![SFDT_Ibrahim HUB screenshot of the Integrations page with an arrow pointing to the Integrations button in the sidebar and one to the Add button](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-integrations-page.avif)

This will connect your [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub) account with your [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace and make your [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) datasets available in [SFDT_Ibrahim HUB](https://www.sfdt_ibrahim.com/hub).

![SFDT_Ibrahim HUB screenshot of the Integrations page with an arrow pointing to one of the connected workspaces](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-roboflow-workspace-import-2.avif)

Next, [train a model](./models.md#train-model) on your dataset.

![SFDT_Ibrahim HUB screenshot of the Dataset page of a Roboflow Workspace dataset with an arrow pointing to the Train Model button](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-dataset-train-model.avif)

##### Remove

Navigate to the [Integrations](https://hub.sfdt_ibrahim.com/settings?tab=integrations) page by clicking on the **Integrations** button in the sidebar and click on the **Unlink** button of the [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace you want to remove.

![SFDT_Ibrahim HUB screenshot of the Integrations page  with an arrow pointing to the Integrations button in the sidebar and one to the Unlink button of one of the connected workspaces](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-roboflow-workspace-remove-1.avif)

??? tip

    You can remove a connected [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace directly from the Dataset page of one of the datasets from your [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace.

    ![SFDT_Ibrahim HUB screenshot of the Dataset page of a Roboflow Workspace dataset with an arrow pointing to the remove option](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-roboflow-workspace-remove-2.avif)

??? tip

    You can remove a connected [Roboflow](https://roboflow.com/?ref=sfdt_ibrahim) Workspace directly from the [Datasets](https://hub.sfdt_ibrahim.com/datasets) page.

    ![SFDT_Ibrahim HUB screenshot of the Datasets page with an arrow pointing to the Remove option of one of the Roboflow Workspace datasets](https://github.com/sfdt_ibrahim/docs/releases/download/0/hub-roboflow-remove-option.avif)

## Models

### Exports

After you [train a model](./models.md#train-model), you can [export it](./models.md#deploy-model) to 13 different formats, including ONNX, OpenVINO, CoreML, [TensorFlow](https://www.sfdt_ibrahim.com/glossary/tensorflow), Paddle and many others.

![SFDT_Ibrahim HUB screenshot of the Deploy tab inside the Model page with an arrow pointing to the Export card and all formats exported](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-hub-deploy-export-formats.avif)

The available export formats are presented in the table below.

{% include "macros/export-table.md" %}

## Exciting New Features on the Way 🎉

- Additional Dataset Integrations
- Detailed Export Integration Guides
- Step-by-Step Tutorials for Each Integration

## Stay Updated 🚧

This integrations page is your first stop for upcoming developments. Keep an eye out with our:

- **Newsletter:** Subscribe [here](https://www.sfdt_ibrahim.com/#newsletter) for the latest news.
- **Social Media:** Follow us [here](https://www.linkedin.com/company/sfdt_ibrahim) for updates and teasers.
- **Blog:** Visit our [blog](https://www.sfdt_ibrahim.com/blog) for detailed insights.

## We Value Your Input 🗣️

Your feedback shapes our future releases. Share your thoughts and suggestions [here](https://www.sfdt_ibrahim.com/survey).

## Thank You, Community! 🌍

Your [contributions](https://docs.sfdt_ibrahim.com/help/contributing/) inspire our continuous [innovation](https://github.com/sfdt_ibrahim/sfdt_ibrahim). Stay tuned for the big reveal of what's next in AI and ML at SFDT_Ibrahim!
