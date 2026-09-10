from setuptools import find_packages, setup

package_name = 'my_first_pkg'

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
    description='Module 2 starter package - write your first ROS 2 node here.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # This line is why "ros2 run my_first_pkg heartbeat" works -
            # it points at the main() function inside heartbeat.py.
            'heartbeat = my_first_pkg.heartbeat:main',
        ],
    },
)
