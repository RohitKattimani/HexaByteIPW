cmake_minimum_required(VERSION 3.10)

project(HexaNavSecurityCore)

set(CMAKE_CXX_STANDARD 17)

add_library(HexaNavCore SHARED
    threat_scanner.cpp
    packet_monitor.cpp
    dns_protector.cpp
    sandbox_engine.cpp
    ai_classifier.cpp
)
