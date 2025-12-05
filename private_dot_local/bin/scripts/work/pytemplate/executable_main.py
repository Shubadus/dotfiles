#!/usr/bin/env python3
from re import sub
import subprocess


from pathlib import Path
from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader('./templates/'))


def create_template():
    pass


def render_template(template_name: str):
    template = env.get_template(template_name)
    return template.render()


def list_templates(path: Path | str):
    # TODO: Right now this is set up for fuzzel, maybe move choice of dmenu to function to find first and an option in argparse to set manually by user
    if isinstance(path, str):
        if path.startswith('~'):
            path = Path(path).expanduser()
        else:
            path = Path(path).resolve()
    templates_paths = list(path.rglob("*.j2"))
    templates = "\n".join([f.name for f in templates_paths])
    result = subprocess.run(['fuzzel', '--dmenu', '--prompt=Templates: '], input=templates, capture_output=True, text=True)
    result.check_returncode()
    return result.stdout.strip()


def main():
    result = list_templates('~/.local/bin/scripts/work/pytemplate/templates/')
    output = render_template(result)
    subprocess.run(['wl-copy', output]).check_returncode()


if __name__ == '__main__':
    main()
