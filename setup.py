from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in worfinsta_v1/__init__.py
from worfinsta_v1 import __version__ as version

setup(
	name="worfinsta_v1",
	version=version,
	description="Influencer marketing platform for advertisers.",
	author="Amit kumar @ Worf",
	author_email="amit@worf.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
