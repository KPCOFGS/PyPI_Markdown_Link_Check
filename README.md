# PyPI_Markdown_Link_Check

## Overview
The PyPI Markdown Link Check is a Python script designed to help users check the validity of markdown links found on the Python Package Index (PyPI) website (`pypi.org`) from GitHub. It fetches the specified PyPI webpage and checks if some markdown links are invalid.

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

This command will check the markdown links found on the specified PyPI webpage and report back if there is any typo

## Note
- The script only checks the markdown links found within the provided PyPI webpage and excludes other links such as http or https links.
- Due to the nature of web content, links may change or become unavailable over time. Therefore, the script provides a snapshot of link validity at the time of execution.

## License
This repository is licend under the [Unlicense](LICENSE)
