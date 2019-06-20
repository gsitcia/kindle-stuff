
from xml.dom.minidom import Document

doc = Document()

# create the envelope element and set its attributes
envelope = doc.createElementNS('', 's:Envelope')
envelope.setAttribute('xmlns:s', 'http://schemas.xmlsoap.org/soap/envelope/')
envelope.setAttribute('s:encodingStyle', 'http://schemas.xmlsoap.org/soap/encoding/')

# create the body element
body = doc.createElementNS('', 's:Body')

# create the function element and set its attribute
fn = doc.createElementNS('', 'u:AddPortMapping')
fn.setAttribute('xmlns:u', 'urn:schemas-upnp-org:service:WANIPConnection:1')

# setup the argument element names and values
# using a list of tuples to preserve order
arguments = [
    ('NewRemoteHost',''),
    ('NewExternalPort', '2400'),           # specify port on router
    ('NewProtocol', 'TCP'),                 # specify protocol
    ('NewInternalPort', '2400'),           # specify port on internal host
    ('NewInternalClient', '192.168.0.104'), # specify IP of internal host
    ('NewEnabled', '1'),                    # turn mapping ON
    ('NewPortMappingDescription', 'Test desc'), # add a description
    ('NewLeaseDuration', '0')]              # how long should it be opened?

# NewEnabled should be 1 by default, but better supply it.
# NewPortMappingDescription Can be anything you want, even an empty string.
# NewLeaseDuration can be any integer BUT some UPnP devices don't support it,
# so set it to 0 for better compatibility.

# container for created nodes
argument_list = []

# iterate over arguments, create nodes, create text nodes,
# append text nodes to nodes, and finally add the ready product
# to argument_list
for k, v in arguments:
    tmp_node = doc.createElement(k)
    tmp_text_node = doc.createTextNode(v)
    tmp_node.appendChild(tmp_text_node)
    argument_list.append(tmp_node)

# append the prepared argument nodes to the function element
for arg in argument_list:
    fn.appendChild(arg)

# append function element to the body element
body.appendChild(fn)

# append body element to envelope element
envelope.appendChild(body)

# append envelope element to document, making it the root element
doc.appendChild(envelope)

# our tree is ready, conver it to a string
pure_xml = doc.toxml()

import requests

# use the object returned by urlparse.urlparse to get the hostname and port
print(pure_xml)

path = "http://192.168.1.1:2555/upnp/445269bc-ed9f-39d6-a86b-a975069c1d8d/WANIPConn1.ctl"

resp = requests.post(path,data=pure_xml,
    headers={'SOAPAction': '"urn:schemas-upnp-org:service:WANIPConnection:1#AddPortMapping"',
     'Content-Type': 'text/xml'})

# print the response status
print(resp.status)

# print the response body
print(resp.text)
