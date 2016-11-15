# ZNC Monitor / Launching Script

This script is a Python 2.7 script designed to be used with Cron to monitor if ZNC is running, and if it is not, run it.

To use it:

 1. Clone the repository, or copy the `znc_monitor.py` script (https://github.com/teward/znc_monitor/blob/master/znc_monitor.py).

 2. Edit the value of `ZNC_BINARY_FILE` and `ZNC_EXECUTABLE_LOCATION` accordingly.  (`znc` being in `/usr/bin/znc` are used as the current 'defaults').
 
 3. Test the script with `znc` not running, and then execute the script with `python znc_monitor.py` (or `python2 znc_monitor.py` if Python3 is the default on your system).
 
 4. Set up a cron job.  I recommend every five minutes.  Edit `/path/to/znc_monitor.py` to be the actual path to the Python script:
 
    ```
*/5 * * * * python /path/to/znc_monitor.py
```

    (use `python2` if your default Python is Python3).
    
That's it!  Not too complicated!

Contributions are welcome, please use a pull request to propose changes.  Changes must be in Git.  Changes must also be explained.
