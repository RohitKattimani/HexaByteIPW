#include "threat_scanner.h"

ThreatScanner::ThreatScanner() {
    blacklist = {
        "phishing-example.com",
        "dangerous-site.net",
        "malware-download.org"
    };
}

bool ThreatScanner::isMaliciousURL(const std::string& url) {
    for (const auto& domain : blacklist) {
        if (url.find(domain) != std::string::npos) {
            return true;
        }
    }
    return false;
}

bool ThreatScanner::detectPhishing(const std::string& url) {
    return (
        url.find("login") != std::string::npos &&
        url.find("verify") != std::string::npos
    );
}

bool ThreatScanner::containsExploitPayload(const std::string& html) {
    return (
        html.find("<script>eval(") != std::string::npos ||
        html.find("document.cookie") != std::string::npos
    );
}
