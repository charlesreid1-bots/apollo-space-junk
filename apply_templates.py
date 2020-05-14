import os, re, sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

"""
Apply Default Values to Jinja Templates
"""

TEMPLATE_FILES= ['service/apollo.service.j2']
REAL_FILES = [t[:-3] for t in TEMPLATE_FILES]

# Should existing files be overwritten
OVERWRITE = False

REQ_ENV_VARS = [
    'APOLLO_PATH',  # path to the apollo repo
    'APOLLO_USER',  # the user to run the service as
]

def usage():
    print(sys.argv[0], "usage:")
    print("")
    print("You must define the following environment variables")
    print("to render the Jinja templates:")
    for env_var in REQ_ENV_VARS:
        print(" "*4,env_var)

for env_var in REQ_ENV_VARS:
    if env_var not in os.environ:
        usage()
        raise Exception(f"Error: required env var not defined: {env_var}")

for template_file, real_file in zip(TEMPLATE_FILES, REAL_FILES):
    template_dir = os.path.basepath(template_file)
    env = Environment(loader=FileSystemLoader(template_dir))
    render_kwargs = {}
    for env_var in REQ_ENV_VARS:
        render_kwargs[env_var.lower()] = os.environ[env_var]
    content = env.get_template(template_file).render(**render_kwargs)


# Write to file
if os.path.exists(rfile) and not OVERWRITE:
    raise Exception("Error: file %s already exists!"%(rfile))
else:
    with open(rfile,'w') as f:
        f.write(content)

