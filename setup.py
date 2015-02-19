from setuptools import setup, find_packages

if __name__ == '__main__':
    package_name = 'bettertutors_sql_models'
    setup(
        name=package_name,
        author='Samuel Marks',
        version='0.1.5',
        test_suite='test',
        packages=filter(lambda p: p != 'test', find_packages()),  # exclude='test' doesn't work
        package_data={package_name: ['logging.conf']},
        install_requires=[
            'peewee==2.4.7',
            'psycopg2'
        ]
    )
