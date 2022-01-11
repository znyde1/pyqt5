import os
import sys

import numpy as np
from PyQt5.QtWidgets import QApplication
from functions import Myclass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = Myclass()
    myWin.show()
    sys.exit(app.exec_())
