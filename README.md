Sample Python Selenium Cucumber Framework

The tech stack used in this project are:

    Python as the programming language for writing test code
    Cucumber as the framework
    PIP3 as the build tool
    VSCode as the preferred IDE for writing python code.

Getting Started

Setup your machine.

    Python > 3.11
    Install VSCode & open the repo
    On Terminal, navigate to repo and run following commands a. Create Virtual Env python3 -m venv behavex-env b. Activate Virtual Env source behavex-env/bin/activate c. Install Packages pip3 install -r requirements.txt

Running tests

    Run tests in Sequence: browser=chrome behavex
    Run tests in Parallel: browser=chrome behavex --parallel-processes 5 --tags @test

Report

    Report will be found here: /output/report.html
