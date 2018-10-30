# web中形成json串

```
//json对象转换成json字符串
JSON.stringify({"data": dataArr})  #json官方的转换方式
或
$.parseJSON({"data": dataArr});
```
# web中解析json数据

```angular2html
//由JSON字符串转换为JSON对象
    var obj = eval('(' + jsonstr + ')');  #这种方式不安全eval会执行json串中的表达式
或
    var obj = jsonstr.parseJSON();   
或
    var obj = JSON.parse(jsonstr); #json官方的转换方式
```

# Python中生成json字符串

```angular2html
json.dumps({'a': 1, 'b':1}
或
jsonify({'a': 1, 'b': 2})
```
## json.dumps和 jsonify的区别:

```angular2html
    使用jsonify时响应的Content-Type字段值为application/json，
    而使用json.dumps时该字段值为text/html。
    Content-Type决定了接收数据的一方如何看待数据，如何处理数据，
    如果是application/json，则可以直接当做json对象处理，
    若是text/html，则还要将文本对象转化为json对象再做处理
```

# Python中解析json

```angular2html
json.loads(jsonstr)
```