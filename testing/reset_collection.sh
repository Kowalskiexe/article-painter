#!/usr/bin/env bash

testing_dir="$(dirname $(realpath "$0"))"
cd "$testing_dir"
cp "./collections/collection.anki2" "./AnkiDir/User 1/collection.anki2"
