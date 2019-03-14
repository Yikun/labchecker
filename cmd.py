from plugins.base import Plugin

for plugin in Plugin.plugins:
    plugin.check()
