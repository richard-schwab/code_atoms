## Error Tracing

Saves which line / error your error is to a variable.   

Especially useful if using a try: / except: but you want to pass and still know which file and line the error was in.

### Example:  

`
from error_trace import get_error

empty_list = []

try:
    first_item = empty_list[0]

except IndexError:
    error_and_line = get_error(print=True)
    pass

`
