# LUZ
## command line utility to retrieve system information

includes sysinfo for following information
- disk size of a path and size of all sub-folders under the given path
- OS build, flavor, architecture, version


## Usage:
### get help
```bash
luz --help (general Luz help)
luz disk --help  (Luz command help)
luz disk size --help (Luz subcommand help)
```

### Disk size information examples


```bash
luz disk size /home/user
```  
returns size of path on disk in KB

```ruby
luz disk size /etc/
total:  105,586 kb
```
----

```bash
luz disk size /home/user -v
```
returns size of path including all subfolders (and their size in bytes) as well as parent path in B, KB, MB and GB

----
return disk size in JSON form
```ruby
luz disk size /home/user --json
```

## Technical
### Packaging
``` sudo pip install -e . ```