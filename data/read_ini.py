from common.read_tools import ReadFileData
from common.path_tools import getPath

def get_ini_data(args):
    '''
    读取ini的内容
    :param args:
    :return:
    '''
    name, key = args
    patah = getPath()
    read = ReadFileData()
    file_path = patah.get_path() + '\config.ini'
    ini_data = read.load_ini(file_path)
    value = ini_data[name][key]
    return value





# get_ini_data(['HTTP','login_url'])
# get_page_data(LoginPageData.username_selectors)

