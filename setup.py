from setuptools import setup, find_packages

version = "1.0.0" # Use SemVer

setup(
	name='coglist',
	version=version,
	packages=find_packages(),
	url='https://github.com/coglist/cogs',
	license='MIT',
	author='vcokltfre, elfq, tag-epic',
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=[
        "templatebot"
    ],
	description='A collection of cogs to create Discord bots with.',
	python_requires='>=3.6',
)