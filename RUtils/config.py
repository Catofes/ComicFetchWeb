__author__ = 'herbertqiao'

import RUtils.singleton as singleton


class RConfig(singleton.Singleton):
    """Config Class

    This class store some import parameters of the app.
    Such as database username, password, etc.
    """

    def __init__(self):
        if hasattr(self, '_init'):
            return
        self._init = True
        self.password="changePassword"
