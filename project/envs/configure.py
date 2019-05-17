from os import environ

# Map namespaced or arbritrary environment keys to names in settings.
KEY_MAPPING = {
    "DJANGO_SECRET_KEY": "SECRET_KEY"
}


def set_required_key(key, fallback=None):
    if (key not in globals() or globals()[key] is None) and key in environ or fallback:
        if key in environ:
            if key in KEY_MAPPING:
                globals()[KEY_MAPPING[key]] = environ[key]
            else:
                globals()[key] = environ[key]
            return
        else:
            if fallback:
                globals()[key] = fallback
                return

    raise KeyError("Missing %s variable.  Please set in .env file, and try again." % key)


# Django configuration
# Internal private key, used for security.  Keep this safe!
set_required_key("DJANGO_SECRET_KEY")

# Website configuration

# Friendly name, used for internal communication
set_required_key("WEBSITE_FRIENDLY_NAME")

# Unique name for the shop, used to configure internal services
set_required_key("WEBSITE_NAMESPACE")

# The base URL for the shop.
set_required_key("WEBSITE_DOMAIN")
globals()["WEBSITE_BASE_URL"] = "https://%s" % globals()["WEBSITE_DOMAIN"]

# Shop admin's name
set_required_key("WEBSITE_ADMIN_NAME")

# Shop admin's email address
set_required_key("WEBSITE_ADMIN_EMAIL")

# The default email address that outgoing email should be sent from
set_required_key("WEBSITE_FROM_EMAIL")

# Key and domain for your Mailgun account
# set_required_key("MAILGUN_API_KEY")  # From https://app.mailgun.com/app/account/security/api_keys
# set_required_key("MAILGUN_SENDER_DOMAIN")  # i.e. mail.mydomain.com

# AWS
# set_required_key("AWS_STORAGE_BUCKET_NAME")
# set_required_key("AWS_S3_HOST")
# set_required_key("AWS_ACCESS_KEY_ID")
# set_required_key("AWS_SECRET_ACCESS_KEY")


# Database config
set_required_key("POSTGRES_DB", "not set")
set_required_key("POSTGRES_USER", "not set")
set_required_key("POSTGRES_PASSWORD", "not set")

