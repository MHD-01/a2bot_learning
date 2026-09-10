from setuptools import find_packages, setup

package_name = 'topics_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='course_student',
    maintainer_email='you@example.com',
    description='Module 3 starter package - a distance sensor and a watchdog that talk over a topic.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # "ros2 run topics_pkg distance_sensor" and
            # "ros2 run topics_pkg watchdog" both work out of the box -
            # you only need to fill in the TODOs inside each file.
            'distance_sensor = topics_pkg.distance_sensor:main',
            'watchdog = topics_pkg.watchdog:main',
        ],
    },
)
