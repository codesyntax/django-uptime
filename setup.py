from setuptools import setup, find_packages

version = "0.4"


setup(
    name="django_uptime",
    version=version,
    description="Editable non-cached monitorization path for Django",
    long_description="""
    Editable non-cached monitorization path for Django. Standarized path for multiple django project moritorization
    """,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 4.0",
    ],
    keywords="moritorization,uptime",
    author="Urtzi",
    author_email="uodriozola@codesyntax.eus",
    url="https://github.com/codesyntax/django-uptime",
    license="MIT license",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Django>=1.11",
    ],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
