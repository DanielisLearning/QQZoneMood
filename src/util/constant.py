# for localhost
REDIS_HOST = '127.0.0.1'
## for docker
REDIS_HOST_DOCKER = 'redis'

UNDEFINE_HOST = 'undefine'

POOL_FLAG = 'POOL_FLAG'

import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
BASE_PATH = os.path.split(rootPath)[0]
sys.path.append(BASE_PATH)

BASE_DIR = BASE_PATH + '/resource/'

qzone_jother = "(function(){ try{return (+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+[])+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+([][[]]+[])[!+[]+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(![]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+!![]+[])+([]+[][(![]+[])[!+[]+!![]+!![]]+([]+{})[+!![]]+(!![]+[])[+!![]]+(!![]+[])[+[]]][([]+{})[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]]+(![]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+[]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!![]+[])[+[]]+([]+{})[+!![]]+(!![]+[])[+!![]]]((!![]+[])[+!![]]+([][[]]+[])[!+[]+!![]+!![]]+(!![]+[])[+[]]+([][[]]+[])[+[]]+(!![]+[])[+!![]]+([][[]]+[])[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]+!![]+!![]]+(![]+[])[!+[]+!![]]+([]+{})[+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(!![]+[])[+[]]+([][[]]+[])[!+[]+!![]+!![]+!![]+!![]]+([]+{})[+!![]]+([][[]]+[])[+!![]])())[+[]]+([][[]]+[])[!+[]+!![]]+(+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+[])+(+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]]+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+([][[]]+[])[!+[]+!![]+!![]]+(![]+[])[+[]]+(+{}+[])[+!![]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+!![]+[])+(!+[]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+[]+[])+(+{}+[])[+!![]]+(!+[]+!![]+[])+(!+[]+!![]+!![]+[])+(+!![]+[])+(+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+([][[]]+[])[!+[]+!![]+!![]]+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(+{}+[])[+!![]]+(![]+[])[+[]]+(!+[]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(+{}+[])[+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]+!![]+!![]+!![]]+(![]+[])[+[]]+([][[]]+[])[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[])+([]+{})[!+[]+!![]]+(!+[]+!![]+!![]+!![]+!![]+[])+(!+[]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+[]);} catch(e) {var xhr = new XMLHttpRequest();xhr.withCredentials = true;xhr.open('post', '//h5.qzone.qq.com/log/post/error/qzonetoken', true);xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');xhr.send(e);}})()";

qzone_jother2 = "(function(){ try{return \"78b6507aba9a886c50d4e4c3974620ffa36c5ed768d10d60cd88bfbaf66b736d004aaacff6a32df499\";} catch(e) {var xhr = new XMLHttpRequest();xhr.withCredentials = true;xhr.open('post', '//h5.qzone.qq.com/log/post/error/qzonetoken', true);xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');xhr.send(e);}})();"

EXPIRE_TIME_IN_SECONDS = 24 * 60 * 60

WEB_SPIDER_INFO = "web_redis_info_"

LOGIN_SUCCESS = "登陆成功！"

LOGIN_NOT_MATCH = "QQ号不匹配"

LOGIN_FAILED = "由于网络等原因登陆失败，请重新扫描二维码或稍后再试"

WEB_IMAGE_PATH = BASE_PATH + '/src/web/static/image/'

GET_MOOD_FAILED = "获取主页信息失败"

GET_MAIN_PAGE_FAILED = "获取主页信息失败"

GET_FIRST_LOGIN_TIME = "获取第一次登陆时间失败"

FINISH_ALL_INFO = "获取全部信息完成"

MOOD_COUNT_KEY = 'mood_count_'
MOOD_FINISH_KEY = 'mood_finish_'
FRIEND_FINISH_KEY = 'friend_finish_'

MOOD_NUM_KEY = 'mood_num_'
FRIEND_NUM_KEY = 'friend_num_'

MOOD_NUM_PRE = 'QQ空间的说说数量'
FRIEND_INFO_PRE = 'QQ好友数量'

STOP_SPIDER_KEY = 'stop_spider_'
STOP_SPIDER_FLAG = 'stop'
FORCE_STOP_SPIDER_FLAG = 'force'
SPIDER_FLAG = 'continue'

CLEAN_DATA_KEY = 'clean_data_'

USER_MAP_KEY = 'qq_user_map'

USER_LOGIN_STATE = 'qq_user_login_state_'

SPIDERING_USER_LIST  = 'spidering_user_list'

WAITING_USER_LIST = 'waiting_user_list'

SPIDER_USER_NUM_LIMIT = 2

QR_CODE_MAP_KEY = 'qr_code_map_key'

STOP_FRIEND_INFO_SPIDER_KEY = 'stop_friend_info_'
FINISH_FRIEND_INFO_ALL = '获取全部好友基本信息完成'

FRIEND_INFO_COUNT_KEY = 'friend_info_count_'

HISTORY_LIKE_AGREE = 'history_like_agree_'

FRIEND_LIST_KEY = 'friend_list_'

FINISH_USER_NUM_KEY = 'finish_user_num_key'

# 电脑上的中文字体
UBUNTU_SYSTEM_FONT_PATH = '/usr/share/fonts/Songti.ttc'
MAC_SYSTEM_FONT_PATH = '/System/Library/Fonts/Hiragino Sans GB.ttc'

SYSTEM_FONT = UBUNTU_SYSTEM_FONT_PATH

if __name__ == '__main__':
    print(BASE_DIR)