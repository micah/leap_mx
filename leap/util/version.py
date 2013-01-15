#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
version.py
----------
Version information for leap_mx.

@authors: Isis Agora Lovecruft, <isis@leap.se> 0x2cdb8b35
@licence: see included LICENSE file
@copyright: 2013 Isis Agora Lovecruft
'''

import os

from twisted.python import versions

name    = 'leap_mx'
version = versions.Version(name, 0, 0, 1, None)
authors = [('Isis Agora Lovecruft', '<isis@leap.se>', '0x2cdb8b35'),]
git_url = 'https://github.com/isislovecruft/leap_mx/'
website = 'https://leap.se'

def getVersion():
    version.authors = authors
    version.git_url = git_url
    version.website = website
    return version

def getRepoDir():
    here = os.getcwd()
    base = here.rsplit(name, 1)[0]
    repo = os.path.join(base, name)
    return repo

def __make_text__(extra_text=None):
    splitter = "-" * len(version.__str__())
    header   = ["\n%s\n" % version.__str__(), "%s\n" % splitter]
    footer   = ["Website: \t%s\n" % website, "Github: \t%s\n" % git_url, "\n"]
    contacts = ["\t%s, %s %s\n" % (a[0], a[1], a[2]) for a in authors]
    contacts.insert(0, "Authors: ")

    with_contacts = header + contacts

    if extra_text is not None:
        if isinstance(extra_text, iter):
            with_contacts.extend((e for e in extra_text))
        elif isinstance(extra_text, str):
            with_contacts.append(extra_text)
        else:
            print "Couldn't add extra text..."

    text = with_contacts + footer
    return text

def __update_version__():
    repo = getRepoDir()
    version_file = os.path.join(repo, 'VERSION')
    version_text = __make_text__()

    with open(version_file, 'w+') as fh:
        fh.writelines((line for line in version_text))
        fh.flush()
        fh.truncate()


if __name__ == "__main__":
    print "Generating new VERSION file..."
    __update_version__()
    print "Done."