from setuptools import setup, find_namespace_packages


setup(name='helper',
      version='1.0.5',
      description='Personal assistant-helper. Addressbook. Notesbook. Folder cleaner',
      author='Anna Khodyka, Olga Fomenko, Nykyforets Volodymyr',
      author_email='nvova@i.ua',
      license='MIT',
      entry_points={'console_scripts': ['helper=helper.main:main']},
      include_package_data=True,
      packages=find_namespace_packages())