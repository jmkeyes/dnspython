from typing import Union, Optional, List, Any, Dict
from . import exception, rdataclass, name, rdatatype

import socket
_gethostbyname = socket.gethostbyname

class NXDOMAIN(exception.DNSException): ...
class YXDOMAIN(exception.DNSException): ...
class NoAnswer(exception.DNSException): ...
class NoNameservers(exception.DNSException): ...
class NotAbsolute(exception.DNSException): ...
class NoRootSOA(exception.DNSException): ...
class NoMetaqueries(exception.DNSException): ...
class NoResolverConfiguration(exception.DNSException): ...
Timeout = exception.Timeout

def resolve(qname : str, rdtype : Union[int,str] = 0,
            rdclass : Union[int,str] = 0,
            tcp=False, source=None, raise_on_no_answer=True,
            source_port=0, lifetime : Optional[float]=None,
            search : Optional[bool]=None):
    ...
def query(qname : str, rdtype : Union[int,str] = 0,
          rdclass : Union[int,str] = 0,
          tcp=False, source=None, raise_on_no_answer=True,
          source_port=0, lifetime : Optional[float]=None):
    ...
def resolve_address(ipaddr: str, *args: Any, **kwargs: Optional[Dict]):
    ...
class LRUCache:
    def __init__(self, max_size=1000):
        ...
    def get(self, key):
        ...
    def put(self, key, val):
        ...
class Answer:
    def __init__(self, qname, rdtype, rdclass, response,
                 raise_on_no_answer=True):
        ...
def zone_for_name(name, rdclass : int = rdataclass.IN, tcp=False,
                  resolver : Optional[Resolver] = None):
    ...

class Resolver:
    def __init__(self, filename : Optional[str] = '/etc/resolv.conf',
                 configure : Optional[bool] = True):
        self.nameservers : List[str]
    def resolve(self, qname : str, rdtype : Union[int,str] = rdatatype.A,
                rdclass : Union[int,str] = rdataclass.IN,
                tcp : bool = False, source : Optional[str] = None,
                raise_on_no_answer=True, source_port : int = 0,
                lifetime : Optional[float]=None,
                search : Optional[bool]=None):
        ...
    def query(self, qname : str, rdtype : Union[int,str] = rdatatype.A,
              rdclass : Union[int,str] = rdataclass.IN,
              tcp : bool = False, source : Optional[str] = None,
              raise_on_no_answer=True, source_port : int = 0,
              lifetime : Optional[float]=None):
        ...
