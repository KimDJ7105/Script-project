from setuptools import setup, find_packages

setup(
    name='ScriptProject',
    version='1.0',
    packages=find_packages(),
    py_modules=['main', 'noti', 'NV', 'teller','keys'],
    package_data={
        'ScriptProject' : ['bookmark_data.xml','spam.pyd'],
        'resource': ['ms.png', 'NV.png', 'plus.png', 'star.png', 'teleg.png', 'tree.png', 'bookmark_data.xml'],
    },
    include_package_data=True,
)