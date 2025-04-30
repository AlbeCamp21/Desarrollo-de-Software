#!/usr/bin/env bash

find . -type f -name "*.html" -print0 | xargs -0 zip archivos_html.zip
