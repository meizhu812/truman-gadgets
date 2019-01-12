# truman-gadgets
light useful gadgets in daily projects

## 2019-01-02
### v1.0.1 fix output consistency
#### example output:
```
>>> Listing files in folder:
--> [D:\Truman\projects\python\truman-gadgets\tgadgets]
--> [INIT]:'test_file'	[EXT]:'.tst'
--|
--| test_file_000.tst
--| test_file_001.tst
--| test_file_002.tst
--| test_file_003.tst
--| test_file_004.tst
--| test_file_005.tst
--| test_file_006.tst
--|..................
--| test_file_093.tst
--| test_file_094.tst
--| test_file_095.tst
--| test_file_096.tst
--| test_file_097.tst
--| test_file_098.tst
--| test_file_099.tst
--|
--# [ 100 ] files found.
### Check sequence of data files, press Enter to continue...


Cleaned testing files.
>>> Listing files in folder:
--> [D:\Truman\projects\python\truman-gadgets\tgadgets]
--> [INIT]:'test_file'	[EXT]:'.tst'
--|
--|..................
--|
--# [ 0 ] files found.
### Check sequence of data files, press Enter to continue...

>>> [Testing Timer...]
--|
01> [Action I...]
--| Sleep for 1 second.
01# [Action I Completed in 1.0 seconds.]
--|
02> [Action II...]
--| Sleep for 2 seconds.
02# [Action II Completed in 2.0 seconds.]
--|
### [Testing Timer Completed in 3.0 seconds.]


>>> [Testing MpProgress...]
--|
01> [Initializing...]
01# [Initializing Completed in 0.06 seconds.]
--|
02> [Testing 'map_async'...]
--| 100%...Finished.
--| Result = 12
02# [Testing 'map_async' Completed in 0.4 seconds.]
--|
03> [Testing 'apply_async'...]
--| 100%...Finished.
--| Result = 12
03# [Testing 'apply_async' Completed in 9.11 seconds.]
--|
### [Testing MpProgress Completed in 9.57 seconds.]

```
## 2019-01-02
### v1.0.0 Intial package uploaded
use `python setup.py install` to install the package
