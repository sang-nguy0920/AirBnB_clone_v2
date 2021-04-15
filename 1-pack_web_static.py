#!/usr/bin/python3
""" generates a .tgz archive from contents of the web_static folder """

from fabric.api import local
import datetime


def do_pack():
    """ generates .tgz archive """
    generated_at = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p versions")
    new_dir = local("tar -cvzf versions/web_static_{}.tgz web_static/"
                    .format(generated_at))
    if new_dir.succeeded:
        return (new_dir)
    else:
        return None
