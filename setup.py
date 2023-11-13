from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here, if applicable
        # For example, if you use 'random' module in your program, you don't need to add it here.
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz:main',  # Assuming your main function is in math_quiz.py
        ],
    },
    ],
)
