from bettertutors_sql_models.models.Signup import Signup

row_to_dict = lambda row: {key: getattr(row, key) for key in row._meta.fields.keys()}

create_tables = lambda db: db.create_tables([Signup], safe=True)
