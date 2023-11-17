# Financial Data Processing

## Overview

This repository contains a COBOL program for processing financial data. The program connects multiple database files into a single CSV file, which is then sent to SQLite3. Subsequently, a Python program converts the SQLite3 database file into a CSV file. Another Python program uploads the data to Google Sheets, and there's a separate script to download data from Google Sheets. Server-side operations are handled using Django.

## Prerequisites

- COBOL compiler (e.g., GnuCOBOL)
- Python 3.x
- Django (for server integration)
- SQLite
- Google API Client Library for Python (`google-api-python-client`)
- Google Auth (`google-auth`)
- Google Sheets API (`google-auth-oauthlib`, `google-auth-httplib2`, `google-api-python-client`)

## Configuration

Ensure that database connection details and Google Sheets API credentials are properly configured in the respective Python scripts. For Django integration, update the database settings in `django_integration/settings.py`.

## Dependencies

- [GnuCOBOL](https://sourceforge.net/projects/gnucobol/)
- [SQLite](https://www.sqlite.org/)
- Python packages (see `requirements.txt`)

## Connecting Google Sheets to Python

To connect Google Sheets to Python, follow these steps:

1. **Create Google API Credentials:**
    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a new project.
    - Enable the Google Sheets API.
    - Create credentials (Service Account Key).
    - Download the JSON file containing the credentials and save it securely (e.g., `onemore.json`).
2. **Install Required Python Packages:**
   ```bash
   pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

## COBOL Settings and DISAM File
This repository includes a COBOL program (gldetlcsvcg.cbl) for processing financial data. If you are interested in modifying or understanding the COBOL settings, please consider the following:

## COBOL Compiler
The COBOL program is designed to be compiled using a COBOL compiler. In this example, GnuCOBOL is recommended.
Follow the documentation of your chosen COBOL compiler for installation and compilation instructions.
## DISAM File
The repository contains a DISAM file (disam72_x86_64bit_eval.tar.gz) for storing settings related to the COBOL program.
## Compiling and Running the COBOL Program
Compile the COBOL program:
bash
Copy code
cobc -x gldetlcsvcg.cbl

## Contact
For any inquiries, please contact Mary at [lefebvre.mary90272@gmail.com].

## Git Large File Storage (LFS) for managing large files:
 version https://git-lfs.github.com/spec/v1
oid sha256:cc111dacb6e452635d65a64462c80b1213ac44599f49d0e0401d76da90de5186
size 2620
