# PageLoader

[![Actions Status](https://github.com/Evglit/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/Evglit/python-project-lvl3/actions)
[![Python CI](https://github.com/Evglit/python-project-lvl3/actions/workflows/pyci.yml/badge.svg)](https://github.com/Evglit/python-project-lvl3/actions/workflows/pyci.yml)<br>
<a href="https://codeclimate.com/github/Evglit/python-project-lvl3/maintainability"><img src="https://api.codeclimate.com/v1/badges/1f727325c967b9263a4d/maintainability" /></a>
<a href="https://codeclimate.com/github/Evglit/python-project-lvl3/test_coverage"><img src="https://api.codeclimate.com/v1/badges/1f727325c967b9263a4d/test_coverage" /></a><br><br>

## Description
PageLoader – утилита командной строки, которая скачивает страницы из интернета и сохраняет их на компьютере. Вместе со страницей она скачивает все ресурсы (картинки, стили и js) давая возможность открывать страницу без интернета.

## Installation

``` bash
pip install --user --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pageloader
```

## Usage

``` bash
usage: page-loader [-h] [-o OUTPUT] [-l LOG_LEVEL] url

This utility downloads pages from the Internet.

positional arguments:
  url

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        output dir (default: "/app")
  -l LOG_LEVEL, --log_level LOG_LEVEL
                        set log level
```

## Example 1. Downloading a page to the current directory.
[![asciicast](https://asciinema.org/a/3O4WQcydsbe6Su4Ji5fcPpJyb.svg)](https://asciinema.org/a/3O4WQcydsbe6Su4Ji5fcPpJyb)

## Example 2. Downloading the page to the specified directory.
[![asciicast](https://asciinema.org/a/HHZcyWtOyqQrr7vaCyn6TRBGg.svg)](https://asciinema.org/a/HHZcyWtOyqQrr7vaCyn6TRBGg)

## Example 2. Downloading a page to the specified directory in debug mode.
[![asciicast](https://asciinema.org/a/bscdKZuUAeAZxQkelz2ctQiCy.svg)](https://asciinema.org/a/bscdKZuUAeAZxQkelz2ctQiCy)
