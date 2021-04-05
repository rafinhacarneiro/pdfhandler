*** Settings ***
Library   ./PDFHandler.py
Library   Collections   

*** Tasks ***

Step 01: Teste
    Open my PDF File
    Get data from my PDF
  
*** Keywords ***

Open my PDF File
    Open Pdf             my_pdf_file.pdf


Get data from my PDF
    @{CONTENT} =         Get Pdf Content
    @{SELECTED} =        Get Values By Pattern   ^.*(\\d{2}/\\d{2}/\\d{4}).*$
    &{METADATA} =        Get Pdf Metadata
    ${STATUS} =          Get Pdf Status

    Log List             ${CONTENT}
    Log List             ${SELECTED}
    Log Dictionary       ${METADATA}
    Log                  ${STATUS}
