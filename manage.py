#!/usr/bin/env python
import os
import sys
import dj_database_url

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_haystack_sample.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}