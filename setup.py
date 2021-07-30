#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'ip_address_skill.chatterbox = ip_address_skill:IpSkill'

setup(
    name='chatterbox_ip_address_skill',
    version='0.0.1a1',
    description='default ip_address skill',
    url='https://github.com/HelloChatterbox/skill-ip-address',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['ip_address_skill'],
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='chatterbox plugin skill',
    entry_points={
        'holmes.plugin.skill': PLUGIN_ENTRY_POINT,
    }
)
