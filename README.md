# THIS PROJECT IS STILL A WORK IN PROGRESS
RenameIO is a tool for renaming batches of files using a few commands on the command line.

## How to use?
How to use is still a WIP.

### What is preferences.json?
Fundamentally it is a settings file, you can set the properties to better fit your use cases. Below there is a table with all properties available at the moment.
|Property|Description|Default value|Accepted values|
|--|--|--|--|
|`filtering_behaviour`|Controls what the filter does to what doesn't pass the check.|`vanish`|`vanish`; `italics`
|`auto_reset_filter`|Clears the filter when you trigger the `filter` function again. | `True` | `True`; `False`
|`use_filter_once` | Clears the filter once it is used | `False` | `True`; `False`
| `pressets_folder` | Folder where pressets are stored | `/pressets`| Any directory path


## Used technologies.

- Python;
- UV.

## Used softwares.

-   Git - Version control;
-   VSCode - Code editing.