import os

class getPath():
    def get_path(self):
        """获取路径"""
        self.path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        return self.path
    def get_tokenpath(self,tokenData_path):
        """拼装存储token路径"""
        self.token_path = self.path +tokenData_path
        return self.token_path
    def get_parameterpath(self,parameterData_path):
        """拼装存储参数路径"""
        self.parameter_path = self.path+parameterData_path
        return self.parameter_path