#ifndef THREAT_SCANNER_H
#define THREAT_SCANNER_H

#include <string>
#include <vector>

class ThreatScanner {
public:
    ThreatScanner();

    bool isMaliciousURL(const std::string& url);
    bool detectPhishing(const std::string& url);
    bool containsExploitPayload(const std::string& html);

private:
    std::vector<std::string> blacklist;
};

#endif
