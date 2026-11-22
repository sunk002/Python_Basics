# 任务1 · SQLAlchemy ORM 练习：设备 Inventory 系统

import os
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# ① 声明基类
Base = declarative_base()

class Device(Base):
    __tablename__ = "devices"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    name        = Column(String(50), index=True, nullable=False)   # 建索引
    type        = Column(String(50), nullable=False)
    version     = Column(String(50))
    location    = Column(String(100))
    create_time = Column(DateTime, default=datetime.now)          

    def __repr__(self):
        return (
            f"Device(设备名称: {self.name} | 类型: {self.type} | "
            f"版本: {self.version} | 位置: {self.location} | "
            f"入库时间: {self.create_time})"
        )


device_list = [
    {'name': 'R1', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Beijing-IDC-A'},
    {'name': 'R2', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Shanghai-IDC-B'},
    {'name': 'SW1', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Beijing-IDC-A'},
    {'name': 'SW2', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Shanghai-IDC-B'},
    {'name': 'FW1', 'type': 'firewall', 'version': 'ASA 9.16', 'location': 'Beijing-IDC-A'},
    {'name': 'FW2', 'type': 'firewall', 'version': 'FTD 7.2', 'location': 'Shenzhen-IDC-C'},
]

def init_db(session):
    """只在空表时插入初始数据,避免重新运行翻倍"""
    if session.query(Device).count() == 0:     #新库才插数据，否则跳过
        for d in device_list:               #变量d
            session.add(Device(**d))        #字典解包
        session.commit()
        print("[INFO] 初始化设备数据成功,已写入 6 条记录")
    else:
        print("[INFO] 数据库已有数据,跳过初始化")


# ④ 四种查询
def show_all(session):
    for dev in session.query(Device).all():
        print(dev)


def query_by_name(session, name):
    for dev in session.query(Device).filter_by(name=name).all():
        print(dev)


def query_by_type(session, dtype):
    for dev in session.query(Device).filter_by(type=dtype).all():
        print(dev)


def query_by_location(session, keyword):
    for dev in session.query(Device).filter(Device.location.like(f"%{keyword}%")).all():
        print(dev)


# ⑤ 菜单
def menu():
    print("请选择查询方式：")
    print("输入 1：查询所有设备")
    print("输入 2：根据设备名称查询")
    print("输入 3：根据设备类型查询")
    print("输入 4：根据机房位置查询")
    print("输入 0：退出")


def main():
    # 数据库文件路径:当前目录下的 devices.db
    db_path = os.path.abspath("devices.db")
    engine = create_engine(f"sqlite:///{db_path}")

    Base.metadata.create_all(engine)          # 建表(已存在则跳过),持久化关键

    Session = sessionmaker(bind=engine)    #会话工厂，类
    session = Session()          #造一个会话实例 Session()

    print(f"[INFO] 数据库文件路径: {db_path}")
    init_db(session)

    while True:
        menu()
        choice = input("请输入查询选项：").strip()

        if choice == "1":
            show_all(session)
        elif choice == "2":
            name = input("请输入设备名称：").strip()
            query_by_name(session, name)
        elif choice == "3":
            dtype = input("请输入设备类型（router/switch/firewall）：").strip()
            query_by_type(session, dtype)
        elif choice == "4":
            keyword = input("请输入机房位置关键词：").strip()
            query_by_location(session, keyword)
        elif choice == "0":
            print("退出程序。")
            break
        else:
            print("无效选项,请重新输入。")

    session.close()


if __name__ == "__main__":
    main()
