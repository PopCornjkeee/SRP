# -*- coding: utf-8 -*-

from spyre import server
import pandas


class VHIApp(server.App):
    title = "VHI App"

    inputs = [{"type": 'dropdown', "label": 'Часовий ряд1', "value": 'VHI',
               "options": [{"label": "VHI", "value": "VHI"},
                           {"label": "VCI", "value": "VCI"},
                           {"label": "TCI", "value": "TCI"}], "key": 'number'},

              {"type": 'dropdown', "label": 'Область', "value": 'Київська',
               "options": [{"label": "Вінницька", "value": "Вінницька"},
                           {"label": "Волинська", "value": "Волинська"},
                           {"label": "Дніпропетровська", "value": "Дніпропетровська"},
                           {"label": "Донецька", "value": "Донецька"},
                           {"label": "Житомирська", "value": "Житомирська"},
                           {"label": "Закарпатська", "value": "Закарпатська"},
                           {"label": "Запорізька", "value": "Запорізька"},
                           {"label": "Івано-Франківська", "value": "Івано-Франківська"},
                           {"label": "Київська", "value": "Київська"},
                           {"label": "Кіровоградська", "value": "Кіровоградська"},
                           {"label": "Львівська", "value": "Львівська"},
                           {"label": "Миколаївська", "value": "Миколаївська"},
                           {"label": "Одеська", "value": "Одеська"},
                           {"label": "Полтавська", "value": "Полтавська"},
                           {"label": "Рівненська", "value": "Рівненська"},
                           {"label": "Сумська", "value": "Сумська"},
                           {"label": "Тернопільська", "value": "Тернопільська"},
                           {"label": "Харківська", "value": "Харківська"},
                           {"label": "Херсонська", "value": "Херсонська"},
                           {"label": "Хмельницька", "value": "Хмельницька"},
                           {"label": "Черкаська", "value": "Черкаська"},
                           {"label": "Чернівецька", "value": "Чернівецька"},
                           {"label": "Чернігівська", "value": "Чернігівська"},
                           {"label": "Республіка Крим", "value": "Республіка Крим"}], "key": 'region'},

              #{"type": "slider", "label": 'Товщина лінії', "key": "width", "value": '1',
               #"min": 1, "max": 10, "action_id": "width"},
              {"type": "text", "label": 'Рік #1', "key": "y1", "value": '2007'},
              {"type": "text", "label": 'Інтервал тижнів, від', "key": "w1", "value": '1'},
              {"type": "text", "label": 'до', "key": "w2", "value": '52'}]

    controls = [{"type": "button", "label": "Побудувати графіки", "id": "submit_plot"}]
    tabs = ["Графік1", "Таблиця1"]
    outputs = [{"type": "plot", "id": "plot", "control_id": "submit_plot", "tab": "Графік1"},
               {"type": "table", "id": "table", "control_id": "submit_plot", "tab": "Таблиця1", "on_page_load": True}]

    @staticmethod
    def table(params):
        check_params(params)
        df = pandas.read_csv("E:\lab\Lab2\data1.csv", encoding='utf-8')
        df = df.drop('Unnamed: 0', 1)
        df = df[(df['region'] == params['region']) & (df['year'] == params['y1']) & (df['week'] >= int(params['w1'])) & (df['week'] <= int(params['w2']))]
        return df

    def plot(self, params):
        df = self.table(params)
        plt = df.plot(x='week', y=[params['number']])#, linewidth=params['width'])
        plt.set_title(params['y1'])
        return plt.get_figure()

def check_params(params):
    if int(params['y1']) < 1981: params['y1'] = 1981
    if int(params['y1']) > 2017: params['y1'] = 2017

    if int(params['w1']) < 1: params['w1'] = 1
    if int(params['w2']) > 52: params['w2'] = 52
    if int(params['w1']) > int(params['w2']):
        params['w1'] = 1
        params['w2'] = 52

app = VHIApp()
app.launch()

