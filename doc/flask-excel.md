# 1.插件说明

​	使用的是flask-excel.0.0.7插件,但是这个插件依赖另外两个插件pyexcel-xls和pyexcel-xlsx,否则官方文档的函数无法运行.

```
flask_excel
pyexcel-xls
pyexcel-xlsx
```

# 2.实例

```
from flask import Flask, request, jsonify, redirect, url_for
import flask_excel as excel

#初始化
excel.init_excel(app)

###list数据导出
@bp.route("/download", methods=['GET'])
def download_file():
	'''
		将列表中的数据生成bill.csv文件提供下载
	'''
    return excel.make_response_from_array(
        [
            ['2018-12-01','下沙',6,'李文明','呵呵哒',230,'许俊峰',100],
            ['2010-12-12','金沙和',29,'矜持','撒地方',1212,'敖东',200],
        ],

        "csv",
        file_name="bill"
    )

##多张表一起导出
@app.route("/export", methods=['GET'])
def doexport():
'''
	将Bill表中的数据导出,生成xls文件提供下载,(可以多张表一起导出)
'''
    return excel.make_response_from_tables(db.session, [Bill,], "xls")

##对数据库中的数据进行过滤后导出
@bp.route("/custom_export", methods=['GET'])
def do_custom_export():
'''
	按条件筛选出数据库中的数据,显示需要的列
'''
    query_sets = Bill.query.all()
    column_names = ['id', 'date']
    return excel.make_response_from_query_sets(query_sets, column_names, "xls",file_name="bill")



```

