# 作者：lucianaib
# 网站：https://lucianaib.blog.csdn.net/
# 日期：2025年1月15日
# 脚本名称：Cursor_ID_Change.py

from __future__ import print_function
import os
import sys
import json
import uuid
import shutil
import platform
from datetime import datetime
import errno


def get_storage_path():
    """获取配置文件路径"""
    system = platform.system().lower()
    home = os.path.expanduser('~')

    if system == 'windows':
        return os.path.join(os.getenv('APPDATA'), 'Cursor', 'User', 'globalStorage', 'storage.json')
    elif system == 'darwin':  # macOS
        return os.path.join(home, 'Library', 'Application Support', 'Cursor', 'User', 'globalStorage', 'storage.json')
    else:  # Linux
        return os.path.join(home, '.config', 'Cursor', 'User', 'globalStorage', 'storage.json')


def generate_random_id():
    """生成随机ID (64位十六进制)"""
    return uuid.uuid4().hex + uuid.uuid4().hex


def generate_uuid():
    """生成UUID"""
    return str(uuid.uuid4())


def backup_file(file_path):
    """创建配置文件备份"""
    if os.path.exists(file_path):
        backup_path = '{}.backup_{}'.format(
            file_path,
            datetime.now().strftime('%Y%m%d_%H%M%S')
        )
        shutil.copy2(file_path, backup_path)
        print('已创建备份文件:', backup_path)


def ensure_dir_exists(path):
    """确保目录存在（兼容 Python 2/3）"""
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def update_storage_file(file_path):
    """更新存储文件中的ID"""
    # 生成新的ID
    new_machine_id = generate_random_id()
    new_mac_machine_id = generate_random_id()
    new_dev_device_id = generate_uuid()

    # 确保目录存在
    ensure_dir_exists(os.path.dirname(file_path))

    # 读取或创建配置文件
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except ValueError:
            data = {}
    else:
        data = {}

    # 更新ID
    data['telemetry.machineId'] = new_machine_id
    data['telemetry.macMachineId'] = new_mac_machine_id
    data['telemetry.devDeviceId'] = new_dev_device_id
    data['telemetry.sqmId'] = '{' + str(uuid.uuid4()).upper() + '}'

    # 写入文件
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

    return new_machine_id, new_mac_machine_id, new_dev_device_id


def main():
    """主函数"""
    try:
        # 获取配置文件路径
        storage_path = get_storage_path()
        print('配置文件路径:', storage_path)

        # 备份原文件
        backup_file(storage_path)

        # 更新ID
        machine_id, mac_machine_id, dev_device_id = update_storage_file(storage_path)

        # 输出结果
        print('\n已成功修改 ID:')
        print('machineId:', machine_id)
        print('macMachineId:', mac_machine_id)
        print('devDeviceId:', dev_device_id)

    except Exception as e:
        print('错误:', str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
