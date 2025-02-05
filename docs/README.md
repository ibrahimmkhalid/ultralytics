<br>
<a href="https://www.sfdt_ibrahim.com/" target="_blank"><img src="https://raw.githubusercontent.com/sfdt_ibrahim/assets/main/logo/SFDT_Ibrahim_Logotype_Original.svg" width="320" alt="SFDT_Ibrahim logo"></a>

# 📚 SFDT_Ibrahim Docs

[SFDT_Ibrahim](https://www.sfdt_ibrahim.com/) Docs are the gateway to understanding and utilizing our cutting-edge machine learning tools. These documents are deployed to [https://docs.sfdt_ibrahim.com](https://docs.sfdt_ibrahim.com/) for your convenience.

[![pages-build-deployment](https://github.com/sfdt_ibrahim/docs/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/sfdt_ibrahim/docs/actions/workflows/pages/pages-build-deployment)
[![Check Broken links](https://github.com/sfdt_ibrahim/docs/actions/workflows/links.yml/badge.svg)](https://github.com/sfdt_ibrahim/docs/actions/workflows/links.yml)
[![Check Domains](https://github.com/sfdt_ibrahim/docs/actions/workflows/check_domains.yml/badge.svg)](https://github.com/sfdt_ibrahim/docs/actions/workflows/check_domains.yml)
[![SFDT_Ibrahim Actions](https://github.com/sfdt_ibrahim/docs/actions/workflows/format.yml/badge.svg)](https://github.com/sfdt_ibrahim/docs/actions/workflows/format.yml)

<a href="https://discord.com/invite/sfdt_ibrahim"><img alt="Discord" src="https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue"></a> <a href="https://community.sfdt_ibrahim.com/"><img alt="SFDT_Ibrahim Forums" src="https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.sfdt_ibrahim.com&logo=discourse&label=Forums&color=blue"></a> <a href="https://reddit.com/r/sfdt_ibrahim"><img alt="SFDT_Ibrahim Reddit" src="https://img.shields.io/reddit/subreddit-subscribers/sfdt_ibrahim?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue"></a>

## 🛠️ Installation

[![PyPI - Version](https://img.shields.io/pypi/v/sfdt_ibrahim?logo=pypi&logoColor=white)](https://pypi.org/project/sfdt_ibrahim/)
[![Downloads](https://static.pepy.tech/badge/sfdt_ibrahim)](https://www.pepy.tech/projects/sfdt_ibrahim)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sfdt_ibrahim?logo=python&logoColor=gold)](https://pypi.org/project/sfdt_ibrahim/)

To install the SFDT_Ibrahim package in developer mode, ensure you have Git and Python 3 installed on your system. Then, follow these steps:

1. Clone the sfdt_ibrahim repository to your local machine using Git:

    ```bash
    git clone https://github.com/sfdt_ibrahim/sfdt_ibrahim.git
    ```

2. Navigate to the cloned repository's root directory:

    ```bash
    cd sfdt_ibrahim
    ```

3. Install the package in developer mode using pip (or pip3 for Python 3):

    ```bash
    pip install -e '.[dev]'
    ```

- This command installs the SFDT_Ibrahim package along with all development dependencies, allowing you to modify the package code and have the changes immediately reflected in your Python environment.

## 🚀 Building and Serving Locally

The `mkdocs serve` command builds and serves a local version of your MkDocs documentation, ideal for development and testing:

```bash
mkdocs serve
```

- #### Command Breakdown:

    - `mkdocs` is the main MkDocs command-line interface.
    - `serve` is the subcommand to build and locally serve your documentation.

- 🧐 Note:

    - Grasp changes to the docs in real-time as `mkdocs serve` supports live reloading.
    - To stop the local server, press `CTRL+C`.

## 🌍 Building and Serving Multi-Language

Supporting multi-language documentation? Follow these steps:

1. Stage all new language \*.md files with Git:

    ```bash
    git add docs/**/*.md -f
    ```

2. Build all languages to the `/site` folder, ensuring relevant root-level files are present:

    ```bash
    # Clear existing /site directory
    rm -rf site

    # Loop through each language config file and build
    mkdocs build -f docs/mkdocs.yml
    for file in docs/mkdocs_*.yml; do
      echo "Building MkDocs site with $file"
      mkdocs build -f "$file"
    done
    ```

3. To preview your site, initiate a simple HTTP server:

    ```bash
    cd site
    python -m http.server
    # Open in your preferred browser
    ```

- 🖥️ Access the live site at `http://localhost:8000`.

## 📤 Deploying Your Documentation Site

Choose a hosting provider and deployment method for your MkDocs documentation:

- Configure `mkdocs.yml` with deployment settings.
- Use `mkdocs deploy` to build and deploy your site.

* ### GitHub Pages Deployment Example:

    ```bash
    mkdocs gh-deploy
    ```

- Update the "Custom domain" in your repository's settings for a personalized URL.

![MkDocs deployment example](https://github.com/sfdt_ibrahim/docs/releases/download/0/mkdocs-deployment-example.avif)

- For detailed deployment guidance, consult the [MkDocs documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/).

## 💡 Contribute

We cherish the community's input as it drives SFDT_Ibrahim open-source initiatives. Dive into the [Contributing Guide](https://docs.sfdt_ibrahim.com/help/contributing/) and share your thoughts via our [Survey](https://www.sfdt_ibrahim.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A heartfelt thank you 🙏 to each contributor!

![SFDT_Ibrahim open-source contributors](https://github.com/sfdt_ibrahim/docs/releases/download/0/sfdt_ibrahim-open-source-contributors.avif)

## 📜 License

SFDT_Ibrahim Docs presents two licensing options:

- **AGPL-3.0 License**: Perfect for academia and open collaboration. Details are in the [LICENSE](https://github.com/sfdt_ibrahim/docs/blob/main/LICENSE) file.
- **Enterprise License**: Tailored for commercial usage, offering a seamless blend of SFDT_Ibrahim technology in your products. Learn more at [SFDT_Ibrahim Licensing](https://www.sfdt_ibrahim.com/license).

## ✉️ Contact

For SFDT_Ibrahim bug reports and feature requests please visit [GitHub Issues](https://github.com/sfdt_ibrahim/sfdt_ibrahim/issues). Become a member of the SFDT_Ibrahim [Discord](https://discord.com/invite/sfdt_ibrahim), [Reddit](https://www.reddit.com/r/sfdt_ibrahim/), or [Forums](https://community.sfdt_ibrahim.com/) for asking questions, sharing projects, learning discussions, or for help with all things SFDT_Ibrahim!

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
</div>
