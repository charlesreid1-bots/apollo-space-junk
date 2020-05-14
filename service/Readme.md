# uptime service

Directory containing files useful for creating a bot startup service
(on Linux, of course).

## Jinja Template

This directory contains a Jinja template for a systemd service
called `apollo.service` that can be installed to run on startup.
The Jinja template contains one parameter that is the location of
the uptime repo on disk.

To render the template using a user-sepcified path:

* Edit `render_template.py` to specify path of uptime repo
* Run `render_template.py` to create `apollo.service`

## Virtual Environment

To run the startup service, you must first create a virtualenv
in the `vp/` folder of the `uptime` repo. To do this, run this
command from the `uptime` repo:

```
virtualenv -p python3.6 vp && source vp/bin/activate'
```

Now install the required software:

```
pip install -r requirements.txt
```

Now the python exeutable at `{{ apollo_path }}/vp/bin/python` will
have the necessary libraries installed and can be used by the
service script.


