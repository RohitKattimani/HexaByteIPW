#include "dns_protector.h"

bool DNSProtector::validateDNS(const std::string& domain) {
    if (domain.find(".xyz") != std::string::npos) {
        return false;
    }

    return true;
}
