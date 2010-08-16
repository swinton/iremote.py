iremote.py - Provides a Python-compatible interface for the Apple Remote
========================================================================

Usage
-----
1. Install iremoted from <http://github.com/swinton/iremoted> along with this Python module.

2. Construct your source code like so:

        from iremote import IRemote

        def my_iremote_handler(event):
            if event == IRemote.NEXT:
                # Next button pressed
                # ...

        iremote = IRemote()
        iremote.add_listener(my_iremote_handler)
        iremote.start()

