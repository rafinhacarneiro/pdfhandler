# PDF Handler

Reads PDF files and returns data with regexp

## Requirements

- [Java Runtime Enviroment](https://www.java.com/pt-BR/download/manual.jsp)
- [Apache Tika](https://github.com/chrismattmann/tika-python)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

## Keywords

```
Open Pdf             path-to-file.pdf

@{CONTENT} =         Get Pdf Content

@{SELECTED} =        Get Values By Pattern   ^.*(\\d{2}/\\d{2}/\\d{4}).*$

&{METADATA} =        Get Pdf Metadata

${STATUS} =          Get Pdf Status
```