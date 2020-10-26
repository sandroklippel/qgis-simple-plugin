# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2020 Sandro Klippel

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


__author__ = "Sandro Klippel"
__copyright__ = "Copyright 2020, Sandro Klippel"
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Sandro Klippel"
__email__ = "sandroklippel at gmail.com"
__status__ = "Prototype"
__revision__ = '$Format:%H$'


class Plugin:
    """Plugin implementation
    """    

    def __init__(self, iface):
        """Constructor

        Args:
            iface (qgis.gui.QgisInterface): a reference to the QGIS GUI interface
        """        
        self.iface = iface

    def initGui(self):
        """This method is called by QGIS when the main GUI starts up or when the plugin is enabled in the Plugin Manager.
        Only want to register the menu items and toolbar buttons here. 
        """        
        pass

    def unload(self):
        """Will be executed when the plugin is disabled. Either in the Plugin Manager or when QGIS shuts down.
        It only removes the previously defined QAction object from the menu and remove the plugin icon from the toolbar.
        """        
        pass

    def run(self):
        """executes the custom plugin functionality. [NOT REQUIRED]
        This method is called by the previously defined QAction object (callback), which went into the toolbar icon and the menu entry.
        """        
        pass