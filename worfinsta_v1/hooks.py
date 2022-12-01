from . import __version__ as app_version

app_name = "worfinsta_v1"
app_title = "Worfinsta V1"
app_publisher = "Amit kumar @ Worf"
app_description = "Influencer marketing platform for advertisers."
app_email = "amit@worf.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/worfinsta_v1/css/worfinsta_v1.css"
# app_include_js = "/assets/worfinsta_v1/js/worfinsta_v1.js"

# include js, css files in header of web template
# web_include_css = "/assets/worfinsta_v1/css/worfinsta_v1.css"
# web_include_js = "/assets/worfinsta_v1/js/worfinsta_v1.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "worfinsta_v1/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "worfinsta_v1.utils.jinja_methods",
#	"filters": "worfinsta_v1.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "worfinsta_v1.install.before_install"
# after_install = "worfinsta_v1.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "worfinsta_v1.uninstall.before_uninstall"
# after_uninstall = "worfinsta_v1.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "worfinsta_v1.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"worfinsta_v1.tasks.all"
#	],
#	"daily": [
#		"worfinsta_v1.tasks.daily"
#	],
#	"hourly": [
#		"worfinsta_v1.tasks.hourly"
#	],
#	"weekly": [
#		"worfinsta_v1.tasks.weekly"
#	],
#	"monthly": [
#		"worfinsta_v1.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "worfinsta_v1.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "worfinsta_v1.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "worfinsta_v1.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"worfinsta_v1.auth.validate"
# ]

app_include_js = ['main.bundle.js']
app_include_css = ['style.bundle.css']