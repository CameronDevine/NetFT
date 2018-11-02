from setuptools import setup, find_packages

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
    name = "NetFT",
    version = "0.6",
    packages = find_packages(),
	author = "Cameron Devine",
	author_email = "camdev@uw.edu",
	description = "A Python library for reading data from ATI Force/Torque sensors with a Net F/T interface box.",
	long_description = long_description,
	license = "BSD",
	keywords = "Robotics Force Torque Sensor NetFT ATI Data Logging",
	url = "https://gitlab.cs.washington.edu/camdev/Net-FT-py",
	scripts = ['bin/NetFT']
)
