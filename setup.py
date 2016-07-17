from setuptools import setup
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

setup(name='static_response_server',
      version='0.1',
      description='Static response server for REST pocs',
      url='https://github.com/alexrochas/static-response-server',
      author='Alex Rocha',
      author_email='alex.rochas@yahoo.com.br',
      license='MIT',
      packages=['server'],
      install_requires=reqs,
      entry_points={
          'console_scripts': ['static-response-server=server.server:start'],
      },
      include_package_data=True,
      zip_safe=False)
