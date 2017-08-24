import sys, shelve

def store_person(db):

    pid = input("输入唯一的ID:")
    person = {}
    person['name'] = input("输入名字：")
    person['age'] = input("输入年龄：")
    person['phone'] = input("输入手机号码：")
    db[pid] = person


def lookup_person(db):
    pid = input("输入ID:")
    field = input("输入你想知道的东西（名字，年龄，手机号码）")
    field = field.strip().lower()
    print(field.capitalize() + ':', db[pid][field])

def print_help():
    print("可用的命令有：")
    print("store : 保存一个人的信息")
    print("lookup: 通过ID查找人")
    print("quit  : 保存更改并退出")
    print("?     : 打印这个消息")

def enter_command():
    cmd = input("输入命令（？for help）:")
    cmd = cmd.strip().lower()
    return cmd


def main():
    database = shelve.open('J:\\practice\\python\\1.dat')
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_person(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print_help()
            elif cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__':
    main()




