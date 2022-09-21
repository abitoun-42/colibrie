# Colibrie
 [![image](https://img.shields.io/pypi/v/colibrie.svg)](https://pypi.org/project/colibrie/) [![image](https://img.shields.io/pypi/l/colibrie.svg)](https://pypi.org/project/colibrie/)

Colibrie is a blazing fast tool to extract tables from PDFs 

## Why Colibrie?

- :rocket: **Efficient**: Colibrie is faster by multiple order of magnitude than any actual existing solution
- :sparkles: **Fidel visual**: Colibrie can provide 1:1 HTML representation of any tables it'll find
- :books: **Reliable**: Colibri will find every valid tables without exception if the PDF is compatible with the core principle of Colibrie
- :memo: **Output**: Each table can be export into to multiple formats, which include : 
  - Pandas Dataframe.
  - HTML.

### Benchmark :
Some number to compare [Camelot](https://github.com/camelot-dev/camelot) (a popular library to extract tables from PDF) and Colibrie
<table>
  <thead>
    <tr>
        <th colspan="2"></th>
        <th colspan="4">Tables extracted</th>
        <th colspan="2"></th>
    </tr>
    <tr>
        <th colspan="2">Times in second</th>
        <th colspan="2">camelot</th>
        <th colspan="2">colibrie</th>
        <th colspan="2"></th>
    </tr>
    <tr style="text-align: right;">
      <th>camelot</th>
      <th>colibrie</th>
      <th>valid</th>
      <th>false positive</th>
      <th>valid</th>
      <th>false positive</th>
      <th>pages count</th>
      <th>pdf file</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.53</td>
      <td>0.00545</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td><a href="https://github.com/abitoun-42/colibrie/files/9620468/boc_20220014_0001_p000_extract_2.pdf">small pdf</a></td>
    </tr>
    <tr>
      <td>5.95</td>
      <td>0.02100</td>
      <td>4</td>
      <td>0</td>
      <td>4</td>
      <td>0</td>
      <td>11</td>
      <td><a href="https://github.com/abitoun-42/colibrie/files/9620506/boc_20210034_0000_0003.pdf">medium pdf</a></td>
    </tr>
    <tr>
      <td>105.00</td>
      <td>0.21900</td>
      <td>62</td>
      <td>1</td>
      <td>62</td>
      <td>0</td>
      <td>167</td>
      <td><a href="https://github.com/abitoun-42/colibrie/files/9620511/boc_20220014_0001_p000.pdf">big pdf</a></td>
    </tr>
    <tr>
      <td>182.00</td>
      <td>0.69000</td>
      <td>175</td>
      <td>1</td>
      <td>177</td>
      <td>0</td>
      <td>269</td>
      <td><a href="https://github.com/abitoun-42/colibrie/files/9620515/boc_20220025_0001_p000.pdf">giant pdf</a></td>
    </tr>
  </tbody>
</table>

## Installation

### using source
```
pip install poetry

git clone https://github.com/abitoun-42/colibrie.git

cd colibrie

poetry install
```
### using pip
```
pip install colibrie
```

## Usage
```
from colibrie.extract_tables import extract_table

tables = extract_table('pdf_path')
```
