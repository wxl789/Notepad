import flask_excel as excel

from flask import Blueprint, request
from flask.json import jsonify

from App.exp import db
from App.models.cement_model import Bill

from App.utils.cement_utils import add_data, update_data, del_data, get_data

bp = Blueprint("cement_BP", __name__, url_prefix="/cement/")


@bp.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def cement():
    method = request.method

    # 查询
    if method == "GET":
        params = request.args

        res = get_data(params)

        return jsonify(res)

    # 添加
    if method == "POST":
        '''
            将数据组成json一起post下来
        '''
        results = request.get_data()

        res = add_data(results)

        return jsonify(res)

    # 修改
    if method == "PUT":
        '''
            将要修改的数据通过json的格式传递
        '''
        results = request.get_data()

        res = update_data(results)

        return jsonify(res)

    # 删除
    if method == "DELETE":
        results = request.get_data()

        res = del_data(results)

        return jsonify(res)


@bp.route("/export/", methods=['GET'])
def do_custom_export():
    return excel.make_response_from_tables(db.session, [Bill, ], "xls", file_name="bill")


@bp.route("/custom_export", methods=['GET'])
def docustomexport():
    query_sets = Bill.query.all()

    column_names = ['id', 'date']

    return excel.make_response_from_query_sets(query_sets, column_names, "xls", file_name="bill")
