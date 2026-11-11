# aws-Iot-core-example

A minimal example of talking to **AWS IoT Core** over MQTT from Python
(learning project, 2022).

- `publish.py` connects as a device, sends one message to a topic and disconnects.
- `subscribe.py` listens to the same topic. When it receives the message
  `{"temperature"}`, it answers with the computer's CPU temperature.

## Requirements

- Python 3.8 or newer
- An AWS account with an IoT Core "thing", its certificate, private key
  and the Amazon root CA certificate

```bash
pip install -r requirements.txt
```

## Setup

1. In the AWS console: **IoT Core → Manage → Things → Create thing**, download the
   device certificate, the private key and `AmazonRootCA1.pem`.
2. Attach a policy to the certificate that allows `iot:Connect`, `iot:Publish`,
   `iot:Subscribe` and `iot:Receive`.
3. Put the three files next to the scripts (they are ignored by git) or point to them
   with environment variables.
4. Find your endpoint: **IoT Core → Settings → Device data endpoint**.

All settings live in `config.py` and can be overridden with environment variables:

| Variable | Default | Meaning |
|---|---|---|
| `IOT_ENDPOINT` | `endpoint` | Your device data endpoint (**required**) |
| `IOT_PORT` | `8883` | MQTT port |
| `IOT_CLIENT_ID` | `333` | MQTT client id |
| `IOT_ROOT_CA` | `./AmazonRootCA1.pem` | Amazon root CA file |
| `IOT_PRIVATE_KEY` | `./333.private.key` | Device private key |
| `IOT_CERTIFICATE` | `./333.cert.pem` | Device certificate |
| `IOT_TOPIC` | `general/inbound` | Topic to publish to / subscribe to |

## Run

```bash
export IOT_ENDPOINT=abc123-ats.iot.eu-central-1.amazonaws.com

python3 subscribe.py   # terminal 1: waits for messages (Enter to stop)
python3 publish.py     # terminal 2: sends one message
```

To test the temperature reply, publish `{"temperature"}` to `general/inbound` from
**IoT Core → MQTT test client**.

> CPU temperature (`pyspectator`) is not available on every operating system;
> on some machines it returns `None`.

## Security

Certificates and keys (`*.pem`, `*.key`, `*.crt`) are listed in `.gitignore` and must never be committed.
