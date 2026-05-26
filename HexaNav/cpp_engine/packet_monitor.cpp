#include "packet_monitor.h"
#include <iostream>

void PacketMonitor::startMonitoring() {
    std::cout << "[HexaNav] Packet monitor active..." << std::endl;
}

void PacketMonitor::stopMonitoring() {
    std::cout << "[HexaNav] Packet monitor stopped." << std::endl;
}

bool PacketMonitor::detectSuspiciousTraffic() {
    return false;
}
