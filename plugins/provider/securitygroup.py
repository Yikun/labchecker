from cmd import Plugin


class SecurityGroupPlugin(Plugin):
    def check(self):
        print("Checking SecurityGroupPlugin...")
