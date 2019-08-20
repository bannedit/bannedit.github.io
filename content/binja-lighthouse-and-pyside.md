Title: Binary Ninja and Lighthouse on OSX
Date: 2019-08-19 21:00
Modified: 2017-11-27 12:30
Category: Development
Tags: binary ninja, binja, lighthouse, reversing, code coverage, plugins
Slug: Binary-Ninja-and-Lighthouse-on-OSX
Status: Draft
Authors: bannedit
Summary:<p>Recently, I purchased a personal license of binary ninja to play around with the API. However, I was also interested in tinkering around with Lighthouse since I've been fairly interested in fuzzing and code coverage lately.</p><p>Sadly, Lighthouse uses PyQT5. Anyone who has ever tried to get PyQT5 working on OSX knows how big of a headache that can be. It typically involved downloading and compiling source code.</p><p>Luckily, Lighthouse also supports PySide. PySide is available via brew and is much simpler to install. However, some minor patching is still required since the version installed by brew is PySide2.</p>

### Introduction

Recently, I purchased a personal license of binary ninja to play around with the API. However, I was also interested in tinkering around with Lighthouse since I've been fairly interested in fuzzing and code coverage lately.

Sadly, Lighthouse uses PyQT5. Anyone who has ever tried to get PyQT5 working on OSX knows how big of a headache that can be. It typically involved downloading and compiling source code.

Luckily, Lighthouse also supports PySide. PySide is available via brew and is much simpler to install. However, some minor patching is still required since the version installed by brew is PySide2.

### Lets Get To Work
To install PySide2 via brew simply run the following command:
```
$ brew install pyside
```

You can double check the installation by testing the import in python.
```
$ python
>>> import PySide2
>>>
```

The next thing we need to do is point Binary Ninja to our brew python installation. The simplest way to do this is to go to the Preferences->Settings menu option and click on Python in the left panel. Now on the right should be a drop down option. The version needed should look something like: 

*/usr/local/Cellar/python@2/2.7.16/Frameworks/Python.framework/Versions/2.7/Python*

Finally, we need to slightly patch Lighthouse. Normally Lighthouse imports PySide instead of PySide2. So this is a pretty simple patch all that is required is to reference PySide2 in the import statements instead of PySide.


**plugin/lighthouse/util/qt/shim.py**
```python
51: # if PyQt5 did not import, try to load PySide
52: if QT_AVAILABLE == False:
53:    try:
54:        import PySide2.QtGui as QtGui
55:        import PySide2.QtCore as QtCore
56:        import PySide2.QtWidgets as QtWidgets
```

Now if we move the contents of the plugin directory into ~/Library/Application Support/Binary Ninja/plugins/

```
$ cd lighthouse/plugin
$ cp -r . "$HOME/Library/Application Support/Binary Ninja/plugins"
``` 

The plugins directory should now look like this:

```
$ ls "$HOME/Library/Application Support/Binary Ninja/plugins"
lighthouse/            lighthouse_plugin.py
```

Now if we load up Binary Ninja we should see that everything works as expected. Obviously, getting PyQT5 working is the most ideal situation since several other useful plugins seem to be using it as well. So, with that in mind I plan on circling back to this in an effort to get PyQT5 working. I will try to do a follow up write up on the process involved in getting everything working for that as well.

### Conclusion

Lighthouse is a great plugin. Having it available in binary ninja should prove very useful. I was initially disappointed that Lighthouse didn't just work out of the box, but with a little work I managed to get it working and plan on using it a lot in the future. Hopefully, other people find this useful as well.
