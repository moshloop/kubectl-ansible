from setuptools import setup, find_packages
import os

setup(
  name = 'kubectl-ansible', version = '1.0',
  packages=find_packages(),
  url = 'https://www/github.com/moshloop/kubectl-ansible',
  author = 'Moshe Immerman', author_email = 'moshe.immerman@gmail.com',
  scripts = ['kubectl-ansible', 'kubectl-ansible-playbook']
)