from setuptools import setup

package_name = 'mpu6050_pkg'

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
    maintainer='sebas',
    maintainer_email='juanmercado5331@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "mpu_sensor_msgs = mpu6050_pkg.mpu_sensor_msgs:main",
            "mpu6050_sub = mpu6050_pkg.mpu6050_sub:main"
        ],
    },
)
