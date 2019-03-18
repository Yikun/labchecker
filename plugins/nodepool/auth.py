from labcheck import Plugin
import yaml


class AuthPlugin(Plugin):

    type = 'nodepool'
    name = 'Auth Check'
    failed = False
    reasons = []

    def check(self):
        with open('/var/lib/nodepool/.config/openstack/clouds.yaml') as f:
            clouds = yaml.load(f)
            op_clouds = [c for c in clouds['clouds']]

        with open('/etc/nodepool/nodepool.yaml') as np:
            clouds = yaml.load(np)
            np_clouds = [c['cloud'] for c in clouds['providers']]

        for cloud in np_clouds:
            if cloud in op_clouds:
                self.failed = True
                self.reasons.append("The clouds.yaml is not set.")
            self.print_result(cloud)