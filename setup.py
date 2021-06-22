from setuptools import setup, find_namespace_packages


setup(name='helper_project',
      version='1.0.1',
      description='Personal assistant-helper. Addressbook. Notesbook. Folder cleaner',
      author='Anna Khodyka, Olga Fomenko, Nykyforets Vova',
      author_email='nvova@i.ua',
      license='MIT',
      entry_points={'console_scripts': ['helper_project=main:main']},
      include_package_data=True,
      packages=find_namespace_packages())