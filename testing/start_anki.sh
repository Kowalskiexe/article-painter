#!/usr/bin/env bash

testing_dir="$(dirname "$(realpath $0)")"
anki -b "$testing_dir/AnkiDir"
