"""Connection settings shared by publish.py and subscribe.py.

Every value can be overridden with an environment variable, so certificates
and the endpoint never have to be written into the code.
"""
import os

CLIENT_ID = os.environ.get("IOT_CLIENT_ID", "333")
ENDPOINT = os.environ.get("IOT_ENDPOINT", "endpoint")  # e.g. abc123-ats.iot.eu-central-1.amazonaws.com
PORT = int(os.environ.get("IOT_PORT", "8883"))
ROOT_CA = os.environ.get("IOT_ROOT_CA", "./AmazonRootCA1.pem")
PRIVATE_KEY = os.environ.get("IOT_PRIVATE_KEY", "./333.private.key")
CERTIFICATE = os.environ.get("IOT_CERTIFICATE", "./333.cert.pem")
TOPIC = os.environ.get("IOT_TOPIC", "general/inbound")
