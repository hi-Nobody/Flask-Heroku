import os

basedir = os.path.abspath(os.path.dirname(__file__))
print(os.path.join(basedir,'app.db'))
class Config (object):
    #Database configuration
    #為了防止受到外部攻擊，所以利用變數的方式儲存DB位置，其中會從DATABASE_URL變數中獲取DB的url，若沒有則將會在專案的basedir創建一個app.db的資料庫
    """
    1.在Unix/Mac中sqlite:////為絕對路徑，而sqlite:///為相對路徑
    2.在Windows中
      a.雙斜線為絕對路徑，需要轉義，ex:'sqlite:///C:\\path\\to\\foo.db'
      b.若是路徑使用原始字符串，需要防止轉義(要加r)，ex: r'sqlite:///C:\path\to\foo.db'
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or r'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False