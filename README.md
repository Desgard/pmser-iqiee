# pmser-iqiyi
🤖 Automatic weekly record robot. Write the weekly record quickly. 

## Screenshot

![](public/screenshot.png)

## Introduction

### Install

```bash
$ clone https://github.com/Desgard/pmser-iqiyi.git
$ cd pmser-iqiyi
$ source venv/bin/activity
$ pip install -r requirement.txt
$ chmod +x pmser-cli.py
```

### Help

```bash
$ ./pmser-cli.py -h
usage: pmser-cli.py [-h] [-u USER] [-w] [-a]

To build the weekly report quickly!

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Filter the item of this user.
  -w, --week            Only show this week report.
  -a, --all             [Default] Show all issues about the user.
```

### Usage

```bash
$ ./pmser-cli.py -u xxxx -w
$ ./pmser-cli.py -u xxxx -a
```

## MIT License

Copyright (c) 2017 Desgard_Duan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.