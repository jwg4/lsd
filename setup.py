from setuptools import setup

setup(
    name='lsd',
    version='0.3.2',
    description='Pounds, shillings and pence conversion',
    long_description=(
        "A library for converting between pre-decimal British" +
        " currency and decimal ('new pence') currency."),
    url='http://github.com/jwg4/lsd',
    author='Jack Grahl',
    author_email='jack.grahl@gmail.com',
    license='MIT',
    packages=['lsd'],
    zip_safe=False,
    test_suite="tests",
    tests_require=["hypothesis==4.26.3"]
)
