from setuptools import setup, find_packages

version = "0.1"


setup(
    name="django-uptime",
    version=version,
    description="Editable non-cached monitorization path for Django",
    long_description="""
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 1.11",
    ],
    keywords="moritorization,uptime",
    author="Urtzi",
    author_email="uodriozola@codesyntax.eus",
    url="https://github.com/codesyntax/django-uptime",
    license="MIT license",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
