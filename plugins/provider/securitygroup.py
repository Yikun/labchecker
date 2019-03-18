from cmd import Plugin
import commands
import yaml

class SecurityGroupPlugin(Plugin):

    failed = False
    reason = ""

    def get_clouds(self):
        with open('/etc/openstack/clouds.yaml') as f:
            clouds = yaml.load(f)
            clouds_list = [c for c in clouds['clouds']]
        return clouds_list


    def check(self):
        clouds = self.get_clouds()
        for cloud in clouds:
            tcp_rule = 'openstack --os-cloud %s security group rule list default \
            --protocol tcp --ingress -f value \
            -c "IP Range" -c "Port Range" -c "Ethertype" -c "Remote Security Group" \
            |grep 0.0.0.0 |grep None | awk \'{print $2}\'' % cloud
            res = commands.getoutput(tcp_rule)
            if "19885:19885" not in res:
                self.failed = False
                self.reason = "IPV4 ingress 19885 port check failed."
            if "22:22" not in res:
                self.failed = False
                self.reason = "IPV4 ingress 19885 port check failed."
            if self.failed:
                print("Provider (%s) security group check: \033[1;31m FAILED \033[0m") % cloud
                print("Reason: \n%s")
            else:
                print("Provider (%s) security group check: \033[1;32m PASSED \033[0m") % cloud

