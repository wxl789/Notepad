# ORM

## 1.插件

​    Flask-SQLAchemy

### 1.1安装插件

​    pip install  Flask-SQLAchemy

### 1.2初始化插件

```
db = SQLAlchemy()

# Flask-SQLAlchemy插件
def init_db(app):
    db.init_app(app)
    
```

## 数据库操作

### 创建数据库

​    db.create_all(object)
    

### 删除库

​    db.delete_all(object)
    

### 添加数据

​    db.session.add(obj)  #添加一条
    db.session.add_all(list[obj])#批量添加

###     删除数据

​    db.session.delete(obj)
    

### 提交数据

​    db.session.commit()
    

### 查询数据

​    object.query.all()  #获取表中的全部数据

#### filter()

​    object.query.filter(过滤条件)

#### 在filter中可以使用的逻辑运算

```
and_(a>b,a<d)
or_(a>b,a<d)
not_(a == b)
```



#### filter_by()

​    通常用在级联上
    object.query.filter_by()

#### offset()

​    设置偏移量
    object.query.offet(number)

#### limit()

​    获取前number个数据
    object.query.limit(number)
    实现分页
    object.query.offset(nu).limit(nu+number)

#### slice(start,end)

​    实现分页
    object.query.slice(nu,nu+number)
    等同于:
    object.query.offset(nu).limit(nu+number)

#### paginate()

​    实现分页
        page--第几页
        per_page -- 每页显示多少数据
        error_out --  当分页查询出现异常的时候 是否抛出错误 默认抛出 改为Flase
    

    pagination = object.query.paginate(page,per_page)
    pagination的属性有:
          pagination.pages      #分页后的总页数
                    page        #当前页码  
                    per_page    #每页显示数据的条数
                    prev_num    #返回上一页的页码
                    next_num    #返回下一页的页码
                    has_prev    #是否存在上一页
                    has_next    #是否存在下一页 
                    
                    items       #返回当前页的数据(返回的类型为list,list中保存的是object类的实例)
                    iter_pages
    pagination对象的方法:
            pagination.iter_pages()  #页码的generator
                      .prev()        #返回上一页的对象
                      .next()        #返回下一页的对象

#### order_by()

​    升序排序
    object.query.order_by("s_age").offset(nu).limit(nu+number)
    降序排序
    object.query.order_by("-s_age").offset(nu).limit(nu+number)

#### get()

​    根据主键获取数据
    object.query.get(15)

#### first()

​    获取第一个数据
    object.query.all().first()

