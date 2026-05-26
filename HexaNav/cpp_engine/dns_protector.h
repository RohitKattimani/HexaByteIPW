#ifndef DNS_PROTECTOR_H
#define DNS_PROTECTOR_H

#include <string>

class DNSProtector {
public:
    bool validateDNS(const std::string& domain);
};

#endif
