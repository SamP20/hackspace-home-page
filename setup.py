from setuptools import setup, find_namespace_packages

setup(
    name='bristolhackspace.homepage',
    packages=find_namespace_packages(include=['bristolhackspace.*']),
    package_data={
        "bristolhackspace": ["*"],
    },
    install_requires=[
        'flask>=2.0',
        'bristolhackspace.flask_theme',
    ],
)