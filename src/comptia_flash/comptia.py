from io import BytesIO
from typing import Type

import PyPDF2
import requests


class CompTIAData:
    acronym: str
    value: str


def get_comptia_data(exam_info: Type) -> list:
    # Request the pdf and use IO to parse the content instead of writing to user system
    response = requests.get(exam_info.url)
    content = BytesIO(response.content)

    read_pdf = PyPDF2.PdfReader(content)
    final_page_num = len(read_pdf.pages)

    comptia_string = ""
    for index, page in enumerate(read_pdf.pages):
        # final page contains extraneous info, skip it
        if index + 1 != final_page_num:
            comptia_string += page.extract_text()
    comptia_list = list(filter(None, comptia_string.split(exam_info.split_id)))
    # first item in the list is all the extraneous info before acronyms begin, so lets remove it
    comptia_list.pop(0)

    comptia_data_list = []
    for comptia_item in comptia_list:
        for item_2 in comptia_item.lstrip().split("\n"):
            if item_2:
                if item_2.count(" "):
                    acronym, acronym_value = item_2.split(" ", 1)
                else:
                    acronym = None
                    acronym_value = item_2

                comptia_data = CompTIAData()
                if acronym and acronym.isupper():
                    comptia_data.acronym = acronym
                    comptia_data.value = acronym_value
                    comptia_data_list.append(comptia_data)
                elif acronym and not acronym.isupper():
                    comptia_data_list[-1].value += acronym + acronym_value
                else:
                    comptia_data_list[-1].value += acronym_value
    comptia_data_list[-1].value = comptia_data_list[-1].value.replace(acronym_value, "")
    return comptia_data_list
