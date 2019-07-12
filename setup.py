import setuptools

with open("README.md", "r") as fh:
    long_des = fh.read()

setuptools.setup(
    name = "YEETER",
    version = "0.0.1",
    author = "Shashank Shirol",
    author_email = 'shashank.shirol1@gmaio.com',
    license = 'MIT',
    description = "A package to print YEET--fancy ways and normal ways;",
    long_description = long_des,
    url = "https://github.com/PonderfulWoop/YEETER",
    packages = ['YEETER']
)
