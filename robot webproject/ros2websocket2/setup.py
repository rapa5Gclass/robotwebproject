from setuptools import setup
from setuptools import find_packages

package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='jyhh1992@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_package.my_node:main',
            'sub = my_package.sub:main',
            'sub2 = my_package.sub2:main',
            'sub3 = my_package.sub3:main',
            'batteryper = my_package.batteryper:main',
            'cmdx = my_package.cmdx:main',
            'cmdz = my_package.cmdz:main',
        ],
    },
)
