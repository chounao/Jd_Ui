import yaml
import json
from configparser import ConfigParser

class MyconfigParser(ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class ReadFileData():
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            return data

    def load_json(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def load_ini(self, file_path):
        config = MyconfigParser()
        config.read(file_path, encoding='utf-8')
        data = dict(config._sections)
        # print(data)
        # print(data['HTTP']['jd_loginUrl'])
        return data

class ReadPagedata():
    def read_page(self,page,selectors):
        if hasattr(page,selectors):
            data = getattr(page,selectors)
            by = data(selectors)[0]
            value = data(selectors)[1]
            return by,value
        else:
            return None,None



class yaml_tool:
    def save_yaml(self,path,save_data):
        """保存yaml"""
        print(path,save_data)
        with open(path, "w", encoding="utf-8") as f:
            f.write(save_data)
    def save_yaml_dict(self,path,save_data):
        """保存成字典"""
        with open(path,"w",encoding="utf-8")as f:
            yaml.dump(save_data,f)
    def read_yamlDatas(self,path):
        """获取token和参数方法"""
        self.token_data =ReadFileData.load_yaml(path)

        return self.token_data
    def read_data(self,key,value,path):
        try:
            self.data = self.read_yamlDatas(path)
            if key in self.data.keys():
                return self.data[key][value]
        except :
            print("找不到对应的%s ",key)

# if __name__ == '__main__':
#     from common.path_tools import getPath
#     a = ReadFileData()
#     path = getPath()
#     config_path = '\config.ini'  # ini文件路径
#     file_path = path.get_path() + config_path
#     a.load_ini(file_path)
