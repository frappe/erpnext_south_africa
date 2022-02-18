from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_south_africa/__init__.py
from erpnext_south_africa import __version__ as version

setup(
	name="erpnext_south_africa",
	version=version,
	description="App to hold regional code for South Africa, built on top of ERPNext.",
	author="Frappe Technologies Private Limited",
	author_email="contact@frappe.io",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
