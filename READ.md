# Project Title

Davening angle to the Kosel from any named place on Earth.

## Description

talPYot is a Python package that provides the davening angle to the Kosel, from any given named location on Earth.
The name is derived from the word Talpiot, which the Gemora Berachos 30a references.
The Gemora says that wherever you are davening, you must face in the direction of the Kosel. Then the Gemora quotes the source to this:
מאי קראה {שיר השירים ד-ד} כמגדל דויד צוארך בנוי לתלפיות, תל שכל פיות פונים בו

### Dependencies

* geopy

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* python3 main.py London

The results will be in a JSON format, like this:

{
    "LocationName": "London, Greater London, England, United Kingdom",
    "DaveningAngle": 119.15978935488904,
    "DirectionCompass": "       ooooooo       \n     oo       oo     \n    o           o    \n   o             o   \n  o               o  \n o                 o \n o                 o \no                   o\no                   o\no                   o\no         ..        o\no           ..      o\no             ..    o\no               .   o\n o                 o \n o                 o \n  o               o  \n   o             o   \n    o           o    \n     oo       oo     \n       ooooooo       "
}


## Authors

Dror Maor 
dror.m.maor@gmail.com

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE file for details

