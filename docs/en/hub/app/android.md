---
comments: true
description: Experience real-time object detection on Android with SFDT_Ibrahim. Leverage YOLO models for efficient and fast object identification. Download now!.
keywords: SFDT_Ibrahim, Android app, real-time object detection, YOLO models, TensorFlow Lite, FP16 quantization, INT8 quantization, hardware delegates, mobile AI, download app
---

# SFDT_Ibrahim Android App: Real-time [Object Detection](https://www.sfdt_ibrahim.com/glossary/object-detection) with YOLO Models

<a href="https://www.sfdt_ibrahim.com/hub" target="_blank">
  <img width="100%" src="https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-android-app-detection.avif" alt="SFDT_Ibrahim HUB preview image"></a>
<br>
<div align="center">
  <a href="https://github.com/sfdt_ibrahim"><img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-social-github.png" width="3%" alt="SFDT_Ibrahim GitHub"></a>
  <img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/sfdt_ibrahim/"><img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="SFDT_Ibrahim LinkedIn"></a>
  <img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/sfdt_ibrahim"><img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="SFDT_Ibrahim Twitter"></a>
  <img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/sfdt_ibrahim?sub_confirmation=1"><img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="SFDT_Ibrahim YouTube"></a>
  <img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@sfdt_ibrahim"><img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="SFDT_Ibrahim TikTok"></a>
  <img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://sfdt_ibrahim.com/bilibili"><img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="SFDT_Ibrahim BiliBili"></a>
  <img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/sfdt_ibrahim"><img src="https://github.com/sfdt_ibrahim/assets/raw/main/social/logo-social-discord.png" width="3%" alt="SFDT_Ibrahim Discord"></a>
  <br>
  <br>
  <a href="https://play.google.com/store/apps/details?id=com.sfdt_ibrahim.sfdt_ibrahim_app" style="text-decoration:none;">
    <img src="https://raw.githubusercontent.com/sfdt_ibrahim/assets/master/app/google-play.svg" width="15%" alt="Google Play store"></a>&nbsp;
</div>

