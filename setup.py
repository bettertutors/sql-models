from setuptools import setup, find_packages

if __name__ == '__main__':
    package_name = 'bettertutors_sql_models'
    setup(
        name=package_name,
        author='Samuel Marks',
        version='0.1.2',
        test_suite=package_name + '.tests',
        packages=find_packages(),
        package_dir={package_name: package_name},
        package_data={package_name: ['logging.conf']},
        install_requires=[
            'peewee==2.4.7',
            'psycopg2'
        ]
    )
