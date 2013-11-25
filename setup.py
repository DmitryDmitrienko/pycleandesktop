from distutils.core import setup

# See http://guide.python-distribute.org/
# See http://docs.python.org/distutils/setupscript.html

setup(
        name='pycleandesktop',
        description='Clean your desktop',
        author='Dmitry Dmitrienko',
        author_email='dmitry.dmitrienko@outlook.com',
        version='master', 
        packages=['cleandesktop'],
        license='BSD 2-clause "Simplified" License',
        url='http://ateska.github.com/ramona/',
        package_dir={
                'cleandesktop': 'src/cleandesktop'
        },
        package_data={
                'cleandesktop': ['data/*.json']
        },
)