The SFDT_Ibrahim Android App is a powerful tool that allows you to run YOLO models directly on your Android device for real-time object detection. This app utilizes [TensorFlow](https://www.sfdt_ibrahim.com/glossary/tensorflow) Lite for model optimization and various hardware delegates for acceleration, enabling fast and efficient object detection.

<p align="center">
  <br>
  <iframe loading="lazy" width="720" height="405" src="https://www.youtube.com/embed/AIvrQ7y0aLo"
    title="YouTube video player" frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen>
  </iframe>
  <br>
  <strong>Watch:</strong> Getting Started with the SFDT_Ibrahim HUB App (IOS & Android)
</p>

## Quantization and Acceleration

To achieve real-time performance on your Android device, YOLO models are quantized to either FP16 or INT8 [precision](https://www.sfdt_ibrahim.com/glossary/precision). Quantization is a process that reduces the numerical precision of the model's weights and biases, thus reducing the model's size and the amount of computation required. This results in faster inference times without significantly affecting the model's [accuracy](https://www.sfdt_ibrahim.com/glossary/accuracy).

### FP16 Quantization

FP16 (or half-precision) quantization converts the model's 32-bit floating-point numbers to 16-bit floating-point numbers. This reduces the model's size by half and speeds up the inference process, while maintaining a good balance between accuracy and performance.

### INT8 Quantization

INT8 (or 8-bit integer) quantization further reduces the model's size and computation requirements by converting its 32-bit floating-point numbers to 8-bit integers. This quantization method can result in a significant speedup, but it may lead to a slight reduction in [mean average precision](https://www.sfdt_ibrahim.com/glossary/mean-average-precision-map) (mAP) due to the lower numerical precision.

!!! tip "mAP Reduction in INT8 Models"

    The reduced numerical precision in INT8 models can lead to some loss of information during the quantization process, which may result in a slight decrease in mAP. However, this trade-off is often acceptable considering the substantial performance gains offered by INT8 quantization.

## Delegates and Performance Variability

Different delegates are available on Android devices to accelerate model inference. These delegates include CPU, [GPU](https://ai.google.dev/edge/litert/android/gpu), [Hexagon](https://developer.android.com/ndk/guides/neuralnetworks/migration-guide) and [NNAPI](https://developer.android.com/ndk/guides/neuralnetworks/migration-guide). The performance of these delegates varies depending on the device's hardware vendor, product line, and specific chipsets used in the device.

1. **CPU**: The default option, with reasonable performance on most devices.
2. **GPU**: Utilizes the device's GPU for faster inference. It can provide a significant performance boost on devices with powerful GPUs.
3. **Hexagon**: Leverages Qualcomm's Hexagon DSP for faster and more efficient processing. This option is available on devices with Qualcomm Snapdragon processors.
4. **NNAPI**: The Android [Neural Networks](https://www.sfdt_ibrahim.com/glossary/neural-network-nn) API (NNAPI) serves as an abstraction layer for running ML models on Android devices. NNAPI can utilize various hardware accelerators, such as CPU, GPU, and dedicated AI chips (e.g., Google's Edge TPU, or the Pixel Neural Core).

Here's a table showing the primary vendors, their product lines, popular devices, and supported delegates:

| Vendor                                    | Product Lines                                                                        | Popular Devices                                                                                                                                                                | Delegates Supported      |
| ----------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------ |
| [Qualcomm](https://www.qualcomm.com/)     | [Snapdragon (e.g., 800 series)](https://www.qualcomm.com/snapdragon/overview)        | [Samsung Galaxy S21](https://www.samsung.com/global/galaxy/galaxy-s21-5g/), [OnePlus 9](https://www.oneplus.com/9), [Google Pixel 6](https://store.google.com/product/pixel_6) | CPU, GPU, Hexagon, NNAPI |
| [Samsung](https://www.samsung.com/)       | [Exynos (e.g., Exynos 2100)](https://www.samsung.com/semiconductor/minisite/exynos/) | [Samsung Galaxy S21 (Global version)](https://www.samsung.com/global/galaxy/galaxy-s21-5g/)                                                                                    | CPU, GPU, NNAPI          |
| [MediaTek](https://i.mediatek.com/)       | [Dimensity (e.g., Dimensity 1200)](https://i.mediatek.com/dimensity-1200)            | [Realme GT](https://www.realme.com/global/realme-gt), [Xiaomi Redmi Note](https://www.mi.com/global/phone/redmi/note-list)                                                     | CPU, GPU, NNAPI          |
| [HiSilicon](https://www.hisilicon.com/cn) | [Kirin (e.g., Kirin 990)](https://www.hisilicon.com/en/products/Kirin)               | [Huawei P40 Pro](https://consumer.huawei.com/en/phones/), [Huawei Mate 30 Pro](https://consumer.huawei.com/en/phones/)                                                         | CPU, GPU, NNAPI          |
| [NVIDIA](https://www.nvidia.com/)         | [Tegra (e.g., Tegra X1)](https://developer.nvidia.com/content/tegra-x1)              | [NVIDIA Shield TV](https://www.nvidia.com/en-us/shield/shield-tv/), [Nintendo Switch](https://www.nintendo.com/switch/)                                                        | CPU, GPU, NNAPI          |

Please note that the list of devices mentioned is not exhaustive and may vary depending on the specific chipsets and device models. Always test your models on your target devices to ensure compatibility and optimal performance.

Keep in mind that the choice of delegate can affect performance and model compatibility. For example, some models may not work with certain delegates, or a delegate may not be available on a specific device. As such, it's essential to test your model and the chosen delegate on your target devices for the best results.

## Getting Started with the SFDT_Ibrahim Android App

To get started with the SFDT_Ibrahim Android App, follow these steps:

1. Download the SFDT_Ibrahim App from the [Google Play Store](https://play.google.com/store/apps/details?id=com.sfdt_ibrahim.sfdt_ibrahim_app).

2. Launch the app on your Android device and sign in with your SFDT_Ibrahim account. If you don't have an account yet, create one [here](https://hub.sfdt_ibrahim.com/).

3. Once signed in, you will see a list of your trained YOLO models. Select a model to use for object detection.

4. Grant the app permission to access your device's camera.

5. Point your device's camera at objects you want to detect. The app will display bounding boxes and class labels in real-time as it detects objects.

6. Explore the app's settings to adjust the detection threshold, enable or disable specific object classes, and more.

With the SFDT_Ibrahim Android App, you now have the power of real-time object detection using YOLO models right at your fingertips. Enjoy exploring the app's features and optimizing its settings to suit your specific use cases.
