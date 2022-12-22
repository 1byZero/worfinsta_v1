# Copyright (c) 2022, Amit kumar @ Worf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from instagram_private_api import Client as AppClient
from instagram_private_api import ClientCookieExpiredError, ClientLoginRequiredError, ClientError, ClientThrottledError



class Scrapper(Document):
 
 def validate(self):
		username = self.influencer_username
	 
		frappe.msgprint(("We are going to Scrap this Instgram id '{0}'").format(
		username
		))
		scraper(username)


def scraper(target):

	u = darkmatterthething2021
	p = NvNDc3h35wZXYnT
	login(u,p)
	setTarget(target)

def setTarget(target):
        target = target
        user = get_user(target)
        target_id = user['id']
        is_private = user['is_private']
        following = check_following()
        


def login(u, p):
        try:
            settings_file = "config/settings.json"
            if not os.path.isfile(settings_file):

                # settings file does not exist
                print(f'Unable to find file: {settings_file!s}')

                # login new
                api = AppClient(auto_patch=True, authenticate=True, username=u, password=p,
                                     on_login=lambda x: onlogin_callback(x, settings_file))
									 
			

            else:
                with open(settings_file) as file_data:
                    cached_settings = json.load(file_data, object_hook=from_json)
                # print('Reusing settings: {0!s}'.format(settings_file))

                # reuse auth settings
                api = AppClient(
                    username=u, password=p,
                    settings=cached_settings,
                    on_login=lambda x: onlogin_callback(x, settings_file))
	

        except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
            print(f'ClientCookieExpiredError/ClientLoginRequiredError: {e!s}')

            # Login expired
            # Do relogin but use default ua, keys and such
            api = AppClient(auto_patch=True, authenticate=True, username=u, password=p,
                                 on_login=lambda x: onlogin_callback(x, settings_file))

        # except ClientError as e:
        #     pc.printout('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(e.msg, e.code, e.error_response), pc.RED)
        #     error = json.loads(e.error_response)
        #     pc.printout(error['message'], pc.RED)
        #     pc.printout(": ", pc.RED)
        #     pc.printout(e.msg, pc.RED)
        #     pc.printout("\n")
        #     if 'challenge' in error:
        #         print("Please follow this link to complete the challenge: " + error['challenge']['url'])
        #     exit(9)
	 
	 



	#  def __init__(self, target, is_file, is_json, is_cli, output_dir, clear_cookies):
    #     self.output_dir = output_dir or self.output_dir
    #     Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    #     u = config.getUsername()
    #     p = config.getPassword()
    #     self.clear_cookies(clear_cookies)
    #     self.cli_mode = is_cli
    #     if not is_cli:
    #       print("\nAttempt to login...")
    #     self.login(u, p)
    #     self.setTarget(target)
    #     self.writeFile = is_file
    #     self.jsonDump = is_json