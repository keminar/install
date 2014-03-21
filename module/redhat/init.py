# encoding: utf-8

import conf
from fabric.api import *
from core.utils import *
from module.common.init import init

class init(init):
	def install(self):
		self.bit = utils().bit()
		super(init, self).prepare()
		run('yum update -y')
		run('yum install -y gcc gcc-c++ gcc-g77 flex bison autoconf make automake ncurses-devel')
		run('yum install -y bzip2-devel zlib-devel libjpeg-devel libpng-devel libtiff-devel freetype-devel gettext-devel')
		run('yum install -y pam-devel openssl-devel libxml2-devel pcre-devel libcurl-devel openldap-devel readline-devel')
		if (self.bit == "64"):
			run('cp -frp /usr/lib64/libldap* /usr/lib/')
		if (self.epel() == "1"):
			run('yum install -y --nogpgcheck libmcrypt-devel')
		super(init, self).install()

	def epel(self):
		version = utils().version()
		fdUrl = conf.FEDORA_URL + '/pub/epel/' + version

		if (self.bit == "32"):
			fdUrl += '/i386/'
		else:
			fdUrl += '/x86_64/'

		if (version == "4"):
			fdUrl += 'epel-release-4-10.noarch.rpm'
		elif (version == "5"):
			fdUrl += 'epel-release-5-4.noarch.rpm'
		elif (version == "6"):
			fdUrl += 'epel-release-6-8.noarch.rpm'
		else:
			return '0'

		run('rpm -ivh ' + fdUrl, warn_only=True)
		return '1'

