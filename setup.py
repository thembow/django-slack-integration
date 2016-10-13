from setuptools import setup, find_packages

setup(
    name='django-slack-integration',
    version='0.0.1',
    description='Slack integration for Django.',
    author='Quantum',
    author_email='quantum@dmoj.ca',
    url='https://github.com/DMOJ/django-slack-integration',
    keywords='django slack messaging',
    packages=find_packages(),
    include_package_data=True,
    license='GNU AGPLv3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: User Interfaces',
    ],
    zip_safe=False,
)
