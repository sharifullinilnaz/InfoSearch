from PyQt5.QtWidgets import QMainWindow
import webbrowser

from Task5.hooks.vector_search import VectorSearch
from Task5.View.WidgetModel import WidgetModel
import nltk

nltk.download('stopwords')
import json


class WidgetService(QMainWindow, WidgetModel):

    def __init__(self):
        super().__init__()
        self.showWindow(self)
        self.button_submit.clicked.connect(self.vector_search)


    def vector_search(self):
        self.items_list.clear()
        result = self.get_items(VectorSearch(self.query_text.text()).result)
        self.items_list.addItems(result.keys())
        self.items_list.itemClicked.connect(self.openBrowser)


    def openBrowser(self, item):
        result = self.get_items(VectorSearch(self.query_text.text()).result)
        webbrowser.open(result.get(str(item.text())))

    def get_items(self, site_index):
        with open('./index.txt', encoding="utf-8") as file:
            name = [row.strip() for row in file]
        sites = {}
        result = dict()
        for elem in name:
            dictData = json.loads(elem)
            sites[dictData["number"]] = dictData["link"]
        # пробегается по полученным из vector search
        for number in site_index:
            with open('./pages/page№' + str(number) + '.txt', encoding="utf-8") as file:
                name = [row.strip() for row in file]
            for elem in name:
                if (elem.startswith('<title>') and elem.endswith('</title>')):
                    result[elem.replace('<title>', '').replace('</title>', '').replace('-1', '')] = sites[number]
        return result
