from App.exp import db


class ModelFun:
    @classmethod
    def commit(cls):
        db.session.commit()
        return None

    @classmethod
    def add(cls, instance):

        if isinstance(instance, list):
            db.session.add_all(instance)
        else:
            db.session.add(instance)

        cls.commit()

        return None

    @classmethod
    def delete(cls, instance):

        if isinstance(instance, list):
            for obj in instance:
                db.session.delete(obj)
        else:
            db.session.delete(instance)

        cls.commit()

        return None

    @classmethod
    def get(cls, condition=None, condition_prama=None, page=1, pre_page=10):
        '''
            分页获取数据,默认是从第一页开始显示,每页显示10条数据
        :param page: 第几页
        :param pre_page: 每页显示的个数
        :return: Pagination 对象
        '''
        datas = None

        if condition and condition_prama:
            datas = cls.query.filter(condition == condition_prama).paginate(page, pre_page)

        else:

            datas = cls.query.paginate(page, pre_page)

        return datas


class Bill(db.Model, ModelFun):
    __tablename__ = "bill"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)

    date = db.Column(db.Date, nullable=False)

    destination = db.Column(db.String(45), nullable=False)

    si_ji = db.Column(db.String(45), nullable=False)

    kai_piao_ren = db.Column(db.String(45), nullable=False)

    t = db.Column(db.Integer, nullable=False)

    price = db.Column(db.Integer, default=0)

    notes = db.Column(db.String(150), nullable=True)

    def model_to_dict(self):
        return {
            "id": self.id,
            "date": str(self.date),
            "si_ji": self.si_ji,
            "kai_piao_ren": self.kai_piao_ren,
            "t": self.t,
            "price": self.price,
            "notes": self.notes,
            "destination": self.destination
        }
