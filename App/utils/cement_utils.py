from builtins import len

from flask import json

from App.models.cement_model import Bill


def get_data(params):
    '''
    传参cmd决定查询方向
    :param params:
    :return:
    '''
    cmd = params.get("cmd")

    page_nu = params.get("page_nu")

    page_nu = int(page_nu) if page_nu else 1

    if cmd == "all":

        datas = Bill.get(page=page_nu)

    elif cmd == "date":
        param = params.get("date")

        datas = Bill.get(condition=Bill.date, condition_prama=param, page=page_nu)

    elif cmd == "kpr":
        param = params.get("kpr")

        datas = Bill.get(condition=Bill.kai_piao_ren, condition_prama=param, page=page_nu)

    elif cmd == "siji":
        param = params.get("siji")

        datas = Bill.get(condition=Bill.si_ji, condition_prama=param, page=page_nu)

    else:
        return {
            "code": 0,
            "msg": "参数%s不存在" % cmd,
            "data": "",
        }

    # 总页面
    page_nums = datas.pages
    # 当前在第几页
    page_index = datas.page
    # 上一页是否存在
    has_prev = datas.has_prev
    # 下一页是否存在
    has_next = datas.has_next
    # 当前页数据
    dataArr = []

    code = 0

    for bill in datas.items:
        dataArr.append(bill.model_to_dict())
        code = 1

    return {
        "code": code,
        "msg": "获取数据成功" if code == 1 else "没有任何数据",
        "data": dataArr,
        "page_index": page_index,
        "page_nums": page_nums,
        "has_prev": has_prev,
        "has_next": has_next,
    }


def add_data(results):
    '''
    向数据库中批量添加数据
    :param results: post下来的json数据
    :return:
    '''

    try:
        results = json.loads(results)

        datas = results.get("data")
    except:
        return {
            "code": 0,
            "msg": "数据不是json标准格式,或入参没有data关键字",
            "data": "",
        }

    bill_li = []

    for data in datas:
        bill = Bill()

        bill.date = data.get('date')

        bill.destination = data.get('destination')

        bill.si_ji = data.get('si_ji')

        bill.kai_piao_ren = data.get('kai_piao_ren')

        bill.t = data.get('t')

        bill.price = data.get('price')

        bill.notes = data.get('notes')

        bill_li.append(bill)

    if len(bill_li) > 0:
        try:
            Bill.add(bill_li)
        except:
            return {
            "code": 0,
            "msg": "入参错误",
            "data": "",
        }

        res = {
            "code": 1,
            "msg": "数据添加成功",
            "data": "",
        }
    else:
        res = {
            "code": 0,
            "msg": "没有数据需要添加",
            "data": "",
        }

    return res


def update_data(results):
    try:
        results = json.loads(results)

        datas = results.get("data")
    except:
        return {
            "code": 0,
            "msg": "数据不是json标准格式,或入参没有data关键字",
            "data": "",
        }

    bill_li = []

    for data in datas:

        try:
            bill = Bill.query.get(data.get('id'))

            bill.id = data.get('id')

            bill.date = data.get('date')

            bill.destination = data.get('destination')

            bill.si_ji = data.get('si_ji')

            bill.kai_piao_ren = data.get('kai_piao_ren')

            bill.t = data.get('t')

            bill.price = data.get('price')

            bill.notes = data.get('notes')

            bill_li.append(bill)

        except:
            return {
                "code": 0,
                "msg": "id不存在",
                "data": "",
            }

    if len(bill_li) > 0:
        try:
            Bill.add(bill_li)
        except:
            return {
                "code": 0,
                "msg": "入参错误",
                "data": "",
            }

        res = {
            "code": 1,
            "msg": "数据修改成功",
            "data": "",
        }
    else:
        res = {
            "code": 0,
            "msg": "没有数据需要修改",
            "data": "",
        }

    return res


def del_data(results):
    try:
        results = json.loads(results)

        datas = results.get("data")
    except:
        return {
            "code": 0,
            "msg": "post的数据不是json标准格式,或入参没有data关键字",
            "data": "",
        }

    try:
        for data in datas:
            bill = Bill.query.get(data.get('id'))
            Bill.delete(bill)

        res = {
            "code": 1,
            "msg": "删除成功",
            "data": "",
        }

    except:
        res = {
            "code": 0,
            "msg": "需要删除的数据id不存在",
            "data": "",
        }

    return res
