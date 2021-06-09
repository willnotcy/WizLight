from setuptools import find_packages, setup
setup(
    name='WizLight',
    packages=find_packages(include=['WizLight']),
    version='0.1.0',
    description='Wiz light python bridge',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)