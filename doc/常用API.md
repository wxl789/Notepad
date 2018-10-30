- 渲染模板

  返回值是一个字符串

  render_template("index.html")

- 获取url

  返回值是一个url

  url_for("to_index")

  url_for("blue_print.to_index")

  url_for("static",filename="css/css.css")

- 重定向

  返回值是一个response
  
  redirect(url_for('blue_print.to_index'))

