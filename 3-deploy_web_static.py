#!/usr/bin/python3
"""
 Fabric script that creates and distributes
 an archive to your web servers.
"""

from fabric.api import local, put, run, env
import datetime
import os
from os.path import exists

env.hosts = ['35.237.133.200', '54.160.239.103']


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


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False

    try:
        temp_path = archive_path.split("/")[-1]
        null_ext = temp_path.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, null_ext))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(temp_path, path, null_ext))
        run('sudo rm /tmp/{}'.format(temp_path))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, null_ext))
        run('sudo rm -rf {}{}/web_static'.format(path, null_ext))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, null_ext))
        return True

    except:
        return False


def deploy():
    """Full deployment"""
    archive_path = do_pack()
    print(archive_path)
    if archive_path is None:
        return False
    return do_deploy(archive_path)

deploy()
