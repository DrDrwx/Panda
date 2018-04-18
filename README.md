# Panda

## Description
Panda is a module which I have developed to stop me rewriting code.
So far it contains a Logger class.

## Logger: Features
Once initialised:
```python
logger = panda.Logger(logFile='panda.plog', verbose=True, write=True, debug=True)
```
The logger has the following options:
```python
- logger.log('Log message')
- logger.error('Error message')
- logger.debug('Debug message')
- logger.warning('Warning message')
- logger.success('Success message')
```
With example outputs:
```text
[2018-04-18 22:04:49] [-] Log message
[2018-04-18 22:04:49] [!] Error: Error message
[2018-04-18 22:04:49] [D] Debug: Debug message
[2018-04-18 22:04:49] [W] Warning: Warning message
[2018-04-18 22:04:49] [+] Success: Success message
```

Each of these functions have `verbose` and `write` flags preset.
You can overwrite each of these to further control the logging, an example:

```python
logger.debug('Something happened...')
```
Each function comes with a timestamp by default.
The above would output the following, for example:
```text
[2018-04-18 22:04:49] [D] Debug: Something happened...
```

However, is it possible to only print these to the screen by doing:
```python
logger.debug('Something happened...', write=False)
```
.. or to only write these to the log file, one can:
```python
logger.debug('Something happened...', verbose=False)
```

It is further possible to change the output's type, using `logType`:
```python
logger.log('Something happened...', logType='plus')

# Options include:
# plus [+], info [-], error [!], debug [D], warn [W]
```

### All Options
```python
logger.log("Log message.", logType="error", write=False, verbose=True)
# Options are set to true by default.
```
