import re
from tika import parser
from bs4 import BeautifulSoup

class PDFHandler():

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def open_pdf(self, filepath, xml = True):
        pdf = parser.from_file(filepath, xmlContent=xml)

        for key, value in pdf.items():
            setattr(self, key, value)

        if xml:
            self._treat_xml()
        else:
            self._treat_plaintext()


    def _treat_xml(self):
        self.content = BeautifulSoup(self.content, "html.parser")
        self.content = [el.text for el in self.content if len(el.text.strip())]

        filtered = []

        for el in self.content:
            el = el.split("\n")
            el = [x.strip() for x in el]

            filtered += el

        self.content = [el.strip() for el in filtered if len(el.strip())]


    def _treat_plaintext(self):
        self.content = self.content.splitlines()
        self.content = [el.strip() for el in self.content if len(el.strip())]


    def get_values_by_pattern(self, regexp):
        pattern = re.compile(regexp)
        
        matches = [pattern.search(el) for el in self.content if pattern.match(el)]
        matches = [match.group(1) for match in matches]
        
        return matches


    def get_pdf_content(self):
        return self.content


    def get_pdf_status(self):
        return self.status

    
    def get_pdf_metadata(self):
        return self.metadata