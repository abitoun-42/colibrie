# Colibrie
Colibrie is a blazing fast repository to extract tables from PDF files 

# Installation
### installation using source
```
pip install poetry

git clone https://github.com/abitoun-42/colibrie.git

cd colibrie

poetry install
```
### installation using pip
```
pip install colibrie
```

# Usage
```
from colibrie.extract_tables import extract_table

tables = extract_table('pdf_path')
```