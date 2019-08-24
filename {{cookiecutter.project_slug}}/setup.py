from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='{{ cookiecutter.module_name }}',
    version='{{ cookiecutter.version }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=readme,
    author="{{ cookiecutter.full_name }}",
    author_email='{{ cookiecutter.email }}',
    packages=[
        '{{ cookiecutter.module_name }}',
    ],
    package_dir={'{{ cookiecutter.module_name }}':
                 '{{ cookiecutter.module_name }}'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='{{ cookiecutter.keywords }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)