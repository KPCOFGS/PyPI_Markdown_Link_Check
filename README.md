# PyPI_Relative_Path_Check

## Overview
The PyPI_Relative_Path_Check is a Python script designed to help users to validate if the relative paths found on a PyPI project has issues. It fetches the specified PyPI relative paths and checks if they are valid.

## Dependencies
The script requires the following dependencies:
- Python 3.x
- requests
- BeautifulSoup4

## Download

You can download the script using `git`

```bash
git clone https://github.com/KPCOFGS/PyPI_Markdown_Link_Check.git
cd PyPI_Markdown_Link_Check
```

You can install the dependencies using pip:

```bash
pip install -r requirements.txt
```

## Usage
To use the script, you need to specify the URL of the PyPI webpage you want to check using the `--link-url` parameter. For example:

```bash
python script.py --link-url PyPI_URL
```

This command will check the links found on the specified PyPI webpage and report back if there are relative paths having problems on the PyPI project

## Note
- The script only checks the relative paths found within the provided PyPI webpage and excludes other links such as http or https links.
- Due to the nature of web content, links may change or become unavailable over time. Therefore, the script provides a snapshot of link validity at the time of execution.

## License
This repository is licensed under the [Unlicense](LICENSE)
