import rfc3161ng
from pyasn1.codec.der import encoder, decoder
from cryptography import x509
from cryptography.hazmat.backends import default_backend

rt = rfc3161ng.RemoteTimestamper('http://rfc3161timestampingserver.pi-docker.lab/',include_tsa_certificate=True,certificate=b"")
tsr = rt(data=b'John Doe',include_tsa_certificate=True,return_tsr=True)
with open("/tmp/data_file.tsr", "wb") as f:
     f.write(encoder.encode(tsr))
tst=encoder.encode(tsr.time_stamp_token)
tst, substrate = decoder.decode(tst, asn1Spec=rfc3161ng.TimeStampToken())
signed_data = tst.content
a=signed_data['certificates']
#print(a)
#print(isinstance(a,list))
print(a[0][0])
certificate=a[0][0]
data = encoder.encode(certificate)
print(data)
backend = default_backend()
x509.load_der_x509_certificate(data, backend)
rt.check(tst, data=b'John Doe')
print(rfc3161ng.get_timestamp(tst))

certificate=None
if certificate == b"":
     print(1)
#if b"huhu" in certificate:
#     print(2)

bla=certificate or b"default"

if certificate is None:
     print(3)
print(bla)