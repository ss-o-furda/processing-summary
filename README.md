# Processing investigation summary

As a result, we get two programs that perform the same action, namely, modify 60 photos of very cute cats and save them to a folder on the disk.
We use Pillow library to add some Gaussian Blur and resize image.

### Sync

The result of executing the synchronous version will be 60 photos of cats, which were processed in 32.63 seconds (in my case. it may be different for you, it also depends on the CPU).

The full log can be seen at [logs](sync_option.log).

### Process

The result of running the version using processing will be 60 photos of cats, which were processed in 9.66 seconds (in my case, yours may be different, also depends on the CPU).

The full log can be seen at [logs](process_option.log).

## Conclusion

Using processing in this case made the program three times faster.

## How to run?

**To run these files and verify the correctness of the programs yourself, you will also need an image library**

to install it you need:

on **macOS**/**linux**:

```
python3 -m venv env

source env/bin/activate

pip3 install Pillow
```

on **windows**:

```
python -m venv env

env/Scripts/activate.bat //In CMD
env/Scripts/Activate.ps1 //In Powershel

pip install Pillow
```

**once installed you can use the following commands**:

### Sync program

on **macOS**/**linux**:

```
python3 sync_option.py
```

on **windows**:

```
python sync_option.py
```

### Process program

on **macOS**/**linux**:

```
python3 process_option.py
```

on **windows**:

```
python process_option.py
```
