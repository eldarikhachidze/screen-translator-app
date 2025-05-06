from setuptools import setup, find_packages

setup(
    name='screen-translator-app',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'tk',
        'pytesseract',
        'Pillow',
        'requests',
        'google-cloud-texttospeech'
    ],
    entry_points={
        'console_scripts': [
            'screen-translator=app.main:main'
        ]
    },
)