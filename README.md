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

PDF used in example : [example.pdf](https://github.com/abitoun-42/colibrie/files/9620593/boc_20210034_0000_0003_extract_2.pdf)


```
from colibrie.extract_tables import extract_table

tables = extract_table('example.pdf')

for table in tables:
   print(table.to_html())
   print(table.to_df())
```

### Output :
<table><tr><td style="text-align:center;" rowspan=1 colspan=4>Classiﬁ cation des associations agréées de surveillance <br>
de la qualité de l’air<br>
</td><td style="text-align:center;" rowspan=1 colspan=4>Classiﬁ cation des bureaux d’études techniques, <br>
des cabinets d’ingénieurs-conseils <br>
et des sociétés de conseils<br>
</td></tr><tr><td style="text-align:center;" rowspan=1 colspan=1>Catégorie<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>Échelon<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>Coefﬁ cient<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>Salaire <br>
minimal <br>
hiérarchique<br>
</td><td style="text-align:center;" rowspan=1 colspan=1></td><td style="text-align:center;" rowspan=1 colspan=1>Position<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>Coefﬁ cient<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>Salaire <br>
minimal <br>
hiérarchique<br>
</td></tr><tr><td style="text-align:center;" rowspan=3 colspan=1>7<br>
</td><td style="text-align:center;" rowspan=3 colspan=1>1<br>
2<br>
3<br>
4<br>
5<br>
6<br>
7<br>
8<br>
9<br>
10<br>
11<br>
12<br>
</td><td style="text-align:center;" rowspan=3 colspan=1>255<br>
268<br>
282<br>
296<br>
311<br>
327<br>
344<br>
362<br>
381<br>
401<br>
422<br>
444<br>
</td><td style="text-align:center;" rowspan=3 colspan=1>1 307,13 €<br>
1 373,77 €<br>
1 445,53 €<br>
1 517,30 €<br>
1 594,19 €<br>
1 676,20 €<br>
1 763,34 €<br>
1 855,61 €<br>
1 953,01 €<br>
2 055,53 €<br>
2 163,17 €<br>
2 275,94 €<br>
</td><td style="text-align:center;" rowspan=6 colspan=1>ETAM<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>1.1.<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>230<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>1 558,80 €<br>
</td></tr><tr><td style="text-align:center;" rowspan=1 colspan=1>1.2.<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>240<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>1 587,50 €<br>
</td></tr><tr><td style="text-align:center;" rowspan=1 colspan=1>1.3.<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>250<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>1 618,50 €<br>
</td></tr><tr><td style="text-align:center;" rowspan=3 colspan=1>6<br>
</td><td style="text-align:center;" rowspan=3 colspan=1>1<br>
2<br>
3<br>
4<br>
5<br>
6<br>
7<br>
8<br>
9<br>
10<br>
11<br>
12<br>
</td><td style="text-align:center;" rowspan=3 colspan=1>310<br>
326<br>
344<br>
363<br>
384<br>
406<br>
430<br>
457<br>
485<br>
515<br>
549<br>
585<br>
</td><td style="text-align:center;" rowspan=3 colspan=1>1 589,06 €<br>
1 671,08 €<br>
1 763,34 €<br>
1 860,74 €<br>
1 968,38 €<br>
2 081,16 €<br>
2 204,18 €<br>
2 342,58 €<br>
2 486,11 €<br>
2 639,89 €<br>
2 814,17 €<br>
2 998,71 €<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>2.1.<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>275<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>1 683,75 €<br>
</td></tr><tr><td style="text-align:center;" rowspan=1 colspan=1>2.2.<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>310<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>1 786,70 €<br>
</td></tr><tr><td style="text-align:center;" rowspan=1 colspan=1>2.3.<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>355<br>
</td><td style="text-align:center;" rowspan=1 colspan=1>1 922,60 €<br>
</td></tr></table>

|    | 0                                                            | 1           | 2               | 3                | 4                                                    | 5            | 6               | 7                |
|---:|:-------------------------------------------------------------|:------------|:----------------|:-----------------|:-----------------------------------------------------|:-------------|:----------------|:-----------------|
|  0 | Classiﬁ cation des associations agréées de surveillance <br> | <NA>        | <NA>            | <NA>             | Classiﬁ cation des bureaux d’études techniques, <br> | <NA>         | <NA>            | <NA>             |
|    | de la qualité de l’air<br>                                   |             |                 |                  | des cabinets d’ingénieurs-conseils <br>              |              |                 |                  |
|    |                                                              |             |                 |                  | et des sociétés de conseils<br>                      |              |                 |                  |
|  1 | Catégorie<br>                                                | Échelon<br> | Coefﬁ cient<br> | Salaire <br>     |                                                      | Position<br> | Coefﬁ cient<br> | Salaire <br>     |
|    |                                                              |             |                 | minimal <br>     |                                                      |              |                 | minimal <br>     |
|    |                                                              |             |                 | hiérarchique<br> |                                                      |              |                 | hiérarchique<br> |
|  2 | 7<br>                                                        | 1<br>       | 255<br>         | 1 307,13 €<br>   | ETAM<br>                                             | 1.1.<br>     | 230<br>         | 1 558,80 €<br>   |
|    |                                                              | 2<br>       | 268<br>         | 1 373,77 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 3<br>       | 282<br>         | 1 445,53 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 4<br>       | 296<br>         | 1 517,30 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 5<br>       | 311<br>         | 1 594,19 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 6<br>       | 327<br>         | 1 676,20 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 7<br>       | 344<br>         | 1 763,34 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 8<br>       | 362<br>         | 1 855,61 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 9<br>       | 381<br>         | 1 953,01 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 10<br>      | 401<br>         | 2 055,53 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 11<br>      | 422<br>         | 2 163,17 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 12<br>      | 444<br>         | 2 275,94 €<br>   |                                                      |              |                 |                  |
|  3 | <NA>                                                         | <NA>        | <NA>            | <NA>             | <NA>                                                 | 1.2.<br>     | 240<br>         | 1 587,50 €<br>   |
|  4 | <NA>                                                         | <NA>        | <NA>            | <NA>             | <NA>                                                 | 1.3.<br>     | 250<br>         | 1 618,50 €<br>   |
|  5 | 6<br>                                                        | 1<br>       | 310<br>         | 1 589,06 €<br>   | <NA>                                                 | 2.1.<br>     | 275<br>         | 1 683,75 €<br>   |
|    |                                                              | 2<br>       | 326<br>         | 1 671,08 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 3<br>       | 344<br>         | 1 763,34 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 4<br>       | 363<br>         | 1 860,74 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 5<br>       | 384<br>         | 1 968,38 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 6<br>       | 406<br>         | 2 081,16 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 7<br>       | 430<br>         | 2 204,18 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 8<br>       | 457<br>         | 2 342,58 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 9<br>       | 485<br>         | 2 486,11 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 10<br>      | 515<br>         | 2 639,89 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 11<br>      | 549<br>         | 2 814,17 €<br>   |                                                      |              |                 |                  |
|    |                                                              | 12<br>      | 585<br>         | 2 998,71 €<br>   |                                                      |              |                 |                  |
|  6 | <NA>                                                         | <NA>        | <NA>            | <NA>             | <NA>                                                 | 2.2.<br>     | 310<br>         | 1 786,70 €<br>   |
|  7 | <NA>                                                         | <NA>        | <NA>            | <NA>             | <NA>                                                 | 2.3.<br>     | 355<br>         | 1 922,60 €<br>   |
-------------------------------------------------------------------------------------
