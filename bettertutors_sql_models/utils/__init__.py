from bettertutors_sql_models.base import db

row_to_dict = lambda row: {key: getattr(row, key) for key in row._meta.fields.keys()}

create_tables = lambda models: db.create_tables(models, safe=True)
