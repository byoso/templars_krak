# Templars Krak

This simple tool purpose is to allow to use entire folder structures as templates. It works in terminal only.

### Installation
first, a little dependence to install:
```
pip install flamewok
```

Then just copy the script `templars` and the folder `templars_krak` into your `~/bin` folder to access this script from anywhere.

### How to use it
In a terminal enter `templars`, your stored templates will then be listed, just choose the one you want to copy in your working directory.

e.g:
```
1* : some folder
2* : another folder
3  : a file

*: [is a directory: add a space and dot after the index (eg:'1 .') to copy 'deployed']

select an index (0 to exit)
> 2        # does a straight copy of your templates (just copy the folder)

> 2 .      # does a loose copy of your templates (copy the inside of the folder)
```
Well, just try, it is easy :P

### Included templates
As I use it myself, I leave in the templar's krak some useful templates for building flask applications quickly.
