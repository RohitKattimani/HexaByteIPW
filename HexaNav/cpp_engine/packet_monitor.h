#ifndef PACKET_MONITOR_H
#define PACKET_MONITOR_H

class PacketMonitor {
public:
    void startMonitoring();
    void stopMonitoring();

    bool detectSuspiciousTraffic();
};

#endif
