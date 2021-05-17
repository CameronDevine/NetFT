from setuptools import setup, find_packages

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
    name = "NetFT",
    version = "2.0.1",
    packages = find_packages(),
	author = "Cameron Devine",
	author_email = "camdev@uw.edu",
	description = "A Python library for reading data from ATI Force/Torque sensors with a Net F/T interface box.",
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	license = "BSD",
	keywords = "Robotics Force Torque Sensor NetFT ATI Data Logging",
	url = "https://github.com/CameronDevine/NetFT",
	project_urls={"Documentation": "https://netft.readthedocs.io/en/latest/"},
	scripts = ['bin/NetFT']
)
