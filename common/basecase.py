import yaml


class BaseCase:
    """公共方法"""

    def get_data(self):
        with open('/Users/madong/PycharmProjects/pythonProject1/data/add.yaml', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            add_data = data['data']['add']
            ids_data = data['data']['ids']
        return add_data, ids_data


basecase = BaseCase()
